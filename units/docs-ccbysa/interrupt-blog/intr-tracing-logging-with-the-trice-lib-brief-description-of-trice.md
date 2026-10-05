---
id: "intr-tracing-logging-with-the-trice-lib-brief-description-of-trice"
type: "concept"
domain: "debug"
title: "Tracing & Logging with the `TRICE` Library (Interrupts too!): Brief Description of Trice"
summary: "Trice is a small, performant software tracer and logger and consists of these parts"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-01-12-trice.md"
doc_source: "https://interrupt.memfault.com/blog/trice#brief-description-of-trice"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Trice_ is a small, performant software tracer and logger and consists of these parts

- [trice.c](https://github.com/rokath/trice/tree/master/pkg/src/trice.c) contains the [less than 1KB](https://github.com/rokath/trice/tree/master/docs/TriceSpace.md) runtime code, which uses [triceConfig.h](https://github.com/rokath/trice/tree/master/test/MDK-ARM_STM32G071RB/Core/Inc/triceConfig.h) as setup.
- [trice.h](https://github.com/rokath/trice/tree/master/pkg/src/trice.h) containing a **C** language macro `TRICE`, generating [tiny code](https://github.com/rokath/trice/tree/master/docs/TriceSpeed.md) for getting real-time `printf` comfort at "speed-of-light" for any microcontroller.
  
Example:

  ```c
  float x = 3.14159265/4;
  TRICE( Id(12345), "info:π/4 is %f with the bit pattern %032b\n",
      aFloat(x), x );
  ```

- PC tool **trice**, executable on all [Go](https://golang.org) platforms.


