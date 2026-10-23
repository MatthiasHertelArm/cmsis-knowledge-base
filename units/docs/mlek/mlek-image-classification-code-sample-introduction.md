---
id: "mlek-image-classification-code-sample-introduction"
type: "concept"
domain: "edge-ai"
title: "Image Classification Code Sample: Introduction"
summary: "This document describes the process of setting up and running the Arm® Ethos™-U NPU Image Classification example."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/img_class.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/img_class.md#introduction"
license: "Apache-2.0"
mode: "V"
---

This document describes the process of setting up and running the Arm® *Ethos™-U* NPU Image Classification example.

This use-case example solves the classical computer vision problem of image classification. The ML sample works with
the *MobileNet v2* model with TensorFlow Lite Micro, or either the *MobileNet v2* or *DeiT tiny* model with ExecuTorch.
These models were both trained with the *ImageNet* dataset, and the overall pipeline is the same for both models.

Use-case code could be found in the following directory: [source/app/use_case/img_class](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../../source/app/use_case/img_class).

### Prerequisites

See [Prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#prerequisites)
