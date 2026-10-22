---
id: "ethu-vela-use-the-ethos-u-configuration"
type: "concept"
domain: "edge-ai"
title: "Vela: Use the Ethos-U configuration"
summary: "Compiling an ML model requires three selections from the Ethos-U configuration:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/vela/src/main.md#use-the-ethos-u-configuration"
license: "Apache-2.0"
mode: "V"
---

Compiling an ML model requires three selections from the Ethos-U configuration:

| Option | Describes |
|---|---|
| `--accelerator-config` | NPU architecture and MAC configuration. The generated command stream is Ethos-U target-specific. |
| `--system-config` | Core clock, AXI port mapping, memory clock ratios, burst lengths, latencies, and outstanding transactions used by the cost model. |
| `--memory-mode` | Placement of constant, arena, and cache memory areas on the AXI-connected memories. |

When a DFP supplies device-specific Ethos-U configuration information and the
CMSIS-Toolbox project includes
[MLOps information](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#mlops-information),
CMSIS-Toolbox places the resolved configuration file in the `.cmsis` directory.
List its available system configurations and memory modes with:

```console
vela --list-configs .cmsis/device-vela.ini  # Use device-specific vela.ini
```

If the project does not provide a device configuration, the Vela installation
includes the generic reference file `Arm/vela.ini` for evaluation,
silicon-vendor development, and manual integration. Its parameters do not
describe a specific production device. List the installed configuration files
and their definitions with:

```console
vela --list-config-files
vela --list-configs Arm/vela.ini
```

The generic `Arm/vela.ini` reference file includes these system configurations:

- Ethos-U55: `Ethos_U55_Deep_Embedded`,
  `Ethos_U55_High_End_Embedded`.
- Ethos-U65: `Ethos_U65_Embedded`, `Ethos_U65_Mid_End`,
  `Ethos_U65_High_End`, `Ethos_U65_Client_Server`.
- Ethos-U85: `Ethos_U85_SYS_Flash_Low`, `Ethos_U85_SYS_Flash_High`,
  `Ethos_U85_SYS_DRAM_Low`, `Ethos_U85_SYS_DRAM_Mid`,
  `Ethos_U85_SYS_DRAM_High`.

### Select a memory mode

The reference configuration defines typically memory modes as shown below.

| Memory Mode       | const
_mem_area     | arena
_mem_area     | cache
_mem_area     | Content |
|-------------------|:-----------------------:|:-----------------------:|:-----------------------:|---------|
| `Sram_Only`       | `Axi0`                  | `Axi0`                  | `Axi0`                  | All model storage uses the memory type selected for `Axi0`. |
| `Shared_Sram`     | `Axi1`                  | `Axi0`                  | `Axi0`                  | Constants remain in the memory selected for `Axi1`; arena and cache share the `Axi0` memory. |
| `Dedicated_Sram`  | `Axi1`                  | `Axi1`                  | `Axi0`                  | The `Axi0` memory is a fast staging cache for an arena in the writable memory selected for `Axi1`. |

Note that there can be memory mode variants such as `Dedicated_Sram_256KB`, `_384KB`, `_512KB`, and
`_1024KB` that inherit `Dedicated_Sram` and set `arena_cache_size`.

The names `Axi0` and `Axi1` are logical aliases in `vela.ini`. Their physical
memory types come from the selected system configuration.

Ethos-U85 can have up to six AXI port interfaces, which Vela maps to `Axi0` and `Axi1`.
The `vela.ini` parameter `<Memory>_ports_used` contains the number of physical AXI
ports that map to a logical alias.

The `vela.ini` file, device interconnect, linker placement, MPU/SAU attributes,
cache policy, driver region indices, and ML inference runtime tensor arena must
agree. The Vela compiler cannot validate the complete firmware memory map.

### Understand arena cache and spilling

`cache_mem_area` does not always create a separate cache allocation. When it
resolves to the same memory type as `arena_mem_area`, the fast-scratch memory region is
folded into `arena_mem_area`. `cache_mem_area` is a distinct area only when
`arena_mem_area` is in a different memory type.

Ethos-U55 provides one read/write and one read-only AXI port and supports
`Sram_Only` and `Shared_Sram` modes. `Dedicated_Sram` places the writable arena
in the memory selected for `Axi1` while reserving the `Axi0` memory for fast
staging. Both paths must be writable, so the `Dedicated_Sram` mode is available
on Ethos-U65 and Ethos-U85.
