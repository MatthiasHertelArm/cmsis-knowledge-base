---
id: "zep-overview"
type: "concept"
domain: "optimization"
title: "Overview"
summary: "The interfaces and APIs provided by the power management subsystem are designed to be architecture and SOC independent. This enables power management implementations to be easily adapted to different SOCs and architectures."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/services/pm/overview.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/services/pm/overview.rst"
license: "Apache-2.0"
mode: "V"
---

The interfaces and APIs provided by the power management subsystem
are designed to be architecture and SOC independent. This enables power
management implementations to be easily adapted to different SOCs and
architectures.

The architecture and SOC independence is achieved by separating the core PM
infrastructure from implementations of the SOC specific components.
Thus a coherent abstraction is presented to the rest of the OS and the application layer.

The power management features are classified into the following categories.

* System Power Management
* Device Power Management
