---
id: "alp-analyze-ethos-u-models-with-mlia-6-python-api-discover-capabilities-from-pyt"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: (Optional) Use the MLIA Python API: Discover capabilities from Python"
summary: "MLIA also exposes helper functions for discovery. Depending on the installed MLIA version, useful helpers can include the following:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/6-python-api.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/6-python-api/#discover-capabilities-from-python"
license: "CC-BY-SA-4.0"
mode: "V"
---

MLIA also exposes helper functions for discovery. Depending on the installed MLIA version, useful helpers can include the following:

```bash
cat > discover_mlia.py <<'PY'
from mlia import list_backends, list_target_profiles, list_targets


print(list_targets())
print(list_target_profiles())
print(list_backends())
PY
```

Run the discovery script:

```bash
python discover_mlia.py
```

Use discovery in integrations so that your product can report what the current environment supports.
