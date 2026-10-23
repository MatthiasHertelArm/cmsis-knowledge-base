---
id: "ethu-driver-compile-time-configuration"
type: "concept"
domain: "edge-ai"
title: "Driver: Compile-time configuration"
summary: "The Ethos-U driver is configured with preprocessor #define statements. The following tables list the supported configuration statements."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/driver/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/driver/src/main.md#compile-time-configuration"
license: "Apache-2.0"
mode: "V"
---

The Ethos-U driver is configured with preprocessor `#define` statements. The following tables
list the supported configuration statements.

### Single-variant build

A single-variant build supports one Ethos-U variant selected at compile time.
Define exactly one Ethos-U family together with its MAC configuration. Do not
define `ETHOSU_MULTI_VARIANT`. When using the CMSIS pack, selection of a
single-variant Ethos-U Driver component defines the corresponding Ethos-U
family automatically.

| Definition | Purpose |
| --- | --- |
| `ETHOSU55`, `ETHOSU65`, or `ETHOSU85` | Select the Ethos-U family. Define exactly one. The CMSIS component selection defines this automatically. |
| `ETHOSU_MACS` | Select the MAC configuration, for example `128` for an Ethos-U55-128 variant. |

### Multi-variant build

A multi-variant build includes support for Ethos-U55, Ethos-U65, and Ethos-U85.
The Ethos-U variant and MAC configuration are selected for each driver instance
at run time. Do not define the single-variant `ETHOSU55`, `ETHOSU65`,
`ETHOSU85`, or `ETHOSU_MACS` statements in this build. When using the CMSIS
pack, selection of the Multi-Variant Ethos-U Driver component defines
`ETHOSU_MULTI_VARIANT` automatically.

| Definition | Purpose |
| --- | --- |
| `ETHOSU_MULTI_VARIANT` | Enable multi-variant support. The CMSIS component selection defines this automatically. This changes the initialization, reservation, platform-operation, and PMU APIs available to the application. |

### Common configuration

The following `#define` statements apply in either a single-variant or
multi-variant build. In a multi-variant build, the memory-routing statements
initialize the default configuration for each included Ethos-U family.

`NPU_QCONFIG` and `NPU_REGIONCFG_0` through `NPU_REGIONCFG_7` provide default
memory-access selectors; they do not contain addresses. `NPU_QCONFIG` selects
the access configuration used to fetch the command stream. The suffix in
`NPU_REGIONCFG_n` identifies the corresponding `base_addr[n]` region, while the
value selects its access configuration. On Ethos-U55 and Ethos-U65, the value
selects an `AXI_LIMITx` access profile. On Ethos-U85, it selects a `MEM_ATTR`
entry. See
Command stream regions and base pointers.

| Definition | Purpose |
| --- | --- |
| `ETHOSU_MAX_WAITERS` | Set the maximum number of distinct Ethos-U variants tracked by driver reservation. The default is `4`. |
| `ETHOSU_SEMAPHORE_WAIT_INFERENCE` | Set the timeout passed to the platform semaphore while waiting for inference completion. The default is `ETHOSU_SEMAPHORE_WAIT_FOREVER`; the platform defines the time unit. See Mutex and semaphores. |
| `NPU_QCONFIG` | Set the default memory-access selector for fetching the command stream. |
| `NPU_REGIONCFG_0` through `NPU_REGIONCFG_7` | Set the default memory-access selector for each corresponding `base_addr[0]` through `base_addr[7]` region. |

### Text logging

The following `#define` statements configure driver text logging through the C
standard I/O streams. See Logging for the generated macro
reference and implementation details.

| Definition | Purpose |
| --- | --- |
| `ETHOSU_LOG_ENABLE` | Enable or disable logging. The default is `1`. |
| `ETHOSU_LOG_SEVERITY` | Select the most verbose compiled log level: `ETHOSU_LOG_ERR`, `ETHOSU_LOG_WARN`, `ETHOSU_LOG_INFO`, or `ETHOSU_LOG_DEBUG`. The default is `ETHOSU_LOG_WARN`. |

### Variant-specific hardware configuration

The configuration headers provide default values for the following hardware
`#define` statements. A silicon vendor can supply values validated for its NPU,
interconnect, memory system, cache policy, and security configuration to adjust
the driver defaults. Do not tune these settings independently. See
Command stream regions and base pointers.

| Ethos-U variant | Configuration definitions |
| --- | --- |
| Ethos-U55 and Ethos-U65 | `AXI_LIMITx_MAX_BEATS_BYTES`, `AXI_LIMITx_MEM_TYPE`, `AXI_LIMITx_MAX_OUTSTANDING_READS`, and `AXI_LIMITx_MAX_OUTSTANDING_WRITES`, where `x` is `0` through `3`. |
| Ethos-U85 | `NPU_MAC_PWR_RAMP_CYCLES`, `NPU_MEM_ATTR_0` through `NPU_MEM_ATTR_3`, `AXI_LIMIT_SRAM_MAX_OUTSTANDING_READ`, `AXI_LIMIT_SRAM_MAX_OUTSTANDING_WRITE`, `AXI_LIMIT_SRAM_MAX_BEATS`, `AXI_LIMIT_EXT_MAX_OUTSTANDING_READ`, `AXI_LIMIT_EXT_MAX_OUTSTANDING_WRITE`, and `AXI_LIMIT_EXT_MAX_BEATS`. |

For Ethos-U55 and Ethos-U65, each `AXI_LIMITx` register defines a complete AXI
access profile, despite the register name suggesting that it contains only
transaction limits. The corresponding `AXI_LIMITx_*` `#define` statements
configure its maximum burst size, memory type, and maximum number of
outstanding read and write transactions. In particular, `AXI_LIMITx_MEM_TYPE`
sets the memory type used to encode the AXI AxCACHE signals.
