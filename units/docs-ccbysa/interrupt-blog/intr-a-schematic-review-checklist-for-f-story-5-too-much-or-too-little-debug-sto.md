---
id: "intr-a-schematic-review-checklist-for-f-story-5-too-much-or-too-little-debug-sto"
type: "concept"
domain: "debug"
title: "A Schematic Review Checklist for Firmware Engineers: Story 5: Too much or too little debug {#story-5-too-much-or-to-little-debug}"
summary: "I worked on a project once with an electrical engineer that proposed we make it hard to attach a debugger to the board."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-18-schematic-review-checklist.md"
doc_source: "https://interrupt.memfault.com/blog/schematic-review-checklist#story-5-too-much-or-too-little-debug-story-5-too-much-or-to-little-debug"
license: "CC-BY-SA-4.0"
mode: "V"
---

I worked on a project once with an electrical engineer that proposed we make it
hard to attach a debugger to the board. He proposed that we force someone to
solder wires/leads to debug pads in order to get a debugger to work. As a young
firmware engineer, I was floored. The debugger was my lifeline, and especially
on a Cortex-M4 could help troubleshoot so many things. Making it difficult for a
firmware engineer to use their most powerful tool seemed ludicrous to me.

However, the electrical engineers point was that firmware engineers rely too
much on debuggers to debug devices, and don't spend enough time building
tools/systems to track down crashes/bugs in the field, where a debugger is
likely not attached. This was a good point. While working on fitness trackers
years ago, I'd seen a firmware update over UART protocol continuously fail
because none of the firmware developers used it (because it was broken of
course). This meant it was only ever used by our QA team, who would file bugs,
but it was never prioritized until one day it became a necessary firmware update
path, and required a lot of scripting on the host side to work around firmware
bugs.

So I think that debuggers are essential tools for firmware engineers, and we
should not hamper their usage. However, it's important to commit to building
tools and systems for debugging systems in the field that use only the tools
that will be available in the field, as your end goal as a firmware developer is
to be able to fix those issues, not just the ones you can see at your desk.
