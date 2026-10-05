---
id: "intr-the-best-and-worst-mcu-sdks"
type: "concept"
domain: "debug"
title: "The Best and Worst MCU SDKs"
summary: "In 2020, an MCU is much more than a hunk of silicon. Indeed, it comes with a whole ecosystem including a BSP, integrated third-party libraries, tooling, field application support, and more."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-10-the-best-and-worst-mcu-sdks.md"
doc_source: "https://interrupt.memfault.com/blog/the-best-and-worst-mcu-sdks"
license: "CC-BY-SA-4.0"
mode: "V"
---

In 2020, an MCU is much more than a hunk of silicon. Indeed, it comes with a
whole ecosystem including a BSP, integrated third-party libraries, tooling,
field application support,  and more.

As firmware engineers, we are often handed down an MCU selection as a fait
accompli. Cost concerns, peripheral, or pinout requirements often take precedent
over the SDK.

Yet we are allowed to have an opinion. So here for you today is my first post in
a new “comparing MCU SDKs” series.



In this post, I download SDKs for 10 popular Cortex-M4 microcontrollers, and
evaluate how straightforward it is to get a simple example compiling. I include
some step by step instructions to get started, a rating out of 10, and a few
comments.



It goes without saying that this is an opinion based on my own very specific
setup (MacOS, vim). Your mileage may vary!
