---
id: "alp-observing-ethos-u-on-alif-2-tool-installation-install-setools"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Set up the Alif Ensemble E8 DevKit: Install SETOOLS"
summary: "Secure Enclave Tools (SETOOLS) is Alif's toolset for flashing firmware to MRAM through the Secure Enclave."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/2-tool-installation/#install-setools"
license: "CC-BY-SA-4.0"
mode: "V"
---

Secure Enclave Tools (SETOOLS) is Alif's toolset for flashing firmware to MRAM through the Secure Enclave.

1. Download the SETOOLS package from the [Alif Ensemble E8 DevKit support page](https://alifsemi.com/support/kits/ensemble-e8devkit/) and extract it to `~/mnist_alif`, editing the command with the name of your `.tar` or `.zip` file:
  
    **macOS and Linux:**
  cd ~/Downloads
  tar xvf `<replace_with_your_alif_security_toolkit_download.tar>` -C ~/mnist_alif
    

  **Windows (PowerShell):**
  cd ~/Downloads
  Expand-Archive <.\replace_with_your_alif_security_toolkit_download.zip> -DestinationPath ~\mnist_alif
    
  

2. Verify the installation: 
  
    **macOS:**
    cd ~/mnist_alif/app-release-exec-macos
    ./app-write-mram -h
    ./app-gen-toc -h
    
  **Linux:**
    cd ~/mnist_alif/app-release-exec-linux
    ./app-write-mram -h
    ./app-gen-toc -h
  
  **Windows:**
    cd ~\mnist_alif\app-release-exec-windows
    .\app-write-mram.exe -h
    .\app-gen-toc.exe -h
  
  
  The extracted folder name can vary by SETOOLS release. The commands assume the package extracts to `app-release-exec-*`. Each command should print a `usage:` message. If either command fails, check that you're in the extracted SETOOLS directory for your operating system.

  **Important:**
  On macOS, the system might block the unsigned binary the first time you run it. If this happens, do the following:

      1. Open **System Settings** or **System Preferences**.
      2. Navigate to **Privacy & Security**.
      3. Select **Allow Anyway**. 

  Then, run the command again. You might need to reapprove for both `./app-*` commands.
