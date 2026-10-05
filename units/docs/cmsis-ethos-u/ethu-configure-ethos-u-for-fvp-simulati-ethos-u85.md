---
id: "ethu-configure-ethos-u-for-fvp-simulati-ethos-u85"
type: "concept"
domain: "edge-ai"
title: "Configure Ethos-U for FVP Simulation Models: Ethos-U85"
summary: "The values marked default are supplied by the selected Generic Ethos-U driver configuration when the board layer does not override them. The SRAM-only U55 configuration must override the shared-SRAM defaults."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/integration/src/fvp-ethos-setup.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/integration/src/fvp-ethos-setup.md#ethos-u85"
license: "Apache-2.0"
mode: "V"
---

| Setting            | SRAM only                      | Shared SRAM                    | Dedicated SRAM                 |
|--------------------|--------------------------------|--------------------------------|--------------------------------|
| Target type        | `SSE-320-U85`                  | `SSE-320-U85`                  | `SSE-320-U85`                  |
| Solution           | `Test-Ethos-U85`               | `Test-Ethos-U85`               | `Test-Ethos-U85`               |
| NPU                | U85, 256 MACs                  | U85, 256 MACs                  | U85, 256 MACs                  |
| Vela INI           | `Model/vela.ini`               | `Model/vela.ini`               | `Model/vela.ini`               |
| Vela `system`      | `Ethos_U85_SYS_DRAM_Mid`       | `Ethos_U85_SYS_DRAM_Mid`       | `Ethos_U85_SYS_DRAM_Mid`       |
| Vela `memory`      | `Sram_Only`                    | `Shared_Sram`                  | `Dedicated_Sram_384KB`         |
| `NPU_QCONFIG`      | `1`                            | `2` (default)                  | `2`                            |
| `NPU_REGIONCFG_0`  | `1`                            | `3` (default)                  | `3`                            |
| `NPU_REGIONCFG_1`  | `0`                            | `0` (default)                  | `2`                            |
| `NPU_REGIONCFG_2`  | Unused                         | Unused                         | `1`                            |
| `ETHOS_CACHE_SIZE` | Not used                       | Not used                       | `393216` bytes                 |
| `ethos_model`      | SRAM_VM0 / RAM1 via `AXI_SRAM` | DDR4_3 / ROM2 via `AXI_EXT`    | DDR4_3 / ROM2 via `AXI_EXT`    |
| `ethos_arena`      | SRAM_VM0 / RAM1 via `AXI_SRAM` | SRAM_VM0 / RAM1 via `AXI_SRAM` | DDR4_1 / RAM0 via `AXI_EXT`    |
| `ethos_cache`      | Unused                         | Unused                         | SRAM_VM0 / RAM1 via `AXI_SRAM` |

The values marked **default** are supplied by the selected Generic Ethos-U
driver configuration when the board layer does not override them. The
SRAM-only U55 configuration must override the shared-SRAM defaults.

After selecting a column, regenerate the solution's `*.cbuild-mlops.yml` file
and convert both models before building:

| NPU | Conversion command |
|-----|--------------------|
| U55 | `python script/model-converter.py Test-Ethos-U55.cbuild-mlops.yml` |
| U65 | `python script/model-converter.py Test-Ethos-U65.cbuild-mlops.yml` |
| U85 | `python script/model-converter.py Test-Ethos-U85.cbuild-mlops.yml` |

> NOTES
>
> - The generated files under `Model/` are shared by all solutions. Always
>   reconvert them after changing the target or Vela configuration.
> - `ROM2` is a read-only linker execution region backed by DDR4_3; it is not
>   physical ROM.
> - `Shared_Sram` places the command stream and constants in external memory
>   and the writable tensor arena in SRAM. It does not use a dedicated Vela
>   arena cache.
> - `Dedicated_Sram_384KB` places the model and writable arena in external
>   DDR4 and reserves 384 KiB of SRAM as the Vela arena cache.
>   `ETHOS_CACHE_SIZE` must equal Vela's `arena_cache_size` of 393216 bytes.
> - Ethos-U55 does not use `Dedicated_Sram` because its AXI1 interface is
>   read-only, while that mode requires a writable arena on Axi1.
