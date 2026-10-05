---
id: "cmlek-overview-2"
type: "concept"
domain: "edge-ai"
title: "Overview"
summary: "The Machine Learning Evaluation Kit (MLEK) pack contains CMSIS Reference Applications and templates for Edge AI development with embedded systems. These applications implement data preprocessing, memory management, and neural network inference pipelines that are optimized for Cortex-M and Ethos-U platforms."
status: "draft"
collection: "cmsis-mlek-packs"
source: "Arm-Examples/cmsis-mlek@6d60f43:overview/README.md"
doc_source: "https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/overview/README.md"
license: "Apache-2.0"
mode: "V"
---

The **Machine Learning Evaluation Kit (MLEK)** pack contains [CMSIS Reference Applications](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/) and templates for Edge AI development with embedded systems. These applications implement data preprocessing, memory management, and neural network inference pipelines that are optimized for Cortex-M and Ethos-U platforms.

Key Features:

- **Rapid Prototyping**: Get working ML applications running quickly with minimal setup.
- **Algorithm Development**: Use example code as design patterns for custom ML algorithm implementation.
- **Model Integration**: Easily swap in custom TensorFlow Lite models with minimal code changes.
- **Performance Validation**: Test and optimize ML performance on target hardware or simulation.
- **Hardware Evaluation**: Compare performance across different Corstone platforms and configurations.

The CMSIS-MLEK software pack is derived from the [Arm® ML embedded evaluation kit](https://git.gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit) and makes the examples easier to access. It also contains interfaces to physical hardware and simplifies porting to target hardware. It contains the following ML applications and uses currently Neural Network Models currently in [TensorFlow Lite](https://www.keil.arm.com/packs/tensorflow-lite-micro-tensorflow) format.

| ML application                                 | Description                                           |  Neural Network Model |
|:-----------------------------------------------|:------------------------------------------------------|:----------------------|
| [MLEK_Audio](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/overview/./MLEK_Audio.md)                  | Recognize the presence of a key word in verbal speech | [MicroNet](https://github.com/ARM-software/ML-zoo/tree/9f506fe52b39df545f0e6c5ff9223f671bc5ae00/models/keyword_spotting/micronet_medium/tflite_int8) |
| [MLEK_Video](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/overview/./MLEK_Video.md)                  | Detects and draws face bounding box in a given image  | [Yolo Fastest](https://github.com/emza-vs/ModelZoo/blob/master/object_detection/yolo-fastest_192_face_v4.tflite) |
| [MLEK_Generic](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/overview/./MLEK_Generic.md)              | Code block allowing you to develop your own use case  | Your custom model |

Each [ML reference application](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/) is a *csolution project* which supports deployment to physical hardware or FVP Corestone simulation models.

(figure: MLEK Reference Application Architecture)

A board layer (`*.clayer.yml`) implements the drivers for the physical interfaces. The API interfaces required by the different applications is shown in the table below.

| Required API Interfaces     | Description     |
|:----------------------------|:----------------|
| **Audio Processing**        |                 |
| CMSIS_VSTREAM_AUDIO_IN      | [CMSIS-Driver vStream](https://arm-software.github.io/CMSIS_6/latest/Driver/group__mci__interface__gr.html) configured for Audio input. |
| STDOUT                      | Standard I/O for printf output. |
| **Video Processing**        |                 |
| CMSIS_VSTREAM_VIDEO_IN      | [CMSIS-Driver vStream](https://arm-software.github.io/CMSIS_6/latest/Driver/group__mci__interface__gr.html) configured for Video input. |
| CMSIS_VSTREAM_VIDEO_OUT     | [CMSIS-Driver vStream](https://arm-software.github.io/CMSIS_6/latest/Driver/group__mci__interface__gr.html) configured for Video output. |
| STDOUT                      | Standard I/O for printf output. |
| **Generic Inference Runner**|                 |
| STDOUT                      | Standard I/O for printf output. |
