---
id: "alp-analyze-ethos-u-models-with-mlia-2-install-and-discover-discover-backends"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Install MLIA and discover capabilities: Discover backends"
summary: "Backends perform the work behind an MLIA analysis flow. List available and installed backends:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/2-install-and-discover.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/2-install-and-discover/#discover-backends"
license: "CC-BY-SA-4.0"
mode: "V"
---

Backends perform the work behind an MLIA analysis flow. List available and installed backends:

```bash
mlia backend list
```

For this Ethos-U demonstration, expect Vela and Corstone backend options:

```output
Name          Installed  Installable
corstone-300  no         yes
corstone-310  no         yes
corstone-320  no         yes
vela          no         yes
```

Use Vela for LiteRT and Tensor Operator Set Architecture (TOSA) checks. Use Corstone for packaged ExecuTorch `.pte` checks.

When you later use `mlia check`, any missing backends required by your target will be installed.
