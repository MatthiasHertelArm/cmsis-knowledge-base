---
id: "intr-beyond-error-codes-debugging-ill-d-step-2-utilize-all-compiler-error-report"
type: "concept"
domain: "debug"
title: "Beyond Error Codes - Debugging Ill-Defined Problems: Steps / Step 2 - Utilize All Compiler Error Reporting Capabilities"
summary: "If you're using vendor tooling that auto-generates your build system for you, you might be missing out on some no-effort error prevention!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-04-18-debugging-steps.md"
doc_source: "https://interrupt.memfault.com/blog/debugging-steps#step-2-utilize-all-compiler-error-reporting-capabilities"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps_

If you're using vendor tooling that auto-generates your build system for you,
you might be missing out on some no-effort error prevention! There are a variety
of compiler flags and static analysis tools in your compiler that can make your
life easier. One of these (`-Wreturn-type`) would have saved me immediately in
[one of my examples](#case-study-2---undefined-fun-times). Philip Johnston over
at Embedded Artistry has written a
[great blog post](https://embeddedartistry.com/blog/2023/09/20/leveraging-your-toolchain-to-improve-security/)
on some of the flags he uses and why they're important.
