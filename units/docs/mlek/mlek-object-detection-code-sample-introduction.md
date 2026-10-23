---
id: "mlek-object-detection-code-sample-introduction"
type: "concept"
domain: "edge-ai"
title: "Object Detection Code Sample: Introduction"
summary: "This document describes the process of setting up and running the Arm® Ethos™-U NPU Object Detection example. Object Detection is a classical computer vision use case in which specific objects need to be identified and located within a full frame."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/object_detection.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/object_detection.md#introduction"
license: "Apache-2.0"
mode: "V"
---

This document describes the process of setting up and running the Arm® *Ethos™-U* NPU Object Detection example.
Object Detection is a classical computer vision use case in which specific objects need to be identified and located
within a full frame. In this specific example the model was trained for face detection. The ML sample was developed
using the *YOLO Fastest* model.  To adopt the model for low power / low memory systems the input images to the model
are monochrome images. The model was trained on the *Wider* dataset (after conversion from RGB to monochrome)
and on *Emza Visual-Sense* dataset `<www.emza-vs.com>`.
The model makes detection faces in size of 20x20 pixels and above.

Use-case code could be found in the following directory: [source/app/use_case/object_detection](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../../source/app/use_case/object_detection).

> **NOTE**: This use case only supports `TensorFlow Lite Micro`.

### Prerequisites

See [Prerequisites](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#prerequisites)
