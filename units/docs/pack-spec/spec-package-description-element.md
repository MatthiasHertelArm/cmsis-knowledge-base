---
id: "spec-package-description-element"
type: "concept"
domain: "pack"
title: "/package/description element"
summary: "Contains a brief description of the software pack. Optionally with link to a file with overview documentation in Markdown format. This Markdown file is indented for web pages that offer software packs in form of a marketplace."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_package_description.html"
license: "Apache-2.0"
mode: "V"
---

Contains a brief description of the software pack. Optionally with link to a file with overview documentation in Markdown format.
This Markdown file is indented for web pages that offer software packs in form of a marketplace.

**Example:**
```
<package>
  ...
  <description overview="./Documentation/README.md">Keil MDK Middleware: File System, Network IPv4/IPv6, USB Device/Host</description>
  ...
</package>
```


 



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| package | element_package |  |  |
| Attributes | Description | Type | Use |
| overview | File path, file name, and file extension in the format path/name.extension. The file path is relative to the root directory of the Pack and contains an overview documentation in Markdown format (file extension *.md). | xs:string | optional |
