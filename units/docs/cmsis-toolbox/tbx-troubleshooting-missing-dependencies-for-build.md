---
id: "tbx-troubleshooting-missing-dependencies-for-build"
type: "concept"
domain: "project"
title: "Troubleshooting: Missing Dependencies for Build"
summary: "Files added using the GNU assembler syntax .incbin or .include directives, or armasm syntax INCBIN, INCLUDE, or GET directives, are not included in the file dependency list."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/Troubleshooting.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Troubleshooting/#missing-dependencies-for-build"
license: "Apache-2.0"
mode: "V"
---

Files added using the GNU assembler syntax `.incbin` or `.include` directives, or armasm syntax `INCBIN`, `INCLUDE`, or `GET` directives, are not included in the file dependency list. As such, the CMake/Ninja build system cannot trigger automatically a build when an file changes that is included with such directives.

Using [`execute`](https://open-cmsis-pack.github.io/cmsis-toolbox/Troubleshooting/YML-Input-Format.md#prepost-build-steps) in the related `cproject.yml` file overcomes this issue.
In this example the file `image.bin` is included using assembler syntax. The `touch` command changes the time stamp of the related assembler file which triggers a rebuild.

```yml
  executes:
    - execute: image_dep
      run: ${CMAKE_COMMAND} -E touch $output$
      input:
        - image.bin
      output:
        - asm.s
```

!!! Tip
    Use the [`images:`](https://open-cmsis-pack.github.io/cmsis-toolbox/Troubleshooting/YML-Input-Format.md#images) node to add the output of external builds.
