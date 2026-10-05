---
id: "svd-file-conventions"
type: "concept"
domain: "pack"
title: "File Conventions: "
summary: "All name tags must comp ly with the ANSI C identifier naming restrictions. In particular, they must not contain any spaces or special characters."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/svd_xml_conventions_gr.html"
license: "Apache-2.0"
mode: "V"
---

All **name** tags must comp
ly with the ANSI C identifier naming restrictions. In particular, they
    must not contain any spaces or special characters. This is necessary to support the generation of device header files
    thus providing consistency between the names being shown by the debugger and the symbols being used in the CMSIS
    compliant target software.
