---
id: "tbx-create-applications-software-components"
type: "concept"
domain: "project"
title: "Create Applications: Software Components"
summary: "A software component encapsulates a set of related functions. Offering API headers provides interfaces to other software components or to the user application."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@6c04673:docs/CreateApplications.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/#software-components"
license: "Apache-2.0"
mode: "V"
---

A software component encapsulates a set of related functions. Offering API headers provides interfaces to other software components or to the user application.

The software pack provides for a software component other optional items such as configuration files, documentation, user code templates that show the usage of the software component, and a debug view description (for [CMSIS-View](https://arm-software.github.io/CMSIS-View/latest/index.html)). A software component typically interfaces to other software components or to device peripherals.

(figure: Software Component Overview)

In the CMSIS-Pack system software components:

- Are identified by the node [components:](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/YML-Input-Format.md#components) using a [component name](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/YML-Input-Format.md#component-name-conventions).
- Use dependencies to describe required interfaces.
- List API header files for provided interfaces.

For example, the lwIP network stack:

- requires a CMSIS-RTOS2 compliant kernel or a FreeRTOS kernel
- CMSIS drivers for the communication interface.
- List API header files for their interfaces.

### Required Interfaces

There are two ways to describe required interfaces, as shown in the diagram below.

- Dependency reference to a component (a selection list is supported).
- Dependency reference to an API definition. Components that implement this API fulfil then the required interface.

(figure: Software Component Stacking)

The API definition has the benefit that components which implement the interface can be added over time. The exact name of the component that requires an interface does not need to be known by the component.

ToDo: A potential improvement is to use the command `csolution list components` to show available implementations for a required interface.

### Using Components

The steps to create an application based on software components are:

1. Step: **Select software components**
    - Install the software pack that provides the required functionality (this could be based on pack datasheets) and identify the required software component(s).
    - Add the pack and the component to your `*.cproject.yml` file.
    - Run `csolution *.csolution.yml list dependencies` to identify other required software components.
    - Run `csolution list components --filter` to identify packs that provide these software components.
    - Repeat this step until all software components are part of your project.

2. Step: **Configure software components**
    - Run `csolution *.csolution.yml update-rte` to copy configuration files into the [RTE directory](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/./build-overview.md#rte-directory-structure).
    - Set the parameters in the configuration files for your application.

3. Step: **Use software components in application program**
    - User code templates provide a starting point for your application.
    - Copy these template files to your project directory and add them to your `*.cproject.yml` file.
    - Adjust the code in the user template files as required.

### Example: Network Stack

In this example, the application requires TCP Socket connectivity. The steps described under [Using Components](#using-components) deliver this content for the `*.cproject.yml` file.

```yml
  packs:
    - pack: Keil::MDK-Middleware@7.16.0
    - pack: ARM::CMSIS@5.9.0
    - pack: ARM::CMSIS-Driver@2.7.2
    - pack: Keil::LPC1700_DFP@2.7.1

  components:
    - component: Network&MDK-Pro Net_v6:Socket:TCP
    - component: Network&MDK-Pro Net_v6:CORE&Release
    - component: Network&MDK-Pro Net_v6:Interface:ETH
    - component: CMSIS:CORE
    - component: CMSIS:RTOS2:Keil RTX5&Source
    - component: CMSIS Driver:Ethernet:KSZ8851SNL
    - component: CMSIS Driver:SPI:SPI
    - component: Device:PIN
    - component: Device:GPIO
    - component: Device:Startup
```

The required interfaces are identified using `csolution list dependencies`:

(figure: Network Stack - Component View)

Adding more components, such as an IoT Client, would be the next step.

(figure: Network Stack - Class View)
