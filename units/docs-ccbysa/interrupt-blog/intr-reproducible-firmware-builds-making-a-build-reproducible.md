---
id: "intr-reproducible-firmware-builds-making-a-build-reproducible"
type: "concept"
domain: "debug"
title: "Reproducible Firmware Builds: Making a Build Reproducible"
summary: "In this article we will examine a very simple app running FreeRTOS which passes a message between two tasks. Every time a message is sent a 64 bit counter is incremented. We will compile the binary from two different directories."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-12-11-reproducible-firmware-builds.md"
doc_source: "https://interrupt.memfault.com/blog/reproducible-firmware-builds#making-a-build-reproducible"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this article we will examine a very simple app running FreeRTOS which passes a message between two tasks. Every time a message is sent a 64 bit counter is incremented. We will compile the binary from two different directories. If the build is reproducible, we should find the binaries match and behave the same when flashed on target. However, what we will find out is that one of the binaries crashes on boot and one does not!

#### Example Project Setup

In this article we will be using:

- the GNU Arm Embedded Toolchain 8-2019-q3-update[^1] for our compiler
- the nRF52840-DK[^2] (ARM Cortex-M4F) as our development board
- SEGGER JLinkGDBServer[^3] as our GDB Server.

#### Enforcing a Compiler Version

A first step for ensuring a build will be reproducible is to enforce that everyone use the same compiler version. It's very easy to add a check to the build system for this. Here's an example of what you could add to a Makefile to accomplish this:

{: #enforce-compiler-for-build}

```
GCC_COMPILER ?= arm-none-eabi-gcc
GCC_VERSION := $(strip $(shell $(GCC_COMPILER) -dumpversion))
EXPECTED_GCC_VERSION := 8.3.1
ifneq ($(GCC_VERSION),$(EXPECTED_GCC_VERSION))
$(error Examples were all compiled against $(EXPECTED_GCC_VERSION). You are using $(GCC_VERSION))
endif
```
