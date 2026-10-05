---
id: "intr-differences-between-elf-32-and-elf-symbol-table-entry"
type: "concept"
domain: "debug"
title: "Differences Between ELF-32 and ELF-64: Symbol Table Entry"
summary: "Differences Between ELF-32 and ELF-64: Symbol Table Entry"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-13-elf-format-differences.md"
doc_source: "https://interrupt.memfault.com/blog/elf-format-differences#symbol-table-entry"
license: "CC-BY-SA-4.0"
mode: "V"
---

| Field    | ELF-32 Type   |     | Field        | ELF-64 Type     |
| -------- | ------------- | --- | ------------ | --------------- |
| st_name  | Elf32_Word    | --  | st_name      | Elf64_Word      |
| st_value | Elf32_Addr    | --  | **st_info**  | unsigned char   |
| st_size  | Elf32_Word    | --  | **st_other** | unsigned char   |
| st_info  | unsigned char | --  | **st_shndx** | Elf64_Half      |
| st_other | unsigned char | --  | **st_value** | **Elf64_Addr**  |
| st_shndx | Elf32_Half    | --  | **st_size**  | **Elf64_Xword** |

Symbol Table Entries differ by:

- Field order
- Entry size
