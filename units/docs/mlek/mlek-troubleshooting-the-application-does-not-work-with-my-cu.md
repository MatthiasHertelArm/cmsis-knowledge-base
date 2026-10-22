---
id: "mlek-troubleshooting-the-application-does-not-work-with-my-cu"
type: "concept"
domain: "edge-ai"
title: "Troubleshooting: The application does not work with my custom model"
summary: "For TensorFlow Lite Micro, ensure that your model is in a fully quantized .tflite file format, either uint8 or int8, and that it has successfully been run through the Vela compiler."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/troubleshooting.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/troubleshooting.md#the-application-does-not-work-with-my-custom-model"
license: "Apache-2.0"
mode: "V"
---

For TensorFlow Lite Micro, ensure that your model is in a fully quantized `.tflite` file format, either `uint8` or
`int8`, and that it has successfully been run through the Vela compiler. For ExecuTorch ensure the model has been
generated using the Arm AOT compiler (which calls Vela) with `--quantize` and `--delegate` options passed to it and the
right target selected with `--target <name>`. See the AOT compiler script
[aot_arm_compiler.py](https://github.com/pytorch/executorch/blob/d6e25e26bf27660ea937cff68cb4c49dbb041d5d/examples/arm/aot_arm_compiler.py)
in ExecuTorch source tree for more details.

Also, please check that the CMake parameters used match the input requirements of your new model.

> **Note:** The Vela tool is not available within this software project. It is a separate Python tool that is available
> from: <https://pypi.org/project/ethos-u-vela/>. The source code is hosted on
> <https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela>.
