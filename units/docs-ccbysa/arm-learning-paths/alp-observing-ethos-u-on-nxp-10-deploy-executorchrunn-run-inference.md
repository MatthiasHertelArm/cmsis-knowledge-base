---
id: "alp-observing-ethos-u-on-nxp-10-deploy-executorchrunn-run-inference"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Deploy and test on FRDM-IMX93: Run inference"
summary: "Start the Cortex-M33 firmware through RemoteProc. RemoteProc is the control plane for this platform: it gives you a consistent way to stop, replace, and start the Cortex-M33 image without manually resetting the system."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board/#run-inference"
license: "CC-BY-SA-4.0"
mode: "V"
---

Start the Cortex-M33 firmware through RemoteProc. RemoteProc is the control plane for this platform: it gives you a consistent way to stop, replace, and start the Cortex-M33 image without manually resetting the system.

```bash { command_line="root@frdm-imx93" }
echo stop > /sys/class/remoteproc/remoteproc0/state
echo executorch_runner_cm33.elf > /sys/class/remoteproc/remoteproc0/firmware
echo start > /sys/class/remoteproc/remoteproc0/state
sleep 15
cat /sys/kernel/debug/remoteproc/remoteproc0/trace0
```

**Note:**
If no firmware is running, the `stop` command prints an error. That is expected and can be ignored.
