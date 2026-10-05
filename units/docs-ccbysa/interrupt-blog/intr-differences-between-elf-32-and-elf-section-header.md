---
id: "intr-differences-between-elf-32-and-elf-section-header"
type: "concept"
domain: "debug"
title: "Differences Between ELF-32 and ELF-64: Section Header"
summary: "Differences Between ELF-32 and ELF-64: Section Header"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-13-elf-format-differences.md"
doc_source: "https://interrupt.memfault.com/blog/elf-format-differences#section-header"
license: "CC-BY-SA-4.0"
mode: "V"
---

| Field        | ELF-32 Type | --  | Field        | ELF-64 Type    |
| ------------ | ----------- | --- | ------------ | -------------- |
| sh_name      | Elf32_Word  | --  | sh_name      | Elf64_Word     |
| sh_type      | Elf32_Word  | --  | sh_type      | Elf64_Word     |
| sh_flags     | Elf32_Word  | --  | sh_flags     | Elf64_Word     |
| sh_addr      | Elf32_Addr  | --  | sh_addr      | **Elf64_Addr** |
| sh_offset    | Elf32_Off   | --  | sh_offset    | **Elf64_Off**  |
| sh_size      | Elf32_Word  | --  | sh_size      | Elf64_Word     |
| sh_link      | Elf32_Word  | --  | sh_link      | Elf64_Word     |
| sh_info      | Elf32_Word  | --  | sh_info      | Elf64_Word     |
| sh_addralign | Elf32_Word  | --  | sh_addralign | Elf64_Word     |
| sh_entsize   | Elf32_Word  | --  | sh_entsize   | Elf64_Word     |

Section headers differ due to:

- Header size
