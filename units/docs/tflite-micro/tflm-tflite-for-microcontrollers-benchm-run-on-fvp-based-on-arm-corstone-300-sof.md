---
id: "tflm-tflite-for-microcontrollers-benchm-run-on-fvp-based-on-arm-corstone-300-sof"
type: "concept"
domain: "edge-ai"
title: "TFLite for Microcontrollers Benchmarks: Run on FVP based on Arm Corstone-300 software"
summary: "For more info about the Corstone-300 software see: tensorflow/lite/micro/cortex_m_corstone_300/README.md."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/benchmarks/README.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/benchmarks/README.md#run-on-fvp-based-on-arm-corstone-300-software"
license: "Apache-2.0"
mode: "V"
---

For more info about the Corstone-300 software see:
[tensorflow/lite/micro/cortex_m_corstone_300/README.md](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/benchmarks/../cortex_m_corstone_300/README.md).

Disclaimer: The FVP can not be used to measure CPU performance.
The results are not reliable, not even for relative measurements.
FVP may however be used for performance measurements when running on NPU and only NPU PMU numbers can be used. The NPU model is cycle accurate within approximately +-10%.

As an example, the person detect downloaded model will be optimized for Ethos-U. For more info see:
[tensorflow/lite/micro/kernels/ethos_u/README.md](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/benchmarks/../kernels/ethos_u/README.md).
And since it only makes sense to measure performance on the NPU, only the person detection benchmark should be run and only with Ethos-U enabled.
See also network tester example, where person detect model is used in the same way when Ethos-U is enabled:
[tensorflow/lite/micro/examples/network_tester/README.md](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/benchmarks/../examples/network_tester/README.md).

The person detect model is not an optimial model for Ethos-U since it quite small. Also note that only the NPU PMU cycles are logged even though the CPU is setting up the Ethos-U driver in each iteration.

To run the person detection benchmark on FVP with Ethos-U:

```
make -f tensorflow/lite/micro/tools/make/Makefile CO_PROCESSOR=ethos_u TARGET=cortex_m_corstone_300 TARGET_ARCH=cortex-m55 run_person_detection_benchmark
```
