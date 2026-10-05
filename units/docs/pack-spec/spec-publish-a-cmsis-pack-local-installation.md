---
id: "spec-publish-a-cmsis-pack-local-installation"
type: "concept"
domain: "pack"
title: "Publish a CMSIS-Pack: Local installation"
summary: "The easiest way to distribute a software pack is attaching it to an email or using other means of electronic distribution (for example using a file server)."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_publish.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html"
license: "Apache-2.0"
mode: "V"
---

The easiest way to distribute a software pack is attaching it to an email or using other means of electronic distribution
(for example using a file server). Install the software pack on a PC using
cpackget,
the pack management tool that comes with the CMSIS-Toolbox:
```
cpackget add vendor.packname.version.pack
```
If the PDSC file does not contain a valid `\elem{url}` element, a
manual installation is required to update a software pack. Otherwise, `cpackget` can check for updates on the server or the
local machine that is specified by `\elem{url}.`

**Note:** For automatic updates on a local machine, specify the `\elem{url}` using the
file URI scheme.
