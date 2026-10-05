---
id: "intr-gnu-build-ids-for-firmware-what-is-the-gnu-build-id"
type: "concept"
domain: "debug"
title: "GNU Build IDs for Firmware: What is the GNU Build ID"
summary: "Firmware engineers are not alone in wanting to uniquely identify a build for debugging purposes. In fact, Linux developers have long wanted to match a coredump to a specific build."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-05-29-gnu-build-id-for-firmware.md"
doc_source: "https://interrupt.memfault.com/blog/gnu-build-id-for-firmware#what-is-the-gnu-build-id"
license: "CC-BY-SA-4.0"
mode: "V"
---

Firmware engineers are not alone in wanting to uniquely identify a build for
debugging purposes. In fact, Linux developers have long wanted to match a
coredump to a specific build.

Roland McGrath of glibc fame came up with the GNU build ID 15 years ago, and
contributed the implementation to various build tools.

The build ID is a 160-bit SHA1 string computed over the elf header bits and
section contents in the file. It is bundled in the elf file as an entry in the
notes section.

Each note section entry has the following layout:

```
+----------------+
|     namesz     |   32-bit, size of "name" field
+----------------+
|     descsz     |   32-bit, size of "desc" field
+----------------+
|      type      |   32-bit, vendor specific "type"
+----------------+
|      name      |   "namesz" bytes, null-terminated string
+----------------+
|      desc      |   "descsz" bytes, binary data
+----------------+

```

In the case of the GNU build ID:
* `name` is `"GNU\0"`, which gives us `namesz` = 4
* `desc` is our 160-bit SHA1 value, which gives us `descsz` = 20
* `type` is 3
