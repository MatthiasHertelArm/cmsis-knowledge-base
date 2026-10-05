---
id: "intr-using-asserts-in-embedded-systems-when-not-to-assert"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: When Not to Assert"
summary: "There are places where it is advised to assert. On the contrary, there are places where it's critical to not assert."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#when-not-to-assert"
license: "CC-BY-SA-4.0"
mode: "V"
---

There are places where it is advised to assert. On the contrary, there are
places where it's critical to **not** assert.

- Avoid asserting on boot up sequences. This is the most common way to introduce
  reboot loops.
- Don't assert on operations that depend on the hardware behaving appropriately.
  If a sensor says it will return a value between 0-100, it's probably best not
  assert when it's above 100, because you can never trust today's cheap
  hardware.
- Don't assert on the contents of data read from persistent storage, unless it's
  guaranteed to be valid. The data read from flash or a filesystem could be
  corrupted.
- If it is very likely the system will recover in a few moments, it might be
  best to not assert. e.g. when running out of heap or byte pool allocations
  during a spike in network packets.
