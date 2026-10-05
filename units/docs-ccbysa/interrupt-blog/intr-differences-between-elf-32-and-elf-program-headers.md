---
id: "intr-differences-between-elf-32-and-elf-program-headers"
type: "concept"
domain: "debug"
title: "Differences Between ELF-32 and ELF-64: Program Headers"
summary: "Program Headers differ due to the following:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-13-elf-format-differences.md"
doc_source: "https://interrupt.memfault.com/blog/elf-format-differences#program-headers"
license: "CC-BY-SA-4.0"
mode: "V"
---

| Field    | ELF-32 Type |     | Field        | ELF-64 Type     |
| -------- | ----------- | --- | ------------ | --------------- |
| p_type   | Elf32_Word  | --  | p_type       | Elf64_Word      |
| p_offset | Elf32_Off   | --  | **p_flags**  | Elf64_Word      |
| p_vaddr  | Elf32_Addr  | --  | **p_offset** | **Elf64_Off**   |
| p_paddr  | Elf32_Addr  | --  | **p_vaddr**  | **Elf64_Addr**  |
| p_filesz | Elf32_Word  | --  | **p_paddr**  | **Elf64_Addr**  |
| p_memsz  | Elf32_Word  | --  | **p_filesz** | **Elf64_Xword** |
| p_flags  | Elf32_Word  | --  | **p_memsz**  | **Elf64_Xword** |
| p_align  | Elf32_Word  | --  | **p_align**  | **Elf64_Xword** |

Program Headers differ due to the following:

- Field order
- Header size
