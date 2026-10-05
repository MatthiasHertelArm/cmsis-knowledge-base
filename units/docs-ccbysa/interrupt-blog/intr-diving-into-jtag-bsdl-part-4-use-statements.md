---
id: "intr-diving-into-jtag-bsdl-part-4-use-statements"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4): Use Statements"
summary: "The use statement indicates that a particular package or library will be used in the current context. For example:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4#use-statements"
license: "CC-BY-SA-4.0"
mode: "V"
---

The use statement indicates that a particular package or library will be used in
the current context. For example:

```plaintext
use STD_1149_1_1994.all;
```

indicates that this file uses the IEEE 1149.1 1994 version of the IEEE 1149.1
standard library. In the BSDL context, this expression indicates that the
definitions and constructs provided in the 1994 IEEE 1149.1 standard are used to
describe the boundary scan behavior. This ensures that the description is
compatible with tools supporting that standard.
