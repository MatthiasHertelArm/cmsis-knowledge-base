---
id: "ethu-vela-create-device-specific-vela-ini-file"
type: "concept"
domain: "edge-ai"
title: "Vela: Create device-specific vela.ini file"
summary: "To support a device manually, create a device-specific vela.ini file. Application developers normally obtain this file from the silicon vendor, either directly or from a DFP through CMSIS-Toolbox."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/vela/src/main.md#create-device-specific-vela-ini-file"
license: "Apache-2.0"
mode: "V"
---

To support a device manually, create a device-specific `vela.ini` file.
Application developers normally obtain this file from the silicon vendor,
either directly or from a DFP through CMSIS-Toolbox.

Creating an Ethos-U configuration requires these steps:

1. Select the Ethos-U variant and MAC configuration integrated into the device.
2. Identify the physical memories accessible to the NPU and obtain their clock,
   bandwidth, latency, burst, and outstanding-transaction characteristics.
3. Define a `System_Config` that models those memories through the logical
   `Axi0` and `Axi1` aliases.
4. Define one or more `Memory_Mode` sections that place constants, the writable
   arena, and optional fast staging storage on those aliases.
5. Create matching linker and driver configurations for the physical memory
   placement.
6. Validate the complete configuration with compiler reports, the linker map,
   and measurements on the device.

The `vela.ini`, linker, MPU/SAU, cache, and driver settings must describe the
same finished device integration.

`vela.ini` uses Python ConfigParser syntax and is case-sensitive for section
names, keys, and values. It contains two section types:

```ini
[System_Config.ConfigurationName]
; NPU clock, AXI mapping, and memory performance

[Memory_Mode.ModeName]
; compiler memory-area placement
```

`ConfigurationName` and `ModeName` must not contain spaces. A file can define
multiple sections of either type; select them with `--system-config` and
`--memory-mode`. Every property is optional, when omitted it defaults to `1`.
It is recommended to define every property that affects the target system.

Any section can contain `inherit=Part.Name` to inherit the values of another section.

- Inherited sections can appear in any order. Do not create recursive inheritance.
- `axi0_port` and `axi1_port` accept only the supported Vela memory types
  `Sram`, `Dram`, `OnChipFlash`, and `OffChipFlash`; custom memory type names are
  not supported.
- Start the name of a custom Ethos-U55 system configuration with
  `Ethos_U55`. The Vela compiler uses this prefix when selecting the U55 AXI
  bandwidth width while translating memory-performance values.
