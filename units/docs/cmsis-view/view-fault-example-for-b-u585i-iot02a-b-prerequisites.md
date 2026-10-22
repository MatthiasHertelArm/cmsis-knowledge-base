---
id: "view-fault-example-for-b-u585i-iot02a-b-prerequisites"
type: "concept"
domain: "trace"
title: "Fault example for B-U585I-IOT02A board (Cortex-M33): Prerequisites"
summary: "This board has to be properly configured with TrustZone enabled. Please follow the steps below carefully:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Examples/Fault/B-U585I-IOT02A/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Examples/Fault/B-U585I-IOT02A/README.md#prerequisites"
license: "Apache-2.0"
mode: "V"
---

### Software

- [**Arm Keil Studio for VS Code**](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack)
- [**STM32CubeMX**](https://www.st.com/en/development-tools/stm32cubemx.html) **v6.12.1** or newer
- [**STM32CubeProgrammer**](https://www.st.com/en/development-tools/stm32cubeprog.html) utility
- [**Keil MDK**](https://developer.arm.com/Tools%20and%20Software/Keil%20MDK) **v5.41** or newer

### Hardware

This board has to be properly configured with **TrustZone** enabled. Please follow the steps below carefully:

Configure the following **Option bytes** with the **STM32CubeProgrammer** utility:

- **User Configuration**:
  - `TZEN`: checked
  - `DBANK`: checked
- **Boot Configuration**:
  - `SECBOOTADD0`:  Value = 0x1800 Address = 0x0c000000
- **Secure Area 1**:
  - `SECWM1_PSTRT`: Value = 0x0    Address = 0x08000000
  - `SECWM1_PEND`:  Value = 0x7f   Address = 0x080fe000
- **Write Protection 1**:
  - `WRP1A_PSTRT`:  Value = 0x7f   Address = 0x080fe000
  - `WRP1A_PEND`:   Value = 0x0    Address = 0x08000000
- **Secure Area 1**:
  - `SECWM2_PSTRT`: Value = 0x7f   Address = 0x08000000
  - `SECWM2_PEND`:  Value = 0x0    Address = 0x08100000
- **Write Protection 1**:
  - `WRP2A_PSTRT`:  Value = 0x7f   Address = 0x081fe000
  - `WRP2A_PEND`:   Value = 0x0    Address = 0x08100000
