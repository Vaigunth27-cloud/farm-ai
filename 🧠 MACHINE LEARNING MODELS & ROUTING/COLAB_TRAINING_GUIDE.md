# 🚀 Quick Google Colab Training Guide (10 Minutes)
### FarmwiseAI Product Challenge 2026 — Team 24

Use Google Colab's free **NVIDIA T4 GPU (16 GB)** to train your YOLO11 model with high accuracy in **10 minutes**.

---

### Step 1: Open Google Colab
1. Go to: **[colab.research.google.com](https://colab.research.google.com)**
2. Click **Upload** and select:
   `D:\farm ai\🧠 MACHINE LEARNING MODELS & ROUTING\Train_YOLO11_Urban_Digital_Twin.ipynb`

---

### Step 2: Enable Free T4 GPU
1. In Colab's top menu, click **Runtime** → **Change runtime type**.
2. Under **Hardware accelerator**, select **T4 GPU**.
3. Click **Save**.

---

### Step 3: Upload the Dataset ZIP
1. In Colab, run **Cell 3**.
2. When prompted, upload the dataset package:
   `D:\farm ai\🧠 MACHINE LEARNING MODELS & ROUTING\urban_intelligence_dataset.zip` (35 MB)
   *(Upload takes ~10 seconds)*

---

### Step 4: Run Training (Takes ~8–10 Minutes)
1. Click **Runtime** → **Run all** (or press `Ctrl+F9`).
2. The notebook will:
   - Train YOLO11n for **50 epochs** on the NVIDIA T4 GPU.
   - Achieve high precision for utility poles, streetlights, buildings, and signboards.
   - Export optimized `best.onnx` and `best.pt`.
   - Automatically download `fine_tuned_weights.zip` to your `Downloads` folder!

---

### Step 5: Replace Weights in D:\farm ai
1. Unzip the downloaded `fine_tuned_weights.zip`.
2. Copy `best.pt` and `best.onnx` into:
   `D:\farm ai\🧠 MACHINE LEARNING MODELS & ROUTING\prototype_model\`
3. That's it! Your entire digital twin and portal will now run the fine-tuned GPU model!
