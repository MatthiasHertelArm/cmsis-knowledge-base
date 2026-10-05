---
id: "intr-selecting-your-next-project-s-mcu-the-best-mcu-for-a-firmware-engineer"
type: "concept"
domain: "debug"
title: "Selecting Your Next Project's MCU: The Best MCU for a Firmware Engineer"
summary: "What if we turn the tables and come up with the firmware list of chips that we then present to the EE? What should we filter the available chips for?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-05-24-choosing-an-mcu.md"
doc_source: "https://interrupt.memfault.com/blog/choosing-an-mcu#the-best-mcu-for-a-firmware-engineer"
license: "CC-BY-SA-4.0"
mode: "V"
---

What if we turn the tables and come up with the firmware list of chips that we
then present to the EE? What should we filter the available chips for?

### Peripherals and Software Stack

We should probably start with the available peripherals. If the product needs
one or more UART, SPI, I2C, CAN, USB, or Ethernet interfaces, then the chip
should better have them. Be cautious not to filter out too many chips at this
stage. Especially if you are designing a product that will be mass-produced. A
small difference in price can become a huge factor. Therefore, if the required
peripherals limit the selection too much, think about bit-banging an interface.
If we only need to read a few bytes from an external memory using I2C then doing
that with two GPIO pins and some code will probably be OK. Also don’t forget
about the “internal” peripherals, DMA, crypto accelerators, (watchdog) timers,
etc.

We also need to check the compatibility of the chip. Interfaces like USB, CAN,
and Ethernet are usually used in combination with a so-called “stack”. That is a
software library that implements all the complicated features of the interfaces.
If we need or want to use a certain stack then the peripheral in the selected
chip needs to be compatible. Otherwise, we might need to implement a driver or
switch to a different stack. Both can be a lot of work. Also, other code that we
want to reuse like libraries or (real-time) operation systems need to be checked
for compatibility. We need to weigh the price difference of the chip against the
amount of work needed to get the incompatible chip to work.

### Tooling

Another thing is tooling. We can not use a chip if we do not have a compiler to
generate code for it. We will need some way to flash the chip. (flash = write
the compiled code into the chip) A development board or simulator for the chip
will speed up firmware development before the project's PCB is available. A
debugger that lets you step through the code and check the values of variables
speeds up the finding of issues. If it can also provide trace information then
that helps to find the hard-to-find bugs. An IDE with syntax highlighting, that
allows for debugging and integrates with the version control system, will help
make software development more efficient.

The freely provided vendor tools might often be enough to get the firmware done.
But software development is often like driving in the dark. One has the map, so
what's the problem. But switching on the headlights helps with making the turns.
Good tools provide light. More light leads to fewer bugs. And therefore it leads
to new features faster. Even expensive tools can pay for themselves due to less
wasted development hours rather fast. The internet is full of war stories of
long bug hunts that would not have been necessary if the right tool would have
shone some light on the issue early on. Also, the best tools are usually not
chip-specific. Heck. Even the ST-provided ST-link debugger can work on Microchip
(and other) devices if used with OpenOCD! So don’t hesitate to ask your manager
for the expensive tools even if you could get it done with what you already
have. Less development time spent is a good argument.

### Community & Popularity

Another plus side for a chip can be if it is part of a bigger chip family. (The
base for the “standard chip” argument) Don’t value this too high. But in case of
an emergency, it can help. If at the end of firmware development the release
date of the product is close but the firmware is just a little bit too big, then
switching to the pin-compatible variant with just a bit more flash or a bit more
RAM might save the day. It is always good to have a plan B even if you never
expect to use it. Don’t plan to fail!

Community support and documentation quality might also be decision-leading
factors. Popularity plays a role. If you select a chip that nobody uses but you,
if the documentation is brief but incorrect and even the vendor suggests using a
different chip, then better listen. Writing firmware for a widely used chip
might help if you run into issues as someone else might have had the same issue
and already found the solution. It will also help on the compatibility side. The
chances that a new library you want to use has support for the chip will be
higher. But again just being a popular chip alone doesn’t mean much. But if you
need to decide between two otherwise equal chips, the more popular will probably
be the better choice. It also has a lower risk of production being stopped. So
unless you are in a chip shortage where the most popular chips are sold out the
fastest, the more popular chip is the better choice.

If you work in a company that buys a lot of chips then you can and should also
ask the distributors and their Field Application Engineers (FAE) to suggest a
chip that meets your requirements. Don’t expect them to recommend a competitor’s
chip though. It is also a good confirmation if the FAE recommends the same chip
you selected.
