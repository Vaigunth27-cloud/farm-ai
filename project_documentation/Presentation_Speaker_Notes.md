# FarmwiseAI — Street View Urban Intelligence Platform
## Executive Presentation Speaker Notes & Presenter Script

This script accompanies the 10-slide master technical presentation:
`D:\farm ai\project_documentation\FarmwiseAI_Technical_Demo.pptx`

---

## Slide-by-Slide Presenter Script

### Slide 1: Title & Introduction
> **Slide Title**: FarmwiseAI — Street View Urban Intelligence Platform  
> **Target Time**: 0:00 – 0:45  
> **Visual Focus**: High-impact dark theme title slide with Urban Intelligence badge and project scope.

**What to Say**:
> *"Good morning, respected evaluators and technical reviewers. Today, we are presenting **FarmwiseAI**, a Street View Urban Intelligence Platform engineered to transform raw street-level imagery into verifiable, actionable digital twins for municipal administration.*
> 
> *Our empirical study area is Ward 29, North Zone, Coimbatore City Municipal Corporation. Over the next 10 minutes, we will walk you through our actual working platform, demonstrate our dual-tier image acquisition, inspect our AI perception pipeline, and share our ongoing model training work with complete architectural honesty."*

---

### Slide 2: The Working Prototype & Master Navigation
> **Slide Title**: Operational Architecture: Master Platform & Dual Ingestion  
> **Target Time**: 0:45 – 1:45  
> **Visual Focus**: Screenshot of the FarmwiseAI master redesign dashboard with Option A and Option B highlighted.

**What to Say**:
> *"Before diving into algorithms, let us look at the actual working product. On screen is our master unified dashboard, built as a zero-dependency responsive SPA.*
> 
> *Notice our left navigation bar: under **Street Intelligence**, we have engineered two distinct, fully functional workflows:*
> 1. *Option A — Find a Place & Capture Street View, tailored for desk officers to search landmarks, navigate map viewports, and capture snapshots.*
> 2. *Option B — Upload Street Images & Analyze, tailored for field survey crews uploading multi-frame dashcam batches.*
> 
> *Both workflows connect to a shared FastAPI backend running Ultralytics YOLO11, EasyOCR, and spatial association engines."*

---

### Slide 3: Key Implemented Features & Capabilities
> **Slide Title**: Verified Capabilities: What is Implemented Today  
> **Target Time**: 1:45 – 2:45  
> **Visual Focus**: Feature matrix cards showing Option A, Option B, FastAPI backend, EasyOCR, Urban AI Agent, and Municipal reports.

**What to Say**:
> *"Let us be completely transparent about what is implemented today versus what is planned. Every card shown here is backed by working code in our repository.*
> 
> *Our system validates image payloads, extracts EXIF GPS coordinates, runs YOLO11 detection across 12 urban classes, transcribes Tamil and English commercial signs with EasyOCR, and generates structured **Urban Asset Passports**.*
> 
> *Furthermore, our **Urban AI Agent** allows city engineers to interrogate municipal datasets in plain English, citing exact corridor scorecards and work orders."*

---

### Slide 4: End-to-End Product Workflow
> **Slide Title**: Operational Workflow: From Street Image to Municipal Action  
> **Target Time**: 2:45 – 3:45  
> **Visual Focus**: Diagram 10 (User Workflow) and Diagram 4 (Detection Flowchart).

**What to Say**:
> *"Here is how a municipal user experiences the platform:*
> 1. *The user inputs a street name or uploads raw camera photos.*
> 2. *The system normalizes the image, extracts camera coordinates, and feeds the tensor into our YOLO11 detector.*
> 3. *Bounding boxes are filtered at a dynamic confidence threshold ($\tau = 0.25$), and shop signages are passed to OCR.*
> 4. *Detections are georeferenced against our GeoJSON corridor topology.*
> 5. *Finally, rather than stopping at bounding boxes, FarmwiseAI populates standardized municipal reports: a Commercial Property Tax Ledger for CCMC and Feeder Maintenance Work Orders for TANGEDCO."*

---

### Slide 5: Overall Technical Architecture (Diagram 1)
> **Slide Title**: System Architecture: Decoupled Perception & Spatial Pipeline  
> **Target Time**: 3:45 – 4:45  
> **Visual Focus**: Diagram 1 (Overall System Architecture) with color-coded subsystems.

**What to Say**:
> *"This diagram represents our end-to-end architectural blueprint:*
> - *At the top is our **Data Acquisition Layer**, supporting live canvas capture and multi-file queues.*
> - *In the middle is our **FastAPI Perception Core**, hosting YOLO11, EasyOCR, and ExifRead.*
> - *Crucially, we incorporate a **Human Verification Layer** via our Tri-View Studio, allowing operators to validate ambiguous detections before data reaches government ledgers.*
> - *At the bottom is our **Spatial & Municipal Engine**, generating vector GeoJSON digital twins and tax penalty registers.*
> 
> *Everything is engineered for offline edge execution on local municipal infrastructure."*

