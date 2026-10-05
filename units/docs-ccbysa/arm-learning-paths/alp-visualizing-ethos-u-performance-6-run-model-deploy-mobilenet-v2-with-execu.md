---
id: "alp-visualizing-ethos-u-performance-6-run-model-deploy-mobilenet-v2-with-execu"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Deploy and run Mobilenet V2 on the Corstone-320 FVP: Deploy Mobilenet V2 with ExecuTorch"
summary: "With your environment and FVP now set up, you're ready to deploy and run a real TinyML model using ExecuTorch."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/6-run-model.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/6-run-model/#deploy-mobilenet-v2-with-executorch"
license: "CC-BY-SA-4.0"
mode: "V"
---

With your environment and FVP now set up, you're ready to deploy and run a real TinyML model using ExecuTorch.

This example deploys the [MobileNet V2](https://pytorch.org/hub/pytorch_vision_mobilenet_v2/) computer vision model. The model is a convolutional neural network (CNN) that extracts visual features from an image. It is used for image classification and object detection.

The Python code for the MobileNet V2 model is in your local `executorch` repo: [executorch/examples/models/mobilenet_v2/model.py](https://github.com/pytorch/executorch/blob/main/examples/models/mobilenet_v2/model.py). You can deploy it using [run.sh](https://github.com/pytorch/executorch/blob/main/examples/arm/run.sh), just like you did in the previous step, with some extra parameters:

**Tip:**

On macOS, make sure Docker is running. FVPs execute inside a Docker container.



```bash
./examples/arm/run.sh \
--aot_arm_compiler_flags="--delegate --quantize --intermediates mv2_u85/ --debug --evaluate" \
--output=mv2_u85 \
--target=ethos-u85-128 \
--model_name=mv2
```

The `--model_name=mv2` flag tells `run.sh` to use the Mobilenet V2 model defined in examples/models/mobilenet_v2/model.py.

**Explanation of run.sh Parameters**
|run.sh Parameter|Meaning / Context|
|--------------|-----------------|
|--aot_arm_compiler_flags|Passes a string of compiler options to the ExecuTorch Ahead-of-Time (AOT) compiler|
|--delegate|Enables backend delegation|
|--quantize|Converts the floating-point model to int8 quantized format using post-training quantization
**Essential for running on NPUs**|
|--intermediates mv2_u85/|Directory where intermediate files (e.g., TOSA, YAMLs, debug graphs) will be saved
Useful output files for **manual debugging**|
|--debug|Verbose debugging logging|
|--evaluate|Validates model output, provides timing estimates|
