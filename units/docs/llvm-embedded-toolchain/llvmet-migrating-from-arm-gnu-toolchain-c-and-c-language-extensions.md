---
id: "llvmet-migrating-from-arm-gnu-toolchain-c-and-c-language-extensions"
type: "concept"
domain: "project"
title: "Migrating from Arm GNU Toolchain: C and C++ language extensions"
summary: "Clang supports the majority of GNU C and C++ extensions as described in Clang Language Extensions."
status: "draft"
collection: "llvm-embedded-toolchain"
source: "ARM-software/LLVM-embedded-toolchain-for-Arm@c9dff0a:docs/migrating.md"
doc_source: "https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm/blob/c9dff0a/docs/migrating.md#c-and-c-language-extensions"
license: "Apache-2.0"
mode: "V"
---

Clang supports the majority of GNU C and C++ extensions as described in
[Clang Language Extensions](https://clang.llvm.org/docs/LanguageExtensions.html).

The following feature checking macros can be used to test whether a particular
feature is supported:
* [`__has_builtin`](https://clang.llvm.org/docs/LanguageExtensions.html#has-builtin)
* [`__has_feature`](https://clang.llvm.org/docs/LanguageExtensions.html#has-feature-and-has-extension)
* [`__has_extension`](https://clang.llvm.org/docs/LanguageExtensions.html#has-feature-and-has-extension)
* [`__has_attribute`](https://clang.llvm.org/docs/LanguageExtensions.html#has-attribute)
