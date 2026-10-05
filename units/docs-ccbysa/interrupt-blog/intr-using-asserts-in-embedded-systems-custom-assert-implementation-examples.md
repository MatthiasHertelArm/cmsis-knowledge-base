---
id: "intr-using-asserts-in-embedded-systems-custom-assert-implementation-examples"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: Custom Assert Implementation Examples"
summary: "It's now time to start asserting ourselves. The examples provided below progress from a naive solution to the best one I've seen and used to date, with each becoming more expressive while also using less (precious) code space."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#custom-assert-implementation-examples"
license: "CC-BY-SA-4.0"
mode: "V"
---

It's now time to start asserting ourselves. The examples provided below progress
from a naive solution to the best one I've seen and used to date, with each
becoming more expressive while also using less (precious) code space.

> NOTE: All of these implementations will behave similarly if a debugger is
> attached. The goal of the exercise is to improve upon asserts that are hit
> while a debugger is **not** attached and all we have is a logging system.

The code starts out in `prv_main`, and will call one of two functions,
`prv_main_path_A`, or `prv_main_path_B`, depending on a randomly generated
boolean variable. Both of these functions will then call either `assert_path_A`
or `assert_path_B`, which gives us **four** unique paths our code can take on
boot.

The example is a bit contrived, but if we had to do a postmortem analysis of
this assert, we'd like to know the path the system took before the assert.
Thankfully, we can build an assert implementation that does just this.
