---
id: "intr-diving-into-jtag-bsdl-part-4-pin-mapping-s"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4): Pin Mapping(s)"
summary: "This element maps logical signals from the Logical Port Description section onto the physical pins of a particular device package."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4#pin-mapping-s"
license: "CC-BY-SA-4.0"
mode: "V"
---

This element maps logical signals from the Logical Port Description section onto
the physical pins of a particular device package. This is necessary because the
logical signals of a chip may be the same, but the specific pins are different
for different packages. For example:

```plaintext
attribute PIN_MAP of XYZ : entity is PHYSICAL_PIN_MAP;

constant DW:PIN_MAP_STRING:=
    "OE  :  1," &
    "Y   :  (2,3,4)," &
    "A   :  (5,6,7)," &
    "GND :  8," &
    "VCC :  9," &
    "TDO :  10," &
    "TDI :  11," &
    "TMS :  12," &
    "TCK :  13," &
    "NC  :  14";
```

The distribution of single pins is quite transparent: one logic name - one pin:

```plaintext
"OE  :  1," &
```

The buses are described next way:

```plaintext
"Y   :  (2,3,4)," &
```
