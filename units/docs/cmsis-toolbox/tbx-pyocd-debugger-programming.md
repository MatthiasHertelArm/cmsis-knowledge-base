---
id: "tbx-pyocd-debugger-programming"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Content of `*.cbuild-run.yml` / `programming:`"
summary: "Part of: Content of .cbuild-run.yml"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#programming"
license: "Apache-2.0"
mode: "V"
---

_Part of: Content of `*.cbuild-run.yml`_

Contains a list of the target's flash programming algorithms. pyOCD uses these algorithms to identify which
memory regions should be treated as flash, and it will automatically select the appropriate algorithm when
programming flash on the target.

`programming:`                                    |              | Content
:-------------------------------------------------|:-------------|:------------------------------------
`- algorithm:`                                    | **Required** | Programming algorithm file including the path.
    `start:`                       | **Required** | Start address of memory covered by the programming algorithm.
    `size:`                        | **Required** | Size of memory covered by the programming algorithm.
    `ram-start:`                   | **Required** | Start address of RAM where the algorithm will be executed from.
    `ram-size:`                    | **Required** | Maximum size of RAM available for executing the programming algorithm.
    `pname:`                       |   Optional   | Specifies the processor for the execution of the algorithm.

**Example:**

```yml
  programming:
    - algorithm: ${CMSIS_PACK_ROOT}/AlifSemiconductor/Ensemble/2.0.4/Flash/algorithms/Ensemble.FLM
      start: 0x80000000
      size: 0x00580000
      ram-start: 0x00000000
      ram-size: 0x00020000
    - algorithm: ${CMSIS_PACK_ROOT}/AlifSemiconductor/Ensemble/2.0.4/Flash/algorithms/Ensemble_IS25WX256.FLM
      start: 0xC0000000
      size: 0x02000000
      ram-start: 0x00000000
      ram-size: 0x00040000
```
