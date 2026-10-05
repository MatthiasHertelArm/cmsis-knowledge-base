---
id: "svd-file-conventions-2"
type: "concept"
domain: "pack"
title: "File Conventions: "
summary: "Number constants shall be entered in hexadecimal, decimal, or binary format. - The Hexadecimal format is indicated by a leading 0x. - The Binary format is indicated by a leading #. - All other formats are interpreted as decimal numbers."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/svd_xml_conventions_gr.html"
license: "Apache-2.0"
mode: "V"
---

Number constants shall be entered in hexadecimal, decimal, or binary format.
        - The Hexadecimal format is indicated by a leading **`0x`**.
        - The Binary format is indicated by a leading **`#`**.
        - All other formats are interpreted as decimal numbers.
        -	The element \tagem{enumeratedValue}.\tagem{value} can be used to define constants.
