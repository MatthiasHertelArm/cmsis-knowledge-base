---
id: "intr-beyond-error-codes-debugging-ill-d-step-1-see-what-changed"
type: "concept"
domain: "debug"
title: "Beyond Error Codes - Debugging Ill-Defined Problems: Steps / Step 1: See What Changed"
summary: "This step seems insultingly simple, and yet it is one I often forget myself. Unless you've never successfully gotten your firmware to boot, presumably, there was a time when your firmware functioned in some capacity."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-04-18-debugging-steps.md"
doc_source: "https://interrupt.memfault.com/blog/debugging-steps#step-1-see-what-changed"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps_

This step seems insultingly simple, and yet it is one I often forget myself.
Unless you've never successfully gotten your firmware to boot, presumably, there
was a time when your firmware functioned in some capacity. Being able to diff
your codebase between "working" and "broken" states is crucial for giving you a
nudge toward what might be broken. You may not understand precisely what is
happening yet, but that's ok. Even knowing the _general area_ the problem might
be in is valuable information.

Find the smallest possible change you can make that induces the bad state.
Depending on when you last made a commit, this step might involve adding
incremental changes between the last working commit and the current broken
state. There's even a
[great article](https://interrupt.memfault.com/blog/git-bisect) already on
Interrupt about using git bisect to accomplish what I'm describing.

Now that you have a general idea of where the problem may lie, it's time to
utilize some error reporting capabilities built into your compiler and MCU.
