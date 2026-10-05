---
id: "alp-vcpkg-tool-installation-removal-remove-vcpkg"
type: "concept"
domain: "project"
title: "Install tools on the command line using vcpkg: Remove vcpkg: Remove vcpkg"
summary: "If you want to remove vcpkg from your system, run one of the following commands:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/vcpkg-tool-installation/removal.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/vcpkg-tool-installation/removal/#remove-vcpkg"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you want to remove `vcpkg` from your system, run one of the following commands:


  **Windows (cmd):**
rmdir /s  %USERPROFILE%\.vcpkg
  
  **Windows (PowerShell):**
Remove-Item -Recurse -Force -Path ~\.vcpkg
  
  **Linux/macOS:**
rm -rf ~/.vcpkg
