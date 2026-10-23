---
id: "view-fault-example-cortex-m7-build-and-run"
type: "concept"
domain: "trace"
title: "Fault example (Cortex-M7): Build and Run"
summary: "To try the example with the Arm Keil Studio, follow the steps below:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Examples/Fault/FVP_MPS2_Cortex-M7/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Examples/Fault/FVP_MPS2_Cortex-M7/README.md#build-and-run"
license: "Apache-2.0"
mode: "V"
---

To try the example with the **Arm Keil Studio**, follow the steps below:

 1. open the example in the **Visual Studio Code**.
 2. in the **Configure Solution** tab select the desired compiler (**AC6** or **GCC**), and click on the **OK** button.
 3. build the solution (in the **CMSIS** extension view click on the **Build solution** button).
 4. run the **FVP model** from the command line by executing the following command:
    - for **AC6**:
      ```shell
      FVP_MPS2_Cortex-M7 -f fvp_config.txt out/Fault/FVP_MPS2_Cortex-M7/Debug/Fault.axf
      ```
    - for **GCC**:
      ```shell
      FVP_MPS2_Cortex-M7 -f fvp_config.txt out/Fault/FVP_MPS2_Cortex-M7/Debug/Fault.elf
      ```

    > **Note**  
    > **The Arm Virtual Hardware executable files have to be in the environment path**.  
    > You can install **Arm Virtual Hardware** via **Arm Keil Studio** by following these steps:
    > - click on the **Arm Tools**.
    > - select **Add Arm Tools Configuration to Workspace**.
    > - under **Arm Virtual Hardware for Cortex®-M based on Fast Models** select the latest available version.
    > - save the **vcpkg-configuration.json** file.

 5. follow the instructions in the **simulator console**.
 6. the result of example running is an `EventRecorder.log` file that contains events that were generated during the code execution.
 7. view the events by using `eventlist` utility by executing the following command:
    ```shell
    eventlist -I %CMSIS_PACK_ROOT%/ARM/CMSIS-View/1.2.0/Fault/ARM_Fault.scvd -I %CMSIS_PACK_ROOT%/ARM/CMSIS-View/1.2.0/EventRecorder/EventRecorder.scvd -I %CMSIS_PACK_ROOT%/ARM/CMSIS-RTX/5.9.0/RTX5.scvd EventRecorder.log
    ```

    > **Note**  
    > If `CMSIS-View v1.2.0` or `CMSIS-RTX v5.9.0` packs are not installed, in the previous command replace the corresponding path with the path of the latest installed packs
    > (for example replace `%CMSIS_PACK_ROOT%/ARM/CMSIS-View/1.2.0/Fault/` with `%CMSIS_PACK_ROOT%/ARM/CMSIS-View/1.2.1/Fault/`)
