---
id: "alp-tflow-nn-stcube-run-nn-setup-stm32cubemx-project"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Run the model on development board: Setup STM32CubeMX project"
summary: "STM32CubeMX is a graphical tool for configuring STM32 microcontrollers.\\ STM32Cube.AI is an extension of STM32CubeMX to import ML models."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/run_nn.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/run_nn/#setup-stm32cubemx-project"
license: "CC-BY-SA-4.0"
mode: "V"
---

[STM32CubeMX](https://www.st.com/en/development-tools/stm32cubemx.html) is a graphical tool for configuring STM32 microcontrollers.\
[STM32Cube.AI](https://www.st.com/content/st_com/en/campaigns/stm32cube-ai.html) is an extension of STM32CubeMX to import ML models.

1. Download and install STM32CubeMX from the [STM32CubeMX product page](https://www.st.com/en/development-tools/stm32cubemx.html).

2. Open STM32CubeMX IDE.

3. Click `Access to Board Selector`. Find your `B-L475E-IOT01A` board and click `Start Project`.

4. Go to `Project Manager`. Enter a project name and select the project location where the project will be saved.

5. Under `Pinout & Configuration`, expand `Pinout` menu, and click `Clear pinouts`.

6. Expand `Software Packs` menu, and click `Select Components`.

7. Locate `X-CUBE-AI`, and click its `Install` button.

8. Expand the menu and enable `X-CUBE-AI` > `Core`. For device application, choose `Validation`. If the status shows a yellow warning, click `Resolve` to install any necessary dependencies.

9. Click `OK` when done.
