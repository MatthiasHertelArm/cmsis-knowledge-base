---
id: "ethu-zephyr-corstone-300-fvp-examples"
type: "concept"
domain: "edge-ai"
title: "Zephyr: Corstone-300 FVP examples"
summary: "CMSIS-Ethos-Zephyr ports the Test-Ethos-U55 example to Zephyr. It retains the example's ML models and CMSIS MLOps workflow while using Zephyr-native implementations for the application runtime and Ethos-U integration."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/zephyr/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/zephyr/src/main.md#corstone-300-fvp-examples"
license: "Apache-2.0"
mode: "V"
---

[CMSIS-Ethos-Zephyr](https://github.com/Arm-Examples/CMSIS-Ethos-Zephyr)
ports the `Test-Ethos-U55` example to Zephyr. It retains the example's ML
models and CMSIS MLOps workflow while using Zephyr-native implementations for
the application runtime and Ethos-U integration.

The
[Arm Ethos Zephyr Playground](https://github.com/Arm-Examples/Arm-Ethos-Zephyr-Playground)
contains an animal-classification application for the
`mps3/corstone300/fvp` board. It includes both a standard TFLM model and a
Vela-compiled model, and enables NPU acceleration with `CONFIG_ETHOS_U=y`.

After installing the Corstone-300 FVP and enabling the TFLM west module, clone
and build the example from the Zephyr tree:

```bash
cd "$ZEPHYR_BASE/samples/modules/tflite-micro"
git clone https://github.com/Arm-Examples/Arm-Ethos-Zephyr-Playground \
  animal_classification
cd animal_classification
west build -b mps3/corstone300/fvp . --pristine auto
source run.sh
```

The example's board overlay enlarges the simulated ITCM and DTCM regions for
the model and tensor arena. Those sizes are FVP example settings, not defaults
for physical targets. For a different board, replace the overlay, Vela target
configuration, memory placement, and runner with values validated for that
device.
