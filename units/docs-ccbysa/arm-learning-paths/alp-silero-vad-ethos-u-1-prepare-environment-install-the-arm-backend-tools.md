---
id: "alp-silero-vad-ethos-u-1-prepare-environment-install-the-arm-backend-tools"
type: "concept"
domain: "edge-ai"
title: "Deploy Silero VAD on Arm Ethos-U with ExecuTorch: Prepare the environment and model inputs: Install the Arm backend tools"
summary: "The Arm setup script downloads the Arm GNU Toolchain, Ethos-U Vela compiler, and supporting Python packages. On Linux, the script also installs the Corstone FVPs. Review the license terms presented by the script before using its EULA acceptance option."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/1-prepare-environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/silero-vad-ethos-u/1-prepare-environment/#install-the-arm-backend-tools"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Arm setup script downloads the Arm GNU Toolchain, Ethos-U Vela compiler, and supporting Python packages. On Linux, the script also installs the Corstone FVPs. Review the license terms presented by the script before using its EULA acceptance option.

**macOS:**
Before you run the Arm setup command on macOS, install [Docker Desktop](https://learn.arm.com/install-guides/docker/docker-desktop/) and follow the [AVH FVPs on macOS install guide](https://learn.arm.com/install-guides/fvps-on-macos/). Add the FVPs-on-Mac `bin` directory to `PATH`. Confirm that Docker is running and that `FVP_Corstone_SSE-320` resolves to the wrapper:

```bash
docker info >/dev/null
command -v FVP_Corstone_SSE-320
```


Run the setup script from the ExecuTorch repository root:

```bash
./examples/arm/setup.sh --i-agree-to-the-contained-eula
source examples/arm/arm-scratch/setup_path.sh
```

The second command adds the downloaded cross-compiler and, on Linux, FVP binaries to the current shell environment. If you start a new shell, you'll need to run the command again.

Check that the two target tools are available:

```bash
command -v arm-none-eabi-g++
command -v FVP_Corstone_SSE-320
```

The compiler resolves under `examples/arm/arm-scratch/`. On Linux, the FVP also resolves under this directory. On macOS, the FVP resolves under the FVPs-on-Mac wrapper directory. If the compiler is missing, source `examples/arm/arm-scratch/setup_path.sh` again. If the FVP is missing on macOS, add the wrapper directory to `PATH`.
