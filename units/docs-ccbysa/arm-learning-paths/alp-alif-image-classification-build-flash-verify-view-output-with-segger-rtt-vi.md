---
id: "alp-alif-image-classification-build-flash-verify-view-output-with-segger-rtt-vi"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Build, flash, and verify inference: View output with SEGGER RTT Viewer"
summary: "If you see Detected: cat! with a class in the 280-285 range, the inference ran successfully on the Ethos-U85 NPU."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/build-flash-verify/#view-output-with-segger-rtt-viewer"
license: "CC-BY-SA-4.0"
mode: "V"
---

- Open **SEGGER J-Link RTT Viewer** on your development machine.
- Set **Connection** to **USB**.
- Filter by manufacturer: **AlifSemiconductor**.
- For **Device**, start typing `AE822F` and select **AE822FA0E5597LS0_M55_HP** (Core: Cortex-M55).
- Select **OK** to connect.

The expected output is:

```output
mv2_runner booted
Ethos-U85 NPU initialized (polling mode)
Model bytes: 3835552
Image bytes: 150528
ExecuTorch runtime initialized
Program loaded successfully
Method 'forward': 1 inputs, 1 outputs, 1 planned buffers
  Planned buffer[0]: 752640 bytes
Loading method 'forward'...
[I] data:0x800432b0
Method loaded, 1 inputs, 1 outputs
Converted input to float32
Input tensor set (1x3x224x224 float32)
Running inference...
[sem_take #1] count=1
[sem_take #2] count=0
Inference complete!
Output tensor: 1000 elements
Top-1 class: 283
Detected: cat! (ImageNet class 283)
```

If you see `Detected: cat!` with a class in the 280-285 range, the inference ran successfully on the Ethos-U85 NPU.
