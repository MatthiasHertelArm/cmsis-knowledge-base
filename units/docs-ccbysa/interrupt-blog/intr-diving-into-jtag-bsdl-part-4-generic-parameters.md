---
id: "intr-diving-into-jtag-bsdl-part-4-generic-parameters"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4): Generic Parameters"
summary: "The generic keyword is used to define a parameter that can be changed when implementing the description in a particular device."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4#generic-parameters"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `generic` keyword is used to define a parameter that can be changed when
implementing the description in a particular device.

```plaintext
generic (PHYSICAL_PIN_MAP : string := "DW");
```

In this example, `PHYSICAL_PIN_MAP` is a generic parameter that defines the chip
body type, which will default to the value "DW".
