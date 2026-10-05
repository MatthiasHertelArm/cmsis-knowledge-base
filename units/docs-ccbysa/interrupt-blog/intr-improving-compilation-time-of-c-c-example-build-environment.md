---
id: "intr-improving-compilation-time-of-c-c-example-build-environment"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects: Example Build Environment"
summary: "To put these suggestions to the test, I took the example LwIP_HTTP_Server_Netconn_RTOS from STM32CubeF4 project[^4], found a GCC port[^10], and used that to test the various operating systems, compilers, and build systems."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects#example-build-environment"
license: "CC-BY-SA-4.0"
mode: "V"
---

To put these suggestions to the test, I took the example
LwIP_HTTP_Server_Netconn_RTOS from STM32CubeF4 project[^4], found a GCC
port[^10], and used that to test the various operating systems, compilers, and
build systems. To easily get the same environment locally, one can clone the
project from the Interrupt repository and perform the appropriate steps for each
compiler.

```
$ git clone git@github.com:memfault/interrupt.git
$ cd interrupt/example/faster-compilation
```

> Make will automatically download the STM32CubeF4 and extract it to the
> appropriate place. When not using Make, download the distribution from
> [Github](https://github.com/STMicroelectronics/STM32CubeF4) and extract it to
> `stm32cube/`

- GCC - Using Make, run `make`. Works on macOS, Linux, and Windows
- Keil - Open
  `stm32cube/Projects/STM32F429ZI-Nucleo/Applications/LwIP/LwIP_HTTP_Server_Netconn_RTOS/MDK-ARM/Project.uvprojx`
- IAR - Open
  `stm32cube/Projects/STM32F429ZI-Nucleo/Applications/LwIP/LwIP_HTTP_Server_Netconn_RTOS/EWARM/Project.eww`

Below are the versions of the programs tested:

- Keil: MDK-Arm 5.29 on Windows, where `armcc` is ARM Compiler 5.06, and
  `armclang` is ARM Compiler 6.13
- IAR: IAR Embedded Workbench for ARM 8.42.1 on Windows
- GCC: GNU ARM Embedded Toolchain 8-2019-q3[^9] for macOS, Linux, and Windows

The operating system environments were as follows:

- Windows: a VirtualBox image of Windows 10 was used, with 8GB RAM and 4 CPU
- Linux: Ubuntu 18.04 on Docker, with 8GB RAM and 4 CPU
- macOS: 10.14 Mojave native installation, 16GB RAM and 4 CPU.
