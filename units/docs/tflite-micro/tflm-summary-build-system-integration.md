---
id: "tflm-summary-build-system-integration"
type: "concept"
domain: "edge-ai"
title: "Summary: Build System Integration"
summary: "This module is the least defined but we strongly recommend the following: 1. A single target makefile.inc for all the architectures that you would like to support along with optional target-specific system_setup.cc. See cortex_m_generic_makefile.inc and xtensa_makefile.inc as examples."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@3f787dc:tensorflow/lite/micro/docs/optimized_kernel_implementations.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/optimized_kernel_implementations.md#build-system-integration"
license: "Apache-2.0"
mode: "V"
---

This module is the least defined but we strongly recommend the following: 1. A
single target makefile.inc for all the architectures that you would like to
support along with optional target-specific
[system_setup.cc](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../cortex_m_corstone_300/system_setup.cc). See
[cortex_m_generic_makefile.inc](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../tools/make/targets/cortex_m_generic_makefile.inc)
and [xtensa_makefile.inc](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../tools/make/targets/xtensa_makefile.inc) as
examples.

1.  A single `ext_libs.inc` (and associated scripts) that downloads any external
    dependencies (including the NN library). For example:

    *   [cmsis_nn.inc](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../tools/make/ext_libs/cmsis_nn.inc) and
        [cmsis_download.sh](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../tools/make/ext_libs/cmsis_download.sh)
    *   [xtensa.inc](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../tools/make/ext_libs/xtensa.inc) and
        [xtensa_download.sh](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../tools/make/ext_libs/xtensa_download.sh)

1.  The optimized kernels will then live in a kernels subdirectory (e.g.
    [kernels/cmsis_nn](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../kernels/cmsis_nn) and
    [kernels/xtensa](https://github.com/tensorflow/tflite-micro/blob/3f787dc/tensorflow/lite/micro/docs/../kernels/xtensa))

Two development workflows that the TFLM team would like to encourage and
support:

1.  Export static library + headers into target-specific development environment

    *   Build a static libtensorflow-microlite.a using the TFLM makefile with:
        `make -f tensorflow/lite/micro/tools/make/Makefile TARGET=`<target>`
        OPTIMIZED_KERNEL_DIR=`<optimize_dir>` microlite`
    *   Optionally build for size or speed. Translated to a valid make command it will be any of these two:
        `make -f tensorflow/lite/micro/tools/make/Makefile TARGET=`<target>`
        OPTIMIZED_KERNEL_DIR=`<optimize_dir>` OPTIMIZE_KERNELS_FOR=KERNELS_OPTIMIZED_FOR_SIZE microlite`
        `make -f tensorflow/lite/micro/tools/make/Makefile TARGET=`<target>`
        OPTIMIZED_KERNEL_DIR=`<optimize_dir>` OPTIMIZE_KERNELS_FOR=KERNELS_OPTIMIZED_FOR_SPEED microlite`
        Check relevant README for given optimization library if this is applicable.
    *   Use the static library and any TFLM headers as part of the overall
        application (with its own build system).

1.  Integrate TFLM with IDE:

    *   This has historically been done using the TFLM Makefile’s support for
        project generation.

    *   However, given the learning curve and high-maintenance overhead, we are
        moving away from supporting project generation via the Makefile and are
        encouraging future IDE integrations to be done outside of the TFLM
        Makefiles.

    *   The TFLM team is currently working through the details on this topic.
