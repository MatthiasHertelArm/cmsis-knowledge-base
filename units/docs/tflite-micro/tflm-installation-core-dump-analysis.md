---
id: "tflm-installation-core-dump-analysis"
type: "concept"
domain: "edge-ai"
title: "Installation: Core Dump Analysis"
summary: "Load the test executable and the generated core file into GDB to inspect the state at the time of the crash."
status: "draft"
collection: "tflite-micro"
source: "tensorflow/tflite-micro@f7ed40d:tensorflow/lite/micro/docs/qemu.md"
doc_source: "https://github.com/tensorflow/tflite-micro/blob/f7ed40d/tensorflow/lite/micro/docs/qemu.md#core-dump-analysis"
license: "Apache-2.0"
mode: "V"
---

Load the test executable and the generated core file into GDB
to inspect the state at the time of the crash.

```bash
$ arm-none-eabi-gdb <TEST_BINARY_PATH> <CORE_FILE_PATH>
(gdb) bt
```

# Useful External Links for QEMU

* The current testing framework uses QEMU's user mode.
  Read [doc](https://www.qemu.org/docs/master/user/index.html)

* QEMU uses ARM [semihosting](https://github.com/ARM-software/abi-aa/blob/main/semihosting/semihosting.rst)
  to replace newlib system calls for specific boards with the host OS.
  Further documentation on how this works is contained in `cortex_m_qemu_makefile.inc`.
