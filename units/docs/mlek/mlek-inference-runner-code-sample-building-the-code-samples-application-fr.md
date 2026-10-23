---
id: "mlek-inference-runner-code-sample-building-the-code-samples-application-fr"
type: "concept"
domain: "edge-ai"
title: "Inference Runner Code Sample: Building the Code Samples application from sources"
summary: "In addition to the already specified build option in the main documentation, the Inference Runner use-case adds the following:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/inference_runner.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/inference_runner.md#building-the-code-samples-application-from-sources"
license: "Apache-2.0"
mode: "V"
---

### Build options

In addition to the already specified build option in the main documentation, the Inference Runner use-case adds the
following:

- `inference_runner_MODEL_PATH` - The path to the NN model file in the `TFLite` format. The model is then
  processed and included in the application `axf` file. The default value points to one of the delivered set of models.

  Note that the parameters `TARGET_PLATFORM` and `ETHOS_U_NPU_ENABLED` must be aligned with the chosen model. In other
  words:

  - If `ETHOS_U_NPU_ENABLED` is set to `On` or `1`, then the NN model is assumed to be optimized. The model naturally
    falls back to the Arm® *Cortex®-M* CPU if an unoptimized model is supplied.
  - if `ETHOS_U_NPU_ENABLED` is set to `Off` or `0`, the NN model is assumed to be unoptimized. Supplying an optimized
    model in this case results in a runtime error.

- `inference_runner_ACTIVATION_BUF_SZ`: The intermediate, or activation, buffer size reserved for the NN model. By
  default, it is set to 2MiB and is enough for most models.

- `inference_runner_DYNAMIC_MEM_LOAD_ENABLED`: This can be set to ON or OFF, to allow dynamic model load capability for use with MPS3 FVPs. See section [Building with dynamic model load capability](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./inference_runner.md#building-with-dynamic-model-load-capability) below for more details.

To build **ONLY** the Inference Runner example application, add `-DUSE_CASE_BUILD=inference_runner` to the `cmake`
command line, as specified in: [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#Building).

### Build process

> **Note:** This section describes the process for configuring the build for the *MPS3: SSE-300*. To build for a
> different target platform, please refer to: [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#Building).

Create a build directory and navigate inside, like so:

```commandline
mkdir build_inference_runner && cd build_inference_runner
```

On Linux, when providing only the mandatory arguments for the CMake configuration, execute the following command to
build **only** Image Classification application to run on the *Ethos-U55* Fast Model:

```commandline
cmake ../ -DUSE_CASE_BUILD=inference_runner
```

To configure a build that can be debugged using Arm DS specify the build type as `Debug` and then use the `Arm Compiler`
toolchain file:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake \
    -DCMAKE_BUILD_TYPE=Debug \
    -DUSE_CASE_BUILD=inference_runner
```

For further information, please refer to:

- [Configuring with custom TPIP dependencies](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../sections/building.md#configuring-with-custom-tpip-dependencies)
- [Using Arm Compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../sections/building.md#using-arm-compiler)
- [Building for different Ethos-U NPU variants](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../sections/building.md#building-for-different-ethos_u-npu-variants)

> **Note:** If re-building with changed parameters values, we recommend that you clean the build directory and re-run
> the CMake command.

If the CMake command succeeds, build the application as follows:

```commandline
make -j4
```

To see compilation and link details, add `VERBOSE=1`.

Results of the build are placed under the `build/bin` folder, like so:

```tree
bin
 ├── mlek_inference_runner.axf
 ├── mlek_inference_runner.htm
 ├── mlek_inference_runner.map
 └── sectors
      └── inference_runner
        ├── ddr.bin
        └── itcm.bin
```

The `bin` folder contains the following files:

- `mlek_inference_runner.axf`: The built application binary for the Inference Runner use-case.

- `mlek_inference_runner.map`: Information from building the application. For example: The libraries used, what was
  optimized, and the location of objects.

- `mlek_inference_runner.htm`: Human readable file containing the call graph of application functions.

- `sectors/inference_runner`: Folder containing the built application. It is split into files for loading into different FPGA memory
  regions.

- `sectors/images.txt`: Tells the FPGA which memory regions to use for loading the binaries in the `sectors/..`
  folder.

### Add custom model

The application performs inference using the model pointed to by the CMake parameter
`inference_runner_MODEL_PATH`.

> **Note:** If you want to run the model using an *Ethos-U*, ensure that your custom model has been successfully run
> through the Vela compiler *before* continuing.

For further information: [Optimize model with Vela compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../sections/building.md#Optimize-custom-model-with-Vela-compiler).

Then, you must set `inference_runner_MODEL_PATH` to the location of the Vela processed model file.

An example:

```commandline
cmake .. \
  -Dinference_runner_MODEL_PATH=<path/to/custom_model_after_vela.tflite> \
  -DUSE_CASE_BUILD=inference_runner
```

> **Note:** Clean the build directory before re-running the CMake command.

The `.tflite` model file pointed to by `inference_runner_MODEL_PATH` is converted to C++ files during the CMake
configuration stage. It is then compiled into the application for performing inference with.

The log from the configuration stage tells you what model path and labels file have been used, for example:

```stdout
-- User option inference_runner_MODEL_PATH is set to <path/to/custom_model_after_vela.tflite>
...
-- Using <path/to/custom_model_after_vela.tflite>
++ Converting custom_model_after_vela.tflite to\
custom_model_after_vela.tflite.cc
...
```

After compiling, your custom model has now replaced the default one in the application.
