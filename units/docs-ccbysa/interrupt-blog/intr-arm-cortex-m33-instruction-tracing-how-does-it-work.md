---
id: "intr-arm-cortex-m33-instruction-tracing-how-does-it-work"
type: "concept"
domain: "debug"
title: "ARM Cortex-M33 Instruction Tracing Without a Debugger: How does it work?"
summary: "One of the things I like the most about the MTB is how incredibly simple it is."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-23-instruction-tracing-mtb-m33.md"
doc_source: "https://interrupt.memfault.com/blog/instruction-tracing-mtb-m33#how-does-it-work"
license: "CC-BY-SA-4.0"
mode: "V"
---

One of the things I like the most about the MTB is how incredibly simple it is. Once enabled, it writes an 8 byte packet to the trace buffer allocated in SRAM every time the program counter (PC) changes non-sequentially (i.e a branch is taken or an exception occurs).

The first 4 bytes of the packet is where the code was prior to branching (the "source address") and the next 4 bytes is the address which was branched to (the "destination address").

Since thumb instructions are always at least half-word aligned, the bottom bit of each word in the
packet is used to encode extra information.

Bit 1 in the "source address", referred to as the "A-bit", differentiates the origin of the
branch. When the bit is set it means the PC update occurred due to an exception or update over a
debugger. When it is not set, it means a normal branch took place.

Bit 1 in the "destination address", referred to as the "S-bit", is set when the packet is the first one captured after a trace has been started. If the MTB has been stopped and started multiple times, this would reveal when there are gaps in the trace information.

With this information we can still recover every single instruction executed. In between branches
we know sequential PCs were fetched between the destination of previous packet to source of next packet!

Putting it all together, the format looks like this:



### Tracing Exception Return

You may recall that exception return for Cortex-M's involves branching to a special [`EXC_RETURN`](https://interrupt.memfault.com/blog/cortex-m-rtos-context-switching#exc-return-info) value.

Returning from an exception results in two packets being written to the MTB. In the first packet, the "source address" will match the address of the instruction exiting the exception and the "destination address" will be the `EXC_RETURN` value. In the second packet, the "source address" will contain the `EXC_RETURN` value and the "destination address" will match the address of the instruction executed upon exception return.
