import os
import hashlib
import numpy as np
from PIL import Image

def get_image_stats(img_path):
    try:
        with Image.open(img_path) as im:
            w, h = im.size
            mode = im.mode
            fmt = im.format
            # Convert to grayscale for image quality metrics
            gray = im.convert('L')
            arr = np.array(gray, dtype=np.float32)
            mean_b = float(np.mean(arr))
            std_b = float(np.std(arr))
            
            # Simple discrete Laplacian for blur metric
            # Laplacian kernel: [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
            # Or difference variance
            gy, gx = np.gradient(arr)
            grad_mag = np.hypot(gx, gy)
            blur_metric = float(np.var(grad_mag))
            
            return {
                "width": w,
                "height": h,
                "mode": mode,
                "format": fmt,
                "mean_brightness": round(mean_b, 2),
                "contrast": round(std_b, 2),
                "sharpness_score": round(blur_metric, 2),
                "corrupted": False,
                "error": None
            }
    except Exception as e:
        return {
            "width": 0, "height": 0, "mode": "UNKNOWN", "format": "UNKNOWN",
            "mean_brightness": 0, "contrast": 0, "sharpness_score": 0,
            "corrupted": True, "error": str(e)
        }

def md5_file(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()

base_dir = r"D:\farm ai"
streets = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

all_records = []
md5_map = {}

for street in sorted(streets):
    s_path = os.path.join(base_dir, street)
    files = sorted([f for f in os.listdir(s_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    for f in files:
        f_path = os.path.join(s_path, f)
        f_size = os.path.getsize(f_path)
        f_hash = md5_file(f_path)
        stats = get_image_stats(f_path)
        
        is_dup = f_hash in md5_map
        if is_dup:
            md5_map[f_hash].append((street, f))
        else:
            md5_map[f_hash] = [(street, f)]
            
        record = {
            "street": street,
            "filename": f,
            "path": f_path,
            "size_bytes": f_size,
            "md5": f_hash,
            **stats
        }
        all_records.append(record)

print(f"Total streets found: {len(streets)}")
print(f"Total images scanned: {len(all_records)}")

# Check duplicate hashes
duplicates = {k: v for k, v in md5_map.items() if len(v) > 1}
print(f"Exact Duplicate Images (by MD5): {len(duplicates)}")
for k, v in duplicates.items():
    print(f"  Hash {k}: {v}")

# Street summary counts
print("\n--- Per-Street Counts ---")
for s in sorted(streets):
    cnt = len([r for r in all_records if r["street"] == s])
    print(f"  {s}: {cnt} images")
