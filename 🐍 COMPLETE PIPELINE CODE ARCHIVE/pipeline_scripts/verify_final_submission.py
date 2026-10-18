import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

key_artifacts = [
    'urban_digital_twin_portal.html',
    'tri_view_studio.html',
    'gis_digital_twin_baseline.html',
    'building_explorer.html',
    'ocr_search_explorer.html',
    'asset_inventory_explorer.html',
    'corridor_intelligence_dashboard.html',
    'urban_ai_assistant.html',
    'municipal_report_portal.html',
    'cloud_architecture_dashboard.html',
    'vlm_routing_visualizer.html',
    'HACKATHON_PRESENTATION.html',
    'HACKATHON_PRESENTATION.md',
    'DEMO_VIDEO_WALKTHROUGH_SCRIPT.md',
    'SUBMISSION_MANIFEST.md',
    os.path.join('prototype_model', 'urban_intel_v1', 'weights', 'best.onnx'),
    os.path.join('prototype_model', 'urban_intel_v1', 'weights', 'best.pt'),
    os.path.join('aws_cloud_architecture', 'template.yaml'),
    os.path.join('aws_cloud_architecture', 'terraform', 'main.tf'),
    os.path.join('aws_cloud_architecture', 'lambda', 'lambda_function.py'),
    os.path.join('vlm_routing_engine', 'routing_engine.py'),
    os.path.join('vlm_routing_engine', 'routing_decisions.csv')
]

print("=== FINAL SUBMISSION VERIFICATION ===")
all_present = True
for f in key_artifacts:
    path = os.path.join(r"D:\farm ai", f)
    exists = os.path.exists(path)
    size = os.path.getsize(path) if exists else 0
    status = f"EXISTS ({size:,} bytes)" if exists else "MISSING"
    print(f"{f:50s} : {status}")
    if not exists:
        all_present = False

print(f"\nAll {len(key_artifacts)} Key Artifacts Verified: {all_present}")
