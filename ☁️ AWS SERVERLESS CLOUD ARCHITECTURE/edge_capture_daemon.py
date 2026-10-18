import os
import sys
import time
import json
import random
import logging
from dataclasses import dataclass, asdict

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(levelname)s] [EdgeNode-01] %(message)s')

@dataclass
class EdgeTelemetry:
    frame_id: str
    timestamp_utc: str
    latitude: float
    longitude: float
    speed_kmh: float
    heading_deg: float
    detections_count: int
    edge_inference_ms: float
    battery_voltage: float
    sync_status: str

class EdgeSurveyDaemon:
    """
    Simulates survey vehicle edge node (NVIDIA Jetson Orin Nano / Raspberry Pi 5)
    operating along Coimbatore Ward 29 corridors.
    Features:
    1. Camera frame acquisition at 5 Hz
    2. Local ONNX/TensorRT inference (<45 ms)
    3. GPS NMEA sentence geotagging
    4. Local SQLite spooling during connectivity dropouts
    5. Opportunistic upload to AWS S3 & IoT Core in ap-south-1
    """
    def __init__(self, target_street="ST01", s3_bucket="fai-tce-team24-urban-data-mumbai"):
        self.target_street = target_street
        self.s3_bucket = s3_bucket
        self.buffer = []
        self.synced_count = 0
        
        # Bounding box coordinates for Ward 29 (Ganapathy, Coimbatore)
        self.curr_lat = 11.026500
        self.curr_lon = 76.983000
        logging.info(f"Initialized Edge Survey Daemon for corridor {target_street}")
        logging.info(f"Target AWS S3 Bucket: s3://{s3_bucket}/edge_telemetry/")

    def capture_frame(self, frame_num: int) -> EdgeTelemetry:
        t0 = time.time()
        
        # Advance mock GPS coordinates along corridor trajectory
        self.curr_lat += random.uniform(0.00005, 0.00010)
        self.curr_lon += random.uniform(0.00003, 0.00008)
        
        # Simulate local edge model inference latency (matching benchmark)
        inference_ms = round(random.uniform(15.2, 28.6), 2)
        detections = random.randint(2, 6)
        
        telemetry = EdgeTelemetry(
            frame_id=f"FRAME-{self.target_street}-{frame_num:04d}",
            timestamp_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            latitude=round(self.curr_lat, 6),
            longitude=round(self.curr_lon, 6),
            speed_kmh=round(random.uniform(18.0, 32.0), 1),
            heading_deg=round(random.uniform(40.0, 48.0), 1),
            detections_count=detections,
            edge_inference_ms=inference_ms,
            battery_voltage=round(random.uniform(12.4, 12.8), 2),
            sync_status="SPOOLED_LOCAL"
        )
        self.buffer.append(telemetry)
        return telemetry

    def sync_to_cloud(self, batch_size=5):
        if not self.buffer:
            return 0
            
        to_sync = self.buffer[:batch_size]
        logging.info(f"Uploading batch of {len(to_sync)} frames to AWS S3 (Region: ap-south-1)...")
        time.sleep(0.08) # Network round-trip simulation
        
        for item in to_sync:
            item.sync_status = "SYNCED_S3_MUMBAI"
            self.synced_count += 1
            
        self.buffer = self.buffer[batch_size:]
        logging.info(f"Sync complete. Total synced frames: {self.synced_count}")
        return len(to_sync)

def run_edge_simulation():
    daemon = EdgeSurveyDaemon(target_street="ST01")
    print("\n--- Starting Edge Survey Vehicle Real-Time Simulation (10 Frames) ---")
    
    for i in range(1, 11):
        telem = daemon.capture_frame(i)
        print(f"[{telem.frame_id}] GPS: ({telem.latitude}, {telem.longitude}) | Speed: {telem.speed_kmh} km/h | Detections: {telem.detections_count} | Latency: {telem.edge_inference_ms} ms")
        time.sleep(0.02)
        
        # Sync every 5 frames
        if i % 5 == 0:
            daemon.sync_to_cloud(batch_size=5)

    print("\nSimulation successfully concluded. 10/10 frames processed & synced.")

if __name__ == "__main__":
    run_edge_simulation()
