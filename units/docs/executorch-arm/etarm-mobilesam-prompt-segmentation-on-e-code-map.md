---
id: "etarm-mobilesam-prompt-segmentation-on-e-code-map"
type: "concept"
domain: "edge-ai"
title: "MobileSAM Prompt Segmentation on Ethos-U: Code Map"
summary: "There is no MobileSAM-specific C++ runtime or CMake project."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:examples/arm/mobilesam_prompt_segmentation_example_ethos_u/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/README.md#code-map"
license: "BSD-3-Clause"
mode: "V"
---

- [`prepare_mobilesam.py`](https://github.com/pytorch/executorch/blob/6368414/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/prepare_mobilesam.py) fetches and
  verifies the external model.
- [`export_mobilesam.py`](https://github.com/pytorch/executorch/blob/6368414/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/model_export/export_mobilesam.py) contains the model,
  quantization, validation, and lowering flow.
- [`run.sh`](https://github.com/pytorch/executorch/blob/6368414/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/run.sh) uses ExecuTorch's standard Arm runner for target execution.
- [`visualize_fvp_output.py`](https://github.com/pytorch/executorch/blob/6368414/examples/arm/mobilesam_prompt_segmentation_example_ethos_u/runtime/visualize_fvp_output.py) checks and plots
  the raw output tensor.

There is no MobileSAM-specific C++ runtime or CMake project.
