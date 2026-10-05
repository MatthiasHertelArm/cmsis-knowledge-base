---
id: "alp-observing-ethos-u-on-nxp-9-build-executorch-runne-set-environment-variables"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Build Cortex-M33 firmware for ExecuTorch: Set environment variables"
summary: "Set three environment variables so the build can find your toolchain, your SDK, and the MCUXpresso Python environment. These must be set before building or running the SDK patch script."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/9-build-executorch-runner-for-cm33/#set-environment-variables"
license: "CC-BY-SA-4.0"
mode: "V"
---

Set three environment variables so the build can find your toolchain, your SDK, and the MCUXpresso Python environment. These must be set before building or running the SDK patch script.

Do this once for your user account, then restart VS Code so the changes take effect.

### Required variables

| Variable | Description |
|----------|-------------|
| `ARMGCC_DIR` | Path to the Arm GCC toolchain root, i.e. a directory starting with `arm-gnu-toolchain-14.2.rel1*` |
| `SdkRootDirPath` | Path to the folder that contains the `mcuxsdk/` subdirectory |
| `MCUX_VENV_PATH` | Path to the MCUXpresso Python venv executables |

Find the installed toolchain directory name:


**Linux/macOS:**
ls ~/.mcuxpressotools/arm-gnu-toolchain-*

**Windows (PowerShell):**
dir $env:USERPROFILE\.mcuxpressotools\arm-gnu-toolchain-*



Use the directory name from the output for the `ARMGCC_DIR` variable below. The name looks like `arm-gnu-toolchain-14.2.rel1-darwin-arm64-arm-none-eabi` (the version number may differ).


**Linux/macOS:**
export ARMGCC_DIR="$HOME/.mcuxpressotools/`<toolchain-dir>`"
export SdkRootDirPath="$HOME/mcuxsdk_root"
export MCUX_VENV_PATH="$HOME/.mcuxpressotools/.venv/bin"

**Windows (PowerShell):**
[Environment]::SetEnvironmentVariable("ARMGCC_DIR", "$env:USERPROFILE\.mcuxpressotools\`<toolchain-dir>`", "User")
[Environment]::SetEnvironmentVariable("SdkRootDirPath", "$env:USERPROFILE\mcuxsdk_root", "User")
[Environment]::SetEnvironmentVariable("MCUX_VENV_PATH", "$env:USERPROFILE\.mcuxpressotools\.venv\Scripts", "User")



These quick checks catch most path mistakes before you start debugging build errors:


**Linux/macOS:**
test -x "$ARMGCC_DIR/bin/arm-none-eabi-gcc" && echo "OK: toolchain" || echo "FAIL: ARMGCC_DIR"
test -d "$SdkRootDirPath/mcuxsdk" && echo "OK: SDK" || echo "FAIL: SdkRootDirPath"

**Windows (PowerShell):**
if (Test-Path "$env:ARMGCC_DIR\bin\arm-none-eabi-gcc.exe") { "OK: toolchain" } else { "FAIL: ARMGCC_DIR" }
if (Test-Path "$env:SdkRootDirPath\mcuxsdk") { "OK: SDK" } else { "FAIL: SdkRootDirPath" }
