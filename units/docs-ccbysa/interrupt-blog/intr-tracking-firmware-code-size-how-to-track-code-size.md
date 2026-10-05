---
id: "intr-tracking-firmware-code-size-how-to-track-code-size"
type: "concept"
domain: "debug"
title: "Tracking Firmware Code Size: How to Track Code Size"
summary: "In the remainder of this blog post, we will set up a code size tracking dashboard for the popular open-source RTOS, Zephyr[^zephyr]."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-03-18-code-size-deltas.md"
doc_source: "https://interrupt.memfault.com/blog/code-size-deltas#how-to-track-code-size"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the remainder of this blog post, we will set up a code size tracking
dashboard for the popular open-source RTOS, Zephyr[^zephyr]. We also want to
take this data and be able to compute the code size **deltas** between commits
to know exactly which commits and by how much each one contributed to the code
size.

Since the Zephyr project is massive in the number of examples, boards, and
features that it encompasses, we will restrict the code size calculations to the
`examples/net/lwm2m_client` example with the `cc3220sf_launchxl` board. This
example was chosen due to its large number of files and dependencies with a hope
that its code size would fluctuate more than a hello world example with limited
dependencies.

We won't be covering how to initially set up building the Zephyr project, as
there are detailed instructions[^zephyr_instructions] about how to get started.
I can't help but feel the setup would have been simpler and quicker if they had
taken advantage of
[Conda](https://interrupt.memfault.com/blog/conda-developer-environments). It would also
have the benefit of being cross-platform and version controlled within the
codebase.

If anyone working on Zephyr is reading this, you should check out how Conda can
make the setup easier 😉.
