---
id: "intr-beyond-error-codes-debugging-ill-d-steps"
type: "concept"
domain: "debug"
title: "Beyond Error Codes - Debugging Ill-Defined Problems: Steps"
summary: "I wrote these steps to get the most information about the error with as little effort as possible. Each step increases in level of effort as you go along."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-04-18-debugging-steps.md"
doc_source: "https://interrupt.memfault.com/blog/debugging-steps#steps"
license: "CC-BY-SA-4.0"
mode: "V"
---

I wrote these steps to get the most information about the error with as little
effort as possible. Each step increases in level of effort as you go along. The
goal is that at some point throughout the steps, you can gain enough information
about the error to isolate and fix it. At the end of the steps, I present a
couple of case studies from my personal experience to showcase how I have used
these steps to debug issues.

While there are some "hardware" aspects to some of the bugs described, I should
note that I designed this guide for debugging "software-induced" errors.
Therefore, the following errors (while just as critical to fix) are out of the
scope of this article:

- Poorly/incorrectly designed circuit boards
- ESD damage or general IC damage/failure
- Brownouts/inadequate power supply
