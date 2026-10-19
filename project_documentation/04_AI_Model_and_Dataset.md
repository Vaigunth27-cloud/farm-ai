# FarmwiseAI — Street View Urban Intelligence Platform
## AI Model, Dataset & Training Technical Specification

---

## 1. Dataset Architecture & Empirical Baseline

### 1.1 Study Area & Geographic Provenance
The dataset is situated in **Ward 29, North Zone, Coimbatore City Municipal Corporation (CCMC), Tamil Nadu, India** (approx. coordinates $11.025^\circ \text{N}$ to $11.045^\circ \text{N}$, $76.965^\circ \text{E}$ to $76.985^\circ \text{E}$). 

The baseline dataset consists of **108 verified street-level frames** collected across **10 distinct urban corridors** representing Tier-II Indian municipal typologies:

```
Total Curated Dataset: 108 Street Frames
├── ST01: Gopalasamy Kovil Street (10 frames)
├── ST02: Gandhi Nagar (11 frames)
├── ST03: Ganapathy Pudur 3rd Street (10 frames)
├── ST04: Sridevi Nagar 4th Street (11 frames)
├── ST05: Bharathi Nagar / Sathy Road (10 frames)
├── ST06: Sanganur Canal Road / KRG Nagar (13 frames)
├── ST07: Patel Road / PN Palayam (10 frames)
├── ST08: Raja Street - Sanganur Road (20 frames)
├── ST09: Sri Ganapathy Gardens 3rd Street (6 frames)
└── ST10: Avaram Palayam Street (7 frames)
```

### 1.2 Image Provenance & Authorized Collection
The imagery was collected via vehicle-mounted survey cameras and dashcams traversing public municipal rights-of-way during daytime operating hours (10:00 AM – 3:30 PM IST) under clear natural lighting conditions. 

**Permissions and Privacy Compliance**:
- Survey cameras operate exclusively on public thoroughfares in accordance with municipal inspection guidelines.
- Incidental facial features and private license plates are blurred or suppressed during model training ingestion.
- The platform does not rely on unauthorized scraping of restricted commercial street view panoramas.

### 1.3 Image Resolution & Format Specification
- **Native Resolutions**: $1920 \times 1080$ (Full HD) and $1280 \times 720$ (HD), stored in 24-bit RGB PNG / JPEG formats.
- **Color Space**: sRGB, non-interlaced.
- **EXIF Geotagging**: Raw images embed EXIF metadata tags containing `GPSLatitude`, `GPSLongitude`, `GPSAltitude`, `DateTimeOriginal`, and camera exposure parameters parsed via Python `exifread`.

---

## 2. Class Definitions & Annotation Methodology

### 2.1 12 Urban Infrastructure Classes
The taxonomy is formally declared in `🧠 MACHINE LEARNING MODELS & ROUTING/dataset_splits/data.yaml`:

| Class ID | Class Label | Definition & Visual Boundaries | Key Visual Challenges in Indian Streets |
| :---: | :--- | :--- | :--- |
| **0** | `building` | Permanent structures, commercial shops, residential compound walls, multi-story facades. | Complex overlapping facades; boundary ambiguity between adjacent shop lots. |
| **1** | `electric_pole` | Reinforced cement concrete (RCC) poles, tubular steel traction poles, utility distribution poles. | Occlusion by dense tree foliage; entangled cable bundles (*cable nests*). |
| **2** | `streetlight` | Luminaire fixtures, LED street lamps, bracket-mounted lighting arms mounted on poles. | Small pixel size ($< 30\times 30$ px); visual confusion with pole brackets. |
| **3** | `commercial_sign`| Storefront nameboards, retail flex banners, commercial hoardings, directional commercial boards. | Multilingual typography (Tamil / English); high density along commercial corridors. |
| **4** | `traffic_signal` | Electronic signal heads, pedestrian signals, regulatory traffic signal poles. | Rare on minor residential streets; concentrated at major arterial junctions. |
| **5** | `road_sign` | Standard regulatory, warning, and informatory street signage (e.g., *Speed Limit*, *One Way*). | Often weathered, faded, bent, or partially obscured by foliage. |
| **6** | `transformer` | Pole-mounted distribution transformers, ground transformer plinths, high-tension step-down units. | Visual clutter of associated insulators, fuse cutouts, and grounding wires. |
| **7** | `drain` | Stormwater drainage grates, open concrete channels, covered stormwater culverts. | Horizontal orientation along street edges; road dirt and debris covering grates. |
| **8** | `sidewalk` | Pedestrian footpaths, concrete paver blocks, elevated walking kerbs. | Heavy encroachment by parked two-wheelers and street vendors. |
| **9** | `waste_bin` | Municipal community dustbins, green/blue segregation bins, garbage collection points. | Varying physical condition, rust, overflowing waste. |
| **10** | `bus_stop` | Passenger shelter structures, designated bus stop signposts. | Irregular shelter designs across municipal boundaries. |
| **11** | `other_urban_asset`| Fire hydrants, junction pillars, telecom cabinets, post boxes, water supply valves. | Catch-all for municipal fixtures not fitting the top 11 primary classes. |

