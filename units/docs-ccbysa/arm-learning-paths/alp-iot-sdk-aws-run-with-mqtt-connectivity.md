---
id: "alp-iot-sdk-aws-run-with-mqtt-connectivity"
type: "concept"
domain: "project"
title: "Build and run Arm Total Solutions for IoT: Enable AWS connectivity: Run with MQTT connectivity"
summary: "Rebuild and run the keyword application."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/iot-sdk/aws.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/iot-sdk/aws/#run-with-mqtt-connectivity"
license: "CC-BY-SA-4.0"
mode: "V"
---

Rebuild and run the `keyword` application.

```console
./ats.sh build-n-run keyword
```

The messages are shown in the terminal as well as in [MQTT test client](#mqtt).

```output
ML_HEARD_ON
109 27329 [ML_MQTT] [INFO] Publish to the MQTT topic <thingname>/ml/inference.
...
```

(figure: keyword #center)
