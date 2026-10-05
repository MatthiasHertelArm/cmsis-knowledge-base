---
id: "intr-practical-zephyr-devicetree-practi-summary-2"
type: "concept"
domain: "debug"
title: "Practical Zephyr - Devicetree practice (Part 5): Dissecting UART peripheral pin multiplexing / Summary"
summary: "Part of: Dissecting UART peripheral pin multiplexing"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-04-17-practical_zephyr_05_dt_practice.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_05_dt_practice#summary"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Dissecting UART peripheral pin multiplexing_

Zephyr streamlines pin multiplexing by requiring the use of `pinctrl` properties for SoC peripherals and by providing a standardized set of pin configuration properties.

The nodes referenced in the `pinctrl-<n>` phandle arrays, however, are entirely vendor-specific and will probably remain so in the foreseeable future. Two patterns for dealing with `pinctrl` nodes exist: The **grouping** and the **node** approach.

- Pin control with the **grouping approach** is the recommended approach and uses macros for the pin assignment. MCUs with restricted pin multiplexing typically provide macros for supported pins and functions, whereas MCUs with unrestricted multiplexing such as Nordics nRF series use parameterized macros.

- Pin control with the **node approach** is only used for MCUs with restricted pin multiplexing: For each supported combination of pins and functions, the vendor provides a DTS file with generated nodes. Pins are assigned to a peripheral by referring to different (generated) nodes.

You can explore the pin control for your vendor of choice by looking it up in [Zephyr's bindings index](https://docs.zephyrproject.org/latest/build/dts/api/bindings.html).
