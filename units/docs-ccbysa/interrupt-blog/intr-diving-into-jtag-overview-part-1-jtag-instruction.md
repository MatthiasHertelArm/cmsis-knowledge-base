---
id: "intr-diving-into-jtag-overview-part-1-jtag-instruction"
type: "concept"
domain: "debug"
title: "Diving into JTAG - Overview (Part 1): JTAG Instruction"
summary: "JTAG instructions are commands that interact with the TAP, enabling test, debug, programming, and configuration functions."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-29-diving-into-jtag-part1.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part1#jtag-instruction"
license: "CC-BY-SA-4.0"
mode: "V"
---

JTAG instructions are commands that interact with the TAP, enabling test, debug, programming, and configuration functions.

As described in the previous chapter even though selecting an instruction will usually not directly trigger any action, merely select the proper register as DR.

Let’s look at some of the most common instructions.

### The `IDCODE` instruction

The `IDCODE` instruction in JTAG is used to get the unique identifier of the device connected to the JTAG circuit. Each device that supports JTAG has its own unique ID code, which can be read using the `IDCODE` command. This can be useful to identify the device type, manufacturer, and version.

This identifier is 32-bit in size and consists of next fields:



  


So when you load `IDCODE` instruction in `IR` register this will force the `IDCODE` register to be selected as the data register.

### The `BYPASS` instruction

The `BYPASS` instruction in the JTAG protocol allows you to bypass one or more components in the JTAG chain without including them in the scan chain. This can be useful when the device does not support JTAG protocol commands or when you want to check other components in the chain.

When the `BYPASS` instruction is passed to a JTAG chain, it skips the device it is targeting and passes control to the next device in the chain. Thus, the `BYPASS` command avoids addressing a device that cannot be scanned by the JTAG protocol and continues to scan devices that are further up the chain.

In addition, the `BYPASS` instruction can be used to speed up a JTAG chain scan since skipping the device reduces the number of cycles required to go through the chain.

So when you load `BYPASS` instruction in `IR` register this will force the 1 bit `BYPASS` register to be selected as the data register.

### The `SAMPLE/PRELOAD` instruction

>**Note**: This command and a few others: `EXTEST`, `INTEST`, `HIGHZ` are
>actively used in the board testing process and will be discussed in detail
>in the second part of this article on the subject of using the JTAG
>protocol for board testing. In the same article they are specified by reference.

This command closes the `TDI` and `TDO` to the BSR (Boundary Scan Register). However, the chip remains in a state of normal operation. During the execution of this command register BSR can be used to capture data, which the chip is exchanged during normal operation. In other words with this command, we can read signals from the pin of the microcontroller without disturbing its operation.

So when you load `SAMPLE/PRELOAD` instruction in `IR` register this will force the BSR register to be selected as the data register.
