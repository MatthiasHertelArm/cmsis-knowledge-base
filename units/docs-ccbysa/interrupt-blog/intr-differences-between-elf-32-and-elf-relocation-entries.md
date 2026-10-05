---
id: "intr-differences-between-elf-32-and-elf-relocation-entries"
type: "concept"
domain: "debug"
title: "Differences Between ELF-32 and ELF-64: Relocation Entries"
summary: "Relocation Entries without addend differ by:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-13-elf-format-differences.md"
doc_source: "https://interrupt.memfault.com/blog/elf-format-differences#relocation-entries"
license: "CC-BY-SA-4.0"
mode: "V"
---

### Relocation Entry Without Addend

| Field    | ELF-32 Type |     | Field    | ELF-64 Type     |
| -------- | ----------- | --- | -------- | --------------- |
| r_offset | Elf32_Addr  | --  | r_offset | Elf64_Addr      |
| r_info   | Elf32_Word  | --  | r_info   | **Elf64_Xword** |

Relocation Entries without addend differ by:

- Entry size

### Relocation Entry With Addend

| Field    | ELF-32 Type |     | Field    | ELF-64 Type      |
| -------- | ----------- | --- | -------- | ---------------- |
| r_offset | Elf32_Addr  | --  | r_offset | Elf64_Addr       |
| r_info   | Elf32_Word  | --  | r_info   | **Elf64_Xword**  |
| r_addend | ELf32_Sword | --  | r_addend | **Elf64_Sxword** |

Relocation Entries with Addend differ by:

- Entry size
