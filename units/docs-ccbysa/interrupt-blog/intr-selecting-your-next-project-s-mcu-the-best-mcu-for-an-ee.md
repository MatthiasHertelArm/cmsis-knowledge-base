---
id: "intr-selecting-your-next-project-s-mcu-the-best-mcu-for-an-ee"
type: "concept"
domain: "debug"
title: "Selecting Your Next Project's MCU: The Best MCU for an EE"
summary: "I assume you, the reader, are the person responsible for the firmware of your project and that you work with an electronics engineer (EE)."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-05-24-choosing-an-mcu.md"
doc_source: "https://interrupt.memfault.com/blog/choosing-an-mcu#the-best-mcu-for-an-ee"
license: "CC-BY-SA-4.0"
mode: "V"
---

I assume you, the reader, are the person responsible for the firmware of your
project and that you work with an electronics engineer (EE). If the EE presents
you with the finished PCB: Yeah, you don’t have to decide on the chip to use.
However, you might run into issues that the EE did not take into account.

For an EE the best chip has no pins at all, is the size of an SMD resistor, has
no special needs to power rails, runs at 0 Hz clock, and costs nearly nothing.
That would make it easy for the EE and getting it to work is within the
firmware's responsibility.

Often the EE will use the parametric search to find the microcontroller to use.
The parametric search is provided by the big distributors (Digikey, Farnell,
Mouser to name a few). It allows you to filter all available chips according to
their features. The EE can filter out all chips with the wrong voltage requirements,
unpractical packages (DIL, SMD, BGA), or improper operating temperature ranges
that the product needs to endure. These and many other filters are provided. In
the end, the EE sorts by price and selects the cheapest. Maybe they select a
handful and let the firmware engineer choose.

Easy right? Not exactly. The cheapest chip that meets the _hardware_ criteria is
usually one of the most painful chips to bring up and write firmware on. We've
all been there.
