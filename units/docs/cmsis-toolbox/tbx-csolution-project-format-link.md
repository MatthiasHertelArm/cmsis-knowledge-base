---
id: "tbx-csolution-project-format-link"
type: "concept"
domain: "project"
title: "CSolution Project Format: Translation Control / `link:`"
summary: "Apply a link attribute to an individual library archive file. Use whole-archive for libraries that rely on static initialization, registration, or other objects that do not satisfy an unresolved symbol."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#link"
license: "Apache-2.0"
mode: "V"
---

_Part of: Translation Control_

Apply a link attribute to an individual library archive file. Use `whole-archive` for libraries that rely on static initialization, registration, or other objects that do not satisfy an unresolved symbol. It prevents the linker from discarding those objects while leaving normal archive selection unchanged for other libraries. This feature is available with the CLANG and GCC compilers.

!!! Note
    For other compilers (AC6, IAR, etc.) the `link:` node is ignored.

Value                                            | Description
:------------------------------------------------|:----------------------------
`whole-archive`                                  | Include every object file for the archive file rather than searching for the required object files.

**Example:**

```yml
groups:
  - group:  "Libraries"
    files:
      - file: lib1.a                 # include all object files from library archive
        link: whole-archive
      - file: lib2.a                 # include only required object files from library archive
```
