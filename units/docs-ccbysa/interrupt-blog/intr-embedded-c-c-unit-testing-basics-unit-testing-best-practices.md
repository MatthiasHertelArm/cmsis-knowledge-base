---
id: "intr-embedded-c-c-unit-testing-basics-unit-testing-best-practices"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Unit Testing Best Practices"
summary: "The \"Minimal Example\" is a contrived example and very rarely will there be a test with no other dependencies."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#unit-testing-best-practices"
license: "CC-BY-SA-4.0"
mode: "V"
---

The "Minimal Example" is a contrived example and very rarely will there be a
test with _no_ other dependencies. Firmware is naturally coupled with other
parts of hardware, and that makes it difficult at first to set up a unit test.

For example, a flash storage module may call an `analytics_inc()` function to
record the number of writes, a `watchdog_feed()` function during a large flash
erase operation, and `timer_schedule()` to help defragment the flash later in
the future. If we are testing only the flash key/value store, we _do not_ want
to include the analytics, watchdog, and timer source files into our unit test.

That brings us to a few best practices to follow, especially when writing unit
tests for complex and entangled code.

- Each `TEST()` within a unit test file should ideally test a single path or
  feature of the module. A test called `TestEverything` is an anti-pattern.
- Each test should be _quick_. A few milliseconds is ideal, and one second is
  the worst case run time.
- Each unit test should ideally include one _real_ implementation of a module.
  The rest should be stubbed or fake versions of the modules not under test.
- Those stubbed and fake versions of modules should be written early, reused,
  and shared.

Which brings us to explaining what are stubs, fakes, and mocks?
