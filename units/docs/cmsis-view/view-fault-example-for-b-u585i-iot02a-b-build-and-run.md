---
id: "view-fault-example-for-b-u585i-iot02a-b-build-and-run"
type: "concept"
domain: "trace"
title: "Fault example for B-U585I-IOT02A board (Cortex-M33): Build and Run"
summary: "To try the example with the Arm Keil Studio, follow the steps below:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Examples/Fault/B-U585I-IOT02A/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Examples/Fault/B-U585I-IOT02A/README.md#build-and-run"
license: "Apache-2.0"
mode: "V"
---

### Arm Keil Studio

To try the example with the **Arm Keil Studio**, follow the steps below:

 1. open the example in the **Visual Studio Code**.
 2. in the **Configure Solution** tab select the **AC6** compiler and click on the **OK** button.

    > **Note**  
    > To use **GCC** instead of AC6 compiler do the following:
    > - in the **Fault.csolution.yml** csolution file replace `compiler: AC6` with `compiler: GCC`.
    > - launch the **STM32CubeMX generator**: in the **CMSIS** extension project view click on the **Run Generator** button for **Device:CubeMX** component.
    > - in the **STM32CubeMX**: open from the menu **Project Manager - Project - Toolchain/IDE**,
    >   select **STM32CubeIDE** and clear **Generate Under Root** check box, and click on the **GENERATE CODE** button.

 3. build the solution (in the **CMSIS** extension view click on the **Build solution** button).
 4. download the built applications (Fault_S/Fault_NS) to the MCU's Flash (in the **CMSIS** extension view click on the **Run** button).  

    > **Note**  
    > In case of issues with download you can use **STM32CubeProgrammer** or **uVision**.  
    > Procedure using **uVision**: open **Fault.csolution.yml** in the **uVision**, click on the **Rebuild** button,
    > in **Options for Target** dialog under **Debug** select **ST-Link Debugger** and click on the **OK** button; now click on the **Download** button.

 5. open the **Serial Terminal** application and connect to the **STMicroelectronics STLink Virtual COM Port (COMx)** (115200-8-N-1).
 6. press the **RESET** button on the board.
 7. follow the instructions in the **Serial Terminal** and observe the results.

### uVision

To try the example with the **uVision**, follow the steps below:

 1. open the example in the **uVision**.
 2. build the projects (select **Project - Batch Build**).
 3. download the built applications (Fault_S/Fault_NS) to the MCU's Flash (click on the **Download** button).
 4. open the **Serial Terminal** application and connect to the **STMicroelectronics STLink Virtual COM Port (COMx)** (115200-8-N-1).
 5. press the **RESET** button on the board.
 6. follow the instructions in the **Serial Terminal** and observe the results.

> **Note**  
> In the debug session fault information can be inspected in the **Component View** and **Event Recorder** windows.
