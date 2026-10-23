---
id: "etarm-executorch-arm-readme-person-detection-example-on-cortex-m"
type: "concept"
domain: "edge-ai"
title: "executorch-arm README: Person detection example on Cortex-M"
summary: "This example demonstrates training, A8W8 quantization, exporting, and deployment of a person detection model based on microYOLO: Towards Single-Shot Object Detection on Microcontrollers [1] in a small demo application using the ExecuTorch Cortex-M backend."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:examples/arm/person_detection_example_cortex_m/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/examples/arm/person_detection_example_cortex_m/README.md#person-detection-example-on-cortex-m"
license: "BSD-3-Clause"
mode: "V"
---

(figure: example)

This example demonstrates training, A8W8 quantization, exporting, and deployment of a person detection model based on [microYOLO: Towards Single-Shot Object Detection on Microcontrollers](https://arxiv.org/pdf/2408.15865) [1] in a small demo application using the ExecuTorch Cortex-M backend. The final product is a real-time streaming video with bounding boxes and a confidence score for all detected people in the frame, running on the Arm Corstone-300 FVP with simulated video and screen interfaces.

Before you begin, install Executorch and relevant Cortex-M dependencies according to the [documentation](https://docs.pytorch.org/executorch/stable/backends/arm-cortex-m/arm-cortex-m-overview.html). Additional pip packages required for the demo are listed in `requirements.txt`. All python scripts by default use the output from the previous script and working default parameters, run them with `--help` to see the full list of options. All intermediate artifacts produced are described in `utils/artifacts.py`.
