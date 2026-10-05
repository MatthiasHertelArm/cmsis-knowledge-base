---
id: "spec-publish-a-cmsis-pack"
type: "concept"
domain: "pack"
title: "Publish a CMSIS-Pack"
summary: "Before you start distributing a software pack, make sure that it does not contain errors. Use the tools described in the createPackUtil section for verification."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_publish.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html"
license: "Apache-2.0"
mode: "V"
---

Before you start distributing a software pack, make sure that it does not contain errors. Use the tools described in the
createPackUtil section for verification. Once you have validated that the PDSC file and the pack contain no errors,
you have basically two options for distributing a software pack:
- cp_LocalInstallation
- cp_WebDownload

The following sections assume that you are familiar with the
CMSIS-Toolbox and
especially with
cpackget.
