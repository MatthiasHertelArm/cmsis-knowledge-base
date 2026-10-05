---
id: "intr-parsing-logs-messages-for-instant"
type: "concept"
domain: "debug"
title: "Parsing Logs Messages for Instant Crash Analysis"
summary: "Having a logger display execution information on the terminal is pretty common for firmware developers. What's less common is having an instant stack trace when the program crashes."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-08-04-firmware-logs-stack-trace.md"
doc_source: "https://interrupt.memfault.com/blog/firmware-logs-stack-trace"
license: "CC-BY-SA-4.0"
mode: "V"
---

Having a logger display execution information on the terminal is pretty common for firmware developers. What's less common is having an instant stack trace when the program crashes.



In this post, I will introduce a few tools to implement a beautiful boosted logger. The example presented here is based on the nRF52 device and its SDK compiled with the GCC toolchain but can be ported to any other Cortex-M microcontroller.

> This post was originally published on [Cyril's website](http://www.cyrilfougeray.com/2020/07/27/firmware-logs-with-stack-trace.html).



(figure: Colorful stack)
