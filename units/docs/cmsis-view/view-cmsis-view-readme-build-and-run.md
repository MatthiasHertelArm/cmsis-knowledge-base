---
id: "view-cmsis-view-readme-build-and-run"
type: "concept"
domain: "trace"
title: "cmsis-view README: Build and Run"
summary: "To try the example with the Arm Keil Studio, follow the steps below:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:Examples/EventStatistic/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/Examples/EventStatistic/README.md#build-and-run"
license: "Apache-2.0"
mode: "V"
---

To try the example with the **Arm Keil Studio**, follow the steps below:

 1. open the example in the **Visual Studio Code**.
 2. in the **Configure Solution** tab select the **AC6** compiler and click on the **OK** button.
 3. build the solution (in the **CMSIS** extension view click on the **Build solution** button).
 4. run the **FVP model** from the command line by executing the following command:
    ```shell
    FVP_Corstone_SSE-300 -f fvp_config.txt --simlimit=60 out/EventStatistic/AVH/Debug/EventStatistic.axf
    ```

    > **Note**  
    > **The Arm Virtual Hardware executable files have to be in the environment path**.  
    > You can install **Arm Virtual Hardware** via **Arm Keil Studio** by following these steps:
    > - click on the **Arm Tools**.
    > - select **Add Arm Tools Configuration to Workspace**.
    > - under **Arm Virtual Hardware for Cortex®-M based on Fast Models** select the latest available version.
    > - save the **vcpkg-configuration.json** file.

 5. wait for simulation to stop.
 6. the result of example running is an `EventRecorder.log` file that contains events that were generated during the code execution.
