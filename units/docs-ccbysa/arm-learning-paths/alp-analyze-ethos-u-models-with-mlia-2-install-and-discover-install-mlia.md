---
id: "alp-analyze-ethos-u-models-with-mlia-2-install-and-discover-install-mlia"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Install MLIA and discover capabilities: Install MLIA"
summary: "MLIA uses plugins. The example target in the Learning Path is Ethos-U, so install the Ethos-U plugin package:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/2-install-and-discover.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/2-install-and-discover/#install-mlia"
license: "CC-BY-SA-4.0"
mode: "V"
---

MLIA uses plugins. The example target in the Learning Path is Ethos-U, so install the Ethos-U plugin package:

```bash
pip install mlia-ethos-u
```

The Ethos-U plugin package depends on a compatible MLIA core package. Installing the target plugin is the recommended starting point because it brings in the matching MLIA core dependency.
