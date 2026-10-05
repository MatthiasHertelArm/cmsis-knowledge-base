---
id: "ethu-zephyr-prerequisites"
type: "concept"
domain: "edge-ai"
title: "Zephyr: Prerequisites"
summary: "Enable the TFLM module in the Zephyr workspace and fetch its dependencies:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/zephyr/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/zephyr/src/main.md#prerequisites"
license: "Apache-2.0"
mode: "V"
---

1. Install Zephyr, its Python virtual environment, and `west` by following the
   [Zephyr Getting Started Guide](https://docs.zephyrproject.org/latest/develop/getting_started/index.html).
2. Select a Zephyr board that describes an Ethos-U NPU, or add the required
   device-specific devicetree node to the board support.
3. Install the FVP or hardware debug connection required by the selected board.
4. Compile the quantized model with Vela for the NPU and memory configuration
   implemented by that board.

Enable the TFLM module in the Zephyr workspace and fetch its dependencies:

```bash
west config manifest.project-filter -- +tflite-micro
west update
```

Run these commands from the west workspace. Re-run `west update` when the
manifest revision or module selection changes.
