---
id: "cmlek-cmsis-mlek-software-pack-continuous-integration-ci"
type: "concept"
domain: "edge-ai"
title: "CMSIS-MLEK Software Pack: Continuous Integration (CI)"
summary: "CMSIS-MLEK Software Pack: Continuous Integration (CI)"
status: "draft"
collection: "cmsis-mlek-packs"
source: "Arm-Examples/cmsis-mlek@6d60f43:README.md"
doc_source: "https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/README.md#continuous-integration-ci"
license: "Apache-2.0"
mode: "V"
---

| CI Workflow                                          | Description
|------------------------------------------------------|------------
| [mkdocs](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/./.github/workflows/mkdocs.yml)             | Builds the pack documentation on a GitHub hosted runner.
| [pack](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/./.github/workflows/pack.yml)                 | Builds the pack on a GitHub hosted runner.
| [test_audio](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/./.github/workflows/test_audio.yml)     | Builds the Keyword spotting application (audio) for different contexts by using the Arm Compiler for Embedded (AC6), execute each of them by using [FVP simulation models](https://arm-software.github.io/AVH/main/simulation/html/index.html), capture the FVP UART output and upload them as artifact.
| [test_video](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/./.github/workflows/test_video.yml)     | Builds the Object detection application (video) for different contexts by using the Arm Compiler for Embedded (AC6).
| [test_generic](https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/./.github/workflows/test_generic.yml) | Builds the a Generic inference application for different contexts by using the Arm Compiler for Embedded (AC6).