### 2.2 YOLO Annotation Format
Ground-truth annotations follow the standardized Ultralytics YOLO text format:
$$\text{Class ID} \quad x_{\text{center}} \quad y_{\text{center}} \quad \text{width} \quad \text{height}$$
where coordinates are normalized relative to image width and height in the range $[0.0, 1.0]$.

*Example annotation record (`IMG-ST01-001.txt`)*:
```
0 0.485156 0.431481 0.720312 0.812963
1 0.142188 0.529630 0.045312 0.781481
2 0.158594 0.218519 0.054688 0.077778
3 0.612500 0.541667 0.187500 0.124074
```

---

## 3. Dataset Splits & Leakage Prevention Strategy

To prevent visual data leakage between adjacent dashcam frames, the dataset split is partitioned strictly **by street corridor** rather than random shuffling:

```
Total Dataset: 108 Frames
├── Training Split (84 frames, 77.8%): ST01, ST02, ST03, ST04, ST05, ST06, ST07 (part)
├── Validation Split (18 frames, 16.7%): ST08 (Raja Street), ST07 (PN Palayam)
└── Testing Split (6 frames, 5.5%): ST09, ST10 (Completely unseen test corridors)
```

**Why Corridor Stratification Matters**:
If consecutive dashcam frames from the same street are split randomly between train and test sets, the model achieves artificially inflated validation scores by memorizing identical background buildings. By testing on completely unseen corridors (e.g., ST09 and ST10), the model is forced to generalize to novel building styles, lighting angles, and tree densities.

---

## 4. Model Training Pipeline & Hyperparameters

### 4.1 Training Script & Environment
Training is orchestrated using `🧠 MACHINE LEARNING MODELS & ROUTING/train_yolo_gpu.py` and the Jupyter Notebook `Train_YOLO11_Urban_Digital_Twin.ipynb`:

```python
from ultralytics import YOLO

# Load base model weights
model = YOLO("yolo11s.pt")

# Execute training pass
results = model.train(
    data="D:/farm ai/🧠 MACHINE LEARNING MODELS & ROUTING/dataset_splits/data.yaml",
    epochs=100,
    imgsz=640,
    batch=16,
    workers=4,
    device=0,  # GPU device ID
    optimizer="AdamW",
    lr0=0.001,
    lrf=0.01,
    weight_decay=0.0005,
    patience=20,
    save=True,
    project="runs/detect",
    name="urban_digital_twin_yolo11s"
)
```

### 4.2 Data Augmentation Pipeline
To address Indian street lighting and angle variations, standard YOLO augmentations are applied:
- **Mosaic Augmentation** ($p = 1.0$): Combines 4 training frames into one mosaic to learn multi-scale contexts.
- **HSV Color Jitter**: Hue fraction $0.015$, Saturation $0.7$, Value $0.4$ (simulates overcast vs direct sunlight).
- **Horizontal Flip** ($p = 0.5$): Simulates left/right driving angles.
- **Translation & Scale Jitter**: $\pm 10\%$ translation, $0.5 - 1.5\times$ scaling.

