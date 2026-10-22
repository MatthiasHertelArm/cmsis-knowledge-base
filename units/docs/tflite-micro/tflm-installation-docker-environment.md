---
id: "tflm-installation-docker-environment"
type: "concept"
domain: "edge-ai"
title: "Installation: Docker Environment"
summary: "As an alternative to installing dependencies on your host machine, you can use the provided Docker environment. For instructions, see the \"Run locally for debugging\" section in the Dockerfile."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@bd621c2:tensorflow/lite/micro/docs/qemu.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/bd621c2/tensorflow/lite/micro/docs/qemu.md#docker-environment"
license: "Apache-2.0"
mode: "V"
---

As an alternative to installing dependencies on your host machine,
you can use the provided Docker environment.
For instructions, see the "Run locally for debugging" section in the
[Dockerfile](https://github.com/tensorflow/tflite-micro/blob/main/ci/Dockerfile.micro).

# Software Emulation with QEMU

TensorFlow Lite Micro uses [QEMU](https://qemu.org) to run tests that have
been cross-compiled for architectures other than x86_64. This setup enables
the rapid execution of unit tests for various hardware targets directly
on a standard development machine.

# Running Unit Tests

You can run all Cortex-M unit tests using a single build script:

```bash
tensorflow/lite/micro/tools/ci_build/test_cortex_m_qemu.sh
```

After this script completes the initial build, you can run an individual
test target as follows:

```bash
make -f tensorflow/lite/micro/tools/make/Makefile \
  TARGET=cortex_m_qemu \
  TARGET_ARCH=cortex-m3 \
  OPTIMIZED_KERNEL_DIR=cmsis_nn
  <TEST_TARGET>
```

# Debugging

You can debug failures either interactively with GDB
or by analyzing the core file after a crash.
