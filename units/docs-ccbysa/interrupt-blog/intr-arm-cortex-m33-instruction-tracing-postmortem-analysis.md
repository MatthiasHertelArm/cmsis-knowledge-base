---
id: "intr-arm-cortex-m33-instruction-tracing-postmortem-analysis"
type: "concept"
domain: "debug"
title: "ARM Cortex-M33 Instruction Tracing Without a Debugger: Postmortem Analysis"
summary: "So far the examples we have walked through are still only helpful if a debugger is attached to the board so the trace stream can be pulled off."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-23-instruction-tracing-mtb-m33.md"
doc_source: "https://interrupt.memfault.com/blog/instruction-tracing-mtb-m33#postmortem-analysis"
license: "CC-BY-SA-4.0"
mode: "V"
---

So far the examples we have walked through are still only helpful if a debugger is attached to the board so the trace stream can be pulled off. Once the product has shipped and is out in the field these strategies will not help to triage what went wrong on devices.

For production, I would recommend collecting the trace buffer and MTB peripheral block (`0xE0043000`-`0xE0043018`) when an unexpected error or fault takes place. With these two pieces of information, we can remotely recover an exact trace of the instructions that were executing prior to the issue!
