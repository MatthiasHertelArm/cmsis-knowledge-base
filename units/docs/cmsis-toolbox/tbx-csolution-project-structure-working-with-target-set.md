---
id: "tbx-csolution-project-structure-working-with-target-set"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Project Examples / Working with target-set"
summary: "A target-set: specifies the context types and additional images that are combined into an application. The following example defines the Run and Debug configurations for the iot-product.csolution.yml application that is shown above using the target-set: node."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#working-with-target-set"
license: "Apache-2.0"
mode: "V"
---

_Part of: Project Examples_

A [`target-set:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#target-set) specifies the [context](#context) types and additional [images](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#images) that are combined into an application. The following example defines the [Run and Debug configurations](#run-and-debug-configuration) for the `iot-product.csolution.yml` application that is shown above using the [`target-set:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#target-set) node.

!!! Note
    [Run and Debug Configuration](#run-and-debug-configuration) shows how a  [`debugger:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#debugger) is specified for a build variant that is defined with [`target-set:`](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/YML-Input-Format.md#target-set).

```yml
solution:
   :                            # setup not shown

  target-types:
    - type: Board
      board: NUCLEO-L552ZE-Q    # uses device defined by the board
      target-set:
        - set:                  # default set for this target
          images:
            - project-context: MQTT_AWS.Debug
            - project-context: Control.Debug
        
    - type: Production-HW
      device: STM32U5X          # specifies device
        - set:                  # default set for this target
          images:               # all projects as release version
            - project-context: Bootloader.Release
            - project-context: TFM.Release
            - project-context: MQTT_AWS.Release
            - project-context: Model.Release
            - project-context: Control.Release
        - set: Debug            # alternative set for debugging on Production-HW
          images:               # projects and images required for debugging
            - image: Bootloader_Dummy.hex           # use an dummy image
            - project-context: TFM.Release
            - project-context: MQTT_AWS.Debug       # load debug build
            - image: Model_Test.hex                 # use a test Model
```

Using the [Build Tools](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/build-tools.md) option `--active` (or `-a`) generates the different build variants:

```bash
cbuild iot-product.csolution.yml -a Board                   # target-type Board with default set
cbuild iot-product.csolution.yml -a Production-HW           # target-type Production-HW with default set
cbuild iot-product.csolution.yml -a Production-HW@Debug     # target-type Production-HW with Debug set
```

When `--active <target-type>` omits the target-set name, the unnamed target-set is selected when available; otherwise, the first named target-set is used. If the selected target-set has no `project-context` entries, or the target type defines no `target-set`, the default context is the first project with the first build type and the selected target type. Specifying `--active <target-type>@<target-set>` selects that set explicitly and uses the same default-context rule when it has no `project-context` entries. An empty selection (`--active ""`) uses the first target type and its first target-set, if present, with the same fallback to the default context.

#### Load Attributes

Load attributes are typically used when testing a bootloader or a bank-swapping mechanism. In such cases, often only symbol information is required. Using `load-offset:` (supported by pyOCD) allows loading the content of a binary image at a different physical address.

The example [STM32_LiveUpdate](https://github.com/Arm-Examples/STM32_LiveUpdate) uses swappable Flash banks to switch to a new firmware version that is initially programmed into the inactive Flash bank. The binary image of the new firmware version uses `load-offset:` (pyOCD only). The ELF symbol information is loaded separately without the offset so that the symbolic information is available for debugging.

```yml
solution:
  compiler: AC6
  target-types:
    - type: Version_1
      device: STM32L476RGTx
      target-set:
        - set:
          images:
            - image: $bin(test_v1)$       # binary file of project test_v1
              load: image
              load-offset: 0x08080000     # load with an offset into Flash
            - project-context: test_v1    # load from project test_v1
              load: symbols               # load only symbol information
          debugger:
            name: ST-Link@pyOCD
            port: 3333
            protocol: swd
            clock: 4000000
  projects:
    - project: test_v1.cproject.yml
```
