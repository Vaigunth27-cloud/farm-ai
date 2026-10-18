# 🧠 Machine Learning Models & Routing Engine
### FarmwiseAI Product Challenge 2026 — Team 24 (Coimbatore Ward 29)

This folder contains the complete multi-tier machine learning models, weights, ONNX deployment artifacts, and the two-tier routing engine.

---

## 📦 Contents & Artifacts

1. **`prototype_model/best.onnx`** (10.12 MB)
   - Opset 18 ONNX export optimized for CPU and edge embedded NPUs.
   - Inference benchmark: **42.0ms** on x86 CPU, **~16ms** on Nvidia Jetson Orin Nano (TensorRT).
   - Input shape: `(1, 3, 640, 640)` normalized RGB.

2. **`prototype_model/best.pt`** (5.45 MB)
   - PyTorch YOLO11n trained weights across 9 municipal fixed asset classes.

3. **`vlm_routing_engine/routing_engine.py`**
   - Two-tier routing implementation: Small-Model First (Tier 1) with selective VLM escalation (Tier 2).
   - High-confidence bounding boxes (>0.75) and standard signs bypass expensive cloud VLMs.
   - Low confidence (<0.60), ambiguous multi-lingual signboards, or zoning violations trigger Tier 2 VLM escalation.

4. **`vlm_routing_engine/routing_decisions.csv`** (201 KB)
   - Evaluation across all 774 pipeline detections:
     - **Fast Path (Tier 1 YOLO11n)**: 580 items (**74.94%**) @ 39.7ms average latency.
     - **Selective VLM (Tier 2 Escalation)**: 194 items (**25.06%**) @ 822.5ms average latency.

5. **`vlm_routing_engine/routing_benchmark_results.json`**
   - **Cost Savings**: **-74.87%** vs 100% VLM baseline ($0.58 vs $2.32 for 774 items).
   - **Latency Speedup**: **3.3x** faster aggregate throughput.
   - **Accuracy**: **+5.8%** boost from selective VLM disambiguation.

6. **`prototype_predictions/`**
   - Visual inspection images of inference predictions on the hold-out spatial test set.

7. **`yolo_annotations/`**
   - 108 standardized YOLO format bounding box labels and `classes.txt`.
