---
id: "alp-img-nn-stcube-deploy-nn-deploy-the-model-with-stm32cub"
type: "concept"
domain: "edge-ai"
title: "Build and run an image classification NN model on an STM32L4 Discovery board: Deploy the image classification NN model on STM32: Deploy the model with STM32Cube"
summary: "3. Find the B-L475E-IOT01A2 board and click Start Project. Accept any defaults."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/img_nn_stcube/deploy_nn.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/img_nn_stcube/deploy_nn/#deploy-the-model-with-stm32cubemx"
license: "CC-BY-SA-4.0"
mode: "V"
---

1. Open STM32CubeMX.

2. Click `Access to Board Selector`.

3. Find the `B-L475E-IOT01A2` board and click `Start Project`. Accept any defaults.

4. Go to `Project Manager`. Set the project name and save location.

5. Set `Toolchain/IDE` as `STM32CubeIDE`

(figure: output3)

6. Go to `Pinout & Configuration` and clear pinouts from the `Pinout` menu.

(figure: output4)

7. In `Software Packs` menu, click `Select Components`. Enable `X-CUBE-AI`. For device application, choose `Validation`. Click `OK` to save.

(figure: output5)

8. Navigate to `X-CUBE-AI` configuration.

9. Click `Add network`. Browse to the model provided (`Data/models/cifar10_model.h5`) or the model you trained by yourself (`Data/models/own_cifar10_model.h5`).

10. Click `Analyze` to check the model.

11. Generate the validation code for the model by clicking `Generate Code`.

(figure: output6)

12. Open STM32CubeIDE.

13. Navigate to `File` > `New` > `Project` > `ST` > `STM32 Project from an Existing STM32CubeMX Configuration File`.

14. Go to the project folder and open the `.ioc` file.

15. Ensure that the board is connected to your computer. If it is correctly connected, build and flash the code by clicking `Run As`.

(figure: output7)

16. If you get an ‘undefined reference’ error, go to `Core/Src/main.c`. Remove `static` from the declaration of the `MX_USART1_UART_Init()` function and also from its definition. Try `Run As` again.

(figure: output8)

With the model now deployed on the STM32 board, you are ready to test it.
