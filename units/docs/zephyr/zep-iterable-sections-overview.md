---
id: "zep-iterable-sections-overview"
type: "concept"
domain: "rtos"
title: "Iterable Sections: Overview"
summary: "An iterable section is a group of statically-defined instances of the same struct that the linker places into a single contiguous output section. The runtime can then iterate over all instances without having to maintain an explicit list."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/iterable_sections/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/iterable_sections/index.rst"
license: "Apache-2.0"
mode: "V"
---

An iterable section is a group of statically-defined instances of the same
struct that the linker places into a single contiguous output section.
The runtime can then iterate over all instances without having to maintain an
explicit list.

Zephyr currently supports two linker-script pipelines: a template-based one that consumes
`.ld` scripts registered via `zephyr_linker_sources()`, and a CMake generated one that consumes
`zephyr_iterable_section()` calls. To work on all supported toolchains, a new iterable must
currently be declared in both.

When `CONFIG_CMAKE_LINKER_GENERATOR=y`, the output sections for iterable sections are emitted from
the `zephyr_iterable_section()` calls. Any `ITERABLE_SECTION_RAM/ROM` definitions in `.ld`
snippets registered via `zephyr_linker_sources()` are ignored.
When `CONFIG_CMAKE_LINKER_GENERATOR=n`, the reverse holds true: `zephyr_iterable_section()`
calls are not consumed and the `.ld` scripts provide the section definitions.

Because upstream Zephyr must build under both configurations, a new iterable section must be
declared in both places.

To create an iterable section requires three pieces that must agree on the struct name and RAM vs.
ROM placement:

1. **C code**: defines the struct and instantiates entries using
   `STRUCT_SECTION_ITERABLE` (or its `const` variant for ROM).

2. **Linker placement**: declared in one of two ways (*both required upstream*):

   - **CMake**: `zephyr_iterable_section()` consumed by the CMake-generated pipeline.
   - **Linker script**: `ITERABLE_SECTION_RAM/ROM` registered with `zephyr_linker_sources()`
     consumed by the template-based pipeline.
