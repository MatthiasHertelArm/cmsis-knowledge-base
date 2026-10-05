---
id: "alp-observing-ethos-u-on-alif-2-tool-installation-verify-usb-connection-to-the-d"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Verify USB connection to the DevKit"
summary: "Check that your computer recognizes the DevKit:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation/#verify-usb-connection-to-the-devkit"
license: "CC-BY-SA-4.0"
mode: "V"
---

Check that your computer recognizes the DevKit:


  **macOS:**
ls /dev/cu.*
  

  **Linux:**
ls /dev/ttyACM* /dev/ttyUSB* 2>/dev/null
  

  **Windows:**
Get-CimInstance Win32_SerialPort | Select-Object DeviceID,Name,Description
  


**Important:**
Close any terminal application that’s connected to SEUART, such as PuTTY, minicom, or screen, before you use the Security Toolkit (SETOOLS). The DevKit exposes only one SEUART interface, so SETOOLS can’t access the port if another application is already using it.


You should see a SEGGER J-Link device. If you're unsure which entry belongs to the DevKit, run the command before and after connecting the board and compare the output. If no device appears, check that the USB cable is connected to the **PRG USB** port and that the cable supports data, not only charging.
