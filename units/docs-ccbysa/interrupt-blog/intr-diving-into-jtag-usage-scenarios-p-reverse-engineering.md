---
id: "intr-diving-into-jtag-usage-scenarios-p-reverse-engineering"
type: "concept"
domain: "debug"
title: "Diving into JTAG — Usage Scenarios (Part 5): Reverse Engineering"
summary: "One of the exciting things is that the SAMPLE instruction does not affect the firmware in any way, which means that you can use it for a logic analyzer built into the controller. Where can it be useful?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-06-12-diving-into-jtag-part-5.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-5#reverse-engineering"
license: "CC-BY-SA-4.0"
mode: "V"
---

One of the exciting things is that the `SAMPLE` instruction does not affect the
firmware in any way, which means that you can use it for a logic analyzer built
into the controller. Where can it be useful? For example, when you don't have an
oscilloscope or analyzer. And, as it seems to me, this function can be useful
when reverse engineering a board, especially microchips with BGA-type packages
or multilayer boards when it is difficult to determine with a simple multimeter
which pin of the chip is responsible for what and then using the `SAMPLE`
command can help.

However, this is a very simple logic analyzer. While seeing some very simple and
low-speed signals (such as controlling LEDs, pressing a button, or controlling
some load) with this analyzer, it is quite easy and simple as shown in the
chapter above, when dealing with higher-speed protocols, the signal that is
drawn on the Waveform is very distorted. Here is an example of how the
transmission of the symbol "**U**" (which has a code equal to `0x55`) through
UART at 1200 baud looks like:



 


and at 2400 baud:



 


As you can see, even at 2400 baud, the signal is distorted (2 bits were lost).

And here is what the SPI signal looks like with baudrate of 250 KBits/sec:



 


As you can see, it is hard to recognize SPI from this waveform, especially if
you look at the SCK signal.

Most likely, the impossibility of analyzing higher-speed signals in this way is
rooted in the limitations of the software and debugger that I use because they
are not designed for such a task. There may be software and hardware for this
purpose somewhere, but unfortunately, they are unavailable to me.

However, despite such limited use of this functionality, it can still be useful
in some specific cases: you can see which pins of the controller are alive and
functioning at all or analyze the logic of the firmware, for example on this
example:

`<iframe width="100%" height="600px" src="https://youtube.com/embed/Z1xsTKtW4J8" frameborder="0" allowfullscreen>``</iframe>`

You can see that after we press the button, communication starts on some
protocol. Although it is difficult to understand it from the signal, it is SPI
protocol.
