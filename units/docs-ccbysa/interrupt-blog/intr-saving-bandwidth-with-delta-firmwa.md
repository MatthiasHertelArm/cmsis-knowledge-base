---
id: "intr-saving-bandwidth-with-delta-firmwa"
type: "concept"
domain: "debug"
title: "Saving bandwidth with delta firmware updates"
summary: "Firmware update capability has become a must-have for most devices."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-08-09-ota-delta-updates.md"
doc_source: "https://interrupt.memfault.com/blog/ota-delta-updates"
license: "CC-BY-SA-4.0"
mode: "V"
---

Firmware update capability has become a must-have for most devices. Whether to
add new features after launch, fix bugs, or urgently patch a security hole,
firmware updates gives modern teams the flexibility they need to move fast and
react to a changing environment.

I've written at length about firmware updates in the past, including on
Interrupt with a [Firmware Update Cookbook](https://interrupt.memfault.com/blog/device-firmware-update-cookbook) and [a post about code
signing](https://interrupt.memfault.com/blog/secure-firmware-updates-with-code-signing),
and even recorded a [webinar on the
topic](https://memfault.com/webinars/device-firmware-update-best-practices/).

Since then, I've heard from some of you that they've run into roadblocks
implementing firmware updates on bandwidth-limited devices. Indeed devices
connected over low bandwidth links like 900MHz wireless or LoRaWAN often
struggle to download a full firmware image in any reasonable time.

One solution is to implement _delta updates_, a technique that
allows devices to download only the bits and pieces they need rather than full
system images.



In this post, we introduce the concept of delta (i.e. partial) firmware updates,
explain why you may want to implement them in your projects and go through an
example implementation from top to bottom.
