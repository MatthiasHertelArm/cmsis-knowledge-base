---
id: "alp-tflow-nn-stcube-setup-set-up-development-board"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Prepare development environment: Set up development board"
summary: "Next, you need to program the STM32 B-L475E-IOT01A2 board to acquire accelerometer data for your neural network model."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/setup/#set-up-development-board"
license: "CC-BY-SA-4.0"
mode: "V"
---

Next, you need to program the STM32 `B-L475E-IOT01A2` board to acquire accelerometer data for your neural network model.

The data collection code for this Learning Path is provided, so you can import the project and program the board using [STM32CubeIDE](https://www.st.com/en/development-tools/stm32cubeide.html).

Download the [zip file](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/project_files/tf_stm32.zip) and extract it into a `tf_stm32` folder.

### Install STM32CubeIDE

Download and run the installer from the `Get Software` section of the [STMicroelectronics website](https://www.st.com/en/development-tools/stm32cubeide.html).

### Program the board 

Within `STM32CubeIDE` follow the steps below:

1. Select `Import project` and navigate to `General` > `Existing Projects into Workspace`.
2. Select the `MCU Dataset Creation` folder from the unzipped package as the root directory, and select `Dataset_Creation` project. Click `Finish` to import.
2. Connect board to host computer via USB. You may need to reset your board before you program the board. Click the black button on the board for the reset.
3. Right click the project and select `Run As`. The project will rebuild, and be flashed to the device. If prompted, accept any suggested firmware updates.
