---
id: "mlek-inference-runner-code-sample-introduction"
type: "concept"
domain: "edge-ai"
title: "Inference Runner Code Sample: Introduction"
summary: "This document describes the process of setting up and running the Arm® Ethos™-U NPU Inference Runner."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/use_cases/inference_runner.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/inference_runner.md#introduction"
license: "Apache-2.0"
mode: "V"
---

This document describes the process of setting up and running the Arm® *Ethos™-U* NPU Inference Runner.

The inference runner is intended for quickly checking profiling results for any wanted network, providing it has been
processed by the Vela compiler.

A simple model is provided with the Inference Runner as an example. However, we expect you to replace this model with
one that you must profile.

For further details, refer to: [Add custom model](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/./inference_runner.md#Add-custom-model).

The inference runner populates all input tensors for the provided model with randomly generated data and an inference is
then performed. Profiling results are then displayed in the console.

The example use-case code can be found in the following directory:
[source/app/use_case/inference_runner](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../../source/app/use_case/inference_runner).

> **NOTE**: This use case only supports `TensorFlow Lite Micro`.

### Prerequisites

See [Prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../documentation.md#prerequisites)
