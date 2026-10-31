# genpark-personal-agent-sleep-slow-wave-delta-power-glymphatic-clearance-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Polysomnography EEG slow-wave activity (SWA) delta band power density and nocturnal glymphatic metabolite clearance auditor.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `evaluate_sleep_slow_wave_glymphatic_clearance`
- **Category**: `personal_agent`

### Method Documentation
Evaluate nocturnal brain waste clearance via EEG Slow-Wave Activity (SWA) delta band power (0.5 - 4.0 Hz).
Nocturnal interstitial fluid-cerebrospinal fluid (ISF-CSF) convective exchange reaches its maximum during synchronized N3 delta sleep.
Computes integrated delta power area, cycle-to-cycle exponential decay dissipation, and amyloid/tau clearance adequacy quotient.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "evaluate_sleep_slow_wave_glymphatic_clearance",
    "arguments": {
    "n3_duration_minutes": 95,
    "total_sleep_minutes": 460,
    "delta_power_uV2_per_cycle": [
        115.0,
        92.0,
        78.0,
        60.0
    ],
    "sleep_efficiency_percent": 91.5
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
