---
id: "alp-iot-sdk-aws-default-build"
type: "concept"
domain: "project"
title: "Build and run Arm Total Solutions for IoT: Enable AWS connectivity: Default build"
summary: "The build will take a few minutes to complete."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/iot-sdk/aws.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/iot-sdk/aws/#default-build"
license: "CC-BY-SA-4.0"
mode: "V"
---

Build and run the `keyword` example:

```console
./ats.sh build-n-run keyword
```
The build will take a few minutes to complete.

The results are output (alongside other data) in the terminal:

```output
*** ML interface initialised
INFO - For timestamp: 0.000000 (inference #: 0); label: on, score: 0.996127; threshold: 0.700000
ML_HEARD_ON
INFO - For timestamp: 0.500000 (inference #: 1); label: on, score: 0.962542; threshold: 0.700000
INFO - For timestamp: 1.000000 (inference #: 2); label: <none>; threshold: 0.000000
ML UNKNOWN
INFO - For timestamp: 1.500000 (inference #: 3); label: off, score: 0.999030; threshold: 0.700000
ML_HEARD_OFF
...
```

Use `Ctrl+C` to stop the simulation.

This confirms your environment is setup correctly to build and run the `keyword` (and `speech`) example applications.
