---
id: "cmlek-target-configuration-reference-app"
type: "concept"
domain: "edge-ai"
title: "Target Configuration Reference Application Hardware"
summary: "This section explains how to use MLEK reference applications with the Arm CMSIS Solution extension for VS Code."
status: "draft"
collection: "cmsis-mlek-packs"
source: "Arm-Examples/cmsis-mlek@6d60f43:docs/target_configuration_refapp.md"
doc_source: "https://github.com/Arm-Examples/cmsis-mlek/blob/6d60f43/docs/target_configuration_refapp.md"
license: "Apache-2.0"
mode: "V"
---

<!-- markdownlint-disable MD013 -->
<!-- markdownlint-disable MD036 -->

### Using VS Code

This section explains how to use MLEK reference applications with the [Arm CMSIS Solution](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution) extension for VS Code.

#### Install Required Packs

Install the CMSIS-MLEK pack and any required board support packs:

```shell
cpackget add ARM::cmsis-mlek
```

#### Create New Solution

1. Open VS Code and use the **Create a new solution** dialog
2. Select one of the MLEK reference applications:

   - **MLEK Keyword Spotting and Audio User Algorithm Template**

   - **MLEK Object Detection and Video User Algorithm Template** 

   - **MLEK Generic Inference Runnner**. (available in pack version 1.0+)


(figure: Select MLEK Template)


3. Configure the target platform and toolchain:

(figure: Configure MLEK Solution)

#### Build and Run

Refer to the [Arm CMSIS CSolution extentions documentation](https://marketplace.visualstudio.com/items?itemName=Arm.cmsis-csolution#cmsis-view) on how to use the CMSIS View. It offers convenient and pre-configured access to build and debug features. 

### Enable Ethos-U NPU support for your target

To enable NPU support for custom hardware:

1. Open the `*.csolution.yml` file and look for the first `target-type`:

```yml
target-types:
  - type: MyCustomBoard
    device: STM32U585AIIx  # Your target MCU
    variables:
    ...
```
To the "type" entry add a suffix that identifies NPU model and MAC configuration. e.g.:
```yml
  - type: MyCustomBoard-U55-128 
  # or 
  - type: MyCustomBoard-U85-512
```
If you do not specify a MAC variant, 256 will be the default. 


This will configure the project to include the correct drivers and models for the NPU selected.
