#!/usr/bin/env bash
# ==============================================================================
# AWS EC2 g4dn.xlarge GPU Instance 1-Click Setup & Model Fine-Tuning
# FarmwiseAI Product Challenge 2026 — Team 22 / 24
# Region: ap-south-1 (Mumbai) | Instance: g4dn.xlarge (NVIDIA T4 16GB GPU)
# ==============================================================================

set -e

echo "=========================================================="
echo "🚀 EC2 g4dn.xlarge GPU Environment Initialization"
echo "=========================================================="

# 1. Verify NVIDIA Driver & GPU
echo "[1/4] Verifying NVIDIA GPU Hardware..."
if ! command -v nvidia-smi &> /dev/null; then
    echo "❌ ERROR: nvidia-smi not found. Ensure Deep Learning AMI (Ubuntu) is used."
    exit 1
fi
nvidia-smi

# 2. System updates and Python dependencies
echo "[2/4] Installing Python 3.11 / PyTorch with CUDA 12.1..."
sudo apt-get update -y && sudo apt-get install -y python3-pip python3-dev libgl1-mesa-glx git-lfs

# Install PyTorch with official CUDA 12.1 wheels
pip3 install --upgrade pip
pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip3 install ultralytics onnx onnxruntime-gpu opencv-python-headless pyyaml pandas

# 3. Verify PyTorch GPU acceleration
echo "[3/4] Testing CUDA acceleration..."
python3 -c "import torch; assert torch.cuda.is_available(), 'CUDA not available!'; print('✅ CUDA is ACTIVE on:', torch.cuda.get_device_name(0), '| VRAM:', round(torch.cuda.get_device_properties(0).total_memory / 1e9, 2), 'GB')"

# 4. Run GPU Fine-Tuning Pipeline (50 Epochs, Batch 16)
echo "[4/4] Starting 50-Epoch GPU Fine-Tuning Pipeline..."
python3 train_yolo_gpu.py --epochs 50 --batch 16 --imgsz 640 --model yolo11n.pt

echo "=========================================================="
echo "🎉 TRAINING & ONNX EXPORT COMPLETE!"
echo "Model artifact is ready at: gpu_training_runs/urban_intel_gpu_yolo11n/weights/best.onnx"
echo "=========================================================="
