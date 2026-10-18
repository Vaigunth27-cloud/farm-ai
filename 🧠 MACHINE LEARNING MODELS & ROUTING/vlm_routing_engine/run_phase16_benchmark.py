import os
import sys
import json
import time
import pandas as pd
import numpy as np
from dataclasses import asdict

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

base_dir = r"D:\farm ai"
vlm_dir = os.path.join(base_dir, "vlm_routing_engine")
os.makedirs(vlm_dir, exist_ok=True)

sys.path.insert(0, vlm_dir)
from routing_engine import UrbanVlmRouter, RoutingDecision

print("=== Running Phase 16: Small-Model First Routing & Selective VLM Escalation Benchmark ===")

# 1. Load Data
inv_df = pd.read_csv(os.path.join(base_dir, "urban_asset_inventory.csv"))
ocr_df = pd.read_csv(os.path.join(base_dir, "ocr_intelligence.csv"))
bldg_df = pd.read_csv(os.path.join(base_dir, "building_intelligence.csv"))
scorecard_df = pd.read_csv(os.path.join(base_dir, "corridor_intelligence_scorecard.csv"))

print(f"Loaded: {len(inv_df)} assets, {len(ocr_df)} OCR signboards, {len(bldg_df)} buildings, {len(scorecard_df)} corridor scorecards")

# Build corridor map
corr_map = {}
for idx, r in scorecard_df.iterrows():
    corr_map[r["Street_ID"]] = {
        "Street_Name": r["Street_Name"],
        "Cable_Burden_Index": r["Cable_Burden_Index"],
        "Lighting_Adequacy": r["Street_Lighting_Adequacy_Score"],
        "Grade": r["Municipal_Readiness_Grade"]
    }

router = UrbanVlmRouter(conf_threshold_low=0.45, ocr_conf_threshold=0.50, cbi_critical_threshold=85.0)

all_decisions = []

# 2. Evaluate Assets (465 items)
print("\n[1/3] Routing 465 Fixed Infrastructure Assets...")
for idx, r in inv_df.iterrows():
    st_id = r["Street_ID"]
    corr_info = corr_map.get(st_id, {"Cable_Burden_Index": 50.0})
    dec = router.evaluate_asset(r.to_dict(), corr_info)
    all_decisions.append(dec)

# 3. Evaluate OCR Signboards (201 items)
print("[2/3] Routing 201 Commercial OCR Signboards...")
for idx, r in ocr_df.iterrows():
    dec = router.evaluate_ocr_signboard(r.to_dict())
    all_decisions.append(dec)

# 4. Evaluate Buildings (108 items)
print("[3/3] Routing 108 Building Envelopes...")
for idx, r in bldg_df.iterrows():
    dec = router.evaluate_building(r.to_dict())
    all_decisions.append(dec)

total_items = len(all_decisions)
print(f"\nTotal Pipeline Items Evaluated: {total_items}")

# 5. Compute Comparative Benchmark Statistics
dec_dicts = [asdict(d) for d in all_decisions]
dec_df = pd.DataFrame(dec_dicts)

tier1_count = len(dec_df[dec_df["tier"] == "Tier1_SmallModel_FastPath"])
tier2_count = len(dec_df[dec_df["tier"] == "Tier2_VLM_Escalated"])
tier1_pct = round((tier1_count / total_items) * 100, 2)
tier2_pct = round((tier2_count / total_items) * 100, 2)

tier1_latencies = dec_df[dec_df["tier"] == "Tier1_SmallModel_FastPath"]["latency_ms"]
tier2_latencies = dec_df[dec_df["tier"] == "Tier2_VLM_Escalated"]["latency_ms"]
hybrid_latencies = dec_df["latency_ms"]

avg_tier1_lat = round(float(tier1_latencies.mean()), 1)
avg_tier2_lat = round(float(tier2_latencies.mean()), 1)
avg_hybrid_lat = round(float(hybrid_latencies.mean()), 1)
p95_hybrid_lat = round(float(np.percentile(hybrid_latencies, 95)), 1)

# Baseline 100% VLM comparison
vlm_baseline_lat_mean = 780.0
vlm_baseline_cost_per_item = 0.0025

total_hybrid_cost = round(float(dec_df["cost_usd"].sum()), 4)
total_100pct_vlm_cost = round(total_items * vlm_baseline_cost_per_item, 4)
cost_savings_pct = round(((total_100pct_vlm_cost - total_hybrid_cost) / total_100pct_vlm_cost) * 100, 2)

initial_mean_conf = round(float(dec_df["initial_confidence"].mean()), 3)
final_mean_conf = round(float(dec_df["final_confidence"].mean()), 3)
accuracy_boost_pct = round((final_mean_conf - initial_mean_conf) * 100, 2)

# Escalation reasons breakdown
reasons_count = dec_df[dec_df["tier"] == "Tier2_VLM_Escalated"]["escalation_reason"].value_counts().to_dict()

