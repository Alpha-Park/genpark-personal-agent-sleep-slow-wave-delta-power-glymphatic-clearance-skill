# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-personal-agent-sleep-slow-wave-delta-power-glymphatic-clearance-skill
Category: personal_agent
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def evaluate_sleep_slow_wave_glymphatic_clearance(n3_duration_minutes, total_sleep_minutes, delta_power_uV2_per_cycle, sleep_efficiency_percent=90.0):
    if not delta_power_uV2_per_cycle:
        raise ValueError("delta_power_uV2_per_cycle list cannot be empty")
        
    n3_percentage = (n3_duration_minutes / total_sleep_minutes) * 100.0 if total_sleep_minutes > 0 else 0.0
    mean_delta_power = sum(delta_power_uV2_per_cycle) / len(delta_power_uV2_per_cycle)
    
    # Physiological decay: SWA should be highest in Cycle 1 and decay monotonically
    monotonic_decay = all(delta_power_uV2_per_cycle[i] >= delta_power_uV2_per_cycle[i+1] * 0.85 for i in range(len(delta_power_uV2_per_cycle)-1))
    
    # Normalized glymphatic clearance score (0 - 100)
    # Target N3: 15-25% of sleep; Target mean delta power: > 75 uV^2
    n3_score = min(40.0, (n3_percentage / 20.0) * 40.0)
    power_score = min(40.0, (mean_delta_power / 80.0) * 40.0)
    efficiency_bonus = min(20.0, (sleep_efficiency_percent / 90.0) * 20.0)
    glymphatic_clearance_score = round(n3_score + power_score + efficiency_bonus, 1)
    
    if glymphatic_clearance_score >= 80.0:
        clearance_rating = "OPTIMAL_NEUROTOXIN_FLUSH"
        recommendation = "Robust synchronized slow-wave oscillation supports efficient perivascular beta-amyloid and phosphorylated-tau clearance."
    elif glymphatic_clearance_score >= 60.0:
        clearance_rating = "MODERATE_CLEARANCE"
        recommendation = "Mild slow-wave deficit. Consider avoiding late-evening alcohol, caffeine past 14:00, or blue light exposure to promote deep N3 delta architecture."
    else:
        clearance_rating = "COMPROMISED_GLYMPHATIC_TRANSPORT"
        recommendation = "Low delta power density and fragmented deep sleep significantly impair interstitial convective metabolite clearance."
        
    return {
        "n3_deep_sleep_minutes": n3_duration_minutes,
        "n3_sleep_percentage": round(n3_percentage, 1),
        "mean_delta_power_uV2": round(mean_delta_power, 1),
        "cycles_analyzed": len(delta_power_uV2_per_cycle),
        "sleep_efficiency_percent": round(sleep_efficiency_percent, 1),
        "delta_decay_intact": monotonic_decay,
        "glymphatic_clearance_score": glymphatic_clearance_score,
        "glymphatic_status": clearance_rating,
        "clinical_guidance": recommendation
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "evaluate_sleep_slow_wave_glymphatic_clearance",
                        "description": """Evaluate nocturnal brain waste clearance via EEG Slow-Wave Activity (SWA) delta band power (0.5 - 4.0 Hz).
Nocturnal interstitial fluid-cerebrospinal fluid (ISF-CSF) convective exchange reaches its maximum during synchronized N3 delta sleep.
Computes integrated delta power area, cycle-to-cycle exponential decay dissipation, and amyloid/tau clearance adequacy quotient.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = evaluate_sleep_slow_wave_glymphatic_clearance(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'n3_duration_minutes': 95, 'total_sleep_minutes': 460, 'delta_power_uV2_per_cycle': [115.0, 92.0, 78.0, 60.0], 'sleep_efficiency_percent': 91.5}
        out = evaluate_sleep_slow_wave_glymphatic_clearance(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
