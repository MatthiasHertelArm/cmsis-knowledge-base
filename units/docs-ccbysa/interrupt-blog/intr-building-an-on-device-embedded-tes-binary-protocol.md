---
id: "intr-building-an-on-device-embedded-tes-binary-protocol"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Binary Protocol"
summary: "The binary protocol is intentionally considered an implementation detail, as I want to have the freedom to change it at will."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#binary-protocol"
license: "CC-BY-SA-4.0"
mode: "V"
---

The binary protocol is intentionally considered an implementation detail, as I want to have the freedom to change it at will.

It is implemented with a C++ protocol library I did previously. The short description is: imagine protocol buffers, but instead of an external tool, it is just a C++ library that gets the definition of protocol via templates.
