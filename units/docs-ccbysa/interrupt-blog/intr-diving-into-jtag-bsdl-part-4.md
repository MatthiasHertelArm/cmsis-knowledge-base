---
id: "intr-diving-into-jtag-bsdl-part-4"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4)"
summary: "In the previous article of this series, we briefly touched on how .bsd files written in Boundary Scan Description Language (BSDL) describe the structure of the boundary scan chain and the instruction set."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the previous article of this series, we briefly touched on how `.bsd` files
written in Boundary Scan Description Language (BSDL) describe the structure of
the boundary scan chain and the instruction set. In this article, we will
examine this language's syntax more closely before seeing how `.bsd` files are leveraged
in JTAG testing in the next article.







> **Note**: In this series of articles, I discuss JTAG from the firmware
> engineer's point of view and to the extent necessary for the firmware
> engineer's work. I do not aim to thoroughly describe the syntax and format of
> BSDL, rather describe it to the extent necessary for simple understanding of
> the files supplied by the vendor chips. Also, I concentrate on the BSDL
> format, although other formats can be used to describe TAP chip controllers:
> SVF, STAPL, etc.
