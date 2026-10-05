---
id: "alp-observing-ethos-u-on-alif-6-alif-cmsis-project-add-the-source-files"
type: "concept"
domain: "edge-ai"
title: "6 alif cmsis project: Add the source files"
summary: "The application code is split across three files:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/6-alif-cmsis-project/#add-the-source-files"
license: "CC-BY-SA-4.0"
mode: "V"
---

The application code is split across three files:

- `main.cpp` is the firmware entry point. It initializes the board, loads the embedded model from `mnist_model_data.h`, passes the MNIST input image to the runner, and prints the predicted digit and output scores.
- `executorch_runner.h` declares the small C-style interface used by `main.cpp` to initialize ExecuTorch and run inference.
- `executorch_runner.cpp` implements the ExecuTorch integration. It initializes the Ethos-U NPU driver and loads the `.pte` program. It also prepares input and output tensors, allocates runtime buffers, and executes the model.

Run these commands to download the source files and place them in `mnist_executorch/`:

```bash
cd ~/mnist_alif/alif_vscode-template/mnist_executorch
curl -o main.cpp https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/refs/heads/main/mnist_executorch/main.cpp
curl -o executorch_runner.cpp  https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/refs/heads/main/mnist_executorch/executorch_runner.cpp
curl -o executorch_runner.h https://raw.githubusercontent.com/arm-education/alif-ethos-u85-npu-mnist/refs/heads/main/mnist_executorch/executorch_runner.h
```
After downloading the files, open them in VS Code. Briefly review how `main.cpp` calls into `executorch_runner.cpp` to initialize ExecuTorch, pass in the MNIST input tensor, and read back the model output.
