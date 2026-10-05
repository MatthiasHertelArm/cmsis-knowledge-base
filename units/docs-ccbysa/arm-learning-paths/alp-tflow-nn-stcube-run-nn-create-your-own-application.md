---
id: "alp-tflow-nn-stcube-run-nn-create-your-own-application"
type: "concept"
domain: "edge-ai"
title: "Build and run a letter recognition NN model on an STM32L4 Discovery board: Run the model on development board: Create your own application"
summary: "You can create your own application from the model you have trained."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/run_nn.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/tflow_nn_stcube/run_nn/#create-your-own-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can create your own application from the model you have trained.

1. Open the list of Software Packages. Change the device application as `Application`.

2. Click `Generate Code` then the project is updated.

3. Open `STM32CubeIDE`. Since you re-generated the code again, you need to delete the existing project and import the project again.

4. Open `X-CUBE-AI/App/app_x-cube-ai.c`. This is the auto-generated code by `STM32CubeMX`.

5. Between `USER_CODE_BEGIN` and `USER_CODE_END`, you can write code for your application.

There are two main functions that you should implement:
 * `acquire_and_process_data()` is for getting data from sensors and processing the data, for example, extracting features.
 * `postprocess()` is for postprocessing the output
