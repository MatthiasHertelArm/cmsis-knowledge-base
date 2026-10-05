---
id: "intr-diving-into-jtag-debugging-part-2-read-of-id-code"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Debugging (Part 2): Read of ID CODE"
summary: "The sequence of bits for reading the IDCODE of the CoreSight JTAG-DP TAP controller will look as follows:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-02-29-diving-into-jtag-part-2.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-2#read-of-id-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

The sequence of bits for reading the `IDCODE` of the CoreSight JTAG-DP TAP controller will look as follows:



Let’s analyze this sequence in detail:

* So the first step is to reset the TAP State Machine to the initial state `Test-Logic-Reset` in order to be sure that we are in a known state. To achieve this, simply hold the `TMS` in logic 1 for 5 clock cycles of `TCK`. The pink bit sequence is responsible for this step:



* Next, we need to load the `IDCODE` command code into the `IR` register, and to do this we put the TAP State Machine into the `Shift-IR` state. To do this, feed the `TMS` line with the sequence [0, 1, 1, 0, 0]. A sequence of blue bits is responsible for this step:



As you can see on the `TDO` line in the last measure there is a one. Let's find out where it came from. The thing is that going through the `Capture-IR` state, the TAP controller loads into the shift register a value of `0b0001` for CoreSight JTAG-DP TAP and `0b00001` for Boundary Scan TAP which starts to move along the `TDO` line from this measure and LSB bits forward. So, over the next 9 clock cycles (including this one) we will get a `TDO` sequence of `0b100010000`.

* The next step is to directly load the `IDCODE` command code into the CoreSight JTAG-DP TAP `IR` register and the `BYPASS` command code into the Boundary Scan TAP `IR` register. I think the situation for the CoreSight JTAG-DP TAP is clear, but why we load the `BYPASS` command into the Boundary Scan TAP should be explained. You remember that there are two TAP controllers in our JTAG chain connected in series and we can not access the CoreSight JTAG-DP TAP registers without having to write something to the Boundary Scan TAP, and the size of the `IR` register for Boundary Scan is 5 bits, and the `DR` register is 32 bits, so to write a new data to the `DR` register of the CoreSight JTAG-DP TAP we need to write a 32 + 32 = 64 bits sequence of bits to the JTAG circuit. This is not very convenient. The `BYPASS` command will help us here. When this command is in the register `IR` the data register of the selected TAP becomes 1 bit long. So now we need to write a sequence of 33 bits Instead of 64. The `IDCODE` code is `0b1110`, and the `BYPASS` command code is `0b11111` total we need to push 9 bits: `0b011111111`. The `TMS` input must be held at logical 0 during the 8 LSB input in order for the machine to remain in `Shift-IR` state. The MSB bit of the instruction is pushed in when there is an exit from this state by setting `TMS` to logical 1. The red bit sequence is responsible for this step:



The `TDO` wire continues to output the sequence `0b100010000` which was loaded in the `Capture-IR` state.

After this step, we are in the `Exit1-IR` state.

* Great, the necessary commands are set in the `IR` registers and now we need to return to the `Run Test/Idle` state for further work. At this point, thanks to the last 1 on the `TMS` line we are in the `Exit-1-IR state` and hence according to the state diagram we need to set the following bit sequence on the `TMS` line to `Run Test/Idle`: [1, 0]. The orange bit sequence is responsible for this step:



* After setting the `IDCODE` command in the `IR` register we need to read `IDCODE` from the `DR` register. To do this the first step is to go to the `Shift-DR` state. To do this we set the following bit sequence [1, 0, 0] on the `TMS` pin considering that we are in the `Run Test/Idle` state at the moment. The yellow bit sequence is responsible for this step:



On the `TDO` line we have the sequence: [0, 0, 1]. The last one is already the LSB of our chip ID. The fact is that passing through the `Capture-DR` state our chip ID is loaded into the shift register and begins to move outward in the next clock cycles.

* In the `Shift-DR` state the remaining bits of the chip ID are unloaded. To remain in the `Shift-DR` state the `TMS` input must be held at logic 0 during the input of all bits except the MSB bit. The MSB data is pulled out when this state is exited by setting `TMS` to a logical 1. The green bit sequence is responsible for this step:



So we got a chip ID of the following kind:

  > 11101110001000000000010111010010

Let’s check this code according to the documentation:



Something is wrong here. What is wrong is that the LSB is in the usual position in the figure, but we took it in the inverted order. Let’s correct this situation:

  > 01001011101000000000010001110111

* And the final step is to go back to the `Run Test/Idle` state:


