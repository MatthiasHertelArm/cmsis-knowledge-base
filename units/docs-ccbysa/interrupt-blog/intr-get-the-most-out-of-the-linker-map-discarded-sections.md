---
id: "intr-get-the-most-out-of-the-linker-map-discarded-sections"
type: "concept"
domain: "debug"
title: "Get the most out of the linker map file: Digging into the map files / Discarded sections"
summary: "Functions and variables that are compiled to be included into the program aren't always part of the final binary if the linker doesn't find any reference to them."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-09-get-the-most-out-of-the-linker-map-file.md"
doc_source: "https://interrupt.memfault.com/blog/get-the-most-out-of-the-linker-map-file#discarded-sections"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Digging into the map files_

Functions and variables that are compiled to be included into the program aren't always part of the final binary if the linker doesn't find any reference to them. They are removed but still appear in the map file under the `Discarded input sections` part. As an example, here are some functions defined in `boards.c` that are never called and thus discarded:

```
 .text.bsp_board_led_state_get
                0x0000000000000000       0x28 _build/nrf52840_xxaa/boards.c.o
 .text.bsp_board_led_on
                0x0000000000000000       0x24 _build/nrf52840_xxaa/boards.c.o
```
