---
id: "intr-diving-into-jtag-bsdl-part-4-logical-port-description"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4): Logical Port Description"
summary: "The port description gives logical names to the I/O pins, and defines their function as input, output, bidirectional, and so on."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4#logical-port-description"
license: "CC-BY-SA-4.0"
mode: "V"
---

The port description gives **logical** names to the I/O pins, and defines their
function as input, output, bidirectional, and so on.

```plaintext
port (
    OE    : in      bit;
    Y     : out     bit_vector(1 to 3);
    A     : in      bit_vector(1 to 3);
    GND   : linkage bit;
    VCC   : linkage bit;
    NC    : linkage bit;
    TDO   : out     bit;
    TMS   : in      bit
    TDI   : in      bit
    TCK   : in      bit
);
```

The `port` block contains both "useful" pins of the chip and the JTAG pins, as
well as power, ground, and missing pins - pins that are not supposed to be
connected to the chip.

If the port is a single port, it is marked as `bit`. If it is a bus, it is
labeled as `bit_vector(X to Y)`. Inputs are `in`, outputs are `out`, and
bidirectional lines are `inout`. Power/ground lines, analog I/O, and pins not
connected to the crystal are marked as `linkage`.
