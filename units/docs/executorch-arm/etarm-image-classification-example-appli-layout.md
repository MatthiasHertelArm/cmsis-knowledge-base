---
id: "etarm-image-classification-example-appli-layout"
type: "concept"
domain: "edge-ai"
title: "Image Classification Example Application: Layout"
summary: "The example is divided into two sections:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/image_classification_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/image_classification_example_ethos_u/README.md#layout"
license: "BSD-3-Clause"
mode: "V"
---

The example is divided into two sections:

- `model_export/README.md` — Covers fine-tuning a model for a new usecase, quantization to INT8, lowering to Ethos-U via ExecuTorch and `.pte` generation.
- `runtime/README.md` — Covers building the bare-metal app, generating headers from the `.pte` and image, and running on the FVP.
