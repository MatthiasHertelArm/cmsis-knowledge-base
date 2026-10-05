---
id: "intr-tracking-firmware-code-size-goals"
type: "concept"
domain: "debug"
title: "Tracking Firmware Code Size: How to Track Code Size / Goals"
summary: "By the end of the post, we will be able to:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-18-code-size-deltas.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-deltas#goals"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: How to Track Code Size_

By the end of the post, we will be able to:

- Store data about each commit and build with a database.
- Look at historical code size data using visualizations.
- Calculate deltas between a commit's code size and its parent's.
- Estimate code size deltas between the master branch and a pull request build
  automatically.

Let's begin!
