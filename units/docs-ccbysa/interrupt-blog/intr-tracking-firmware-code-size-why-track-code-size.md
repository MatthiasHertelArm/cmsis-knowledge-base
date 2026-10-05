---
id: "intr-tracking-firmware-code-size-why-track-code-size"
type: "concept"
domain: "debug"
title: "Tracking Firmware Code Size: Why Track Code Size?"
summary: "If you are a firmware engineer, you've likely run into code sizes issues."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-18-code-size-deltas.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-deltas#why-track-code-size"
license: "CC-BY-SA-4.0"
mode: "V"
---

If you are a firmware engineer, you've likely run into code sizes issues.
Firmware, like a gas, will expand to take up all available space, whether it's
extra debug logs, a full featured command line interface, or fancy animation &
images.

With this in mind, it is wise to constantly track and measure the code size of a
project during development to know when and why the code size grows. This means
that each commit and a handful of build configurations should be tracked so an
accurate picture can be painted.

Most projects simply print out size information after each build. It may look
like this:

```
Memory region         Used Size  Region Size  %age Used
           FLASH:      153108 B         1 MB     14.60%
            SRAM:       44544 B       256 KB     16.99%
        IDT_LIST:          56 B         2 KB      2.73%
```

This is a step in the right direction, but it does not give us any sense of the
changes to code size over time. Instead, we must track this information from
commit to commit. With this information, your team can:

- Prevent large (possibly accidental) code size increases due to non-optimal
  code for function usage (e.g. a few years ago, by adding a call to newlib's
  `sscanf(...)`, I increased the firmware size by 2kB).
- Retroactively find large spikes or decreases in code size when looking for
  easy-win optimizations.
- Estimate when the code size will exceed the limit by looking at historical
  data.
- Over time, learn which coding patterns contribute to the code size increases.
- Calculate code size deltas on every new pull request. You would likely prefer
  to merge a shiny new feature which adds 2kB of code instead of a poorly
  implemented bug-fix which also adds 2kB.
