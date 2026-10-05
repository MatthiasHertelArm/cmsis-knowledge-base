---
id: "ethu-driver-command-stream-regions-and-base-pointers"
type: "concept"
domain: "edge-ai"
title: "Driver: Command stream regions and base pointers"
summary: "Vela generates command streams that refer to memory regions. The system configuration and memory mode selected in the vela.ini file determine the expected memory area for each memory region used by the compiled ML model."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:documentation/doxygen/driver/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/documentation/doxygen/driver/src/main.md#command-stream-regions-and-base-pointers"
license: "Apache-2.0"
mode: "V"
---

### Determine the memory regions used by Vela

Vela generates command streams that refer to
memory regions. The system configuration and memory mode selected in the
`vela.ini` file determine the expected memory area for each memory region used
by the compiled ML model.

The Ethos-U NPU and driver support eight base pointers and the corresponding
`REGIONCFG[0] ... REGIONCFG[7]` selectors. Vela currently uses only three
regions:

- region 0: permanent model data, such as constants and weights
  (`const_mem_area`).
- region 1: the scratch arena (`arena_mem_area`).
- region 2: optional fast scratch, used when `cache_mem_area` maps to `Sram` and
  uses a different logical alias from `arena_mem_area`.

Consequently, only regions 0 through 2 are referenced in the following section.

The memory mode selects which Vela logical alias, `Axi0` or `Axi1`, each memory
area uses. The following table shows the default `vela.ini` settings. Region 2
(`cache_mem_area`) is used only when region 1 (`arena_mem_area`) uses a
different logical alias.

| Vela memory mode | Region 0 (const_mem_area) | Region 1 (arena_mem_area) | Region 2 (cache_mem_area) |
| --- | --- | --- | --- |
| `Sram_Only` | `Axi0` | `Axi0` | `Axi0` (not used) |
| `Shared_Sram` | `Axi1` | `Axi0` | `Axi0` (not used) |
| `Dedicated_Sram` | `Axi1` | `Axi1` | `Axi0` |

The system configuration maps each logical alias to a Vela memory type. The
following tables show two example mappings from the default `vela.ini`
settings.

**Example using `--system-config Ethos_U55_High_End_Embedded`:**

| Vela memory mode | Region 0 (const_mem_area) | Region 1 (arena_mem_area) | Region 2 (cache_mem_area) |
| --- | --- | --- | --- |
| `Sram_Only` | `Sram` | `Sram` | Not used |
| `Shared_Sram` | `OffChipFlash` | `Sram` | Not used |
| `Dedicated_Sram` | `OffChipFlash` | `OffChipFlash` (invalid) | `Sram` |

**Example using `--system-config Ethos_U85_SYS_DRAM_Mid`:**

| Vela memory mode | Region 0 (const_mem_area) | Region 1 (arena_mem_area) | Region 2 (cache_mem_area) |
| --- | --- | --- | --- |
| `Sram_Only` | `Sram` | `Sram` | Not used |
| `Shared_Sram` | `Dram` | `Sram` | Not used |
| `Dedicated_Sram` | `Dram` | `Dram` | `Sram` |

The linker maps each Vela memory type to physical memory. Even when region 0 is
in `Dram`, it may be placed in ROM (Flash) because it contains constants.
Driver base addresses and access settings must match the memory placement
selected by Vela and the linker.

> [!Note]
> If the physical memory differs from the memory type modeled by the selected
> system configuration, Vela's performance estimates are no longer accurate.

### Configure memory access with NPU_QCONFIG and NPU_REGIONCFG_x

The simplest setup uses a single-variant
driver with one fixed memory-access configuration for all ML models. The
`NPU_QCONFIG` definition selects the memory-access configuration used to
fetch the command stream. Each `NPU_REGIONCFG_x` definition selects the
memory-access configuration for region `x`. In the Vela configurations above,
`x` is 0, 1, or 2.

> [!Note]
> If the `NPU_QCONFIG` and `NPU_REGIONCFG_x` macros are not defined, the driver
> uses the default values listed below.

Selector encodings are NPU-specific; see
Ethos-U55 and Ethos-U65 and
Ethos-U85 below.

### Other memory-access setup methods

The memory-access configuration can also be selected at run time:

- In a single-variant build, override the
  weak ethosu_config_select() function. The function
  receives the memory address and an index: `-1` for the command stream, or the
  region number for a base address.
- In a multi-variant build, set `qconfig`
  and `regioncfg` in the device configuration passed to ethosu_init_ex(). Alternatively, provide a per-driver `config_select`
  callback through `ethosu_device_user_ops` when the selection depends on the
  memory address.

### Memory region usage by the driver

The inference invocation functions (ethosu_invoke_v3(), ethosu_invoke_async(), and
ethosu_invoke_auto()) receive `custom_data_ptr`,
which points to the Vela-generated custom-operator payload. This payload
contains metadata and the command stream. The `base_addr` argument points to an array containing
the actual base address of each memory region, and `num_base_addr` specifies the number of entries.

Vela uses memory region 2 for fast scratch memory. The `fast_memory` and
`fast_memory_size` arguments to ethosu_init() or
ethosu_init_ex() specify the physical location and size
of this memory.

The following table maps invocation parameters to the corresponding NPU
registers and driver definitions.

| Invocation function parameter | Address register | Access-configuration selector | Default definition |
| --- | --- | --- | --- |
| `custom_data_ptr` | `QBASE` | `QCONFIG` | `NPU_QCONFIG` |
| `base_addr[n]` | `BASEP[n]` | `REGIONCFG[n]` | `NPU_REGIONCFG_n` |

