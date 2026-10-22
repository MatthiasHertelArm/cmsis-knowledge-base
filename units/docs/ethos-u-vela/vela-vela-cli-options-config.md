---
id: "vela-vela-cli-options-config"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / Config"
summary: "Specifies the path to the Vela configuration file. The format of the file is a Python ConfigParser .ini file."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#config"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Specifies the path to the Vela configuration file.  The format of the file is a
Python ConfigParser `.ini` file.  This option can be specified multiple times to
allow multiple files to be searched for the required system config and memory
mode.  Custom configuration files can be used by adding a .ini file in an
appropriate directory under the `ethosu/config_files` directory or by providing
its absolute path. More details can be found in the Configuration File and List
Configuration Files sections.  
**Type: POSIX path**  
**Default: Use default configuration**  

```bash
vela network.tflite --config DirectoryName/my_vela_cfg1.ini --config absolute/path/to/my_vela_cfg2.ini --system-config My_Sys_Cfg --memory-mode My_Mem_Mode
```
