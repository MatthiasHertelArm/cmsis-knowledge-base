---
id: "ethu-vela-invocation"
type: "concept"
domain: "edge-ai"
title: "Vela: Invocation"
summary: "Only the input ML model file and accelerator configuration are needed for a basic build:"
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@cf13d8d:documentation/doxygen/vela/src/main.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/cf13d8d/documentation/doxygen/vela/src/main.md#invocation"
license: "Apache-2.0"
mode: "V"
---

```console
vela [Options] NETWORK
```

- `Options` are described in the tables below and can precede or follow `NETWORK`. Use `vela --help` for the exact `Options` provided by the installed version.
- `NETWORK` is the path to the `.tflite` or `.tosa` ML model input file.

Only the input ML model file and accelerator configuration are needed for a basic
build:

```console
vela --accelerator-config ethos-u55-128 my_network.tflite
```

For meaningful scheduling and performance estimates, also select a platform
configuration, memory mode, and optimization strategy:

```console
vela my_network.tflite \
  --accelerator-config ethos-u55-128 \
  --config path/to/device-vela.ini \
  --system-config DEVICE_SYSTEM_CONFIG \
  --memory-mode DEVICE_MEMORY_MODE \
  --optimise Performance
```

### Options for input, output, and discovery

| Option | Description |
|---|---|
| `-h`, `--help` | Show command help and exit. |
| `--version` | Show the installed Vela version and exit. |
| `--api-version` | Show the deprecated external-API version. Planned for removal. |
| `--supported-ops-report` | Write `SUPPORTED_OPS.md` for TFLite operator constraints and exit. |
| `--list-config-files` | List packaged `vela.ini` configuration files and exit. |
| `--list-configs FILE` | List system configurations and memory modes in a `vela.ini` file and exit. |
| `--output-dir DIR` | Output directory; defaults to `output`. |
| `--output-format {tflite,raw}` | Select the output format; defaults to `tflite`. Raw output is an `.npz` archive and requires complete NPU placement. |
| `--enable-debug-db` | Write an ML model debug database into the output directory. |
| `--config FILE` | Read a ConfigParser-format `vela.ini` file. May be supplied more than once; later files can extend or override earlier definitions. |
| `--timing` | Report time spent in compiler stages. |
| `--force-symmetric-int-weights` | Force signed integer weight zero-points to zero. |

Raw output holds command streams, weight data, and tensor quantization metadata
for Ethos-U regions. It omits CPU regions and therefore is not a general
TFLite-to-TOSA conversion format.

### Options for Ethos-U target and scheduling

| Option | Description and values |
|---|---|
| `--accelerator-config TARGET` | Select Ethos-U hardware target: `ethos-u55-{32,64,128,256}`, `ethos-u65-{256,512}`, or `ethos-u85-{128,256,512,1024,2048}`. The suffix is the MACs-per-cycle configuration. |
| `--system-config NAME` | Select `[System_Config.NAME]` from the configuration files. The internal default provides functional defaults, but a platform-specific definition gives useful scheduling estimates. |
| `--memory-mode NAME` | Select `[Memory_Mode.NAME]`, which maps constants, arena, and cache to the system's memory areas. |
| `--tensor-allocator {LinearAlloc,Greedy,HillClimb}` | Choose the tensor allocator; defaults to `HillClimb`. |
| `--max-block-dependency {0,1,2,3}` | Deprecated. Set the maximum block-dependency delay between NPU kernel operations; defaults to `3`. A lower value can increase execution time. |
| `--optimise {Performance,Size}` | `Performance` is the default and minimizes inference time; `Size` minimizes peak SRAM and ignores the arena-cache size. |
| `--arena-cache-size BYTES` | Override the selected memory mode's cache capacity for `Performance` optimization. This is a byte count, not KiB. |
| `--cpu-tensor-alignment BYTES` | Alignment for CPU tensors, including custom-operator inputs and outputs; defaults to `16`. Keep it consistent with the ML inference runtime allocation. |
| `--recursion-limit COUNT` | Python recursion limit used during compilation; defaults to `1000`. |
| `--hillclimb-max-iterations COUNT` | Maximum HillClimb allocator iterations; defaults to `99999`. |
| `--cop-format {COP1,COP2}` | Select the custom-operator payload metadata format; defaults to `COP1`. |
| `--separate-io-regions` | Place custom-operator inputs and outputs into separate logical regions. Requires `--cop-format COP2`. |
| `--ignore-ops OP[,OP...]` | Force named TFLite builtin operator types, such as `ADD,ARGMAX`, onto the CPU. Repeatable and ignored for TOSA. |

### Options for reporting and diagnostics

| Option | Description |
|---|---|
| `--show-cpu-operations` | List TFLite operations that were not placed on the NPU. |
| `--show-subgraph-io-summary` | Summarize every subgraph and its inputs and outputs. |
| `--verbose-all` | Enable all verbose reports. The resulting output can be very large. |
| `--verbose-config` | Show resolved system and memory configuration. |
| `--verbose-graph` | Trace graph rewrites. |
| `--verbose-quantization` | Show quantization processing. |
| `--verbose-packing` | Show operation/pass packing. |
| `--verbose-performance` | Show detailed performance estimates. |
| `--verbose-tensor-purpose` | Show tensor-purpose assignment. |
| `--verbose-tensor-format` | Show tensor-format assignment. |
| `--verbose-schedule` | Show the selected schedule. |
| `--verbose-allocation` | Show tensor allocation. |
| `--verbose-high-level-command-stream` | Print the high-level command stream. |
| `--verbose-register-command-stream` | Print the register command stream. |
| `--verbose-operators` | List operators. |
| `--verbose-weights` | Show weight information. |
| `--verbose-cycle-estimate` | Show cycle-estimation details. |
| `--verbose-progress` | Show compilation progress. |
