---
id: "intr-diving-into-jtag-usage-scenarios-p-board-bring-up"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Usage Scenarios (Part 5): Board Bring Up"
summary: "Although assembled PCBs can be tested in production, as far as I know, it is not a mandatory procedure."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-06-12-diving-into-jtag-part-5.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-5#board-bring-up"
license: "CC-BY-SA-4.0"
mode: "V"
---

Although assembled PCBs can be tested in production, as far as I know, it is not
a mandatory procedure. So when these boards come to the Embedded department,
especially when it's the first batch that firmware/embedded developers will work
with, the boards should be tested to ensure they work properly before they start
working on the firmware. Usually (at least in the case where I worked), this is
done by the circuit designer. Still, since the microcontroller is empty, this
check is limited to the test that the board does not burn up when turned on and
that the power supply system provides all the necessary voltages.

Sometimes, a special test firmware can be prepared specifically for bring-up,
which automatically or via the CLI interface can enable/disable board modules
for testing. In any case, no matter how it happens, bring-up almost always
requires interaction between the embedded and circuit designer and additional
work to create test firmware.

However, JTAG Boundary Scan can facilitate this work by allowing the circuit
designer to control the microcontroller pins and thus perform a better and
deeper analysis of the board without depending on the programmer. It also saves
the programmer from having to write special firmware for bring-up. You only need
a test board, a .BSDL file for the corresponding microcontroller, a debugger,
and a unique program to control the controller pins through GUI. Also, an
additional advantage of this approach is universality, i.e., you don't need to
write a new version of the test firmware for each new microcontroller. And if
you remember that Boundary Scan allows you to check the signal integrity for a
multiprocessor chain, where processors may have BGA cases and multilayer boards,
and it may be very difficult to get to the contacts with probes.

Let's see what is needed for an elementary bring-up. To begin with, at least,
you need to be able to control the microcontroller pins (set to logic one/logic
zero) and read the state in which the microcontroller pin is located, and JTAG
allows you to do this, and programs like TopJTAG Probe allow you to do it more
or less conveniently.

As a board for bring-up, I will use what I am already familiar with from the
previous parts.
[STM32F407G-DISC1](https://www.st.com/en/evaluation-tools/stm32f4discovery.html)
with microcontroller
[STM32F407VG](https://www.st.com/en/microcontrollers-microprocessors/stm32f407vg.html).

### GPIO output control

Let's control the LEDs on our board. Quite a workable task for bring-up. So we
know that the LEDs are connected to pins: `PD12`, `PD13`, `PD14`, `PD15`. They
are turned on by setting the pin to a logical one and turned off by a logic
zero. To select the required level on a pin, it is necessary to find this pin in
the _Pin_ window and select the necessary actions from the context menu:

`<iframe width="100%" height="600px" src="https://www.youtube.com/embed/DrXdemXd80I" frameborder="0" allowfullscreen>``</iframe>`

### GPIO input state view

Another necessary operation for such a bring-up is to view the state of the chip
pin. This can also be done using the JTAG Boundary Scan and TopJTAG application.
You can view the output state either in the _Watch_ window or in the _Waveform_
window. Let's look at the state of the output to which the button is connected:

`<iframe width="100%" height="600px" src="https://youtube.com/embed/DrXdemXd80I" frameborder="0" allowfullscreen>``</iframe>`

> **Note:** As mentioned in the article
> [Diving into JTAG. Part 3 - Boundary Scan](https://interrupt.memfault.com/blog/diving-into-jtag-part-3),
> there can be several scan cells per pin, and here you can see two of them: one
> for receiving and one for transmitting. When the controller transmits
> something, the receiving scan cell duplicates this signal, as seen in the
> video with LEDs. Still, if the output works only for receiving, the signal is
> present only on one cell, as seen in the video with the button.
