---
id: "ethu-arm-cmsis-ethos-u-supported-npus"
type: "concept"
domain: "edge-ai"
title: "Arm CMSIS Ethos-U: Supported NPUs"
summary: "The selected single-variant component supplies the corresponding configuration header and NPU-family definition. The Multi-Variant component supplies all three backends and defines ETHOSU_MULTI_VARIANT."
status: "draft"
collection: "cmsis-ethos-u"
source: "ARM-software/CMSIS-Ethos-U@b2b641e:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-Ethos-U/blob/b2b641e/README.md#supported-npus"
license: "Apache-2.0"
mode: "V"
---

| NPU support | Component variant | Backend implementation |
|---|---|---|
| [Arm Ethos-U55](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u55) | `Generic U55` | `source/src/ethosu_backend_u55.c` |
| [Arm Ethos-U65](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u65) | `Generic U65` | `source/src/ethosu_backend_u65.c` |
| [Arm Ethos-U85](https://www.arm.com/products/silicon-ip-cpu/ethos/ethos-u85) | `Generic U85` | `source/src/ethosu_backend_u85.c` |
| Ethos-U55, Ethos-U65, and Ethos-U85 | `Multi-Variant` | All three backends |

The selected single-variant component supplies the corresponding configuration
header and NPU-family definition. The `Multi-Variant` component supplies all
three backends and defines `ETHOSU_MULTI_VARIANT`.
