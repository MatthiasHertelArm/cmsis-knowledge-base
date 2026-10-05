---
id: "alp-observing-ethos-u-on-alif-2-tool-installation-install-j-link"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Install J-Link"
summary: "SEGGER J-Link provides the debug connection for Real-Time Transfer (RTT) output, which you'll use later to view inference results."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation/#install-j-link"
license: "CC-BY-SA-4.0"
mode: "V"
---

SEGGER J-Link provides the debug connection for Real-Time Transfer (RTT) output, which you'll use later to view inference results.

Install J-Link version 7.94 or later for Alif Ensemble E8 support:


  **macOS:**
brew install --cask segger-jlink
JLinkExe --version
  
  **Linux:**
wget https://www.segger.com/downloads/jlink/JLink_Linux_x86_64.deb
sudo dpkg -i JLink_Linux_x86_64.deb
JLinkExe --version
  
  **Windows:**
1. Download the J-Link installer from the [SEGGER website](https://www.segger.com/downloads/jlink/).
2. Run the installer and follow prompts.
3. Verify in Command Prompt: `JLink.exe --version`.
