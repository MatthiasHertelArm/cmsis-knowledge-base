---
id: "alp-observing-ethos-u-on-nxp-10-deploy-executorchrunn-prerequisites"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Deploy and test on FRDM-IMX93: Prerequisites"
summary: "Before deploying, verify the following on your FRDM-IMX93 board:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board/#prerequisites"
license: "CC-BY-SA-4.0"
mode: "V"
---

Before deploying, verify the following on your FRDM-IMX93 board:

1. **Ethos-U kernel driver is loaded.** The Linux `ethosu` driver must be bound so the NPU is powered and clocked:

   ```bash { command_line="root@frdm-imx93" output_lines="2" }
   ls /dev/ethosu*
   /dev/ethosu0
   ```

   If `/dev/ethosu0` doesn't exist, the NPU isn't powered and the firmware will hang at NPU initialization.

2. **DDR memory is reserved for the CM33.** The NXP BSP reserves two DDR regions by default:

   ```dts
   reserved-memory {
       model@c0000000 {
           reg = <0 0xc0000000 0 0x400000>;   /* 4MB for .pte model */
           no-map;
       };
       ethosu_region@A8000000 {
           reg = <0 0xa8000000 0 0x8000000>;  /* 128MB for NPU working memory */
           no-map;
       };
   };
   ```
