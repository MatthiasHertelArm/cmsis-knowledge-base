---
id: "intr-building-an-on-device-embedded-tes-motivation"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Motivation"
summary: "When developing any code, being able to test is crucial for sustainable development."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#motivation"
license: "CC-BY-SA-4.0"
mode: "V"
---

When developing any code, being able to test is crucial for sustainable development.

In the case of executable code on systems with GPOS, widely used solutions are GoogleTest or Catch libraries.
What we usually expect from such a framework is:
- a tool that will organize and orchestrate the execution of the tests
- basic functions/API to check the correctness of the results in the test
- features for scaling: fixtures, parameterized tests, executing tests multiple times, metrics

In the context of microprocessors, these libraries are not usable.
They rely on the file system, input/output into a terminal, and dynamic memory. They also do not care about tight limits for code size.

These frameworks are usable only for testing parts of the embedded firmware.
These parts are independent of the hardware: algorithms, internal business logic, and others.
We, however, can't test anything that is tied to the hardware.

For that reason, I decided to implement a custom opinionated testing framework designed for a specific use case: executing tests on the embedded hardware itself.

The goal is to be able to test embedded code that is tied to the hardware itself:
- interrupt-based mechanics
- control algorithms that are unpractical to simulate
- code tied to peripherals
