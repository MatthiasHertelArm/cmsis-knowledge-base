---
id: "tbx-experimental-features-server-mode"
type: "concept"
domain: "project"
title: "Experimental Features: Server Mode"
summary: "The csolution tool supports the command line argument rpc to initiate a server mode. With this mode rpc commands can be initiated."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/Experimental-Features.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/Experimental-Features/#server-mode"
license: "Apache-2.0"
mode: "V"
---

The `csolution` tool supports the command line argument `rpc` to initiate a server mode. With this mode [rpc commands](https://github.com/Open-CMSIS-Pack/csolution-rpc/blob/main/api/csolution-openapi.yml) can be initiated. The first set of commands will be used by the VS Code CMSIS Solution extension to select components and packs for projects and layers.

Refer to [github.com/Open-CMSIS-Pack/csolution-rpc](https://github.com/Open-CMSIS-Pack/csolution-rpc) for more information.