### Ethos-U55 and Ethos-U65

Ethos-U55 and Ethos-U65 provide the `AXI0` and `AXI1` access paths.

| Memory placement | AXI port |
| --- | --- |
| SRAM | `AXI0` |
| DRAM/Flash | `AXI1` |

> [!Note]
> On Ethos-U55 `AXI1` port is read-only and cannot access writable scratch data.

The driver provides the following default values:

| Ethos-U variant | NPU_QCONFIG | NPU_REGIONCFG_0 | NPU_REGIONCFG_1 | NPU_REGIONCFG_2 |
| --- | --- | --- | --- | --- |
| Ethos-U55 | `2` -> `AXI1` | `3` -> `AXI1` | `0` -> `AXI0` | `1` -> `AXI0` |
| Ethos-U65 | `2` -> `AXI1` | `3` -> `AXI1` | `0` -> `AXI0` | `1` -> `AXI0` |

For Ethos-U55 and Ethos-U65, `QCONFIG` and the `REGIONCFG[0..7]` fields
accept values 0 through 3. The value selects an AXI port, an outstanding
transaction counter, and the corresponding `AXI_LIMITx` access profile.

| Value | AXI port | AXI access profile | Transaction counter |
| --- | --- | --- | --- |
| `0` | `AXI0` | `AXI_LIMIT0` | `AXI0_OUTSTANDING_COUNTER0` |
| `1` | `AXI0` | `AXI_LIMIT1` | `AXI0_OUTSTANDING_COUNTER1` |
| `2` | `AXI1` | `AXI_LIMIT2` | `AXI1_OUTSTANDING_COUNTER2` |
| `3` | `AXI1` | `AXI_LIMIT3` | `AXI1_OUTSTANDING_COUNTER3` |

Transaction counters enforce the limits in the corresponding
`AXI_LIMITx` profile. For their use in performance analysis, see
Monitoring AXI transaction
latency.

Each `AXI_LIMITx` access profile contains the burst split alignment, the memory
type used to encode AxCACHE, and the maximum number of outstanding read and
write transactions. These fields are configured by
`AXI_LIMITx_MAX_BEATS_BYTES`, `AXI_LIMITx_MEM_TYPE`,
`AXI_LIMITx_MAX_OUTSTANDING_READS`, and
`AXI_LIMITx_MAX_OUTSTANDING_WRITES`, respectively.

### Ethos-U85

The AXI ports are referred to as `AXI_SRAM` and `AXI_EXT`.

| Memory placement | AXI port |
| --- | --- |
| SRAM | `AXI_SRAM` |
| DRAM/Flash | `AXI_EXT` |

The driver provides the following default values:

| Ethos-U variant | NPU_QCONFIG | NPU_REGIONCFG_0 | NPU_REGIONCFG_1 | NPU_REGIONCFG_2 |
| --- | --- | --- | --- | --- |
| Ethos-U85 | `2` -> `MEM_ATTR_2` -> `AXI_EXT` | `3` -> `MEM_ATTR_3` -> `AXI_EXT` | `0` -> `MEM_ATTR_0` -> `AXI_SRAM` | `1` -> `MEM_ATTR_1` -> `AXI_SRAM` |

For Ethos-U85, each `NPU_MEM_ATTR_n` `#define` supplies the packed value written
to the corresponding `MEM_ATTR[n]` register. The suffix `n` identifies the
entry; it is not the value assigned to the `#define`. Each entry selects the AXI
port and specifies the memory domain and the memory type used to encode the
AxCACHE signals.

`QCONFIG` and each `REGIONCFG` field contain an index from 0 through 3 that
selects one of these `MEM_ATTR` entries. The default `MEM_ATTR_0` and
`MEM_ATTR_1` entries use `AXI_SRAM`, while `MEM_ATTR_2` and `MEM_ATTR_3` use
`AXI_EXT`. For example, `NPU_QCONFIG` defaults to `2`, selecting `MEM_ATTR_2`;
the default packed value of `NPU_MEM_ATTR_2` is `(1 << 2)`, or `4`, which
selects `AXI_EXT`.

These default `MEM_ATTR` values are set by the driver to replicate the default
Ethos-U55 and Ethos-U65 behavior, making it easier to correlate configurations
across variants, but the `MEM_ATTR` values can be configured by the user.

Ethos-U85 AXI limits are configured in the `AXI_SRAM` and `AXI_EXT` registers.
There is one `AXI_SRAM` register and one `AXI_EXT` register, so those limit
settings apply to all ports in each group.

Ethos-U85 AXI information:

| U85 configuration (MACs/CC) | Number of SRAM ports | Maximum outstanding reads per port | Maximum outstanding writes per port |
| --- | --- | --- | --- |
| 128 | 2 | 12 | 16 |
| 256 | 2 | 12 | 16 |
| 512 | 2 | 12 | 16 |
| 1024 | 2 | 12 | 16 |
| 2048 | 4 | 12 | 16 |

| U85 configuration (MACs/CC) | Number of EXT ports | Maximum outstanding reads per port | Maximum outstanding writes per port |
| --- | --- | --- | --- |
| 128 | 1 | 32 | 32 |
| 256 | 1 | 32 | 32 |
| 512 | 1 | 64 | 32 |
| 1024 | 2 | 64 | 32 |
| 2048 | 2 | 64 | 32 |
