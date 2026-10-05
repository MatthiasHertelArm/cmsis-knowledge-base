---
id: "intr-diving-into-jtag-overview-part-1-example"
type: "concept"
domain: "debug"
title: "Diving into JTAG - Overview (Part 1): Example"
summary: "Now that we’ve covered the theory, it’s time to see the JTAG protocol in action."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-11-29-diving-into-jtag-part1.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part1#example"
license: "CC-BY-SA-4.0"
mode: "V"
---

Now that we’ve covered the theory, it’s time to see the JTAG protocol in action. Let’s consider an example where we read the ID code value from a chip, with an `IR` length of 4 bits.The sequence of bits on pins `TMS`, `TDI`, `TDO`, state machine transitions, and states of switches SW1 - SW4 are shown in the following gif:



  


So, initially we are in the `Run-Test/Idle` state. In order to read the chip ID code we need to write the instruction code `IDCODE` into `IR` (let it be `0b1110` for our example). To write the instruction to `IR` we need to select the blue branch of our state machine. Images `2` and `3` show this transition. Image `3` shows how the keys `SW1` and `SW2` are switched when entering the `Select-IR-Scan` state. Next, at step `4` in the `Capture-IR` state, the `0b0001` pattern is loaded into the shift register. In step `5`, a transition to the `Shift-IR` state is made and at this transition, bit `1` of the loaded pattern is advanced to the `TDO` pin.

Steps `6-7` show the sequential shift of the `IDCODE (0b1110)` instruction bit by bit into the shift register with the last bit being shifted in at the moment of transition to the `Exit1-IR` state (step `8`). At step `9` (state `Update-IR`), the instruction code written to the shift register is latched into the `IR` register.  At `10` we return to the initial state. We have written the instruction code, now we need to read the data corresponding to this instruction, for this purpose we will use the green branch of the automaton. At step `11` we go to the `Select-DR-Scan` state, at that the keys `SW1` and `SW2` are switched to the `DR` register and the `ID` register is selected because during the `IR` phase we selected the instruction `IDCODE`. In step `12` the `Capture-DR` state, 32 bits of `ID` code are loaded into the shift register. At step `13` the transition to the `Shift-DR` state is performed and at this transition the low-order bit of the `ID` code is advanced to the `TDO` output. Steps `14-20` show the sequential shift of the chip id code `(0b111001101)` bit by bit. At step `21`, a transition to the `Exit1-DR` state is made and the last bit of the `ID` of the code is promoted. Step `22` (`Update-DR` state) - there should be a latch of the code written to the shift register into the selected `DR` register, but in case of `IDCODE` command this does not happen. At step `23` we return to the initial state again.

In Part 2 of this series, we'll dive into debugging with JTAG.

>**Note**: This article was originally published by Aliaksandr on his blog. You can find the original article [here](https://medium.com/@aliaksandr.kavalchuk/diving-into-jtag-protocol-part-1-overview-fbdc428d3a16).
