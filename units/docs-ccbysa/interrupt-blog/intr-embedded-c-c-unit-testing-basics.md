---
id: "intr-embedded-c-c-unit-testing-basics"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics"
summary: "Complex embedded projects have thousands and frequently tens of thousands lines of code. The majority of that code is entirely software (rather than \"firmware\"), and software in every industry is typically unit tested."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics"
license: "CC-BY-SA-4.0"
mode: "V"
---

Complex embedded projects have thousands and frequently tens of thousands lines
of code. The majority of that code is entirely software (rather than
"firmware"), and software in every industry is typically unit tested. However,
in the embedded and firmware industry, unit testing is typically an
after-thought or a task that is begun after working on a project for months or
even years.

Today's firmware projects require filesystems, BLE and Wi-Fi stacks, specialized
data structures (both in-memory and in-flash), and complex algorithms, such as
those interpreting accelerometer and gyroscope data. _All_ of these items can be
easily unit tested after becoming acquainted with best practices and writing a
few tests of your own.



In this post, we go into detail on how to properly build abstractions to stub,
fake, and mock out implementations of low level embedded software and provide a
full real-world example of a unit test using the CppUTest 3.8 unit test
framework.



This is the second post in our [Building Better Firmware series](),
following the [post](https://interrupt.memfault.com/blog/continuous-integration-for-firmware)
about Continuous Integration for firmware projects, which is a wonderful pre-cursor
to this post.
