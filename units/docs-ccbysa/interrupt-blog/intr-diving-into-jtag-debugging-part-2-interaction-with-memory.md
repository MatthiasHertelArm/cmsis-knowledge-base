---
id: "intr-diving-into-jtag-debugging-part-2-interaction-with-memory"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Debugging (Part 2): Interaction with memory"
summary: "Great, the JTAG connection works and we’ve read the IDCODE. Let's now proceed and try interacting with the microcontroller's memory by writing a value to it and reading it back."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-29-diving-into-jtag-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-2#interaction-with-memory"
license: "CC-BY-SA-4.0"
mode: "V"
---

Great, the JTAG connection works and we’ve read the `IDCODE`. Let's now proceed and try interacting with the microcontroller's memory by writing a value to it and reading it back. After all, reading/writing memory is one of the primary operations when debugging a microcontroller.

To interact with the microcontroller’s memory, we need to understand the mechanism behind it. The JTAG protocol itself doesn’t provide any specifics about this. Access to the internal resources of ARM architecture controllers (such as memory) is facilitated by a special module called DAP (Debug Access Port). I’ve detailed this module extensively in this article [A Deep Dive into the ARM Debug Access Port](https://piolabs.com/blog/engineering/diving-into-arm-debug-access-port.html). Unfortunately, without this knowledge, advancing further might be challenging. Therefore, I highly recommend reading that article or the official documentation [IHI0031 — ARM Debug Interface](https://developer.arm.com/documentation/ihi0031/latest/).

The first step for any access operation to the internal resources of an ARM architecture microcontroller with a DAP module is to request clocking and power for the debug module. This is done by setting the `CSYSPWRUPREQ` and `CDBGPWRUPREQ` bits in the DP `CTRL/STAT` register.



After this initial setup, we can begin our memory operations.

In the following two sections, I will be heavily referencing the “Practical Part” from the article [A Deep Dive into the ARM Debug Access Port](https://piolabs.com/blog/engineering/diving-into-arm-debug-access-port.html). This section describes the algorithm for reading/writing memory through interaction with the DAP module. Additionally, I will supplement this algorithm with a sequence of bits, illustrating how this will appear from the perspective of the JTAG protocol.
