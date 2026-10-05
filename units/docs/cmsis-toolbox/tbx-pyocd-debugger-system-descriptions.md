---
id: "tbx-pyocd-debugger-system-descriptions"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Content of `*.cbuild-run.yml` / `system-descriptions:`"
summary: "Part of: Content of .cbuild-run.yml"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#system-descriptions"
license: "Apache-2.0"
mode: "V"
---

_Part of: Content of `*.cbuild-run.yml`_

Contains a list of system description files for the target's peripherals and software components. The `svd` files are
processed by pyOCD to present debug views and decode register reads/writes.

`system-descriptions:`                            |              | Content
:-------------------------------------------------|:-------------|:------------------------------------
`- file:`                                         | **Required** | Specifies the file name including the path.
    `type:`                        | **Required** | Specifies the file type (see table below).
    `info:`                        |   Optional   | Brief description of the file.
    `pname:`                       |   Optional   | File is used only for a specific processor; default is for all processors.

`type:` | Description
:-------|:------------------
`svd`   | [System View Description (`*.svd`) file](https://open-cmsis-pack.github.io/svd-spec/main/index.html) specified in the [DFP](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html#element_debug).

!!! Note
    Currently pyOCD has a limitation of only processing the `svd` file for the processor listed in `start-pname:`.

**Example:**

```yml
  system-descriptions:
    - file: ${CMSIS_PACK_ROOT}/AlifSemiconductor/Ensemble/2.0.4/Debug/SVD/AE722F80F55D5LS_CM55_HE_View.svd
      type: svd
      pname: M55_HE
    - file: ${CMSIS_PACK_ROOT}/AlifSemiconductor/Ensemble/2.0.4/Debug/SVD/AE722F80F55D5LS_CM55_HP_View.svd
      type: svd
      pname: M55_HP
```
