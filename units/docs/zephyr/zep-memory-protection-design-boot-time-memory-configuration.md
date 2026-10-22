---
id: "zep-memory-protection-design-boot-time-memory-configuration"
type: "concept"
domain: "rtos"
title: "Memory Protection Design: Boot Time Memory Configuration"
summary: "This is the configuration of the MPU after the kernel has started up. It should contain the following:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/usermode/memory_domain.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/usermode/memory_domain.rst"
license: "Apache-2.0"
mode: "V"
---

This is the configuration of the MPU after the kernel has started up. It should
contain the following:

- Any configuration of memory regions which need to have special caching or
  write-back policies for basic hardware and driver function. Note that most
  MPUs have the concept of a default memory access policy map, which can be
  enabled as a "background" mapping for any area of memory that doesn't
  have an MPU region configuring it. It is strongly recommended to use this
  to maximize the number of available MPU regions for the end user. On
  ARMv7-M/ARMv8-M this is called the System Address Map, other CPUs may
  have similar capabilities. See mem_mgmt_api for information on
  how to annotate the system map in the device tree.

- One or more read-only, executable regions for program text and ro-data that are
  accessible to user mode. This could be further sub-divided into a
  read-only region for ro-data, and a read-only, executable region for text, but
  this will require an additional MPU region. This is required so that
  threads running in user mode can read ro-data and fetch instructions.

- Depending on configuration, user-accessible read-write regions to support
  extra features like GCOV, HEP, etc.

Assuming there is a background map which allows supervisor mode to access any
memory it needs, and regions are defined which grant user mode access to
text/ro-data, this is sufficient for the boot time configuration.
