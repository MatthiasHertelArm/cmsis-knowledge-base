---
id: "czep-zephyr-integration-with-cmsis-tool-add-another-board"
type: "concept"
domain: "project"
title: "Zephyr Integration with CMSIS-Toolbox: Add another board"
summary: "If you use a different board, extend the zephyr.csolution.yml file with:"
status: "draft"
collection: "cmsis-zephyr"
source: "Arm-Examples/CMSIS-Zephyr@ef8713c:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/README.md#add-another-board"
license: "Apache-2.0"
mode: "V"
---

If you use a different board, extend the [`zephyr.csolution.yml`](https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/zephyr.csolution.yml) file with:

```yml
  # List the packs that define the device and/or board.
  packs:
    - pack: Vendor::DFP
    - pack: Vendor::BSP

  # List different hardware targets that are used to deploy the solution.
  target-types:
    - type: SpecifyName
      board: Vendor::Board_name      # Vendor is optional
      device: Vendor::Device_name    # Vendor and device name are optional
```

To find the packs, open [https://www.keil.arm.com/boards/](https://www.keil.arm.com/boards/) and search for your board.

- `pack: Vendor::BSP` is listed under CMSIS Pack on the [Board](https://www.keil.arm.com/boards/) page.
- `pack: Vendor::DFP` is listed under CMSIS Pack on the related [Device](https://www.keil.arm.com/devices/) page.

### Board name different in Zephyr and CMSIS Pack

Frequently the [Zephyr board name](https://docs.zephyrproject.org/latest/boards/index.html#) does not match. In this case add the variable `west-board:` as shown below.

Use [Zephyr - Supported Boards and Shields](https://docs.zephyrproject.org/latest/boards/index) and find your board. Under **Supported Features** the `board_name`, `board_name/soc_name` or `board_name/soc_name/core_name` is listed; this is what you specify with `west-board:`.

```yml
  target-types:
    - type: B-L475-IOT01A
      board: STMicroelectronics::B-L475E-IOT01A
      device: STMicroelectronics::STM32L475VGTx
      variables:
        - west-board: disco_l475_iot1/stm32l475xx
```
