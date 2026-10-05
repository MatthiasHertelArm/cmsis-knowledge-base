---
id: "alp-alif-image-classification-application-code-the-inference-pipeline"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Add the application code: The inference pipeline"
summary: "The run_inference() function handles the full pipeline from model loading to output. It starts by initializing the ExecuTorch runtime and creating a zero-copy data loader that reads the compiled .pte model directly from flash memory."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/application-code/#the-inference-pipeline"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `run_inference()` function handles the full pipeline from model loading to output. It starts by initializing the ExecuTorch runtime and creating a zero-copy data loader that reads the compiled `.pte` model directly from flash memory. The program is then parsed and method metadata queried to determine how much planned memory the model needs.

Memory is set up next: sub-allocations are carved from the SRAM1 pool for planned buffers, and a memory manager ties together the method, temp, and planned allocators. Once memory is in place, the `forward` method is loaded.

Before inference runs, the input tensor is prepared by converting the embedded int8 image data to float32. This is needed because the model's first operator is `quantize_per_tensor`, which expects float input. Inference then runs in three stages: the quantize operator executes on the CPU, the entire MobileNetV2 backbone runs as a single NPU command stream on the Ethos-U85, and the dequantize operator runs back on the CPU. Finally, the argmax of the 1000-class output vector gives the predicted ImageNet class.

The NPU handles the bulk of the computation. The CPU-side overhead of ExecuTorch loading, input conversion, and quantize/dequantize is small compared to the NPU workload.

The application code is in place. The next section configures the memory layout to accommodate the model and ExecuTorch runtime.
