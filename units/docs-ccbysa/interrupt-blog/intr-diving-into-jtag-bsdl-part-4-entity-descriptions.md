---
id: "intr-diving-into-jtag-bsdl-part-4-entity-descriptions"
type: "concept"
domain: "debug"
title: "Diving into JTAG — BSDL (Part 4): Entity Descriptions"
summary: "The entity statement names the entity, such as the device name (e.g., STM32F405_415_407_417_LQFP100). An entity description begins with an entity statement and terminates with an end statement:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-29-diving-into-jtag-part-4.md"
doc_source: "https://interrupt.memfault.com/blog/diving-into-jtag-part-4#entity-descriptions"
license: "CC-BY-SA-4.0"
mode: "V"
---

The entity statement names the entity, such as the device name (e.g.,
`STM32F405_415_407_417_LQFP100`). An entity description begins with an `entity`
statement and terminates with an `end` statement:

```plaintext
entity XYZ is
    {statements to describe the entity go here}
end XYZ
```

All of the rest of the attributes and descriptions that we will look at we can
be located within this block. This structure allows the device to be described
for testing, debugging, and diagnostic purposes, providing the necessary
information for tools and equipment utilizing boundary scan technology.
