---
id: "alp-analyze-ethos-u-models-with-mlia-1-overview-why-use-mlia"
type: "concept"
domain: "edge-ai"
title: "Analyze machine learning models for Arm Ethos-U with Arm ML Inference Advisor: Understand where MLIA fits in model preparation: Why use MLIA"
summary: "Use Arm ML Inference Advisor (MLIA) to evaluate whether a machine learning model is suitable for a target inference platform."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/1-overview.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/1-overview/#why-use-mlia"
license: "CC-BY-SA-4.0"
mode: "V"
---

Use Arm ML Inference Advisor (MLIA) to evaluate whether a machine learning model is suitable for a target inference platform.

MLIA is most useful before full deployment or runtime profiling, when you're asking questions such as:

- Will this model map cleanly to my target?
- Which operators or layers are likely to matter most for performance?
- Is the model compute-bound, memory-bound, or affected by low multiply-accumulate (MAC) utilization?
- Is the model well-optimized for my Arm target hardware?
- What should I investigate before building firmware or running on a board?

MLIA doesn't make the final optimization decision for you. It gives target-aware evidence so that you can decide what to change, what to measure next, and which workflow stage deserves attention.

You'll use the CLI to complete the following tasks:

- Discover installed targets, target profiles, and backends
- Run compatibility checks
- Run performance analysis
- Inspect advice and metrics

Arm Ethos-U is the example target in the Learning Path.

If you want to automate the same checks, you can [optionally use the Python API](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/6-python-api/). The API is useful when you want to embed MLIA results in another product, dashboard, CI job, or tool.
