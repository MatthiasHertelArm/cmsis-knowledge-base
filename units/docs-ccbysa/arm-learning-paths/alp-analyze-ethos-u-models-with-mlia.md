---
id: "alp-analyze-ethos-u-models-with-mlia"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor"
summary: "Use Arm ML Inference Advisor (MLIA) from the command line to check model compatibility, estimate performance, and identify target-aware model improvement opportunities for Ethos-U."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/_index.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/"
license: "CC-BY-SA-4.0"
mode: "V"
---

Use Arm ML Inference Advisor (MLIA) from the command line to check model compatibility, estimate performance, and identify target-aware model improvement opportunities for Ethos-U.

**Who is this for:** This Learning Path is for ML developers who want to use the Arm ML Inference Advisor (MLIA) to evaluate whether a model is suitable for a target before moving into deployment, graph inspection, or runtime profiling.

**Learning objectives:**

- Use the MLIA CLI to discover target profiles and backends.
- Run compatibility and performance analysis on LiteRT, Tensor Operator Set Architecture (TOSA), and ExecuTorch artifacts.
- Interpret MLIA JSON output, advice, Vela estimates, and Corstone whole-model NPU performance counters.
- (Optional) Call the MLIA Python API from automation or other tools.

**Prerequisites:**

- Ubuntu 22.04 LTS or another compatible Linux environment
- Python 3.10 or later
- Git and Git Large File Storage (LFS) to download the model artifacts
- Basic familiarity with machine learning model deployment concepts
- Basic familiarity with command-line tools

**Steps:**

1. Understand where MLIA fits in model preparation
2. Install MLIA and discover capabilities
3. Analyze LiteRT artifacts with MLIA and Vela
4. Analyze TOSA IR artifacts with MLIA and Vela
5. Analyze ExecuTorch artifacts with MLIA and Corstone
6. (Optional) Use the MLIA Python API

Time: about 45 minutes.
