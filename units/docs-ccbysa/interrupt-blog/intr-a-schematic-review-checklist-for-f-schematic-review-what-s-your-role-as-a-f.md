---
id: "intr-a-schematic-review-checklist-for-f-schematic-review-what-s-your-role-as-a-f"
type: "concept"
domain: "debug"
title: "A Schematic Review Checklist for Firmware Engineers: Schematic Review - What's Your Role as a Firmware Engineer"
summary: "Most of the schematic reviews I've attended are led by electrical engineers and are focused on the electrical components of the system. There are usually some questions about whether the proper diode was used or the capacitors were selected properly."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-07-18-schematic-review-checklist.md"
doc_source: "https://interrupt.memfault.com/blog/schematic-review-checklist#schematic-review-what-s-your-role-as-a-firmware-engineer"
license: "CC-BY-SA-4.0"
mode: "V"
---

Most of the schematic reviews I've attended are led by electrical engineers and
are focused on the electrical components of the system. There are usually some
questions about whether the proper diode was used or the capacitors were
selected properly. Things that an electrical engineer should care about but
typically fly over my head. As a firmware engineer, I've found it useful to
think about what hardware features the code I'll end up writing will need.
Starting from that perspective, I can leverage the schematic review as an
opportunity to catch design issues while the fix is relatively cheap, before
hardware has gone through various rounds of testing, which can be the difference
between hitting a schedule or not.

"Schematic review" here is mostly used as an easy blog post title, and a clear
time for the firmware and electrical teams to interact. However, the important
piece of this post is that you as a firmware engineer work with your electrical
engineering counterpart to ensure you have the hardware you need to develop,
debug, and deploy your code. And you identify those needs early on in the
development cycle with the electrical team when changes to PCBs are relatively
cheap.

Some pre-schematic review checklist items:

- [x] Get invited to the schematic review. Really, this is a callout to be
      working with your electrical engineer. If you've been working with your
      electrical engineer, providing guidance on what hardware you'll need,
      being invited to the schematic review should be a given.
- [x] Build your checklist upfront. Use this blog post as a starting point, but
      make sure you customize the list for the given project.
