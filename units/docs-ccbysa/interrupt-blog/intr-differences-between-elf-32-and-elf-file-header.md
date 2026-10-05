---
id: "intr-differences-between-elf-32-and-elf-file-header"
type: "concept"
domain: "debug"
title: "Differences Between ELF-32 and ELF-64: File Header"
summary: "The table below shows the structure file headers for both types."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-13-elf-format-differences.md"
doc_source: "https://interrupt.memfault.com/blog/elf-format-differences#file-header"
license: "CC-BY-SA-4.0"
mode: "V"
---

The table below shows the structure file headers for both types.

| Field       | ELF-32 Type   | --  | Field           | ELF-64 Type    |
| ----------- | ------------- | --- | --------------- | -------------- |
| e_ident[16] | unsigned char | --  | **e_ident[16]** | unsigned char  |
| e_type      | Elf32_Half    | --  | e_type          | Elf64_Half     |
| e_machine   | Elf32_Half    | --  | e_machine       | Elf64_Half     |
| e_version   | Elf32_Word    | --  | e_version       | Elf64_Word     |
| e_entry     | Elf32_Addr    | --  | e_entry         | **Elf64_Addr** |
| e_phoff     | Elf32_Off     | --  | e_phoff         | **Elf64_Off**  |
| e_shoff     | ELf32_Off     | --  | e_shoff         | **Elf64_Off**  |
| e_flags     | Elf32_Word    | --  | e_flags         | Elf64_Word     |
| e_ehsize    | Elf32_Half    | --  | e_ehsize        | Elf64_Half     |
| e_phentsize | Elf32_Half    | --  | e_phentsize     | Elf64_Half     |
| e_phnum     | Elf32_Half    | --  | e_phnum         | Elf64_Half     |
| e_shentsize | Elf32_Half    | --  | e_shentsize     | Elf64_Half     |
| e_shnum     | Elf32_Half    | --  | e_shnum         | Elf64_Half     |
| e_shstrndx  | Elf32_Half    | --  | e_shstrndx      | Elf64_Half     |

The file headers differ in two ways:

- Header size
- `e_ident` byte specification

### e_ident Bytes

The `e_ident` field is composed of 16 bytes, which differ very minimally between
the two formats. You very likely would not encounter an issue here, but there is
a slight difference. ELF-64 specifies byte 7 as `EI_OSABI` and byte 8 as
`EI_ABIVERSION` with padding starting at byte 9. ELF-32 lacks these components
and instead starts padding at byte 7. ELF-32 specifies padding bytes as 0, so we
at least have well-defined values for forward compatibility.

| Byte Name         | ELF-32 Index | ELF-64 Index |
| ----------------- | ------------ | ------------ |
| EI_MAG0           | 0            | 0            |
| EI_MAG1           | 1            | 1            |
| EI_MAG2           | 2            | 2            |
| EI_MAG3           | 3            | 3            |
| EI_CLASS          | 4            | 4            |
| EI_DATA           | 5            | 5            |
| EI_VERSION        | 6            | 6            |
| **EI_OSABI**      | -            | **7**        |
| **EI_ABIVERSION** | -            | **8**        |
| EI_PAD            | 7            | **9**        |

The other noticeable difference in practice is byte 4, `EI_CLASS`. For ELF-32
this byte is 0x1, while for ELF-64 it is 0x2.
