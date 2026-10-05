---
id: "ethu-zephyr-configure-the-application"
type: "concept"
domain: "edge-ai"
title: "Zephyr: Configure the application"
summary: "Enable TFLM and Ethos-U in the application's prj.conf:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/zephyr/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/zephyr/src/main.md#configure-the-application"
license: "Apache-2.0"
mode: "V"
---

Enable TFLM and Ethos-U in the application's `prj.conf`:

```text
CONFIG_CPP=y
CONFIG_TENSORFLOW_LITE_MICRO=y
CONFIG_ETHOS_U=y
```

Add stack, heap, C++ language-level, and logging options according to the
application's measured requirements. Keep the non-Vela model available only if
the application intentionally supports a CPU fallback; enabling
`CONFIG_ETHOS_U` requires the Vela-compiled model for NPU execution.

When the Arm GNU Toolchain is supplied through `vcpkg` and the application is
intended to use the toolchain's Newlib, select it explicitly:

```text
CONFIG_NEWLIB_LIBC=y
CONFIG_PICOLIBC=n
CONFIG_PICOLIBC_USE_MODULE=n
CONFIG_MINIMAL_LIBC=n
```
