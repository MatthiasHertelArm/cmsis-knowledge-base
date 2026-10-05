---
id: "intr-a-schematic-review-checklist-for-f"
type: "concept"
domain: "debug"
title: "A Schematic Review Checklist for Firmware Engineers"
summary: "Schematic reviews are a part of the hardware development cycle in many if not most, hardware development companies. Typically led by the electrical engineering team, it is easy to overlook design issues that will be important to the firmware team."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-18-schematic-review-checklist.md"
doc_source: "https://interrupt.memfault.com/blog/schematic-review-checklist"
license: "CC-BY-SA-4.0"
mode: "V"
---

Schematic reviews are a part of the hardware development cycle in many if not
most, hardware development companies. Typically led by the electrical
engineering team, it is easy to overlook design issues that will be important to
the firmware team. This post tells of a few stories of design misses that I have
made and puts some common lessons learned into a checklist for other firmware
engineers. It is not meant to be an exhaustive list, but rather a starting point
for a firmware engineer to build their own checklist with the goal of helping
teams catch software/hardware interaction bugs earlier in the design cycle when
they're cheaper to fix.



This post is written in a voice that makes two general assumptions:

1. The reader is a firmware engineer.
2. The reader is not doing the schematic layout

While those two assumptions helped me write this post, I think the
learnings/stories in it are still applicable for a variety of setups. e.g.: If
the reader is an electrical engineer that wants to understand some firmware
concerns. Or if the reader is responsible for both the electrical and firmware
design of a project. With either of these assumptions broken, feel free to put
on your firmware engineer hat and read! Hopefully, this will be helpful for you.
