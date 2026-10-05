---
id: "vela-vela-cli-options-list-configuration-files"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Command Line Interface / List Configuration Files"
summary: "Displays the configuration files in the ethosu/config_files directory. All configuration files must have the .ini extension and be placed in an appropriately named directory under ethosu/config_files."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/OPTIONS.md#list-configuration-files"
license: "Apache-2.0"
mode: "V"
---

_Part of: Command Line Interface_

Displays the configuration files in the `ethosu/config_files` directory. All
configuration files must have the .ini extension and be placed in an
appropriately named directory under `ethosu/config_files`. Note that the file
depth from `ethosu/config_files` must be exactly 2 for the file to be
discovered (e.g. `config_files/directory_name/my_config_file.ini`).  
This option can be used without the required Network argument.  

```bash
vela --list-config-files
```
