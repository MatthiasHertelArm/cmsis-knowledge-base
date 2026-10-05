---
id: "intr-improving-compilation-time-of-c-c-why-speed-up-firmware-build"
type: "concept"
domain: "debug"
title: "Improving Compilation Time of C/C++ Projects: Why Speed Up Firmware Build?"
summary: "Waiting for a build to complete is a waste of time. It's as if someone decided to tie your hands behind your back a few minutes, tens of hundreds of times a day, ruining your productivity."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-02-11-improving-compilation-times-c-cpp-projects.md"
doc_source: "https://interrupt.memfault.com/blog/improving-compilation-times-c-cpp-projects#why-speed-up-firmware-build"
license: "CC-BY-SA-4.0"
mode: "V"
---

Waiting for a build to complete is a **waste of time**. It's as if someone
decided to tie your hands behind your back a few minutes, tens of hundreds of
times a day, ruining your productivity. If your team consists of 5 engineers and
the build takes 5 minutes, at 20 builds a day (conservative estimate), that's 8
hours... a whole work day for an extra single engineer!

Although we commonly run up against slow build times when trying to move
quickly, there are many other pieces of "infrastructure" (or lack thereof) that
can slow down the productivity of a firmware team.

- Manually verifying the build succeeds for all targets ([continuous
  integration](https://interrupt.memfault.com/blog/continuous-integration-for-firmware))
- Manual and rigorous testing ([unit
  testing](https://interrupt.memfault.com/blog/unit-testing-basics))
- Painstaking and repetitive debugging ([automated
  debugging](https://interrupt.memfault.com/blog/automate-debugging-with-gdb-python-api))
- Poor developer environment management ([using an environment
  manager](https://interrupt.memfault.com/blog/conda-developer-environments))
- Inability to reproduce a build ([reproducible
  builds](https://interrupt.memfault.com/blog/reproducible-firmware-builds))

Despite the important topics listed above, I believe that the build system is
one of the most important pieces of "infrastructure". The build system needs
constant supervision to keep everyone on the team as productive as possible.
There's no use in paying an engineer (or ten) if the majority of the time during
the day is spent waiting for builds to complete.
