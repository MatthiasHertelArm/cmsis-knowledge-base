---
id: "czep-zephyr-integration-with-cmsis-tool-rtt-and-segger-systemview"
type: "concept"
domain: "project"
title: "Zephyr Integration with CMSIS-Toolbox: RTT and SEGGER SystemView"
summary: "SEGGER Real-Time Transfer (RTT) enables real-time data exchange between a target device and a host debugger without requiring an additional UART interface. RTT is also the transport mechanism used for SystemView."
status: "draft"
collection: "cmsis-zephyr"
source: "Arm-Examples/CMSIS-Zephyr@ef8713c:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/README.md#rtt-and-segger-systemview"
license: "Apache-2.0"
mode: "V"
---

SEGGER Real-Time Transfer (RTT) enables real-time data exchange between a target device and a host debugger without requiring an additional UART interface. RTT is also the transport mechanism used for SystemView.

RTT and SystemView are integrated in Zephyr and enabled in the [`zephyr.csolution.yml`](https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/zephyr.csolution.yml) file with the `west-defs` under the `build-type: Debug-RTT`. RTT and SystemView are currently used for CI testing and can be used with pyOCD as shown below.

The `Debug-RTT` configurations for `target-type: IFX_T2G_B_H` are excluded from the CI build matrix because RTT support is not available for this Zephyr target.

**Example invocation for `target-type: STM32H7B3I-DK`:**

```bash
pyocd load --cbuild-run <path>\out\zephyr+STM32H7B3I-DK.cbuild-run.yml
pyocd run  --cbuild-run <path>\out\zephyr+STM32H7B3I-DK.cbuild-run.yml
```

The pyOCD `run` command now outputs test messages to the debug console and collects the file `out\zephyr+STM32H7B3I-DK.SVdat`, which can be analyzed with [SEGGER SystemView](https://www.segger.com/products/development-tools/systemview/).
