---
id: "alp-deploy-mobilesam-on-ethos-u-run-the-example-run-the-application-on-the-fvp"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Build and run MobileSAM on the Corstone-320 FVP: Run the application on the FVP"
summary: "On macOS, the FVPs-on-Mac wrapper needs access to the repository files inside its container. Set its mount and working directories from the ExecuTorch repository root, preserving any existing configuration:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/run-the-example.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/run-the-example/#run-the-application-on-the-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

On macOS, the FVPs-on-Mac wrapper needs access to the repository files inside its container. Set its mount and working directories from the ExecuTorch repository root, preserving any existing configuration:

```bash
if [[ "$(uname -s)" == "Darwin" ]]; then
  export FVP_MOUNT_DIR="${FVP_MOUNT_DIR:-$PWD}"
  export FVP_WORKDIR="${FVP_WORKDIR:-$PWD}"
fi
```

Enable pipeline failure reporting, then run the ELF on the Corstone-320 Fixed Virtual Platform (FVP):

```bash
set -o pipefail

backends/arm/scripts/run_fvp.sh \
  --elf=arm_test/mobilesam/runner/arm_executor_runner \
  --target=ethos-u85-256 \
  --timeout=300 \
  --semihosting-cwd=arm_test/mobilesam/io \
  '--semihosting-cmd-line=executor_runner -i input.bin -o output' \
  --fast 2>&1 | tee arm_test/mobilesam/fvp.log
```

The runner reads the tensor specified by `-i input.bin` and writes its first output tensor to `output-0.bin` under `arm_test/mobilesam/io/`. The console transcript is saved to `arm_test/mobilesam/fvp.log`; validation reads the tensor file.

Confirm that the run created the output file before continuing:

```bash
test -s arm_test/mobilesam/io/output-0.bin
```

The check exits successfully without printing anything when the file exists and is not empty. The next page checks its shape and segmentation agreement.
