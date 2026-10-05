---
id: "alp-iot-sdk-aws-repeat-with-the-speech-example"
type: "concept"
domain: "project"
title: "Build and run Arm Total Solutions for IoT: Enable AWS connectivity: Repeat with the speech example"
summary: "Observe the output on the terminal and your MQTT console."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/iot-sdk/aws.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/iot-sdk/aws/#repeat-with-the-speech-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

Build and run the `speech` example.

```console
./ats.sh build-n-run speech
```

Observe the output on the terminal and your MQTT console.

```output
INFO - Complete recognition: turn down the temperature in the bedroom
134 14506 [ML_MQTT] [INFO] Publish to the MQTT topic <thingname>/ml/inference.
```

(figure: speech #center)

See the [README.md](https://github.com/ARM-software/open-iot-sdk/blob/main/v8m/README.md#setting-up-aws-connectivity) for full details.
