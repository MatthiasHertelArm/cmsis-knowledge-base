---
id: "ethu-vela-system-configuration-parameters"
type: "concept"
domain: "edge-ai"
title: "Vela: Create device-specific vela.ini file / System configuration parameters"
summary: "Part of: Create device-specific vela.ini file"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/vela/src/main.md#system-configuration-parameters"
license: "Apache-2.0"
mode: "V"
---

_Part of: Create device-specific vela.ini file_

The system configuration maps the two logical aliases in `vela.ini` to memory
types and supplies the performance model. `axi0_port` and `axi1_port` connect
the aliases used by a memory mode to those types; they do not by themselves
identify a physical memory or hardware port. Parameters for a memory type are
needed only when `axi0_port` or `axi1_port` selects that type.

Derive the values from the device data sheet, interconnect description, and
measured memory behavior:

- use the integrated Ethos-U clock for `core_clock`;
- map each logical alias to the memory type that most closely represents the
  physical memory connected through that access path;
- express memory clock or bandwidth scaling relative to the Ethos-U core clock;
- convert read and write latency to Ethos-U core cycles; and
- use supported burst lengths and outstanding-transaction limits from the
  device interconnect.

These inputs form a scheduling cost model, not a cycle-accurate hardware model.
Start with conservative values when the hardware documentation gives a range,
then compare compiler estimates and hardware measurements for representative ML
models.

| Parameter | Type or values | Description |
|---|---|---|
| `core_clock` | Float, Hz | Ethos-U core frequency. Scientific notation such as `500e6` is accepted. |
| `axi0_port` | `Sram`, `Dram`, `OnChipFlash`, `OffChipFlash` | Memory type assigned to the logical `Axi0` alias. |
| `axi1_port` | `Sram`, `Dram`, `OnChipFlash`, `OffChipFlash` | Memory type assigned to the logical `Axi1` alias. |
| `<Memory>_clock_scale` | Float, `0.0` to `1.0` | Memory clock/bandwidth scale relative to `core_clock`. `<Memory>` is `Sram`, `Dram`, `OnChipFlash`, or `OffChipFlash`. |
| `<Memory>_ports_used` | Integer | Number of ports used for memory (used for `Sram`, `Dram`, `OnChipFlash`) |
| `<Memory>_burst_length` | Integer, bytes | Minimum efficient transfer burst. |
| `<Memory>_read_latency` | Integer, cycles | Read latency used by the cost model. |
| `<Memory>_write_latency` | Integer, cycles | Write latency used by the cost model. Use `0` for a read-only memory when appropriate. |
| `<Memory>_max_reads` | Integer | Maximum outstanding reads. |
| `<Memory>_max_writes` | Integer | Maximum outstanding writes. Use `0` for a read-only memory when appropriate. |

The option reference lists the full metric set for `Sram`, `Dram`, and
`OffChipFlash`, and lists `OnChipFlash_clock_scale` for on-chip Flash.
Use `--verbose-config` with the installed Vela version to inspect the resolved
properties supported by that version.

The values in `vela.ini` are used by the Vela compiler to optimize the ML model for the target and the output report.
They can alter scheduling, buffering, DMA insertion, allocation sizes, and the generated
command stream. `core_clock` is primarily used to convert cycle estimates to time.
