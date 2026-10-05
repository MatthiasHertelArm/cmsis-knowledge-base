---
id: "ethu-test-ethos-u-exploring-ethos-u-configurations"
type: "concept"
domain: "edge-ai"
title: "Test-Ethos-U: Exploring Ethos-U configurations"
summary: "The Vela configuration, generated command stream, linker placement, and driver region configuration describe the same memory system and must remain consistent."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:examples/Test-Ethos-U/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/examples/Test-Ethos-U/README.md#exploring-ethos-u-configurations"
license: "Apache-2.0"
mode: "V"
---

The Vela configuration, generated command stream, linker placement, and driver
region configuration describe the same memory system and must remain
consistent.

The
[Configure Ethos-U for FVP Simulation Models](https://arm-software.github.io/CMSIS_Ethos_U/latest/integration/fvp-ethos-setup.html)
reference lists the supported configurations and their corresponding values.

After selecting a configuration, apply the values from its table column and
review these project settings together:

- the `System_Config`, `Memory_Mode`, and `arena_cache_size` values in `Model/vela.ini`;
- `NPU_QCONFIG` and `NPU_REGIONCFG_*` in `Test-Ethos-U*.csolution.yml`;
- the `ethos_model`, `ethos_arena`, and `ethos_cache` linker sections in the Board layer; and
- the cache, security, and MPU/SAU attributes for those physical memories.

The default `arena_cache_size` is 384 KiB and must match `ETHOS_CACHE_SIZE`
in boards layer `ethos_setup.c`.
