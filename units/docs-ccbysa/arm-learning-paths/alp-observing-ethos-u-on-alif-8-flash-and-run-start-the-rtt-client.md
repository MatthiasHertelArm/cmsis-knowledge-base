---
id: "alp-observing-ethos-u-on-alif-8-flash-and-run-start-the-rtt-client"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Flash and run the project on the Alif Ensemble E8 DevKit: Start the RTT client"
summary: "Open a second terminal and start the RTT client:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/8-flash-and-run.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/8-flash-and-run/#start-the-rtt-client"
license: "CC-BY-SA-4.0"
mode: "V"
---

Open a second terminal and start the RTT client:


  **macOS and Linux:**
JLinkRTTClient
  

  **Windows (PowerShell):**
& "C:\Program Files\SEGGER\JLink_V954\JLinkRTTClient.exe"
  


The output is similar to:

```output
ExecuTorch MNIST NPU Demo
Alif Ensemble E8 - Cortex-M55 HP

Initializing SRAM0 power...
SRAM0 enabled successfully

Loading model ...
Running inference...
Inference completed!
Predicted digit: ...
```

The predicted digit depends on the image you converted in the previous section.
