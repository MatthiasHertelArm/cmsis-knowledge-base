---
id: "devt-svd-validation-and-generation-tool"
type: "concept"
domain: "pack"
title: "SVD Validation and Generation Tool"
summary: "The utility svdconv validates CMSIS-SVD files and generates CMSIS-compliant device header files. It distributed as part of the CMSIS-Toolbox."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/svdconv/SVDConv/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/svdconv/SVDConv/README.md"
license: "Apache-2.0"
mode: "V"
---

The utility `svdconv` validates [CMSIS-SVD](https://arm-software.github.io/CMSIS_5/develop/SVD/html/index.html) files
and generates CMSIS-compliant device header files. It distributed as part of
the [CMSIS-Toolbox](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/blob/main/docs/installation.md).

`svdconv` performs the following operations:

- Checks the syntactical and structural compliance with the specified CMSIS-SVD format.
- Checks the consistency, correctness, and completeness of the CMSIS-SVD file against the CMSIS-SVD schema file.
- Generates CMSIS-compliant device header files, which can be used for software development.

>` **NOTE:** Consider using the `--strict` option to receive all pedantic warnings. Some rules are skipped by default
due to backward compatibility reasons. All newly developed/updated SVD files should rather respect all rules.
