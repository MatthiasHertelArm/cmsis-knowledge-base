---
id: "alp-tflow-nn-stcube-run-nn-demo-with-the-sample-applicati"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Run the model on development board: Demo with the sample application"
summary: "A sample application is provided. This uses a feature-based model, trained with the letters O and S written in a horizontal plane."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/run_nn.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/run_nn/#demo-with-the-sample-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

A sample application is provided. This uses a feature-based model, trained with the letters `O` and `S` written in a horizontal plane.

**Notice:**
There is a bug in the example as supplied. You must edit `/Core/Src/main.c` before building.

Locate the function call in `main()` to
* `MX_USART1_UART_Init()`

and move to before the call to
* `MX_X_CUBE_AI_Init()`


1. Using a terminal application (such as `PuTTY`), set up the serial connection to the board. `COM` number will be as before. The baud rate should be 115200.

2. Import the application. Click the File tab and click `Import`. Select `Existing project into workspace`. Go to `tf_stm32` folder and select `MCU_Activity_Recognition`.

3. Open `X-CUBE-AI/App/app_x-cube-ai.c`. Observe that functions are provided for data acquisition from the accelerometer sensor and feature extraction.

4. Build application and flash to target with `Run As`.

5. Observe output on the terminal.

6. Press the blue button on the board, draw a letter, then press the button again.
