---
id: "intr-arm-cortex-m33-instruction-tracing-basic-terminology"
type: "concept"
domain: "debug"
title: "ARM Cortex-M33 Instruction Tracing Without a Debugger: Basic Terminology"
summary: "The Micro Trace Buffer (MTB) is a peripheral that can be used for instruction tracing. Instruction execution information is written by the MTB to a dedicated area of SRAM."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-23-instruction-tracing-mtb-m33.md"
doc_source: "https://interrupt.memfault.com/blog/instruction-tracing-mtb-m33#basic-terminology"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Micro Trace Buffer (MTB) is a peripheral that can be used for instruction tracing. Instruction execution information is written by the MTB to a dedicated area of SRAM. This means no external pins or special debuggers are needed to view the trace history.

ARM Cortex-M33 [^m33-mtb] and ARM Cortex-M0+[^m0-mtb] designs may have an MTB integrated (inclusion of the feature is optional). The easiest way to find out if an MCU includes the MTB unit is to search the datasheet for mentions of "MTB".

> The MTB is not present on Cortex-M3, Cortex-M4, or Cortex-M7s. However, most Cortex-M MCUs do implement
> the Embedded Trace Macrocell (ETM) [^etm]. By default, this trace information is streamed out
> over dedicated pins and you need special trace hardware[^4] to read and process the information. However, some MCUs do include an Embedded Trace Buffer (ETB) that allows trace data to be redirected to RAM instead. A full discussion of the ETM & ETB is outside the scope of this article.
