---
id: "intr-differences-between-elf-32-and-elf-data-representation-differences"
type: "concept"
domain: "debug"
title: "Differences Between ELF-32 and ELF-64: Data Representation Differences"
summary: "The main place where the two formats differ is in how they represent data."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-13-elf-format-differences.md"
doc_source: "https://interrupt.memfault.com/blog/elf-format-differences#data-representation-differences"
license: "CC-BY-SA-4.0"
mode: "V"
---

The main place where the two formats differ is in how they represent data. One
difficult part of looking at either standard is that data types are not defined
with a naming scheme that makes the size of each type obvious, e.g. `uint32_t`.
The following tables highlight the differences between the two:

| ELF-32 Type   | Size | Alignment | --  | ELF-64 Type      | Size  | Alignment |
| ------------- | ---- | --------- | --- | ---------------- | ----- | --------- |
| Elf32_Addr    | 4    | 4         | --  | **Elf64_Addr**   | **8** | **8**     |
| Elf32_Off     | 4    | 4         | --  | **Elf64_Off**    | **8** | **8**     |
| Elf32_Half    | 2    | 2         | --  | Elf64_Half       | 2     | 2         |
| Elf32_Word    | 4    | 4         | --  | Elf64_Word       | 4     | 4         |
| Elf32_Sword   | 4    | 4         | --  | Elf64_Sword      | 4     | 4         |
| unsigned char | 1    | 1         | --  | unsigned char    | 1     | 1         |
| -             | -    | -         | --  | **Elf64_Xword**  | **8** | **8**     |
| -             | -    | -         | --  | **Elf64_Sxword** | **8** | **8**     |

The differences are that address and offset fields match their native sizes of
32 vs 64 bits and ELF-64 introduces a long type with signed and unsigned
variants.
