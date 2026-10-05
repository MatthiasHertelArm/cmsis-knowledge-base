---
id: "intr-smart-ring-development-part-1-rese-conclusion"
type: "concept"
domain: "debug"
title: "Smart Ring Development  (Part 1) － Research and Prototype: Conclusion"
summary: "Building a Smart Ring isn't an easy task due to space requirements and tight coupling between electronics, mechanical design, and usability. In many ways, it's similar to building a smartphone, where everything is carefully picked to fit together."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-06-13-smart-ring-development-part-1.md"
doc_source: "https://interrupt.memfault.com/blog/smart-ring-development-part-1#conclusion"
license: "CC-BY-SA-4.0"
mode: "V"
---

Building a Smart Ring isn't an easy task due to space requirements and tight
coupling between electronics, mechanical design, and usability. In many ways,
it's similar to building a smartphone, where everything is carefully picked to
fit together. It was the first project I worked on where every single chip had
to be WLCSP or BGA, there was no space for legs sticking out of a package, and
even QFN with no leads was too big! The PCB required a complex rigid-flex design
with laser microvias, and every bit of it was routed with traces to get this
product to work.

In the next article, we will dive into the hardware design of
[Open Ring](https://github.com/stawiski/open-ring), so stick around and read on!









{:.no_toc}
