---
id: "alp-observing-ethos-u-on-alif-3-docker-executorch-setu-set-up-arm-ethos-u-dependencie"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: (Optional) Set up a Docker development environment: Set up Arm Ethos-U dependencies"
summary: "This script sets up the following dependencies: - TOSA Libraries - Ethos-U SDK structure - CMake toolchain files"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/3-docker-executorch-setup/#set-up-arm-ethos-u-dependencies"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the ExecuTorch Arm setup script:
```bash
cd $ET_HOME
# Run the Arm setup script
./examples/arm/setup.sh --i-agree-to-the-contained-eula
```

This script sets up the following dependencies:
- TOSA Libraries
- Ethos-U SDK structure
- CMake toolchain files

<!-- ### Download Arm GNU Toolchain

The setup script doesn't download the toolchain automatically. Download it manually:

```bash
cd $ET_HOME/examples/arm
mkdir -p ethos-u-scratch && cd ethos-u-scratch
# Detect architecture and download appropriate toolchain
ARCH=$(uname -m)
if [ "$ARCH" = "x86_64" ]; then
    echo "Downloading toolchain for x86_64..."
    wget -q --show-progress https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz
    tar -xf arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz
    TOOLCHAIN_DIR="arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi"
else
    echo "Downloading toolchain for aarch64..."
    wget -q --show-progress https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-aarch64-arm-none-eabi.tar.xz
    tar -xf arm-gnu-toolchain-13.3.rel1-aarch64-arm-none-eabi.tar.xz
    TOOLCHAIN_DIR="arm-gnu-toolchain-13.3.rel1-aarch64-arm-none-eabi"
fi
# Clean up archive to save space
rm -f arm-gnu-toolchain-*.tar.xz*
# Add to PATH
export PATH="$(pwd)/$TOOLCHAIN_DIR/bin:$PATH"
echo "export PATH=\"$(pwd)/$TOOLCHAIN_DIR/bin:\$PATH\"" >> ~/.bashrc
```

**Note:**
The toolchain download is approximately 139 MB and may take 10-30 minutes depending on your connection speed.
 -->
