---
id: "etarm-image-classification-example-appli"
type: "concept"
domain: "edge-ai"
title: "Image Classification Example Application"
summary: "This end-to-end example shows how to use the Arm backend in ExecuTorch across both ahead-of-time (AoT) and runtime flows. It covers this by providing examples of:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/image_classification_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/image_classification_example_ethos_u/README.md"
license: "BSD-3-Clause"
mode: "V"
---

This end-to-end example shows how to use the Arm backend in ExecuTorch across both ahead-of-time (AoT) and runtime flows. It covers
this by providing examples of:

- Scripts to fine-tune a DeiT-Tiny model on the Oxford-IIIT Pet dataset, quantize it, and export an Ethos-U–ready ExecuTorch program.
- A simple bare-metal image-classification app for Corstone-320 (Ethos-U85-256) that embeds the exported program and a sample image.
- Running the app on the Corstone-320 Fixed Virtual Platform (FVP).
