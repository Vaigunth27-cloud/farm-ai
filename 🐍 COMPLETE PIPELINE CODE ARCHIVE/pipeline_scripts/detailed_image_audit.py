import os
import hashlib
import numpy as np
import pandas as pd
from PIL import Image

base_dir = r"D:\farm ai"
streets = sorted([d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))])

records = []
for s in streets:
    s_dir = os.path.join(base_dir, s)
    files = sorted([f for f in os.listdir(s_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))])
    for idx, f in enumerate(files):
        f_path = os.path.join(s_dir, f)
        f_size = os.path.getsize(f_path)
        with Image.open(f_path) as im:
            w, h = im.size
            mode = im.mode
            fmt = im.format
            gray = im.convert('L')
            arr = np.array(gray, dtype=np.float32)
            mean_b = float(np.mean(arr))
            std_b = float(np.std(arr))
            gy, gx = np.gradient(arr)
            grad_mag = np.hypot(gx, gy)
            blur_metric = float(np.var(grad_mag))
            
            # Check crop top-left (first 100x100) to check UI presence
            # In Street View screenshots, top-left is often translucent/white overlay
            tl_crop = arr[:80, :200]
            tl_mean = float(np.mean(tl_crop))
            
        records.append({
            "street": s,
            "filename": f,
            "index_in_folder": idx + 1,
            "width": w,
            "height": h,
            "aspect_ratio": round(w / h, 3),
            "size_kb": round(f_size / 1024, 1),
            "format": fmt,
            "mode": mode,
            "mean_brightness": round(mean_b, 1),
            "contrast_std": round(std_b, 1),
            "sharpness": round(blur_metric, 1),
            "tl_overlay_brightness": round(tl_mean, 1)
        })

df = pd.DataFrame(records)
print(f"Total images analyzed: {len(df)}")
print("\nResolution distribution:")
print(df.groupby(["width", "height"]).size())

print("\nQuality Summary per Street:")
summary = df.groupby("street").agg(
    count=("filename", "count"),
    avg_size_kb=("size_kb", "mean"),
    avg_sharpness=("sharpness", "mean"),
    avg_brightness=("mean_brightness", "mean"),
    avg_contrast=("contrast_std", "mean")
)
print(summary.to_string())
