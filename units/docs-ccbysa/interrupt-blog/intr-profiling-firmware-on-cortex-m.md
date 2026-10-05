---
id: "intr-profiling-firmware-on-cortex-m"
type: "concept"
domain: "debug"
title: "Profiling Firmware on Cortex-M"
summary: "Although microcontrollers in 2020 sometimes come with GHz clock frequencies and even multiple cores, performance is a major concern when developing embedded applications. Indeed, most firmware projects face some real-time constraints which must be carefully managed."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-02-profiling-firmware-on-cortex-m.md"
doc_source: "https://interrupt.memfault.com/blog/profiling-firmware-on-cortex-m"
license: "CC-BY-SA-4.0"
mode: "V"
---

Although microcontrollers in 2020 sometimes come with GHz clock frequencies and
even multiple cores, performance is a major concern when developing embedded
applications. Indeed, most firmware projects face some real-time constraints
which must be carefully managed.

Good profiling tools are therefore essential to firmware development.
Historically, profiling was done by toggling GPIOs when specific parts of the
code execute. A logic analyzer could then be used to measure the time between
different GPIO toggles.

Today, modern microcontrollers implement multiple features to enable advanced
profiling techniques. All you need is a debugger and a laptop to get started.


In this post, we explore different techniques that can be used to profile
firmware applications running on ARM Cortex-M microcontrollers. To profile our
Mandelbrot application on STM32, we start with a naive debugger-based sampling
method, and eventually discover ITM, DWT cycle counters, and more!
