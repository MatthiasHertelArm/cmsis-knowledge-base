---
id: "intr-differences-between-elf-32-and-elf-elf-64-vs-elf-32"
type: "concept"
domain: "debug"
title: "Differences Between ELF-32 and ELF-64: ELF-64 vs ELF-32"
summary: "At a high level, the two formats are structurally very similar but will differ in the following ways:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-03-13-elf-format-differences.md"
doc_source: "https://interrupt.memfault.com/blog/elf-format-differences#elf-64-vs-elf-32"
license: "CC-BY-SA-4.0"
mode: "V"
---

At a high level, the two formats are structurally very similar but will differ
in the following ways:

- Data Representation: data types for addresses, offsets, and sizes will match
  their native sizes and alignments
- Padding: Equivalent data types in ELF-64 may be packed differently compared to
  ELF-32 to minimize padding

Throughout this post I will highlight the differences in the internal structures
in the following ways:

- If a data type differs or is a different native size, the data type will be
  bold (i.e. **Elf64_Addr**)
- If a field is in a different order within a structure, the field name will be
  bold (i.e. **st_size** )
- If both a data type and field order differ, both the data type _and_ field
  name will be bold

At the end of each structure section, I will also include a few bullet points to
summarize if sizes, field order, or both differ.
