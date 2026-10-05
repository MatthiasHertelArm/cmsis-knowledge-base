---
id: "alp-img-nn-stcube-run-nn-test-model"
type: "concept"
domain: "edge-ai"
title: "Build and run an image classification NN model on an STM32L4 Discovery board: Run the image classification NN model on STM32: Test model"
summary: "Navigate to the working folder, and then the Misc folder. Execute the tool with:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/img_nn_stcube/run_nn.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/img_nn_stcube/run_nn/#test-model"
license: "CC-BY-SA-4.0"
mode: "V"
---

Navigate to the working folder, and then the `Misc` folder. Execute the tool with:

```console
python ui_python_ai_runner.py
```
If the board is not detected, click the black button on the board to reset, then click on `Refresh NN and camera`.

**Troubleshooting:**
- The testing tool has been written with `X-CUBE-AI 7.0.0`. Later versions may not connect successfully.
- Ensure that the serial port, which uses the same interface, is not connected to terminal application.


Select the model network from the list of models deployed on the board.

(figure: output9)

Select the network and the label file (`Data/labels/cifar10_labels.txt`)

(figure: output10)

Open an image to test. The tool will automatically launch a new pane, and show the inference result.

Observe that the model correctly predicted the label. In addition, note the time taken to finish the prediction.

(figure: output11)

You can also use your workstation camera to test image classification. Hold an appropriate picture up to your camera, then press `S`. The tool captures the image and sends it to the board.

(figure: output12)

You have now successfully ran the model on your STM32 board.
