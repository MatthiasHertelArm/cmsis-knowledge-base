---
id: "vela-vela-cli-options-accelerator-configuration"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Accelerator Configuration"
summary: "Choose which hardware accelerator configuration to compile for. Format is accelerator name followed by a hyphen, followed by the number of MACs in the configuration."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#accelerator-configuration"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Choose which hardware accelerator configuration to compile for.  Format is
accelerator name followed by a hyphen, followed by the number of MACs in the
configuration.  
**Type: String**  
**Default: ethos-u55-256**  
**Choices: [ethos-u55-32, ethos-u55-64, ethos-u55-128, ethos-u55-256, ethos-u65-256, ethos-u65-512, ethos-u85-128, ethos-u85-256, ethos-u85-512, ethos-u85-1024, ethos-u85-2048]**  

```bash
vela network.tflite --accelerator-config ethos-u55-64
```
