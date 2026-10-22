---
id: "cet-executorch-on-ethos-u-adapting-the-template"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch on Ethos-U: Adapting the template"
summary: "To use a different ML model, replace or modify model/model.py and update the ML model name or input handling as required: get_model(input_shape) builds the ML model for the input-shape of the mlops: node, and get_calibration_inputs(input_shape, calibration_samples) returns the …"
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/README.md#adapting-the-template"
license: "Apache-2.0"
mode: "V"
---

To use a different ML model, replace or modify `model/model.py` and update the
ML model name or input handling as required: `get_model(input_shape)` builds the
ML model for the `input-shape` of the `mlops:` node, and
`get_calibration_inputs(input_shape, calibration_samples)` returns the samples
the quantizer is calibrated with; give it representative data for a trained
ML model. The runner in `src/app_main.cpp` builds its input tensor with the same
fixed shape and prints the output as ten floats, so an ML model with another
input shape or output needs matching changes there. Then re-run
`create_ai_layer.py` and build.

Give a vision ML model its input as NHWC, the layout of a camera frame, as
`model/model.py` does: the ML model permutes it to the NCHW its convolutions take,
and Vela folds that into the first convolution. With an NCHW input the NPU
first reorders the image in an operation of its own.

To target another Ethos-U configuration, update the target and `mlops:`
settings in the CMSIS solution and re-run all three steps. The generated Vela
options then follow that configuration automatically; `vela: misc:` takes any
further Vela option, for example `--optimise Size`. Moving to a different
board or reference platform also requires the corresponding device pack, board
support, memory layout, and FVP configuration.

When updating ExecuTorch, update the pack and Python package versions
together. More information is available in
[ExecuTorch pack maintenance and versioning](https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/documentation/executorch-pack-maintenance.md).
