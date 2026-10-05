---
id: "intr-embedded-c-c-unit-testing-basics-unit-testing-overview"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Unit Testing Overview"
summary: "Unit testing is a method of testing software where individual software components are isolated and tested for correctness."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#unit-testing-overview"
license: "CC-BY-SA-4.0"
mode: "V"
---

Unit testing is a method of testing software where individual software
components are isolated and tested for correctness. Ideally, these unit tests
are able to cover most if not all of the code paths, argument bounds, and
failure cases of the software under test.

Through proper use of unit tests, and especially while using practices from Test
Driven Development (TDD)[^0], the time it takes to **stabilize** embedded
software can decrease dramatically, making individuals and teams more productive
and firmware less likely to experience functional bugs, control flow bugs, and
even fatal issues, such as memory leaks and (gasp!) bootloops.

{:.no_toc}

### Life Before Unit Testing

Here are a few examples that I've experienced in the past that were alleviated
by the team doubling down on unit testing the firmware.

- You find testing on target hardware **slow** and **inconvenient**, especially
  when multiple devices (e.g. a mobile phone) or prior setup (e.g. a factory
  reset) is required
- Bugs and regressions occur **repeatedly** in a single piece of software.
- Deadlocks, HardFaults and Memory Leaks are the norm and have become accepted
  (unit testing example for preventing deadlocks included below!).
- The amount of time spent debugging and testing firmware is **60% or
  more**[^1].
- The first instinct when starting a new software module is to write a chunk of
  code and **test on hardware**.

{:.no_toc}

### Life After Unit Testing (Possibly)

At a previous company, after scrapping most legacy code and writing new modules
with 90%+ code coverage and through the use of TDD, this is what development
felt like sometimes.

- You write a new file, maybe an in-flash log storage module, and it works the
  **first time** when flashed on the device (no better feeling).
- Regressions are caught **immediately** when runnings tests locally or in CI.
- Memory leaks are raised as errors in unit tests.
- Testing a majority of the firmware only takes **a minute**.
- The overall codebase has better structure and cleaner boundaries between
  modules.

{:.no_toc}
