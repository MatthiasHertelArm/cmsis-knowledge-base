---
id: "cmlek-cmsis-mlek-software-pack-examples-description"
type: "concept"
domain: "edge-ai"
title: "CMSIS-MLEK Software Pack: Examples description"
summary: "The provided applications implement data preprocessing, memory management, and neural network inference pipelines that are optimized for Cortex-M and Ethos-U platforms. The examples are prepared to run with Keil Studio."
status: "draft"
collection: "cmsis-mlek-packs"
source: "Arm-Examples/cmsis-mlek@6d60f43:README.md"
doc_source: "https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/README.md#examples-description"
license: "Apache-2.0"
mode: "V"
---

The provided applications implement data preprocessing, memory management, and neural network inference pipelines that are optimized for Cortex-M and Ethos-U platforms. The examples are prepared to run with [Keil Studio](https://mdk-packs.github.io/vscode-cmsis-solution-docs/index.html).

The CMSIS-MLEK software pack is derived from the [Arm® ML embedded evaluation kit](https://git.gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit) and makes the examples easier to access. It also contains interfaces to physical hardware and simplifies porting to target hardware. It contains the following ML applications and uses currently Neural Network Models currently in [TensorFlow Lite](https://www.keil.arm.com/packs/tensorflow-lite-micro-tensorflow) format.

| ML application                                 | Description                                           | Neural Network Model
|------------------------------------------------|-------------------------------------------------------|---------------------
| [Keyword spotting (KWS)](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/./template/audio)     | Recognize the presence of a key word in verbal speech | [MicroNet](https://github.com/ARM-software/ML-zoo/tree/9f506fe52b39df545f0e6c5ff9223f671bc5ae00/models/keyword_spotting/micronet_medium/tflite_int8)
| [Object detection](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/./template/video)           | Detects and draws face bounding box in a given image  | [Yolo Fastest](https://github.com/emza-vs/ModelZoo/blob/master/object_detection/yolo-fastest_192_face_v4.tflite)
| [Generic inference runner](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/./template/generic) | Code block allowing you to develop your own use case  | Your custom model

Refer to [Overview](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/./overview/README.md) for more details.
