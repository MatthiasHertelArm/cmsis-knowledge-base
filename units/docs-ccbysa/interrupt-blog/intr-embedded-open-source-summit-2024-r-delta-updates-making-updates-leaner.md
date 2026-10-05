---
id: "intr-embedded-open-source-summit-2024-r-delta-updates-making-updates-leaner"
type: "concept"
domain: "debug"
title: "Embedded Open Source Summit 2024 Recap: Delta Updates: Making Updates Leaner"
summary: "I only caught glimpses of this talk but I understand they have been doing some research on how to strategically prepare the filesystem images so that delta updaters would be able to compress the delta more efficiently."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-08-eoss-recap.md"
doc_source: "https://interrupt.memfault.com/blog/eoss-recap#delta-updates-making-updates-leaner"
license: "CC-BY-SA-4.0"
mode: "V"
---

- [YouTube link](https://www.youtube.com/watch?v=1rzf7tE-cKY&list=PLbzoR-pLrL6q2lcVcQ8s1uVNxde0aVdp3&index=5&pp=iAQB)
- Recommended by: Thomas

I only caught glimpses of this talk but I understand they have been doing some
research on how to strategically prepare the filesystem images so that delta
updaters would be able to compress the delta more efficiently. This is a
fascinating topic as we know how important compressing updates can be for some
of our customers, especially these relying on expensive cellular modem radios!
