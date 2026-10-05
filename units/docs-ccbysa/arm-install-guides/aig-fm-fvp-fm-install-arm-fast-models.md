---
id: "aig-fm-fvp-fm-install-arm-fast-models"
type: "concept"
domain: "project"
title: "Arm Fast Models: Install Arm Fast Models"
summary: "Unzip the downloaded installation archive."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/fm_fvp/fm.md"
doc_source: "https://learn.arm.com/install-guides/fm_fvp/fm/#install-arm-fast-models"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Windows

Unzip the downloaded installation archive.

It is easiest to run the installation wizard (`setup.exe`), and follow on-screen instructions.

Once installed, open the `System Canvas` IDE, and select `File` > `Preferences` > `Applications` from the menu.

Set the `Path to Microsoft Viaual C++ application devenv.com` to your Visual Studio installation (`<install_dir>\Common7\IDE`). Click `OK` to save.

### Linux

Use the `setup.sh` script to install:
```command
./setup.sh --i-accept-the-end-user-license-agreement --no-interactive
```
You may be prompted to install additional libraries before proceeding.
```command
sudo apt-get install -y libsm6 libxcursor1 libxft2 libxrandr2 libxt6 libxinerama1
```
Once installed, set up environment with script of the form:
```command
. <install_directory>/FastModelTools_<version>/etc/source_all.sh
```
The installer will output the exact script for your setup.

Full instructions are provided in the [Fast Models User Guide](https://developer.arm.com/documentation/100965/latest/Installing-Fast-Models/Installation).
