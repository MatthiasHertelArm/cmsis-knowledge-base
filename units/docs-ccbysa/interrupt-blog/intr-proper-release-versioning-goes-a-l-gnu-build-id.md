---
id: "intr-proper-release-versioning-goes-a-l-gnu-build-id"
type: "concept"
domain: "debug"
title: "Proper Release Versioning Goes a Long Way: GNU Build ID"
summary: "GNU Build ID's are our final missing piece to our versioning story. The build ID is a 160-bit SHA1 string computed over the elf header bits and section contents in the file."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2021-01-19-release-versioning.md"
doc_source: "https://interrupt.memfault.com/blog/release-versioning#gnu-build-id"
license: "CC-BY-SA-4.0"
mode: "V"
---

[GNU Build ID's](https://interrupt.memfault.com/blog/gnu-build-id-for-firmware) are our final missing piece to our versioning story. The build ID is a 160-bit SHA1 string computed over the elf header bits and section contents in the file. Because it's computed over the binary itself, we can be sure that every unique binary will produce a unique build ID. Perfect!

A build ID serves three purposes:

1. To uniquely identify and differentiate a specific firmware version from other ones.
2. Conversely, to verify that two binaries are the same exact build.
3. To match debug symbols to a given binary.

The specifics on how to add a GNU Build ID are laid out in our [previous post](https://interrupt.memfault.com/blog/gnu-build-id-for-firmware#adding-the-gnu-build-id-to-your-builds).

If you don't use GCC as your compiler, fret not! We have [a script in the Memfault Firmware SDK repo](https://github.com/memfault/memfault-firmware-sdk/blob/master/scripts/fw_build_id.py) to help out a number of our customers include a unique build identifier for their firmware builds, regardless of compiler, build system, or platform.

The future looks promising for the use of GNU Build ID's as well. A new symbol server, [debuginfod](https://sourceware.org/elfutils/Debuginfod.html) was recently released, and various tools are integrating it as a way to pull down debug symbols for binaries that include a build ID.
