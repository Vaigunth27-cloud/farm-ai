"""
GPU-Accelerated YOLO11 Fine-Tuning & Evaluation Pipeline
Designed for AWS EC2 g4dn.xlarge (NVIDIA T4 GPU) & Local CUDA Workstations
FarmwiseAI Product Challenge 2026 — Team 22 / 24
"""

import os
import sys
import argparse
import torch
from pathlib import Path

# Ensure UTF-8 console output
sys.stdout.reconfigure(encoding='utf-8')

def check_hardware():
    print("=" * 60)
    print("🚀 HARDWARE ACCELERATION CHECK")
    print("=" * 60)
    cuda_avail = torch.cuda.is_available()
    print(f"  PyTorch Version : {torch.__version__}")
    print(f"  CUDA Available  : {cuda_avail}")
    if cuda_avail:
        device_count = torch.cuda.device_count()
        device_name = torch.cuda.get_device_name(0)
        vram_gb = torch.cuda.get_device_properties(0).total_memory / (1024**3)
        print(f"  GPU Device      : {device_name} ({device_count} GPU found)")
        print(f"  Total VRAM      : {vram_gb:.2f} GB")
        device = 0
    else:
        print("  ⚠️ WARNING: No CUDA GPU detected. Falling back to CPU.")
        device = 'cpu'
    print("=" * 60)
    return device

def train_model(epochs=50, batch_size=16, imgsz=640, model_variant="yolo11n.pt", device=0):
    from ultralytics import YOLO

    root_dir = Path(__file__).resolve().parent
    data_yaml = root_dir / "dataset_splits" / "data.yaml"
    project_dir = root_dir / "gpu_training_runs"
    os.makedirs(project_dir, exist_ok=True)

    print(f"\n📦 Initializing YOLO model: {model_variant}")
    print(f"📄 Dataset config: {data_yaml}")
    print(f"🎯 Target epochs: {epochs} | Batch size: {batch_size} | Image size: {imgsz}")

    model = YOLO(model_variant)

    # Production-grade fine-tuning hyperparameters
    train_args = {
        "data": str(data_yaml),
        "epochs": epochs,
        "batch": batch_size,
        "imgsz": imgsz,
        "device": device,
        "workers": 4 if device != 'cpu' else 2,
        "project": str(project_dir),
        "name": f"urban_intel_gpu_{model_variant.replace('.pt', '')}",
        "exist_ok": True,
        "pretrained": True,
        # Optimization hyperparameters
        "optimizer": "AdamW",
        "lr0": 0.001,
        "lrf": 0.01,
        "cos_lr": True,          # Cosine learning rate scheduler
        "warmup_epochs": 3.0,
        "warmup_momentum": 0.8,
        # Loss gains tuned for small & thin urban objects (poles, signs, wires)
        "box": 7.5,
        "cls": 0.7,
        "dfl": 1.5,
        # Data Augmentations
        "mosaic": 1.0,
        "mixup": 0.15,
        "flipud": 0.0,
        "fliplr": 0.5,
        "close_mosaic": 10,       # Turn off mosaic during final 10 epochs for sharp boundaries
        "save": True,
        "val": True,
        "verbose": True
    }

    print("\n🔥 Commencing training run...")
    results = model.train(**train_args)

    # Evaluate on hold-out validation set
    print("\n📊 Evaluating trained model on hold-out validation split...")
    metrics = model.val()
    print(f"  mAP@50    : {metrics.box.map50:.4f}")
    print(f"  mAP@50-95 : {metrics.box.map:.4f}")
    print(f"  Precision : {metrics.box.mp:.4f}")
    print(f"  Recall    : {metrics.box.mr:.4f}")

    # Export to ONNX (Opset 18)
    print("\n⚡ Exporting optimized model to ONNX runtime artifact...")
    best_weights = Path(model.trainer.save_dir) / "weights" / "best.pt"
    onnx_path = model.export(format="onnx", opset=18, dynamic=False, simplify=True)

    print("\n" + "=" * 60)
    print("✅ FINE-TUNING RUN COMPLETE!")
    print(f"  PyTorch Weights : {best_weights}")
    print(f"  ONNX Artifact   : {onnx_path}")
    print("=" * 60)

    return best_weights, onnx_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GPU-Accelerated YOLO Training")
    parser.add_argument("--epochs", type=int, default=50, help="Number of training epochs (default: 50)")
    parser.add_argument("--batch", type=int, default=16, help="Batch size (default: 16)")
    parser.add_argument("--imgsz", type=int, default=640, help="Image size (default: 640)")
    parser.add_argument("--model", type=str, default="yolo11n.pt", help="Base model variant (default: yolo11n.pt)")
    args = parser.parse_args()

    active_device = check_hardware()
    train_model(
        epochs=args.epochs,
        batch_size=args.batch,
        imgsz=args.imgsz,
        model_variant=args.model,
        device=active_device
    )
