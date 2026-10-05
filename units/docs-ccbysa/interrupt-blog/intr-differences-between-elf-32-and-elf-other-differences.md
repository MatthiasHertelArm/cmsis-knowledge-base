---
id: "intr-differences-between-elf-32-and-elf-other-differences"
type: "concept"
domain: "debug"
title: "Differences Between ELF-32 and ELF-64: Other Differences"
summary: "Differences Between ELF-32 and ELF-64: Other Differences"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-13-elf-format-differences.md"
doc_source: "https://interrupt.memfault.com/blog/elf-format-differences#other-differences"
license: "CC-BY-SA-4.0"
mode: "V"
---

- Slight differences between the two for “None” values of certain fields. ELF-32
  generally more consistent and specifies them while ELF-64 only sometimes does.
- ELF-64 provides some reserved ranges for OS-specific values. These reserved
  ranges are not specified for ELF-32.
