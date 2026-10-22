---
id: "zepb-mimxrt1060-evk-system-clock"
type: "concept"
domain: "bring-up"
title: "mimxrt1060_evk: Hardware / System Clock"
summary: "The MIMXRT1060 SoC is configured to use SysTick as the system clock source, running at 600MHz."
status: "draft"
collection: "zephyr-boards"
source: "zephyrproject-rtos/zephyr@76280bc:boards/nxp/mimxrt1060_evk/doc/index.rst"
doc_source: "https://docs.zephyrproject.org/latest/boards/nxp/mimxrt1060_evk/doc/index.html#system-clock"
license: "Apache-2.0"
mode: "V"
---

_Part of: Hardware_

The MIMXRT1060 SoC is configured to use SysTick as the system clock source,
running at 600MHz.

When power management is enabled, the 32 KHz low frequency
oscillator on the board will be used as a source for the GPT timer to
generate a system clock. This clock enables lower power states, at the
cost of reduced resolution
