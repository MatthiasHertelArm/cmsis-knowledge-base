---
id: "intr-pocket-article-undefined-behavior-undefined-trap-on-an-embedded-platform"
type: "concept"
domain: "debug"
title: "Pocket article: Undefined Behavior Sanitizer Trap on Error: Undefined trap on an embedded platform"
summary: "On an embedded platform, you might need to insert a software breakpoint (eg _asm_(\"bkpt 1\"); or similar) in the correct fault handler, and also deal with pushing / popping the stack frame prior to the ISR."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-06-22-ubsan-trap.md"
doc_source: "https://interrupt.memfault.com/blog/ubsan-trap#undefined-trap-on-an-embedded-platform"
license: "CC-BY-SA-4.0"
mode: "V"
---

On an embedded platform, you might need to insert a software breakpoint (eg
`__asm__("bkpt 1");` or similar) in the correct fault handler, and also deal
with pushing / popping the stack frame prior to the ISR.

The full description of that technique is beyond the scope of this article but
if you are headed down that path
[https://github.com/adamgreen/CrashCatcher](https://github.com/adamgreen/CrashCatcher)
is worth a look!









{:.no_toc}
