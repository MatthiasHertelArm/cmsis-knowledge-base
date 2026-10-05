---
id: "zep-configuration-system-kconfig"
type: "concept"
domain: "project"
title: "Configuration System (Kconfig)"
summary: "The Zephyr kernel and subsystems can be configured at build time to adapt them for specific application and platform needs. Configuration is handled through Kconfig, which is the same configuration system used by the Linux kernel."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/build/kconfig/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/build/kconfig/index.rst"
license: "Apache-2.0"
mode: "V"
---

The Zephyr kernel and subsystems can be configured at build time to adapt them
for specific application and platform needs. Configuration is handled through
Kconfig, which is the same configuration system used by the Linux kernel. The
goal is to support configuration without having to change any source code.

Configuration options (often called *symbols*) are defined in `Kconfig`
files, which also specify dependencies between symbols that determine what
configurations are valid. Symbols can be grouped into menus and sub-menus to
keep the interactive configuration interfaces organized.

The output from Kconfig is a header file `autoconf.h` with macros that
can be tested at build time. Code for unused features can be compiled out to
save space.

The following sections explain how to set Kconfig configuration options, go
into detail on how Kconfig is used within the Zephyr project, and have some
tips and best practices for writing `Kconfig` files.

Users interested in optimizing their configuration for security should refer
to the Zephyr Security Guide's section on the hardening.
