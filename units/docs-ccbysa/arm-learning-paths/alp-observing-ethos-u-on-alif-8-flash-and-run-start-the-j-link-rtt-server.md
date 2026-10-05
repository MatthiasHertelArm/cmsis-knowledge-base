---
id: "alp-observing-ethos-u-on-alif-8-flash-and-run-start-the-j-link-rtt-server"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Flash and run the project on the Alif Ensemble E8 DevKit: Start the J-Link RTT server"
summary: "Open a new terminal and start J-Link Commander:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/8-flash-and-run.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/8-flash-and-run/#start-the-j-link-rtt-server"
license: "CC-BY-SA-4.0"
mode: "V"
---

Open a new terminal and start J-Link Commander:


  **macOS and Linux:**
JLinkExe -device AE822FA0E5597LS0_M55_HP -if SWD -speed 4000
  

  **Windows (PowerShell):**
& "C:\Program Files\SEGGER\JLink_V954\JLink.exe" -device AE822FA0E5597LS0_M55_HP -if SWD -speed 4000
  


At the `J-Link>` prompt, run:

```text
connect
r
g
```

Leave this terminal open. It acts as the RTT server.
