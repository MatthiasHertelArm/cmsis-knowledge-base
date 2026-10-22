---
id: "ethint-board-alifsemiconductor-appkit-e8-board-layer-for-m55-high-performance-cor"
type: "concept"
domain: "edge-ai"
title: "Board: AlifSemiconductor AppKit-E8-AIML: Board Layer for M55 High Performance Core"
summary: "This setup is configured using Conductor Tool, an interactive tool provided by Alif Semiconductor for device configuration. Refer to \"Alif Conductor Tool Manual\" for additional information."
status: "draft"
collection: "cmsis-ethos-integration"
source: "Arm-Examples/CMSIS-Ethos-Integration@9b906f5:Board/AppKit-E8_M55_HP/README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Ethos-Integration/blob/9b906f5/Board/AppKit-E8_M55_HP/README.md#board-layer-for-m55-high-performance-core"
license: "Apache-2.0"
mode: "V"
---

Device: AE822FA0E5597BS0:M55_HP

This setup is configured using **Conductor Tool**, an interactive tool provided by Alif Semiconductor for device configuration.
Refer to ["Alif Conductor Tool Manual"](https://conductor.alifsemi.com/Alif_HTML_DCT_User_Help/Content/Help%20Manual.htm) for additional information.

### System Configuration

| System Component        | Setting
|:------------------------|:----------------------------------------
| Heap                    | 96 kB (configured in M55_HP linker file)
| Stack (MSP)             |  8 kB (configured in M55_HP linker file)

### STDIO mapping

**STDIO** is routed to Virtual COM port via **UART4** peripheral

> Note:
> For STDOUT (printf output) configure SW4 to position U4 (UART4)

### CMSIS-Driver mapping

| CMSIS-Driver           | Peripheral | Board connector/component    | Connection
|:-----------------------|:-----------|:-----------------------------|:----------------------
| Driver_ETH_MAC0        | ETH        | Ethernet RJ45 connector (J4) | CMSIS_ETH
| Driver_USART4          | UART4      | PRG USB connector (J3)       | STDIN, STDOUT, STDERR
| Driver_USBD0           | USB        | MCU USB connector (J2)       | CMSIS_USB_Device
| CMSIS-Driver VIO       | GPIO       | RGB LED, Joystick            | CMSIS_VIO
| Driver_vStreamVideoIn  | MIPI CSI   | MIPI Camera (J9)             | CMSIS_VSTREAM_VIDEO_IN
| Driver_vStreamVideoOut | MIPI DSI   | GLCD Display (J15)           | CMSIS_VSTREAM_VIDEO_OUT

### CMSIS-Driver Virtual I/O mapping

| CMSIS-Driver VIO | Board component
|:-----------------|:----------------------------
|vioBUTTON0        | Joystick Select Button
|vioJOYup          | Joystick Up
|vioJOYdown        | Joystick Down
|vioJOYleft        | Joystick Left
|vioJOYright       | Joystick Right
|vioJOYselect      | Joystick Select Button
|vioLED0           | RGB LED Red
|vioLED1           | RGB LED Green
|vioLED2           | RGB LED Blue

### CMSIS-Driver vStream configuration

| Driver                 | Stream Format Description
|:-----------------------|:----------------------------------------------------
| Driver_vStreamVideoIn  | RAW10 Bayer GRBG video, resolution 1280 x 720 (W x H)
| Driver_vStreamVideoOut | RGB888 video,           resolution  480 x 800 (W x H)
