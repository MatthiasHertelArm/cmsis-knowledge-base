---
id: "vela-vela-cli-options-memory-mode"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Memory Mode"
summary: "Selects the memory mode to use as specified in the Vela configuration file (see section below)."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#memory-mode"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Selects the memory mode to use as specified in the Vela configuration file (see
section below).  
**Type: String**  
**Default: Default config maps to the following configs from the example `vela.ini` file**  
- **Ethos-U85 and Ethos-U65** - Memory mode Dedicated SRAM: the SRAM is only for use by the
  Ethos-U.  The non-SRAM memory is assumed to be read-writeable  
- **Ethos-U55** - Memory mode Shared SRAM: the SRAM is shared between the
  Ethos-U and the Cortex-M software.  The non-SRAM memory is assumed to be
  read-only  

```bash
vela network.tflite --config my_vela_cfg.ini --memory-mode My_Mem_Mode
```
