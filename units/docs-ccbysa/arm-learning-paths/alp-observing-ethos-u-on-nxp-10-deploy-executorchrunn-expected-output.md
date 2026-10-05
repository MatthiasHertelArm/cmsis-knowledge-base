---
id: "alp-observing-ethos-u-on-nxp-10-deploy-executorchrunn-expected-output"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Deploy and test on FRDM-IMX93: Expected output"
summary: "The key indicators of a successful inference run:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board/#expected-output"
license: "CC-BY-SA-4.0"
mode: "V"
---

You should see output similar to:

```output
NPU config match
NPU arch match
cmd_end_reached 0x1
bus_status_error 0x0
1 inferences finished
Output[0]: dtype=6, numel=1000, nbytes=4000
Program complete, exiting.
```

The key indicators of a successful inference run:

| Output | Meaning |
|--------|---------|
| `NPU config match` | The compiled model's NPU configuration matches the hardware |
| `NPU arch match` | The compiled model's architecture version matches the hardware |
| `cmd_end_reached 0x1` | The NPU executed all 116 operators in the command stream |
| `bus_status_error 0x0` | No AXI bus errors during NPU memory access |
| `numel=1000` | MobileNet V2 output: 1000 ImageNet classification scores (one per class) |

The model runs with uninitialized input data, so the output scores don't correspond to a real image classification. To get meaningful predictions, feed a real 224x224 RGB image as input.

**Note:**
If the trace buffer shows `Program identifier '' != expected 'ET12'`, the `.pte` model wasn't loaded into DDR at `0xC0000000`. Reload the model using the steps above.
