---
id: "aig-install-guides-cmsis-toolbox-download-cmsis-toolbox"
type: "concept"
domain: "project"
title: "CMSIS-Toolbox: Download CMSIS-Toolbox"
summary: "Download and unpack the latest version of CMSIS-Toolbox from the Arm Tools Artifactory."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/cmsis-toolbox.md"
doc_source: "https://learn.arm.com/install-guides/cmsis-toolbox/#download-cmsis-toolbox"
license: "CC-BY-SA-4.0"
mode: "V"
---

Download and unpack the latest version of `CMSIS-Toolbox` from the [Arm Tools Artifactory](https://artifacts.tools.arm.com/cmsis-toolbox/).

For more information about the contents of the installation, see [Releases](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/releases).

### Download for Arm64 hosts

The commands depend on the host operating system. Replace `2.14.1` with the latest version.


  **Windows:**
wget https://artifacts.tools.arm.com/cmsis-toolbox/2.14.1/cmsis-toolbox-windows-arm64.zip
tar -xf cmsis-toolbox-windows-arm64.zip
  
  **Linux:**
wget https://artifacts.tools.arm.com/cmsis-toolbox/2.14.1/cmsis-toolbox-linux-arm64.tar.gz
tar -xf cmsis-toolbox-linux-arm64.tar.gz
  
  **macOS:**
curl -L -o cmsis-toolbox-darwin-arm64.tar.gz https://artifacts.tools.arm.com/cmsis-toolbox/2.14.1/cmsis-toolbox-darwin-arm64.tar.gz
tar -xf cmsis-toolbox-darwin-arm64.tar.gz
  


### Download for x86_64 hosts

The commands depend on the host operating system. Replace `2.14.1` with the latest version.


  **Windows:**
wget https://artifacts.tools.arm.com/cmsis-toolbox/2.14.1/cmsis-toolbox-windows-amd64.zip
tar -xf cmsis-toolbox-windows-amd64.zip
  
  **Linux:**
wget https://artifacts.tools.arm.com/cmsis-toolbox/2.14.1/cmsis-toolbox-linux-amd64.tar.gz
tar -xf cmsis-toolbox-linux-amd64.tar.gz
  
  **macOS:**
curl -L -o cmsis-toolbox-darwin-amd64.tar.gz https://artifacts.tools.arm.com/cmsis-toolbox/2.14.1/cmsis-toolbox-darwin-amd64.tar.gz
tar -xf cmsis-toolbox-darwin-amd64.tar.gz
