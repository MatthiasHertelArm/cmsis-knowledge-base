---
id: "intr-a-deep-dive-into-arm-cortex-m-debu-debug-path"
type: "concept"
domain: "debug"
title: "A Deep Dive into ARM Cortex-M Debug Interfaces: Debug Path"
summary: "The end to end path of our debug setup looks like this:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-08-06-a-deep-dive-into-arm-cortex-m-debug-interfaces.md"
doc_source: "https://interrupt.memfault.com/blog/a-deep-dive-into-arm-cortex-m-debug-interfaces#debug-path"
license: "CC-BY-SA-4.0"
mode: "V"
---

The end to end path of our debug setup looks like this:



The following image from the ARM Debug Interface Architecture manual[^2] captures what the path
looks like inside the NRF52840. The "physical connection" in this case is the SWD path in the image above.


