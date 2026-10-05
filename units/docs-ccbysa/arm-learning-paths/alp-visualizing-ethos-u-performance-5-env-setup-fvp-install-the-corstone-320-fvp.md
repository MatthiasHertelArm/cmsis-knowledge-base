---
id: "alp-visualizing-ethos-u-performance-5-env-setup-fvp-install-the-corstone-320-fvp"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Set up the Corstone-320 Fixed Virtual Platform: Install the Corstone-320 FVP"
summary: "Before you begin, make sure you’ve completed the steps in the previous section to install ExecuTorch."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/5-env-setup-fvp.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/5-env-setup-fvp/#install-the-corstone-320-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before you begin, make sure you’ve completed the steps in the previous section to install ExecuTorch.

**Note:**
If you're using macOS, you need to perform additional setup to support FVP execution.  

See the FVPs-on-Mac GitHub repo for instructions before continuing.


Run the setup script provided in the ExecuTorch examples directory:

```bash
cd $HOME/executorch/examples/arm
./setup.sh --i-agree-to-the-contained-eula
```

The `--i-agree-to-the-contained-eula` flag is required to run the script. It indicates your acceptance of Arm’s licensing terms for using the FVP.

This installs the FVP and extracts all necessary components. It also prints a command to configure your shell environment.
