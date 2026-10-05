---
id: "intr-seamless-firmware-development-with"
type: "concept"
domain: "debug"
title: "Seamless firmware development with PlatformIO"
summary: "A few weeks ago, I wrote about MCU SDKs and how frustrating I sometimes found it to be confronted with one Eclipse-based IDE after another. If you haven't read my latest updates to that post, check it out!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-08-seamless-firmware-with-platformio.md"
doc_source: "https://interrupt.memfault.com/blog/seamless-firmware-with-platformio"
license: "CC-BY-SA-4.0"
mode: "V"
---

A few weeks ago, [I wrote about MCU SDKs](https://interrupt.memfault.com/blog/the-best-and-worst-mcu-sdks) and how frustrating I sometimes found
it to be confronted with one Eclipse-based IDE after another. If you haven't
read my latest updates to that post, check it out!

But what if I told you that there exists an embedded project management tool
which ties you neither to a toolchain, nor to a development environment? Did I
mention it is available for Windows, Linux, and Mac?



In this post, I'd like to introduce PlatformIO. I will go over what PlatformIO
is, how you can use it for your project, and what it is good at.  I also
highlight a few shortcomings worth keeping in mind.



While I am not ready to give PlatformIO a full-throated endorsement for all
projects, it works very well for specific platforms and RTOS-es. Most
importantly, it proposes an approach to library and toolchain management for
embedded that is the best I've seen yet. I hope you will give it a whirl!
