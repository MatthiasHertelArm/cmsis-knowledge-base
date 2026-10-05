---
id: "intr-gnu-build-ids-for-firmware"
type: "concept"
domain: "debug"
title: "GNU Build IDs for Firmware"
summary: "In this post, we demonstrate how to use the GNU Build ID to uniquely identify a build. We explain what the GNU build ID is, how it is enabled, and how it is used in a firmware context."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-29-gnu-build-id-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-build-id-for-firmware"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this post, we demonstrate how to use the GNU Build ID to uniquely
identify a build. We explain what the GNU build ID is, how it is enabled,
and how it is used in a firmware context.


Much has been written on how to craft a firmware version. From Embedded
Artistry's excellent [blog
post](https://embeddedartistry.com/blog/2016/10/27/giving-you-build-a-version),
to Wolfram Rösler's [how to](https://gitlab.com/wolframroesler/version).

Versions are a great way to identify a *release*: a set of interfaces and
capabilities bundled together.

Versions do not - however - identify a specific binary all that well. For
example, you could have multiple binaries for a given version in order to
accommodate different variants of your hardware in the field.

For this, we need something else. This is where the GNU build ID comes in.

Why would we want to identify a specific binary? A few cases:

* To match a set of debug symbols to a given binary when trying to debug a
  device
* To verify that two binaries are in fact the same build
