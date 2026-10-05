---
id: "intr-using-asserts-in-embedded-systems-why-you-should-assert"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: Why You Should Assert"
summary: "Using Asserts in Embedded Systems: Why You Should Assert"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#why-you-should-assert"
license: "CC-BY-SA-4.0"
mode: "V"
---

- Asserts generally occur while the system is still in control (e.g. not in a
  HardFault, etc). This means that the system can safely perform cleanup
  operations and record debugging information.
- Developers connected to a debugger very quickly find programmatic mistakes and
  invalid usage of API's.
- Asserting function arguments removes the need to check for argument validity
  and error handling code in upper layers, which may in turn reduce code size.
- Good placement of asserts can reduce chances of exceptions by catching
  out-of-bounds accesses, invalid pointer dereferences, invalid state machine
  transitions, and nonsensical operations (like a malloc of 12MB on a 64kB MCU).
- Asserts can help developers quickly understand assumptions made by a certain
  piece of code (e.g. a module that takes a `uint8_t` but requires a value
  within the range of 1 to 64).
