---
id: "etarm-mobilesam-prompt-segmentation-on-e-limitations"
type: "concept"
domain: "edge-ai"
title: "MobileSAM Prompt Segmentation on Ethos-U: Limitations"
summary: "See model export and runtime for details of each stage."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:examples/arm/mobilesam_prompt_segmentation_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/README.md#limitations"
license: "BSD-3-Clause"
mode: "V"
---

- The exported model accepts one image tensor and uses one fixed positive point.
- It returns a low-resolution mask. Upsampling and thresholding are host-side
  post-processing.
- The demo image is also the calibration image. Product use requires a
  representative calibration set.
- The default fast FVP mode validates correctness. Its counters are not a
  performance benchmark or a measurement of real-device latency.

See [model export](https://github.com/pytorch/executorch/blob/658390c/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/README.md) and
[runtime](https://github.com/pytorch/executorch/blob/658390c/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/runtime/README.md) for details of each stage.