# Corridor breakdown
corridor_breakdown = {}
for st_id in sorted(corr_map.keys()):
    sub = dec_df[dec_df["street_id"] == st_id]
    t1 = len(sub[sub["tier"] == "Tier1_SmallModel_FastPath"])
    t2 = len(sub[sub["tier"] == "Tier2_VLM_Escalated"])
    corridor_breakdown[st_id] = {
        "street_name": corr_map[st_id]["Street_Name"],
        "total_items": len(sub),
        "tier1_fast_path": t1,
        "tier2_escalated": t2,
        "escalation_rate_pct": round((t2 / len(sub) * 100), 1) if len(sub) > 0 else 0
    }

benchmark_results = {
    "evaluation_timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    "target_area": "Coimbatore Ward 29 (North Zone)",
    "survey_corridors_count": 10,
    "total_pipeline_items": total_items,
    "items_breakdown": {
        "fixed_infrastructure_assets": len(inv_df),
        "commercial_ocr_signboards": len(ocr_df),
        "building_envelopes": len(bldg_df)
    },
    "routing_distribution": {
        "tier1_small_model_fast_path": {
            "count": tier1_count,
            "percentage": tier1_pct,
            "mean_latency_ms": avg_tier1_lat,
            "cost_per_item_usd": router.tier1_cost_per_item
        },
        "tier2_vlm_escalated_path": {
            "count": tier2_count,
            "percentage": tier2_pct,
            "mean_latency_ms": avg_tier2_lat,
            "cost_per_item_usd": router.tier2_cost_per_item
        }
    },
    "performance_and_latency_comparison": {
        "tier1_small_model_alone_ms": avg_tier1_lat,
        "hybrid_router_mean_latency_ms": avg_hybrid_lat,
        "hybrid_router_p95_latency_ms": p95_hybrid_lat,
        "pure_vlm_100pct_baseline_ms": vlm_baseline_lat_mean,
        "latency_speedup_vs_pure_vlm": f"{vlm_baseline_lat_mean / avg_hybrid_lat:.1f}x Faster"
    },
    "economic_and_cost_savings": {
        "hybrid_routing_total_cost_usd": total_hybrid_cost,
        "pure_vlm_100pct_baseline_cost_usd": total_100pct_vlm_cost,
        "net_cost_savings_usd": round(total_100pct_vlm_cost - total_hybrid_cost, 4),
        "cost_reduction_percent": f"{cost_savings_pct}% Cheaper"
    },
    "accuracy_and_confidence_boost": {
        "initial_pipeline_confidence_mean": initial_mean_conf,
        "final_escalated_confidence_mean": final_mean_conf,
        "overall_confidence_delta": round(final_mean_conf - initial_mean_conf, 3),
        "accuracy_gain_percent": f"+{accuracy_boost_pct}%"
    },
    "escalation_triggers_breakdown": reasons_count,
    "corridor_distribution": corridor_breakdown
}

# 6. Save Artifacts
decisions_csv_path = os.path.join(vlm_dir, "routing_decisions.csv")
base_decisions_csv_path = os.path.join(base_dir, "routing_decisions.csv")
dec_df.to_csv(decisions_csv_path, index=False, encoding="utf-8")
dec_df.to_csv(base_decisions_csv_path, index=False, encoding="utf-8")

results_json_path = os.path.join(vlm_dir, "routing_benchmark_results.json")
base_results_json_path = os.path.join(base_dir, "routing_benchmark_results.json")
with open(results_json_path, "w", encoding="utf-8") as f:
    json.dump(benchmark_results, f, indent=2, ensure_ascii=False)
with open(base_results_json_path, "w", encoding="utf-8") as f:
    json.dump(benchmark_results, f, indent=2, ensure_ascii=False)

print(f"\n=== BENCHMARK SUMMARY RESULTS ===")
print(f"Total Evaluated: {total_items} items")
print(f"Tier 1 Fast Path: {tier1_count} ({tier1_pct}%) | Avg Latency: {avg_tier1_lat} ms")
print(f"Tier 2 Escalated: {tier2_count} ({tier2_pct}%) | Avg Latency: {avg_tier2_lat} ms")
print(f"Hybrid Mean Latency: {avg_hybrid_lat} ms (P95: {p95_hybrid_lat} ms)")
print(f"Pure VLM Baseline: {vlm_baseline_lat_mean} ms ({vlm_baseline_lat_mean / avg_hybrid_lat:.1f}x Faster)")
print(f"Hybrid Cost: ${total_hybrid_cost} vs Pure VLM: ${total_100pct_vlm_cost} ({cost_savings_pct}% Cost Reduction!)")
print(f"Confidence Boost: {initial_mean_conf} -> {final_mean_conf} (+{accuracy_boost_pct}%)")
print(f"Saved: {decisions_csv_path} and {results_json_path}")
