---
id: "alp-visualizing-ethos-u-performance-7-configure-fvp-gui-find-your-ip-address"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Enable GUI and deploy a model on Corstone-320 FVP: Find your IP address"
summary: "You'll use the IP address of your active network interface (inet) later to pass as an argument to the FVP."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/7-configure-fvp-gui.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/7-configure-fvp-gui/#find-your-ip-address"
license: "CC-BY-SA-4.0"
mode: "V"
---

Note down your computer's IP address:
```bash
ip addr show 
```
You'll use the IP address of your active network interface (inet) later to pass as an argument to the FVP.

**Note:**

For macOS, note down your `en0` IP address (or whichever network adapter is active):

```bash
ipconfig getifaddr en0 # Returns your Mac's WiFi IP address
```
