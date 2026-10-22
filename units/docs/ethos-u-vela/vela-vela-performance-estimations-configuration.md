---
id: "vela-vela-performance-estimations-configuration"
type: "concept"
domain: "edge-ai"
title: "Vela Performance Estimations: Configuration"
summary: "The first section of the summary shows the configuration used for optimizing the network."
status: "draft"
collection: "ethos-u-vela"
source: "artificial-intelligence/ethos-u/ethos-u-vela@4bd6685:PERFORMANCE.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/PERFORMANCE.md#configuration"
license: "Apache-2.0"
mode: "V"
---

The first section of the summary shows the configuration used for
optimizing the network.

```
Accelerator configuration               Ethos_U55_256
System configuration                 internal-default
Memory mode                          internal-default
Accelerator clock                                 500 MHz
Design peak SRAM bandwidth                       4.00 GB/s
Design peak Off-chip Flash bandwidth             0.50 GB/s
```

### Accelerator configuration

This shows the selected accelerator configuration.  It identifies the Embedded
NPU that the compiler is targeting.  
__NOTE: It is crucial to select the correct device, otherwise a run-time check
in the driver will fail.__  
To select a different accelerator configuration use the CLI option
`--accelerator-config`, see [OPTIONS.md](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#Accelerator-Configuration).

### System configuration

The selected system configuration from the provided configuration file or the
default value.  
__NOTE: It is very important to select a system
configuration that correctly describes the target embedded system.__   
This is because the compiler makes some of its optimization decisions based upon
this information.  Failing to select the correct configuration could result in
run-time errors, bit-inexact operation, or suboptimal operation of the Embedded
NPU.  To select a different system configuration use the CLI option
`--system-config`, see [OPTIONS.md](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#System-Config).

### Memory mode

The selected memory mode from the provided configuration file or the default value.  
__NOTE: It is very important to select a memory mode that correctly describes
the target embedded system.__  
This is because the compiler makes some of its optimization decisions based upon
this information.  To select a different memory mode use the CLI option
`--memory-mode`, see [OPTIONS.md](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#Memory-Mode).

### Accelerator clock

The accelerator clock for the given the system configuration.

### Design peak memory bandwidth

The design peak memory bandwidth for the given system configuration.
It gives the theoretical maximum bandwidth of the memory based upon the
[System Configuration](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/4bd6685/OPTIONS.md#Configuration-File) parameters specified
and the AXI port width of the Ethos-U NPU.
