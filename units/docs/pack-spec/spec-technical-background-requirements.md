---
id: "spec-technical-background-requirements"
type: "concept"
domain: "pack"
title: "Technical background: Requirements"
summary: "Packs can require other packs to be available (and can even ask for a specific version of a pack):"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_creation.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/cp_Packs.html"
license: "Apache-2.0"
mode: "V"
---

Packs can require other packs to be available (and can even ask for a specific version of a pack):



There are three different requirement types:
- The `packages` section lists CMSIS Packs that have been used to configure the project. This includes the specification of
  a version range to ensure compatibility. If no version is provided, the latest installed version is used. If not yet
  installed, the latest available version will be installed before resolving the configuration.
- The `compilers` section specifies the toolchains that are supported by this example. The required compiler version is
  specified using the version element. If no compiler is specified, it is assumed that any toolchain will work.
- The `languages` section allows to specify requirements regarding the programming language, for example C99 standard. If no
  language requirements are set, ANSI C is assumed.
