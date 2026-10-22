---
id: "tbx-pyocd-debugger-cbuild-run"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Content of `*.cbuild-run.yml` / `cbuild-run:`"
summary: "Part of: Content of .cbuild-run.yml"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#cbuild-run"
license: "Apache-2.0"
mode: "V"
---

_Part of: Content of `*.cbuild-run.yml`_

The top-level `cbuild-run:` node identifies the file as a `*.cbuild-run.yml` file. All Run and Debug configuration nodes
are nested under this node. The table below is an excerpt of the full [File Structure of `*.cbuild-run.yml`](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/YML-CBuild-Format.md#file-structure-of-cbuild-runyml)
configuration and highlights the nodes relevant to pyOCD. The contents of each node are described in the following sections.

`cbuild-run:`                                                     |              | Content
:-----------------------------------------------------------------|:-------------|:------------------------------------
    [`board-pack:`](#board-pack)                   |   Optional   | Identifies the board pack used.
    [`board-pack-path:`](#board-pack-path)         |   Optional   | Path to the board pack on the host computer.
    [`device:`](#device)                           | **Required** | Identifies the device.
    [`device-pack:`](#device-pack)                 |   Optional   | Identifies the device pack used.
    [`device-pack-path:`](#device-pack-path)       |   Optional   | Path to the device pack on the host computer.
    [`output:`](#output)                           |   Optional   | Lists the images (ELF, HEX, BIN) in this solution.
    [`system-resources:`](#system-resources)       |   Optional   | Lists target system resources.
    [`system-descriptions:`](#system-descriptions) |   Optional   | Lists target's description files for peripherals and software components.
    [`debugger:`](#debugger)                       |   Optional   | Configures the debugger.
    [`debug-vars:`](#debug-vars)                   |   Optional   | Debug variables.
    [`debug-sequences:`](#debug-sequences)         |   Optional   | Debug sequences.
    [`programming:`](#programming)                 |   Optional   | Lists flash algorithms for programming.
    [`flash-info:`](#flash-info)                   |   Optional   | Lists flash information for flash programming using debug sequences.
    [`debug-topology:`](#debug-topology)           |   Optional   | Debug topology.
