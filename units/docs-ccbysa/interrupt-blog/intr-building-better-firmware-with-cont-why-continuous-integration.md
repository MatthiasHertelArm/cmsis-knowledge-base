---
id: "intr-building-better-firmware-with-cont-why-continuous-integration"
type: "concept"
domain: "debug"
title: "Building Better Firmware with Continuous Integration: Why Continuous Integration"
summary: "Continuous Integration requires efforts, rigor, and infrastructure. It can even be very expensive! So why do it at all? In my opinion, there is a scale at which there are no alternatives."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-09-17-continuous-integration-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/continuous-integration-for-firmware#why-continuous-integration"
license: "CC-BY-SA-4.0"
mode: "V"
---

Continuous Integration requires efforts, rigor, and infrastructure. It can
even be very expensive! So why do it at all? In my opinion, there is a
scale at which there are no alternatives.

First and foremost, CI enforces the level of discipline required to keep a
codebase working at scale. As complexity and velocity grow:
* Finding when and where an issue was introduced gets more difficult
* Side effects are less well understood, making it more likely that a change in
   one part of the codebase will break a feature in another.
* Testing every feature and hardware configuration takes more and more time.

Additionally, CI infrastructure serves as a reference environment which can be
used to reproduce builds and generate shipping images. No more "it works on
my machine". If it fails in CI, it must be considered broken.
