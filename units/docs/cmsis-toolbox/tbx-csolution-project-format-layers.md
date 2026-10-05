---
id: "tbx-csolution-project-format-layers"
type: "concept"
domain: "project"
title: "CSolution Project Format: Source File Management / `layers:`"
summary: "Add a software layer to a project. Used in .cproject.yml files."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#layers"
license: "Apache-2.0"
mode: "V"
---

_Part of: Source File Management_

Add a software layer to a project. Used in `*.cproject.yml` files.

`layers:`                                                 |              | Content
:---------------------------------------------------------|:-------------|:------------------------------------
[`- layer:`](#layer)                                      |   Optional   | Path to the `*.clayer.yml` file that defines the layer.
&nbsp;&nbsp;&nbsp; [`type:`](#layer-type)                 |   Optional   | Refers to an expected layer type. Enables the [auto-selection of layers](#auto-select-layers).
&nbsp;&nbsp;&nbsp; [`for-context:`](#for-context)         |   Optional   | Include layer for a list of *build* and *target* types.
&nbsp;&nbsp;&nbsp; [`not-for-context:`](#not-for-context) |   Optional   | Exclude layer for a list of *build* and *target* types.

**Example:**

```yml
  layers:
    # Socket
    - layer: ./Socket/FreeRTOS+TCP/Socket.clayer.yml
      for-context:
        - +IP-Stack
    - layer: ./Socket/WiFi/Socket.clayer.yml
      for-context:
        - +WiFi
    - layer: ./Socket/VSocket/Socket.clayer.yml
      for-context:
        - +FVP

    # Board
    - layer: ./Board/IMXRT1050-EVKB/Board.clayer.yml
      for-context:
        - +IP-Stack
        # - +WiFi
    - layer: ./Board/B-U585I-IOT02A/Board.clayer.yml
      for-context:
        - +WiFi
    - layer: ./Board/AVH_MPS3_Corstone-300/Board.clayer.yml
      for-context:
        - +FVP
```

#### `layer:` `type:`

The `layer:` - `type:` is used in combination with the meta-data of the [`connections:`](#connections) to check the list of available `*.clayer.yml` files for matching layers. Instead of an explicit `layer:` node that specifies a `*.clayer.yml` file, the `type:` is used to search for matching layers with the `csolution` command `list layers`.

**Example:**

```yml
  layers:
    - type: Socket              # search for matching layers of type `Socket`

    - type: Board               # search for matching layers of type `Board`
```

When combined with [`variables:`](#variables) it is possible to define the required `*.clayer.yml` files at the level of the `*.csolution.yml` file.  Refer to [`variables:`](#variables) for an example.
