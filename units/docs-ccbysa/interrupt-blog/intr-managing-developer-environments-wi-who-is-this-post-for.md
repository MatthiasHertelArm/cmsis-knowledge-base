---
id: "intr-managing-developer-environments-wi-who-is-this-post-for"
type: "concept"
domain: "debug"
title: "Managing Developer Environments with Conda: Who Is This Post For?"
summary: "Every developer should build, debug, and test the firmware using the exact same versions of the compiler, build system, and other tools. The specific tools used should also be in lock-step with the code base revision being worked on."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-01-07-conda-developer-environments.md"
doc_source: "https://interrupt.memfault.com/blog/conda-developer-environments#who-is-this-post-for"
license: "CC-BY-SA-4.0"
mode: "V"
---

Every developer should build, debug, and test the firmware using the **exact
same versions** of the compiler, build system, and other tools. The specific
tools used should also be in lock-step with the code base revision being worked
on. This ensures that there is one way to do all everyday tasks and they
**always work**. It's also a critical step towards having [reproducible
builds](https://interrupt.memfault.com/blog/reproducible-firmware-builds).

If you or your teammates have experienced any of the following more than once,
it may be time to consider using Conda or similar environment manager.

- After coming back from a 2 week vacation, you find that getting a functional
  development environment again takes hours or even days.
- Updating a package required by the firmware build is a monumental effort and
  requires communication in all channels, including email, slack, and various
  wiki pages.
- You find that a build from your machine works correctly but not the one from
  CI or your co-workers machine.
- You check out a 6 month-old revision of your project and realize it's probably
  quicker to reformat your computer and start over than to try and piece
  together an environment to build the firmware.
- You use Windows, macOS, or Linux _without_ Docker.
