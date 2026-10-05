---
id: "alp-analyze-ethos-u-models-with-mlia-2-install-and-discover-discover-target-profiles"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Install MLIA and discover capabilities: Discover target profiles"
summary: "MLIA target profiles describe the target configuration used for analysis. List the target profiles available in your environment:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/2-install-and-discover.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/2-install-and-discover/#discover-target-profiles"
license: "CC-BY-SA-4.0"
mode: "V"
---

MLIA target profiles describe the target configuration used for analysis. List the target profiles available in your environment:

```bash
mlia target list
```

For Ethos-U, typical bundled profiles include:

| Target profile | Ethos-U NPU | Multiply-accumulates per cycle |
| --- | --- | --- |
| `ethos-u55-128` | Ethos-U55 | 128 |
| `ethos-u55-256` | Ethos-U55 | 256 |
| `ethos-u65-256` | Ethos-U65 | 256 |
| `ethos-u65-512` | Ethos-U65 | 512 |
| `ethos-u85-128` | Ethos-U85 | 128 |
| `ethos-u85-256` | Ethos-U85 | 256 |
| `ethos-u85-512` | Ethos-U85 | 512 |
| `ethos-u85-1024` | Ethos-U85 | 1024 |
| `ethos-u85-2048` | Ethos-U85 | 2048 |


`ethos-u85-256` is the Ethos-U85 profile that's used in the examples. If you want MLIA to evaluate the same model for a different Ethos-U configuration, use a different profile.
