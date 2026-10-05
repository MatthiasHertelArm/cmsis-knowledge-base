---
id: "intr-embedded-c-c-unit-testing-basics-overview"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Real World Unit Test Example / Overview"
summary: "We are tasked with writing a Key/Value storage module in a firmware project. The requirements are as follows:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#overview"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

We are tasked with writing a Key/Value storage module in a firmware project. The
requirements are as follows:

- The module should have the ability to read, write, and delete key/value pairs.
- The backing data should be stored in `littlefs`.
- The number of times a key/value pair is read, written, or deleted is counted
  using an `analytics.c` module with a function call to `analytics_increment`.
  This might be used to track roughly how often the flash chip is written to.
- The module should be locked by a mutex so that only one consumer can be
  writing, reading, or deleting from the `/kv` directory of `littlefs`.

In an ideal world, and in our realistic one as well, it is possible for us to
write this entire module _and_ test it without actually using real hardware.

Let's get started!

{:.no_toc}
