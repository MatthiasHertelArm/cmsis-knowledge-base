---
id: "intr-diving-into-jtag-bsdl-part-4-idcode-register-description"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4): IDCODE Register Description"
summary: "The IDCODE_REGISTER attribute is used to define the IDCODE register of the chip. This attribute is part of the IEEE 1149.1 (JTAG) specification. The format is:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4#idcode-register-description"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `IDCODE_REGISTER` attribute is used to define the `IDCODE` register of the
chip. This attribute is part of the IEEE 1149.1 (JTAG) specification. The format
is:

```plaintext
attribute IDCODE_REGISTER of <entity> : entity is
    "{specific attribute value}";
```

For example:

```plaintext
attribute IDCODE_REGISTER of STM32F405_415_407_417_LQFP100: entity is
     "XXXX" &                  -- 4-bit version number
     "0110010000010011" &      -- 16-bit part number
     "00000100000" &           -- 11-bit identity of the manufacturer
     "1";                      -- Required by IEEE Std 1149.1
```
