---
id: "alp-tflow-nn-stcube-run-nn-validate-the-nn-model"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Run the model on development board: Validate the NN model"
summary: "You will now validate the NN model built in the previous section on the desktop and the development board."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/run_nn.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/run_nn/#validate-the-nn-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

You will now validate the NN model built in the previous section on the desktop and the development board.

### Validate on desktop

1. On the STM32CubeAI menu, locate `X-CUBE-AI` configuration from the list of `Categories`.

2. click `Add network`. Browse to the generated model (`.h5` file). You can also specify other values, such as validation input, and validation output. Leave as default for now.

3. Click `Analyze`, then it will generate a detailed report on the model. You can check the number of parameters, the size of the weights, and the amount of memory to be used.

4. Click `Show graph` to visualize your model.

5. Click `Validate on Desktop` to validate the model with the provided input and output on your desktop.

### Validate on development board

To validate the model on the target, you need to first generate code and install the code on the target.

6. Click `Validate on target`, and enable `Automatic compilation and download`. Select the appropriate toolchain (`STM32CubeIDE`), and click `OK`.