---

### Slide 6: AI Detection, Taxonomy & Empirical Dataset
> **Slide Title**: AI Perception Engine: 12 Urban Classes & Empirical Baseline  
> **Target Time**: 4:45 – 5:45  
> **Visual Focus**: Actual annotated corridor frame, 12-class taxonomy, and corridor breakdown table (108 frames / 10 streets).

**What to Say**:
> *"Our AI engine is calibrated to 12 urban classes essential for Indian city governance—from buildings and electric poles to streetlights, transformers, and commercial signboards.*
> 
> *Our empirical dataset comprises 108 high-resolution frames gathered across 10 representative corridors in Ward 29, Coimbatore. Notice how we prevent data leakage: our training, validation, and test splits are partitioned **by corridor**, not randomly shuffled. Corridors ST09 and ST10 are kept completely unseen to rigorously evaluate how our model handles novel architectural facades and lighting angles."*

---

### Slide 7: Innovation & Architectural Differentiation
> **Slide Title**: Key Innovations: Moving Beyond Generic Object Detectors  
> **Target Time**: 5:45 – 6:45  
> **Visual Focus**: 4 Innovation Pillars (Evidence-Linked Passports, Dual Ingestion, Multilingual Sign-Tax Pairing, Grounded RAG Agent).

**What to Say**:
> *"Why is FarmwiseAI different from a standard object detection project?*
> 1. ***Evidence-Linked Infrastructure Passports***: *Every single asset has an auditable visual trail. If a commercial establishment is flagged for unassessed tax, the exact pixel crop and GPS pin are attached to the notice.*
> 2. ***Dual-Tier Ingestion***: *We serve both desk-based complaints and city-wide survey vehicles.*
> 3. ***Native Multilingual Text-Asset Pairing***: *We extract Tamil and English shop names to detect commercial tax evasion.*
> 4. ***Grounded RAG Urban Agent***: *Our conversational AI cites real municipal ledgers, preventing hallucinations."*

---

### Slide 8: Technical Achievements, Metrics & Current Limitations
> **Slide Title**: Experimental Progress, Validation Metrics & Honest Constraints  
> **Target Time**: 6:45 – 7:45  
> **Visual Focus**: Prototype evaluation metrics table (mAP50: 0.728, Buildings: 0.884, Poles: 0.715), confusion matrix, and limitation callouts.

**What to Say**:
> *"Here are our actual experimental metrics logged across 34 validation runs in `runs/detect/`.*
> 
> *Our prototype YOLO model achieves mAP50 of 0.728 across all classes, with building facades reaching 0.884. However, we maintain strict technical honesty: we observed confusion between vertical tree trunks and electric poles in residential layouts, and weathered road signs scored lower.*
> 
> *Furthermore, monocular cameras lack LiDAR depth, and overlapping frames require robust duplicate matching. These limitations define our active engineering focus."*

---

### Slide 9: Active Engineering: Re-Annotation & Next Milestones
> **Slide Title**: Active Engineering: Label Refinement & GPU Retraining  
> **Target Time**: 7:45 – 8:45  
> **Visual Focus**: Diagram 5 (Annotation & Training Flowchart) highlighting active steps, and the 4-phase development roadmap.

**What to Say**:
> *"What are we working on right now?*
> 
> *We are actively conducting comprehensive manual re-annotation across all 108 corridor frames in our dataset to guarantee clean, verified ground truth labels. Once verified, we are executing a full 100-epoch hyperparameter fine-tuning pass on GPU.*
> 
> *Our next development milestones include implementing multi-view Hungarian matching for moving survey vehicles and deploying a progressive web app for field survey teams."*

---

### Slide 10: Conclusion & Operational Impact
> **Slide Title**: Conclusion: Transforming Urban Governance with Visual Evidence  
> **Target Time**: 8:45 – 9:30  
> **Visual Focus**: Summary impact cards: Municipal Revenue Protection, Public Electrical Safety, Nighttime Mobility, and auditable open-source delivery.

**What to Say**:
> *"In conclusion, FarmwiseAI demonstrates that ordinary street-level photography—when paired with purpose-built computer vision, spatial topology, and grounded conversational AI—can solve long-standing urban governance bottlenecks.*
> 
> *By turning visual evidence into actionable municipal ledgers, we provide cities like Coimbatore with a reliable, scalable, and auditable path to digital twin governance.*
> 
> *We now invite the panel to explore the live working demonstration. Thank you."*
