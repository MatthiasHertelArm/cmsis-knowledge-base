---
id: "alp-visualizing-ethos-u-performance-5-env-setup-fvp-verify-your-setup"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Set up the Corstone-320 Fixed Virtual Platform: Verify your setup"
summary: "Run a quick test to check that the FVP is working:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/5-env-setup-fvp.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/5-env-setup-fvp/#verify-your-setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run a quick test to check that the FVP is working:


```bash
./examples/arm/run.sh --target=ethos-u85-256
```

This executes a built-in example on the Ethos-U85 configuration of the Corstone-320 platform.

**macOS:**

On macOS, make sure Docker is running. FVPs execute inside a Docker container on macOS systems.



If you see example output from the platform, the setup is complete.
