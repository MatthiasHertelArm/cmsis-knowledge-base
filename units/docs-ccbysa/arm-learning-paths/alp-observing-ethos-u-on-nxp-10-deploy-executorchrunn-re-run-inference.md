---
id: "alp-observing-ethos-u-on-nxp-10-deploy-executorchrunn-re-run-inference"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Deploy and test on FRDM-IMX93: Re-run inference"
summary: "The executor_runner runs inference once when the firmware starts. To re-run, reload the firmware:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board/#re-run-inference"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `executor_runner` runs inference once when the firmware starts. To re-run, reload the firmware:

```bash { command_line="root@frdm-imx93" }
echo stop > /sys/class/remoteproc/remoteproc0/state
sleep 2
echo start > /sys/class/remoteproc/remoteproc0/state
sleep 15
cat /sys/kernel/debug/remoteproc/remoteproc0/trace0
```

The trace buffer resets at the start of each firmware load, so you'll always see fresh output.
