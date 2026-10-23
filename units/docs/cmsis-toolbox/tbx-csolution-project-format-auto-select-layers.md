---
id: "tbx-csolution-project-format-auto-select-layers"
type: "concept"
domain: "project"
title: "CSolution Project Format: Auto-select Layers"
summary: "To find compatible layers in software packs, projects and layers can be annotated. The command csolution list layers lists compatible layers. This enables reference applications that work across a range of different hardware targets where:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/YML-Input-Format.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/#auto-select-layers"
license: "Apache-2.0"
mode: "V"
---

To find compatible layers in software packs, projects and layers can be annotated. The command `csolution list layers` lists compatible layers. This enables [reference applications](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/ReferenceApplications.md) that work across a range of different hardware targets where:

- The `*.cproject.yml` file of the reference application lists with the `connections:` node the required functionality with `consumes:`.

- The `*.clayer.yml` project part lists with the `connections:` node the implemented functionality with `provides:`.

Example projects that use `connections:` for layer selection:

- [MDK-Middleware examples](https://arm-software.github.io/MDK-Middleware/latest/General/working_with_examples.html) use board layers to run on different hardware boards.

- [Sensor SDK Example](https://github.com/Open-CMSIS-Pack/Sensor-SDK-Example) shows how board layers and shield layers may be used to run different sensor shields on many boards.

- [AWS_MQTT_Demo](https://github.com/Arm-Examples/AWS_MQTT_Demo) combines the board layer and communication socket layer. Optionally a shield layer can be used to connect WiFi drivers.

### `connections:`

The `connections:` node contains meta-data that describes the compatibility of the `*.cproject.yml` and `*.clayer.yml` project parts.  The `connections:` node lists functionality (drivers, pins, and other software or hardware resources). The node `consumes:` lists required functionality; the node `provides:` is the implemented functionality of that project part.

This works across multiple levels, which means that a `*.clayer.yml` file could also require other functionality using `consumes:`.

The `connections:` node is used to identify compatible software layers. These software layers could be stored in CMSIS software packs using the following structure:

- A reference application described in a `*.cproject.yml` file could be provided in a git repository. This reference application uses software layers that are provided in CMSIS software packs.

A CMSIS Board Support Pack (BSP) contains a configured board layer described in a `*.clayer.yml` file. This software layer is pre-configured for a range of use cases and provides drivers for I2C and SPI interfaces, along with pin definitions and provisions for an Arduino shield.

- For a sensor, a CMSIS software pack contains the sensor middleware and software layer (`*.clayer.yml`) that describes the hardware of the Arduino sensor shield. This shield can be applied to many different hardware boards that provide an Arduino shield connector.

This `connections:` node enables therefore software reuse in multiple ways:

- The board layer can be used by many different reference applications, as the `provided:` functionality enables a wide range of use cases.

The sensor hardware shield and middleware can be used across many different boards that provide an Ardunio shield connector and board layer support.

The structure of the `connections:` node is:

`connections:`                       |              | Description
:------------------------------------|:-------------|:------------------------------------
[- `connect:`](#connect)             | **Required** | Lists specific functionality with a brief verbal description

#### `connect:`

The `connect:` node describes one or more functionalities that belong together.

`connect:`                           |              | Description
:------------------------------------|:-------------|:------------------------------------
[`set:`](#set)                       |   Optional   | Specifies a *config-id*.*select* value that identifies a configuration option
`info:`                              |   Optional   | Verbal description displayed when this connect is selected
[`provides:`](#provides)             |   Optional   | List of functionality (*key*/*value* pairs) that are provided
[`consumes:`](#consumes)             |   Optional   | List of functionality (*key*/*value* pairs) that are required

The behavior of the `connect:` node depends on the usage in *csolution project* files.

- In a `cproject.yml` file the `connect:` node is always active.
- In a `clayer.yml` file the `connect:` node is only active if one or more `key` listed under `provides:` is listed under `consumes:` in other active `connect:` nodes. It is also active by default if the `connect:` node has no `provides:` node.

**Example:**

In the example below the `connect` for:

- `Sensor Communication Interface` is only active when the `SENSOR_I2C` is in the `consumes:` list of other active `connect` nodes.
- `Sensor Interrupt` is only active when the `SENSOR_INT` is in the `consumes:` list of other active `connect` nodes.
- `Core Functionality` is always active as it does not have a `provides:` list.

```yml
layer:
  type: Shield

  connections:
    - connect: Sensor Communication Interface
      provides:
        - SENSOR_I2C
      consumes:
        - ARDUINO_UNO_I2C
    - connect: Sensor Interrupt
      provides:
        - SENSOR_INT
      consumes:
        - ARDUINO_UNO_D2
    - connect: Core Functionality
      consumes:
        - CMSIS-RTOS2
```

#### `set:`

Some hardware boards have configuration settings (DIP switch or jumper) that configure interfaces. These settings have an impact on the functionality (for example, hardware interfaces). With `set:` *config-id*.*select*, the possible configuration options are considered when evaluating compatible `*.cproject.yml` and `*.clayer.yml` project parts. The **`csolution` Project Manager** iterates the `connect:` node with a `set:` *config-id*.*select* as described below:

- For each *config-id* only one `connect:` node with a *select* value is active at a time. Each possible *select* value is checked for a matching configuration.

- When project parts have a matching configuration, the `set:` value along with the `info:` is shown to the user. This allows the user to enable the correct hardware options.

Refer to [Example: Sensor Shield](#example-sensor-shield) for a usage example.

#### `provides:`

A user-defined *key*/*value* pair list of functionality that is implemented or provided by a `project:` or `layer:`.

The **`csolution` Project Manager** combines all the *key*/*value* pairs that are listed under `provides:` and matches them with the *key*/*value* pairs that are listed under `consumes:`. For *key*/*value* pairs listed under `provides:` the following rules exist for a match with `consumes:` *key*/*value* pair:

- It is possible to omit the *value*. It matches with an identical *key* listed in `consumes:`
- A *value* is interpreted as a number. Depending on the value prefix, this number must be:
    - when `consumes:` *value* is a plain number identical to this value.
    - when `consumes:` *value* is prefixed with `+`, higher or equal then this *value* or the sum of all *values* in multiple `consumes:` nodes.

#### `consumes:`

A user-defined *key*/*value* pair list of functionality that is required or consumed by a `project:` or `layer:`.

For *key*/*value* pairs listed under `consumed:` the following rules exist:

- When no *value* is specified, it matches with any *value* of an identical *key* listed under `provides:`.
- A *value* is interpreted as a number. This number must be identical in the `provides:` value pair.
- A *value* that is prefixed with `+` is interpreted as a number that is added together in case that the same *key* is listed multiple times under `consumes:`. The sum of this value must be lower or equal to the *value* upper limit of the `provides:` *key*.

### Example: Board

This `connections:` node of a board layer describes the available interfaces.  The WiFi interface requires a CMSIS-RTOS2 function.

```yml
  connections:                          # describes the functionality of a board layer
    - connect: WiFi interface
      provides:
        - CMSIS-Driver WiFi:
      requires:
        - CMSIS-RTOS2:

    - connect: SPI and UART interface
      provides:
        - CMSIS-Driver SPI:
        - CMSIS-Driver UART:
```

### Example: Simple Project

This shows the `connections:` node of a complete application project composed of two software layers.

*MyProject.cproject.yml*

```yml
  connections:
    - connect: all resources
      provides:
        - RTOS2:          # implements RTOS2 API interface
      consumes:
        - IoT_Socket:     # requires IoT_Socket interface
        - STDOUT:         # requires STDOUT interface
        - Heap:  +30000   # requires an additional 30000 bytes memory heap
  :
  layers:
    - layer: MySocket.clayer.yml
    - layer: MyBoard.clayer.yml
```

*MySocket.clayer.yml*

```yml
  connections:
    - connect:
      consumes:
        - RTOS2:          # requires RTOS2 API interface
        - VSocket:        # requires VSocket interface
        - Heap: +20000    # requires an additional 20000 bytes memory heap
      provides:
        - IoT_Socket:     # provides IoT_Socket interface
```

*MyBoard.clayer.yml*

```yml
  connections:
    - connect:
      consumes:
        - RTOS2:
      provides:
        - VSocket:
        - STDOUT:
        - Heap:  65536
```

### Example: Sensor Shield

This sensor shield layer provides a set of interfaces that are configurable.

```yml
  connections:
    - connect: I2C Interface 'Std'
      set:  comm.I2C-Std
      info: JP1=Off  JP2=Off
      provides:
        - Sensor_I2C:
      consumes:
        - Ardunio_Uno_I2C:

    - connect: I2C Interface 'Alt'
      set:  comm.I2C-Alt
      info: JP1=On  JP2=Off
      provides:
        - Sensor_I2C:
      consumes:
        - Ardunio_Uno_I2C-Alt:

    - connect: SPI Interface 'Alt'
      set:  comm.SPI
      info: JP2=On
      provides:
        - Sensor_SPI:
      consumes:
        - Ardunio_Uno_SPI:

    - connect: Sensor Interrupt INT0
      set:  SensorIRQ.0
      info: JP3=Off
      provides:
        - Sensor_IRQ:
      consumes:
        - Ardunio_Uno_D2:

    - connect: Sensor Interrupt INT1
      set:  SensorIRQ.1
      info: JP3=On
      provides:
        - Sensor_IRQ:
      consumes:
        - Ardunio_Uno_D3:
```
