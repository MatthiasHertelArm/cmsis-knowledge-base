---
id: "tflm-porting-to-a-new-platform-step-5-integrating-optimized-kernel-impl"
type: "concept"
domain: "edge-ai"
title: "Porting to a new platform: Step 5: Integrating Optimized Kernel Implementations"
summary: "TFLM has optimized kernel implementations for a variety of targets that are in sub-folders of the kernels directory."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/new_platform_support.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/new_platform_support.md#step-5-integrating-optimized-kernel-implementations"
license: "Apache-2.0"
mode: "V"
---

TFLM has optimized kernel implementations for a variety of targets that are in
sub-folders of the [kernels directory](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/kernels).

It is possible to use the project generation script to create a tree with these
optimized kernel implementations (and associated third party dependencies).

For example:
```
python3 tensorflow/lite/micro/tools/project_generation/create_tflm_tree.py \
  -e hello_world -e micro_speech -e person_detection \
  --makefile_options="TARGET=cortex_m_generic OPTIMIZED_KERNEL_DIR=cmsis_nn TARGET_ARCH=project_generation" \
  /tmp/tflm-cmsis
```

will create an output tree with all the sources and headers needed to use the
optimized [cmsis\_nn kernels](https://github.com/tensorflow/tflite-micro/tree/main/tensorflow/lite/micro/kernels/cmsis_nn) for Cortex-M platforms.


# Advanced Integration Topics

In order to have tighter coupling between your platform-specific TFLM
integration and the upstream TFLM repository, you might want to consider the
following:

 1. Set up a GitHub repository for your platform
 1. Nightly sync between TFLM and your platform-specific GitHub repository
 1. Using GitHub actions for CI

For some pointers on how to set this up, we refer you to the GitHub repositories
that integrated TFLM for the:
 * [Arduino](https://github.com/tensorflow/tflite-micro-arduino-examples): supported by the TFLM team
 * [Sparkfun Edge](https://github.com/advaitjain/tflite-micro-sparkfun-edge-examples): for demonstration purposes only, not officially supported.

Once you are set up with continuous integration and the ability to integrate
newer versions of TFLM with your platform, feel free to add a build badge to
TFLM's [Community Supported TFLM Examples](https://github.com/tensorflow/tflite-micro#community-supported-tflm-examples).

# Getting Help

[Here are some ways](https://github.com/tensorflow/tflite-micro#getting-help) that you can
reach out to get help.
