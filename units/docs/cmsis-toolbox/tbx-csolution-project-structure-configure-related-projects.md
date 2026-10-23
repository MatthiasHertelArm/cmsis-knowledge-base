---
id: "tbx-csolution-project-structure-configure-related-projects"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Project Examples / Configure Related Projects"
summary: "A solution is the software view of the complete system. It combines projects that can be generated independently and therefore, manages related projects. It may also be deployed to different targets during development as described in section Software Layers."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#configure-related-projects"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Examples_

A solution is the software view of the complete system. It combines projects that can be generated independently and
therefore, manages related projects. It may also be deployed to different targets during development as described in section [Software Layers](#software-layers).

The picture below shows a system that is composed of:

- Project A that implements a time-critical control algorithm running on an independent processor #2.
- Project B is a cloud-connected IoT application with Machine Learning (ML) functionality.
- Project C is the separate data model of the ML algorithm, allowing independent updates.
- Project D implements the device security (for example, with TF-M that runs with TrustZone in secure mode).

In addition, such systems may have a boot-loader that can also be implemented as another independent project.

(figure: Related Projects of an Embedded System)

At the level of the `*.csolution.yml` file, the `target-types:` and `build-types:` are managed so that a common set is available across all `*.cproject.yml` files in the system.

- `target-types:` typically describe a different hardware target system.

- `build-types:` typically describe a build variant of the same hardware target system.

Both types are used for peripherals and the same hardware configuration but may compile a different variant (i.e. with test I/O enabled) of an application.

**Related Projects: `iot-product.csolution.yml`**

```yml
solution:
   :                            # setup not shown

  target-types:
    - type: Board
      board: NUCLEO-L552ZE-Q    # uses device defined by the board

    - type: Production-HW
      device: STM32U5X          # specifies device

  build-types:
    - type: Debug
      optimize: none
      debug: on

    - type: Release
      optimize: balanced
      debug: on

    - type: Test
      optimize: size
      debug: on

  projects:
    - project: ./security/TFM.cproject.yml           # Project D: Only generated for build type: Release
      for-context: .Release
    - project: ./application/MQTT_AWS.cproject.yml   # Project B
    - project: ./mldata/Model.cproject.yml           # Project C
    - project: ./bootloader/Bootloader.cproject.yml  # Not generated for target type: Board
      not-for-context: +Board
    - project: ./processor2/Control.cproject.yml     # Project A
```
