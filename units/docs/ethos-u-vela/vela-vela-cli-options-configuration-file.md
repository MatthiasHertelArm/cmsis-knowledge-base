---
id: "vela-vela-cli-options-configuration-file"
type: "concept"
domain: "edge-ai"
title: "Vela CLI Options: Configuration File"
summary: "This is used to describe various properties of the Ethos-U embedded system. The configuration file is selected using the --config CLI option along with a file that describes the properties."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@eb9cf0d:OPTIONS.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/OPTIONS.md#configuration-file"
license: "Apache-2.0"
mode: "V"
---

This is used to describe various properties of the Ethos-U embedded system.  The
configuration file is selected using the `--config` CLI option along with a file
that describes the properties.  The format of the file is a Python ConfigParser
`.ini` file format consists of sections used to identify a configuration, and
key/value pair options used to specify the properties.  All sections and
key/value pairs are case-sensitive.

There are two types of section, system configuration `[System_Config.*]`
sections and memory mode `[Memory_Mode.*]` sections.  A complete Ethos-U
embedded system should define at least one entry in each section, where an entry
is identified using the format `[Part.Name]` (Part = {System_Config or
Memory_Mode}, Name = {a string with no spaces}.).  A configuration file may
contain multiple entries per section, with the entries `.Name` being used to
select it using the `--system-config` and `--memory-mode` CLI options.  If the
CLI options are not specified then default options will be used.

Each section contains a number of options which are described in more detail
below.  All options are optional.  If they are not specified, then they will be
assigned a value of 1 (or the equivalent).  They will not be assigned the value
of the default configuration.

One special option is the `inherit` option.  This can be used in any section and
its value is the name of another section to inherit options from.  The only
restriction on this option is that recursion is not allowed and so it cannot
reference its own section.

To see the configuration values being used by Vela use the `--verbose_config`
CLI option.  This can also be used to display a full list of all the available
options.

An example Vela configuration file, called `vela.ini`, is included in the
`ethosu/config_files/Arm` directory. Example usage based on this file is:

```bash
vela network.tflite --accelerator-config ethos-u55-256 --config Arm/vela.ini --system-config Ethos_U55_High_End_Embedded --memory-mode Shared_Sram
```

Hardware vendors and/or users may wish to contribute their own configuration
files for various SoC platforms by adding a .ini file in an appropriate
directory under the ethosu/config_files directory.  This can be done by
following the process outlined in [CONTRIBUTING.md](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/eb9cf0d/CONTRIBUTING.md).  These can
then be accessed with `--config <DirectoryName>/config.ini` as in the example
above.

To use configuration files located outside the config_files directory, provide
its absolute path to `--config`. The `--list-config-files` option can be used to
view all available configuration files:

```bash
vela --list-config-files
```

The following is an in-line explanation of the Vela configuration file format:

```ini
; file: my_vela_cfg.ini
; -----------------------------------------------------------------------------
; Vela configuration file

; -----------------------------------------------------------------------------
; System Configuration

; My_Sys_Cfg
[System_Config.My_Sys_Cfg]
core_clock=???                 ---> Clock frequency of the Ethos-U.  ??? = {float in Hz}
axi0_port=???                  ---> Memory type connected to AXI0.  ??? = {Sram, Dram, OnChipFlash or OffChipFlash}
axi1_port=???                  ---> Memory type connected to AXI1.  ??? = {Sram, Dram, OnChipFlash or OffChipFlash}
Sram_clock_scale=???           ---> Scaling of core_clock to specify the Sram bandwidth.  Only required if selected by an AXI port.  ??? = {float 0.0 to 1.0}
Sram_ports_used=???            ---> Number of Sram ports used. Only required if selected by an AXI port. ??? = {int}
Sram_burst_length=???          ---> Minimum efficient burst length in Sram. Only required if selected by an AXI port. ??? = {int in Bytes}
Sram_read_latency=???          ---> Read latency in Sram. Only required if selected by an AXI port. ??? = {int in Cycles}
Sram_write_latency=???         ---> Write latency in Sram. Only required if selected by an AXI port. ??? = {int in Cycles}
Sram_max_reads=???             ---> Max outstanding reads in Sram. Only required if selected by an AXI port. ??? = {int}
Sram_max_writes=???            ---> Max outstanding writes in Sram. Only required if selected by an AXI port. ??? = {int}
Dram_clock_scale=???           ---> Scaling of core_clock to specify the Dram bandwidth.  Only required if selected by an AXI port.  ??? = {float 0.0 to 1.0}
Dram_ports_used=???            ---> Number of Dram ports used. Only required if selected by an AXI port. ??? = {int}
Dram_burst_length=???          ---> Minimum efficient burst length in Dram. Only required if selected by an AXI port. ??? = {int in Bytes}
Dram_read_latency=???          ---> Read latency in Dram. Only required if selected by an AXI port. ??? = {int in Cycles}
Dram_write_latency=???         ---> Write latency in Dram. Only required if selected by an AXI port. ??? = {int in Cycles}
Dram_max_reads=???             ---> Max outstanding reads in Dram. Only required if selected by an AXI port. ??? = {int}
Dram_max_writes=???            ---> Max outstanding writes in Dram. Only required if selected by an AXI port. ??? = {int}
OnChipFlash_clock_scale=???    ---> Scaling of core_clock to specify the OnChipFlash bandwidth.  Only required if selected by an AXI port.  ??? = {float 0.0 to 1.0}
OffChipFlash_clock_scale=???   ---> Scaling of core_clock to specify the OffChipFlash bandwidth.  Only required if selected by an AXI port.  ??? = {float 0.0 to 1.0}
OffChipFlash_ports_used=???    ---> Number of OffChipFlash ports used. Only required if selected by an AXI port. ??? = {int}
OffChipFlash_burst_length=???  ---> Minimum efficient burst length in OffChipFlash. Only required if selected by an AXI port. ??? = {int in Bytes}
OffChipFlash_read_latency=???  ---> Read latency in OffChipFlash. Only required if selected by an AXI port. ??? = {int in Cycles}
OffChipFlash_write_latency=??? ---> Write latency in OffChipFlash. Only required if selected by an AXI port. ??? = {int in Cycles}
OffChipFlash_max_reads=???     ---> Max outstanding reads in OffChipFlash. Only required if selected by an AXI port. ??? = {int}
OffChipFlash_max_writes=???    ---> Max outstanding writes in OffChipFlash. Only required if selected by an AXI port. ??? = {int}

; -----------------------------------------------------------------------------
; Memory Mode

; My_Mem_Mode_Parent
[Memory_Mode.My_Mem_Mode_Parent]
const_mem_area=???     ---> AXI port used by the read-only data (e.g. weight tensors, scale & bias tensors).  ??? = {Axi0, Axi1}
arena_mem_area=???     ---> AXI port used by the read-write data (e.g. feature map tensors, internal buffers).  ??? = {Axi0, Axi1}
cache_mem_area=???     ---> AXI port used by the dedicated SRAM read-write (e.g. feature map part-tensors, internal buffers).  ??? = {Axi0, Axi1}
arena_cache_size=???   ---> Size of the arena/cache memory area.  ??? = {int in Bytes}

; My_Mem_Mode_Child
[Memory_Mode.My_Mem_Mode_Child]
inherit=???            ---> Parent section to inherit from.  An option in the child overwrites an identical option in the parent.  ??? = {[Part.Name]}
arena_cache_size=???   ---> Size of the arena/cache memory area.  ??? = {int in Bytes}
```
