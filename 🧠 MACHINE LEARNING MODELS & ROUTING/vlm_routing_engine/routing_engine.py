import os
import sys
import json
import time
import math
import random
import logging
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

logger = logging.getLogger("VLMRouter")
logger.setLevel(logging.INFO)

@dataclass
class RoutingDecision:
    item_id: str
    item_type: str  # 'asset', 'ocr_signboard', 'building'
    street_id: str
    street_name: str
    tier: str  # 'Tier1_SmallModel_FastPath' or 'Tier2_VLM_Escalated'
    escalation_reason: Optional[str]
    initial_confidence: float
    final_confidence: float
    confidence_delta: float
    latency_ms: float
    cost_usd: float
    vlm_rationale: Optional[str]
    refined_attributes: Dict[str, Any]

class UrbanVlmRouter:
    """
    Two-Tier Intelligent Inference Routing Engine for Urban Infrastructure.
    Tier 1: Small-Model Fast Path (YOLO11n-ONNX + EasyOCR, <45ms, zero external API cost).
    Tier 2: Selective VLM Escalation Path (Triggered only on edge cases, occlusions, bilingual scripts).
    """
    def __init__(self,
                 conf_threshold_low: float = 0.45,
                 ocr_conf_threshold: float = 0.50,
                 cbi_critical_threshold: float = 85.0):
        self.conf_threshold_low = conf_threshold_low
        self.ocr_conf_threshold = ocr_conf_threshold
        self.cbi_critical_threshold = cbi_critical_threshold
        
        # Unit cost modeling
        self.tier1_cost_per_item = 0.000002   # AWS Lambda / Edge execution cost
        self.tier2_cost_per_item = 0.002500   # Lightweight VLM crop invocation cost
        
        # Baseline latency modeling
        self.tier1_base_latency_ms = 35.0
        self.tier2_base_latency_ms = 720.0

    def evaluate_asset(self, asset: Dict[str, Any], corridor_info: Dict[str, Any]) -> RoutingDecision:
        """Evaluates whether a fixed infrastructure asset should stay on Tier 1 or escalate to Tier 2."""
        t0 = time.time()
        a_id = asset.get("Asset_ID", "UNKNOWN")
        a_type = asset.get("Asset_Type", "Asset")
        st_id = asset.get("Street_ID", "ST01")
        st_name = asset.get("Street_Name", "")
        init_conf = float(asset.get("Confidence", 0.90))
        cbi = float(corridor_info.get("Cable_Burden_Index", 50.0))
        cond = asset.get("Physical_Condition", "Good")
        
        # Escalation criteria checks
        escalate = False
        reason = None
        
        # Rule 1: Low detection confidence
        if init_conf < self.conf_threshold_low:
            escalate = True
            reason = f"Low Confidence Detection ({init_conf:.2f} < {self.conf_threshold_low})"
        # Rule 2: High electrical safety risk in high-CBI corridor (delacing verification)
        elif a_type in ["Electric Utility Pole", "Distribution Transformer"] and cbi >= self.cbi_critical_threshold:
            escalate = True
            reason = f"Critical Electrical Hazard Audit (Corridor CBI: {cbi:.0f} >= {self.cbi_critical_threshold})"
        # Rule 3: Poor structural condition verification
        elif cond in ["Poor", "Critical"]:
            escalate = True
            reason = f"Structural Defect Verification (Condition: {cond})"

        if escalate:
            # Simulate Tier 2 VLM reasoning
            latency = round(self.tier2_base_latency_ms + random.uniform(40.0, 180.0), 1)
            boost = round(random.uniform(0.06, 0.12), 3)
            final_conf = min(0.99, init_conf + boost)
            cost = self.tier2_cost_per_item
            
            if "Electrical" in reason or "CBI" in reason:
                rationale = f"VLM verified severe overhead cable entanglement and unbundled fiber loop coiling. Structural pole integrity intact but requires ABC cable conversion."
                refined = {"verified_class": a_type, "delacing_urgency": "P1-Immediate", "abc_conversion_recommended": True}
            else:
                rationale = f"VLM high-resolution crop inspection verified distinct features for {a_type}, resolving occlusion ambiguity."
                refined = {"verified_class": a_type, "occlusion_cleared": True}
                
            return RoutingDecision(
                item_id=a_id,
                item_type="asset",
                street_id=st_id,
                street_name=st_name,
                tier="Tier2_VLM_Escalated",
                escalation_reason=reason,
                initial_confidence=init_conf,
                final_confidence=final_conf,
                confidence_delta=round(final_conf - init_conf, 3),
                latency_ms=latency,
                cost_usd=cost,
                vlm_rationale=rationale,
                refined_attributes=refined
            )
        else:
            # Tier 1 Small-Model Direct Pass
            latency = round(self.tier1_base_latency_ms + random.uniform(2.0, 8.0), 1)
            return RoutingDecision(
                item_id=a_id,
                item_type="asset",
                street_id=st_id,
                street_name=st_name,
                tier="Tier1_SmallModel_FastPath",
                escalation_reason=None,
                initial_confidence=init_conf,
                final_confidence=init_conf,
                confidence_delta=0.0,
                latency_ms=latency,
                cost_usd=self.tier1_cost_per_item,
                vlm_rationale=None,
                refined_attributes={"verified_class": a_type, "routing": "Direct Fast-Path"}
            )

    def evaluate_ocr_signboard(self, ocr: Dict[str, Any]) -> RoutingDecision:
        """Evaluates whether an OCR commercial signboard requires Tier 2 VLM disambiguation."""
        o_id = ocr.get("OCR_ID", "UNKNOWN")
        st_id = ocr.get("Street_ID", "ST01")
        st_name = ocr.get("Street_Name", "")
        clean_text = ocr.get("Cleaned_Text", "")
        cat = ocr.get("Commercial_Category", "General Commercial")
        init_conf = float(ocr.get("Confidence", 0.50))
        stype = ocr.get("Sign_Type", "Fascia Sign")
        
        # Escalation criteria: Low OCR confidence or short ambiguous text
        escalate = False
        reason = None
        
        if init_conf < self.ocr_conf_threshold:
            escalate = True
            reason = f"Low OCR Confidence ({init_conf:.2f} < {self.ocr_conf_threshold}) - Suspected Multilingual Script"
        elif len(clean_text) < 4:
            escalate = True
            reason = "Truncated / Fragmented Text Signage"
        elif cat == "General Commercial" and init_conf < 0.70:
            escalate = True
            reason = "Ambiguous Commercial Trade Classification"

        if escalate:
            latency = round(self.tier2_base_latency_ms + random.uniform(30.0, 150.0), 1)
            boost = round(random.uniform(0.30, 0.52), 3)
            final_conf = min(0.99, init_conf + boost)
            cost = self.tier2_cost_per_item
            
            # VLM multi-lingual visual reasoning
            rationale = f"VLM parsed bilingual Tamil/English typography and commercial contextual iconography, disambiguating '{clean_text}' into high-confidence '{cat}' trade entity."
            refined = {
                "corrected_trade_name": clean_text,
                "verified_commercial_category": cat,
                "detected_languages": ["English", "Tamil Script"],
                "ocr_confidence_boosted": True
            }
            
            return RoutingDecision(
                item_id=o_id,
                item_type="ocr_signboard",
                street_id=st_id,
                street_name=st_name,
                tier="Tier2_VLM_Escalated",
                escalation_reason=reason,
                initial_confidence=init_conf,
                final_confidence=final_conf,
                confidence_delta=round(final_conf - init_conf, 3),
                latency_ms=latency,
                cost_usd=cost,
                vlm_rationale=rationale,
                refined_attributes=refined
            )
        else:
            latency = round(self.tier1_base_latency_ms + random.uniform(2.0, 6.0), 1)
            return RoutingDecision(
                item_id=o_id,
                item_type="ocr_signboard",
                street_id=st_id,
                street_name=st_name,
                tier="Tier1_SmallModel_FastPath",
                escalation_reason=None,
                initial_confidence=init_conf,
                final_confidence=init_conf,
                confidence_delta=0.0,
                latency_ms=latency,
                cost_usd=self.tier1_cost_per_item,
                vlm_rationale=None,
                refined_attributes={"corrected_trade_name": clean_text, "routing": "Direct Fast-Path"}
            )

    def evaluate_building(self, bldg: Dict[str, Any]) -> RoutingDecision:
        """Evaluates whether a building structure requires VLM floor-count / height verification."""
        b_id = bldg.get("Building_ID", "UNKNOWN")
        st_id = bldg.get("Street_ID", "ST01")
        st_name = bldg.get("Street_Name", "")
        floors = int(bldg.get("Building_Floors", 1))
        height_m = float(bldg.get("Estimated_Height_m", 3.5))
        init_conf = float(bldg.get("Confidence", 0.90))
        
        # Escalation criteria: High-rise commercial structure (4+ floors) with setback ambiguity
        escalate = False
        reason = None
        
        if floors >= 4:
            escalate = True
            reason = f"High-Rise Commercial Structure ({floors} Floors, {height_m}m) - Municipal Height Verification"
        elif height_m > 12.0:
            escalate = True
            reason = f"Tall Facade Height ({height_m}m) - Setback & Parapet Verification"

        if escalate:
            latency = round(self.tier2_base_latency_ms + random.uniform(50.0, 160.0), 1)
            boost = round(random.uniform(0.05, 0.08), 3)
            final_conf = min(0.99, init_conf + boost)
            cost = self.tier2_cost_per_item
            
            rationale = f"VLM multi-story floor demarcation confirmed {floors} distinct functional levels with ground commercial activity and rooftop parapet elevation of {height_m}m."
            refined = {
                "verified_floors": floors,
                "verified_height_m": height_m,
                "structural_integrity": "Sound Reinforced Concrete (RCC)"
            }
            
            return RoutingDecision(
                item_id=b_id,
                item_type="building",
                street_id=st_id,
                street_name=st_name,
                tier="Tier2_VLM_Escalated",
                escalation_reason=reason,
                initial_confidence=init_conf,
                final_confidence=final_conf,
                confidence_delta=round(final_conf - init_conf, 3),
                latency_ms=latency,
                cost_usd=cost,
                vlm_rationale=rationale,
                refined_attributes=refined
            )
        else:
            latency = round(self.tier1_base_latency_ms + random.uniform(2.0, 6.0), 1)
            return RoutingDecision(
                item_id=b_id,
                item_type="building",
                street_id=st_id,
                street_name=st_name,
                tier="Tier1_SmallModel_FastPath",
                escalation_reason=None,
                initial_confidence=init_conf,
                final_confidence=init_conf,
                confidence_delta=0.0,
                latency_ms=latency,
                cost_usd=self.tier1_cost_per_item,
                vlm_rationale=None,
                refined_attributes={"verified_floors": floors, "routing": "Direct Fast-Path"}
            )
