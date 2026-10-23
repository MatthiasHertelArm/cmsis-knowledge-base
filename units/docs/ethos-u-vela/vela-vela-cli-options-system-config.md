---
id: "vela-vela-cli-options-system-config"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / System Config"
summary: "Selects the system configuration to use as specified in the Vela configuration file (see section below)."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#system-config"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Selects the system configuration to use as specified in the Vela configuration
file (see section below).  
**Type: String**  
**Default: Default config maps to the following configs from the example `vela.ini` file**  
- **Ethos-U85** - System configuration Ethos_U85_SYS_DRAM_Mid: SRAMx2 (32 GB/s)
  and DRAM (12 GB/s)  
- **Ethos-U65** - System configuration Ethos-U65 Client-Server: SRAM (16 GB/s)
  and DRAM (12 GB/s)  
- **Ethos-U55** - System configuration Ethos-U55 High-End Embedded: SRAM
  (4 GB/s) and Flash (0.5 GB/s)  

```bash
vela network.tflite --config my_vela_cfg.ini --system-config My_Sys_Cfg
```
