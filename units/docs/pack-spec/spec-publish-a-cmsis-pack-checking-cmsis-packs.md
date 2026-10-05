---
id: "spec-publish-a-cmsis-pack-checking-cmsis-packs"
type: "concept"
domain: "pack"
title: "Publish a CMSIS-Pack: Checking CMSIS-Packs"
summary: "Software packs are ZIP files that contain a PDSC file and other content. The ZIP file needs to be consistent and the PDSC file within has to be validated against the XML schema file (PACK.xsd)."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_publish.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html"
license: "Apache-2.0"
mode: "V"
---

Software packs are ZIP files that contain a PDSC file and other content. The ZIP file needs to be consistent
and the PDSC file within has to be validated against the XML schema file (PACK.xsd). An open-source checking tool is available
that helps you with both tasks: a
Bash library for gen-pack scripts.
Make sure that you have used it to validate your PDSC file and the pack contents before submitting it to any
pack indexing service. The library can be used on all major host operating systems and can also be run
in GitHub actions.
