---
id: "intr-embedded-open-source-summit-2024-r-maximizing-sdcard-life-performance-and-m"
type: "concept"
domain: "debug"
title: "Embedded Open Source Summit 2024 Recap: Maximizing SDCard Life, Performance and Monitoring with KrillKounter"
summary: "(EDIT: An initial version of this post incorrectly attributed the \"silent-read-only behavior\" to Samsung - Andrew clarified that this was observed on a SanDisk card. We regret the error.)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-08-eoss-recap.md"
doc_source: "https://interrupt.memfault.com/blog/eoss-recap#maximizing-sdcard-life-performance-and-monitoring-with-krillkounter"
license: "CC-BY-SA-4.0"
mode: "V"
---

- [YouTube link](https://www.youtube.com/watch?v=mxed984GAIw&list=PLbzoR-pLrL6q2lcVcQ8s1uVNxde0aVdp3&index=51&pp=iAQB)
- Recommended by: Thomas

_(EDIT: An initial version of this post incorrectly attributed the
"silent-read-only behavior" to Samsung - Andrew clarified that this was observed on a SanDisk card. We regret the error.)_

Andrew Murray of the good penguin shared of their research on SDCards. Like
Andy, we often run into customers who use SDCard as their primary flash storage
and have lots of questions about the reliability of these cards. I will now
systematically point them to this great talk!

Andy started with a very thorough explanation of how flash storage works. I
thought I knew the topic well but I still learnt quite a bit, especially what
multi-layer flash storage really is and how it works (the 0 and 1 on the flash
are really analog values - instead of reducing one analog value to a 0 or a 1,
the multi-layer flash will infer 2 or 4 bits from one analog value - this is why
these types of flash memory are more “fragile” - fascinating stuff). He also
covered in great details the role of the flash controller and its different
roles.

He then presented a test setup that his team and him devised to take some
real-world measurement of flash storage and see how it would fail. He discusses
how different flash brands can fail in different ways (some `<s>`Samsung</s>
SanDisk apparently goes read-only - without telling the OS that it’s not
writing, some other flash just start timing-out on all read and write
operations).

KrillKounter is their attempt to build a tool from all this research. It will
keep track of how many writes to a flash (not easy because it needs to be
tracked across reboots and for each SDCard that might get pulled/inserted in the
device).

There was a lot more in this talk and I can’t recommend it enough!
