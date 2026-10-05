---
id: "intr-embedded-open-source-summit-2024-r-patterns-and-anti-patterns-in-embedded-d"
type: "concept"
domain: "debug"
title: "Embedded Open Source Summit 2024 Recap: Patterns and Anti-Patterns in Embedded Development"
summary: "Marta Rybczynska walks through security incidents from 2023 concerning devices running Embedded Linux, protocols used by devices, and the Linux kernel itself while going over what patterns and anti-patterns we can take away from the incidents."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-08-eoss-recap.md"
doc_source: "https://interrupt.memfault.com/blog/eoss-recap#patterns-and-anti-patterns-in-embedded-development"
license: "CC-BY-SA-4.0"
mode: "V"
---

- [YouTube link](https://youtu.be/M3lWe54jxiA?si=ATQc7wt3HQy4eE6v)
- Recommended by: Pat

Marta Rybczynska walks through security incidents from 2023 concerning devices
running Embedded Linux, protocols used by devices, and the Linux kernel itself
while going over what patterns and anti-patterns we can take away from the
incidents. In particular, I found the segment about the train software
fascinating. That the security researchers found that almost every train had a
different software version really shows the importance of having a defined OTA
and versioning process, not just for software management but also security. As a
big fan of the Yocto project, I also great enjoyed the fun fact about how the
now-infamous XZ backdoor wouldn’t build on the Yocto Release Candidate that
included it!
