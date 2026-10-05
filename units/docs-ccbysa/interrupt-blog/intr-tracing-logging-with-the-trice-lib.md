---
id: "intr-tracing-logging-with-the-trice-lib"
type: "concept"
domain: "debug"
title: "Tracing & Logging with the `TRICE` Library (Interrupts too!)"
summary: "If you develop software for an embedded system, you need some kind of system feedback. Debuggers are awesome tools, but when it comes to analyzing dynamic behavior in the field, they cannot be used."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-01-12-trice.md"
doc_source: "https://interrupt.memfault.com/blog/trice"
license: "CC-BY-SA-4.0"
mode: "V"
---



If you develop software for an embedded system, you need some kind of system feedback. Debuggers are awesome tools, but when it comes to analyzing dynamic behavior in the field, they cannot be used.

For remote debugging, many engineers turn to `printf`, which can usually be quickly put in place after having a `putchar()` implemented. This turns out to be an expensive way, in terms of processor clocks and required FLASH memory for the strings.

If you're using a bigger microcontroller, you might have tracing hardware like an ETM. but it requires expensive tools and a direct connection, so it can not be used to debug in-field issues.

Unhappy with this situation, you might start building clever solutions to do in-field debugging, such as using digital pins, streaming byte sequences of tracing data, or even emitting some proprietary LED blinking codes, all of which would be difficult to build and interpret.



Embedded engineers need something as easy to use as `printf`, usable within interrupts, small enough for today's MCU's, and have minimal performance impact when running. The _Trice_ technique tries to fill this gap. It is the result of a long-year dissatisfaction and several attempts to find a loophole to make embedded programming more fun and effective.
