---
id: "intr-selecting-your-next-project-s-mcu-ee-and-firmware-engineers-mcu-features"
type: "concept"
domain: "debug"
title: "Selecting Your Next Project's MCU: EE and Firmware Engineers & MCU Features"
summary: "The requirements of an MCU for a firmware engineer look quite different. They care about significantly different things! Does the MCU have the peripherals needed, does it have good performance, and enough RAM and flash memory."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-05-24-choosing-an-mcu.md"
doc_source: "https://interrupt.memfault.com/blog/choosing-an-mcu#ee-and-firmware-engineers-mcu-features"
license: "CC-BY-SA-4.0"
mode: "V"
---

The requirements of an MCU for a firmware engineer look quite different. They
care about significantly different things! Does the MCU have the peripherals
needed, does it have good performance, and enough RAM and flash memory. As for
the software requirements, firmware engineers are also looking for a solid set
of drivers, supported OS's, and tools. Researching all of this is tedious work.

One way around this is to stick to the processors already in use in other
projects. The argument would be that the people involved already know the chip,
the tools are already available, and buying more of it might make it even
cheaper also for the other projects. If the current standard chip can not be
used then you can probably find one that can be used in the same family or at
least from the same vendor that fits the requirements. That might not be the
cheapest chip, it might not even be on the EE’s list, but we can select it
anyway. We convince the manager that it is easier to use this chip as we already
have the knowledge and tools and that new tools would come in more expensive
than the cheaper chip the EE has found. And this might be the right way to go.
It all depends.

If you are true to yourself, you probably have to admit that the effort planned
for “learning a new chip” is a combination of not wanting to learn something new
and the fear of running into issues with the new chip. There is the risk of
something going catastrophically wrong with the new chip, such as a missing
required feature or an unforeseen errata. But if the benefits outweigh the
risks, we should jump into the adventure.

The differences between chips are bigger than one would expect. For example, the
Raspberry Pi RP2040 is a 32bit dual-core processor that runs at a maximum of 130
MHz and costs about one dollar. The ATMEGA649-16MUR is an 8-bit single-core
processor running at a maximum of 16 MHz and costs $3.69. Pricing is a dark art
of the vendors and many factors influence it. If the vendor provides a widely
used framework for an established chip, the prices may go up (or not go down) as
people will want to stick with it. Then producing more of a chip that is being
used in a high turnaround product (Mobile phone,..) results in less effort than
switching the machines to something only a few customers need.
