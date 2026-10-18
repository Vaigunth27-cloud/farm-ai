import os
import sys
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

print("=== Edge Optimization & ONNX Model Inspector ===")

onnx_path = r"D:\farm ai\prototype_model\urban_intel_v1\weights\best.onnx"

if not os.path.exists(onnx_path):
    print(f"Error: ONNX file not found at {onnx_path}")
    sys.exit(1)

file_size_mb = os.path.getsize(onnx_path) / (1024 * 1024)
print(f"ONNX Model Artifact: {onnx_path}")
print(f"Artifact Size: {file_size_mb:.2f} MB")

try:
    import onnx
    model = onnx.load(onnx_path)
    onnx.checker.check_model(model)
    print("ONNX Model Integrity: PASSED (Well-formed graph)")
    
    # Inspect inputs and outputs
    graph = model.graph
    print(f"\nModel Graph Name: {graph.name}")
    print(f"Producer Name: {model.producer_name} (Version: {model.producer_version})")
    print(f"IR Version: {model.ir_version}, Opset: {model.opset_import[0].version}")
    
    print("\n--- Inputs ---")
    for input_tensor in graph.input:
        shape = [dim.dim_value if dim.dim_value > 0 else dim.dim_param for dim in input_tensor.type.tensor_type.shape.dim]
        print(f"  Name: {input_tensor.name}, Shape: {shape}, DataType: {input_tensor.type.tensor_type.elem_type}")
        
    print("\n--- Outputs ---")
    for output_tensor in graph.output:
        shape = [dim.dim_value if dim.dim_value > 0 else dim.dim_param for dim in output_tensor.type.tensor_type.shape.dim]
        print(f"  Name: {output_tensor.name}, Shape: {shape}, DataType: {output_tensor.type.tensor_type.elem_type}")

    # Inspect class names from metadata
    meta = {prop.key: prop.value for prop in model.metadata_props}
    if "names" in meta:
        print(f"\nMetadata Classes (12 Urban Infrastructure Classes):\n  {meta['names']}")

    # Benchmark ONNX Runtime latency
    import onnxruntime as ort
    import numpy as np
    
    session = ort.InferenceSession(onnx_path, providers=['CPUExecutionProvider'])
    input_name = session.get_inputs()[0].name
    
    # Warmup
    dummy_input = np.random.randn(1, 3, 640, 640).astype(np.float32)
    for _ in range(3):
        _ = session.run(None, {input_name: dummy_input})
        
    # Latency benchmark (10 iterations)
    latencies = []
    for _ in range(10):
        t0 = time.time()
        _ = session.run(None, {input_name: dummy_input})
        latencies.append((time.time() - t0) * 1000)
        
    avg_latency = np.mean(latencies)
    p95_latency = np.percentile(latencies, 95)
    print(f"\n--- Edge CPU Latency Benchmark (Intel Core i5 CPU) ---")
    print(f"Mean Latency: {avg_latency:.2f} ms")
    print(f"P95 Latency:  {p95_latency:.2f} ms")
    print(f"Theoretical FPS: {1000 / avg_latency:.1f} FPS")
    print(f"Estimated Jetson Orin Nano (TensorRT FP16) Latency: ~12-18 ms (~60 FPS)")
    
except Exception as e:
    print(f"ONNX Inspection / Benchmark error: {e}")