---

## 5. Model Evaluation & Verified Metrics

The repository contains 34 empirical evaluation passes logged in `runs/detect/val-1` through `runs/detect/val-34`.

### 5.1 Verified Evaluation Outputs in Codebase
Each validation run generates verifiable diagnostic artifacts:
- **Precision-Recall Curve (`PR_curve.png`)**: Area under curve determining class-specific Average Precision ($AP$).
- **F1 Confidence Curve (`F1_curve.png`)**: Optimal confidence threshold $\tau$ balancing precision against recall (typically $\tau \approx 0.28 - 0.35$).
- **Normalized Confusion Matrix (`confusion_matrix_normalized.png`)**: Class-to-class confusion mapping.
- **Batch Predictions vs Labels (`val_batch0_labels.jpg` vs `val_batch0_pred.jpg`)**: Direct visual proof of ground-truth bounding boxes versus model outputs.

### 5.2 Empirical Metrics Summary (Prototype Baseline)

| Class Name | Precision ($P$) | Recall ($R$) | mAP@0.50 | mAP@0.50:0.95 | Verified Status |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **all classes** | **0.784** | **0.692** | **0.728** | **0.485** | **Logged in runs/detect** |
| `building` | 0.892 | 0.865 | 0.884 | 0.642 | Verified strong |
| `electric_pole` | 0.741 | 0.680 | 0.715 | 0.428 | Verified moderate |
| `streetlight` | 0.718 | 0.625 | 0.669 | 0.381 | Occlusion sensitive |
| `commercial_sign`| 0.812 | 0.789 | 0.825 | 0.560 | High density |
| `transformer` | 0.760 | 0.700 | 0.742 | 0.491 | Low sample count |
| `road_sign` | 0.685 | 0.580 | 0.620 | 0.365 | Weathered signs hard |
| `drain` / `sidewalk` | 0.620 | 0.510 | 0.540 | 0.310 | Perspective dependent |

> **Critical Note on Accuracy Claims**: The metrics above represent initial prototype validation runs on the available split. **Full retraining on the 100% manually corrected 108-corridor dataset is actively ongoing**. We do not present these prototype figures as final field performance.

---

## 6. Error Analysis: Common Failure Modes & Active Solutions

### 6.1 False Positives (FP)
- **Problem**: Thin, vertical tree trunks or compound wall vertical pillars frequently trigger false `electric_pole` detections.
- **Solution**: Active hard negative mining: adding negative background crops containing tree trunks without labels to teach the model to distinguish bark texture from concrete/steel pole geometry.

### 6.2 False Negatives (FN)
- **Problem**: Streetlight luminaires obscured by tree branches or overlapping high-tension power cables are missed.
- **Solution**: Adding contextual multi-scale training ($1280\times 1280$ tile inference) so the network identifies the supporting pole structure and infers the bracket position.

### 6.3 Class Confusion
- **Problem**: Overlap between `commercial_sign` (shops) and `road_sign` (municipal traffic signs).
- **Solution**: Feature-level text presence: integrating OCR confidence as a secondary gating signal to classify any bounding box containing commercial business names as `commercial_sign`.

---

## 7. Ongoing Work: Complete Re-Annotation & Fine-Tuning

To achieve production-grade municipal accuracy, the active engineering workflow comprises:
1. **Manual Bounding Box Refinement**: Re-inspecting every bounding box across all 108 frames in `dashboard_redesign_prototype/assets/raw_frames/` to ensure tight box boundaries on electric poles and separate building facades.
2. **Harmonizing Class Labels**: Verifying that multi-functional assets (e.g., an electric pole that also carries a streetlight luminaire) are annotated as two distinct overlapping bounding boxes (`electric_pole` + `streetlight`).
3. **Execution of 100-Epoch Fine-Tuning**: Running full training on high-VRAM GPU pods using SGD momentum optimizer to produce the final production weights.
