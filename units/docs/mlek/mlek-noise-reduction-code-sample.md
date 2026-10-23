---
id: "mlek-noise-reduction-code-sample"
type: "concept"
domain: "edge-ai"
title: "Noise Reduction Code Sample"
summary: "Noise Reduction Code Sample"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/noise_reduction.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/noise_reduction.md"
license: "Apache-2.0"
mode: "V"
---

- [Noise Reduction Code Sample](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#noise-reduction-code-sample)
  - [Introduction](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#introduction)
  - [How the default neural network model works](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#how-the-default-neural-network-model-works)
  - [Post-processing](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#post_processing)
    - [Dumping of memory contents from the Fixed Virtual Platform](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#dumping-of-memory-contents-from-the-fixed-virtual-platform)
    - [Dumping post processed results for all inferences](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#dumping-post_processed-results-for-all-inferences)
  - [Prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#prerequisites)
  - [Building the code sample application from sources](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#building-the-code-sample-application-from-sources)
    - [Build options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#build-options)
    - [Build process](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#build-process)
    - [Add custom input](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#add-custom-input)
    - [Add custom model](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#add-custom-model)
  - [Setting up and running Ethos-U NPU code sample](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#setting-up-and-running-ethos_u-npu-code-sample)
    - [Setting up the Ethos-U NPU Fast Model](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#setting-up-the-ethos_u-npu-fast-model)
    - [Starting Fast Model simulation](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#starting-fast-model-simulation)
    - [Running Noise Reduction](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#running-noise-reduction)
