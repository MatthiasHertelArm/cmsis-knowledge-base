---
id: "etarm-executorch-arm-readme-person-detection-example-on-cortex-m"
type: "concept"
domain: "edge-ai"
title: "executorch-arm README: Person detection example on Cortex-M"
summary: "This example demonstrates training, exporting and deployment of a person detection model based on microYOLO: Towards Single-Shot Object Detection on Microcontrollers [1] in a small demo application."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/person_detection_example_cortex_m/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/person_detection_example_cortex_m/README.md#person-detection-example-on-cortex-m"
license: "BSD-3-Clause"
mode: "V"
---

This example demonstrates training, exporting and deployment of a person detection model based on [microYOLO: Towards Single-Shot Object Detection on Microcontrollers](https://arxiv.org/pdf/2408.15865) [1] in a small demo application.

Before you begin, install Executorch and relevant Cortex-M dependencies according to the [documentation](https://docs.pytorch.org/executorch/stable/backends/arm-cortex-m/arm-cortex-m-overview.html). Additional pip packages required for the demo are listed in `requirements.txt`.
