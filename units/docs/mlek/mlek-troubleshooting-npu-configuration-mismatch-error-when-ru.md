---
id: "mlek-troubleshooting-npu-configuration-mismatch-error-when-ru"
type: "concept"
domain: "edge-ai"
title: "Troubleshooting: NPU configuration mismatch error when running inference"
summary: "If you see the following error message when an inference is executed:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/troubleshooting.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/troubleshooting.md#npu-configuration-mismatch-error-when-running-inference"
license: "Apache-2.0"
mode: "V"
---

If you see the following error message when an inference is executed:

```commandline
NPU config mismatch: npu.macs_per_cc=8 optimizer.macs_per_cc=7
NPU config mismatch: npu.shram_size=48 optimizer.shram_size=24
ERROR - Invoke failed.
ERROR - Inference failed.
```

It shows that the configuration of model file doesn't match the number of MACs units on the FVP.

For TensorFlow Lite Micro, the Vela configuration parameter `accelerator-config` used for producing the .`tflite` file
that is used while building the application should match the MACs configuration that the FVP is emulating.
For ExecuTorch, the Arm AOT compiler `--target` parameter determines the number of MACs the resulting model will run
with.

For example, if the `accelerator-config` from the Vela command was `ethos-u55-128`, the FVP should be emulating the
128 MACs configuration of the Ethos™-U55 block(default FVP configuration). If the `accelerator-config` used was
`ethos-u55-256`, the FVP must be executed with additional command line parameter to instruct it to emulate the
256 MACs configuration instead.

The [deploying on an FVP](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./deployment.md#deploying-on-an-fvp) page provides guidance
on how to instruct the FVP to change the number of MACs units.

Note that when the FVP is launched and the application starts executing, various parameters about the system are
logged over UART. These include the MACs/cc configuration of the FVP.

```log
INFO - MPS3 core clock has been set to: 32000000Hz
INFO - CPU ID: 0x410fd220
INFO - CPU: Cortex-M55 r0p0
INFO - Ethos-U device initialised
INFO - Ethos-U version info:
INFO -  Arch:       v1.0.6
INFO -  Driver:     v0.16.0
INFO -  MACs/cc:    128
INFO -  Cmd stream: v0
INFO - Target system design: Arm Corstone-300 - AN552
INFO - Arm Corstone-300 - AN552 platform initialised
INFO - ARM ML Embedded Evaluation Kit
```
