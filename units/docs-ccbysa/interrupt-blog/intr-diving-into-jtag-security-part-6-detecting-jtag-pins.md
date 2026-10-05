---
id: "intr-diving-into-jtag-security-part-6-detecting-jtag-pins"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Security (Part 6): Attack / Detecting JTAG pins"
summary: "If there is absolutely no documentation for a given chip, the first thing an attacker would do is detect the actual JTAG pins. Special tools leverage some features of the JTAG protocol to automate the detection process."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-08-14-diving-into-jtag-part-6.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-6#detecting-jtag-pins"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Attack_

If there is absolutely no documentation for a given chip, the first thing an
attacker would do is detect the actual JTAG pins. Special tools leverage some
features of the JTAG protocol to automate the detection process. Let's dive into
them.

#### IDCODE Scan

Feature one: very often the `IR` register is connected to the `IDCODE` register,
which means that the intended pinout can be tested by a method called **IDCODE
Scan**. This method is simple because there is no need to scan `IR` and the
`IDCODE` register has a fixed length of 32 bits. The algorithm of the method is
as follows:

1. First we select the pins we want to scan and put these pins in correspondence
   with JTAG lines (`TMS`, `TCK`, etc.), by luck, as you want. But, if there are
   too many pins to be tested, you can potentially reduce their number by doing
   some work with measuring the electrical parameters (resistance, voltage) of
   the tested pins and using these measurements to draw conclusions about the
   pin belonging to one or another JTAG signal, at least to determine GND and
   VCC and not to include these pins in further scanning. This procedure is
   shown very well in this video [clip](https://youtu.be/_FSM_10JXsM?t=753).
2. Generate the sequence `0b0100` on the selected `TMS` pin to move to the
   `Shift-DR` state.
3. Hold `TMS` in logic zero and generate 32 clock pulses on the `TCK` pin.
4. Read the bits to be advanced on `TDO`.
5. If more than one zero or one is read from `TDO`, this is a pretty good
   indication that the electrical JTAG connection is working properly. You can
   try googling the read `IDCODE` and with some luck, you will be able to
   determine not only the JTAG pins, but also the type of microcontroller. If
   the `TDO` pin reads only ones or zeros, you have incorrectly assigned the
   pins in step 1, and you need to reassign the pins and repeat the whole
   procedure.

However, this method has a number of disadvantages:

- This method does not find the `TDI` pin.
- If the JTAG circuit contains more than one TAP, it may take more than 32
  iterations to find `IDCODE`, which means that if after e.g. 64 iterations you
  do not get a `TDO` pattern similar to `IDCODE` on the `TDO` pin, it does not
  mean that you have selected the wrong pins; it is possible that the JTAG
  circuit contains many TAPs.

#### BYPASS Scan

This method uses the `BYPASS` register to scan the JTAG circuit. The `BYPASS`
register allows you to skip a logic element in the circuit and directly transfer
data from input to output, minimizing latency.

1. The first step is the same as the first step in the `IDCODE` scan method.
2. Send the sequence `0b01100` on the selected `TMS` pin to move it to the
   `Shift-IR` state.
3. Send the `BYPASS` command. Since the size of the `IR` register is not known,
   you have to send a large number of ones (as many as 1024, for example).
4. Send the sequence `0b11000` to the selected `TMS` pin, thus moving to the
   `Shift-DR` state.
5. Using the `TDI` output - send some bit pattern that can be easily recognized.
6. Read the bits from the `TDO` pin. If a bit pattern is detected, it means that
   you have selected the pins correctly.

This algorithm is slower than the previous one, but it can detect all JTAG pins.

> If you have a lot of candidate output, it is recommended to first reduce the
> number of candidates using `IDCODE Scan` and then refine `BYPASS Scan`.

Of course, every time to do all these steps manually is quite boring and tedious
so smart people have long ago automated this process. Quite popular tools are:
[JTAGenum](https://github.com/cyphunk/JTAGenum/tree/master) and
[JTAGULATOR](http://www.grandideastudio.com/jtagulator/).

> If the highest level of RDP 2 protection has been applied to the
> microcontroller, JTAGulator and similar tools will not help.

Examples of such attacks are described in more detail in the following sources:

- [JTAG Scanning](https://github.com/cyphunk/JTAGenum/wiki/Embedded-Analysis#jtag-scanning)
- [Hardware Debugging for Reverse Engineers Part 2: JTAG, SSDs and Firmware Extraction](https://wrongbaud.github.io/posts/jtag-hdd/)
- [JTAGulator: Introduction and Demonstration](https://youtu.be/uVIsbXzQOIU)
- [03 - How To Find The JTAG Interface - Hardware Hacking Tutorial](https://youtu.be/_FSM_10JXsM)
