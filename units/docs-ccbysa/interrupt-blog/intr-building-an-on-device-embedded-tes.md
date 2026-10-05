---
id: "intr-building-an-on-device-embedded-tes"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library"
summary: "There are too few C/C++ testing libraries designed for embedded devices. The traditional libraries are not designed for constrained resources and rely on host functionality like a filesystem or standard output."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are too few C/C++ testing libraries designed for embedded devices. The traditional libraries are not designed for constrained resources and rely on host functionality like a filesystem or standard output.

In this post, I detail why I've decided to design a new testing library for microcontrollers and cover the rationale, design choices, and thoughts on the prototype.
