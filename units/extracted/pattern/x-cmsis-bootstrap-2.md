---
id: "x-cmsis-bootstrap-2"
type: "pattern"
domain: "project"
title: "Compiler line in a CMSIS vcpkg-configuration.json"
status: "draft"
extracted_from: "proc-cmsis-bootstrap"
source: "cmsis-bootstrap/SKILL.md"
license: "Apache-2.0"
---

For another compiler replace the GCC line:

| Compiler | Line in `requires` |
|---|---|
| `AC6` | `"arm:compilers/arm/armclang": "^6.24.0"` |
| `CLANG` | `"arm:compilers/arm/llvm-embedded": "^17.0.1"` |
| `IAR` | none: remove the line, the user provides the compiler |

The file only names the tools. The Arm Tools Environment Manager fetches them when the folder is opened in VS Code.
