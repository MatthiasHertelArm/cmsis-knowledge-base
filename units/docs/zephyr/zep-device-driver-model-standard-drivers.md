---
id: "zep-device-driver-model-standard-drivers"
type: "concept"
domain: "rtos"
title: "Device Driver Model: Standard Drivers"
summary: "Device drivers which are present on all supported board configurations are listed below."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/drivers/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/drivers/index.rst"
license: "Apache-2.0"
mode: "V"
---

Device drivers which are present on all supported board configurations
are listed below.

* **Interrupt controller**: This device driver is used by the kernel's
  interrupt management subsystem.

* **Timer**: This device driver is used by the kernel's system clock and
  hardware clock subsystem.

* **Serial communication**: This device driver is used by the kernel's
  system console subsystem.

* **Entropy**: This device driver provides a source of entropy numbers
  for the random number generator subsystem.


**Important:** Use the random API functions for random values. Entropy functions should not be directly used as a random number generator source as some hardware implementations are designed to be an entropy seed source for random number generators and will not provide cryptographically secure random number streams.
