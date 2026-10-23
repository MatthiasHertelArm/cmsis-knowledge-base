---
id: "mlek-noise-reduction-code-sample-building-the-code-sample-application-fro"
type: "concept"
domain: "edge-ai"
title: "Noise Reduction Code Sample: Building the code sample application from sources"
summary: "In addition to the already specified build option in the main documentation, keyword spotting use case adds:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/noise_reduction.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/noise_reduction.md#building-the-code-sample-application-from-sources"
license: "Apache-2.0"
mode: "V"
---

### Build options

In addition to the already specified build option in the main documentation, keyword spotting use
case adds:

- `noise_reduction_MODEL_PATH` - The path to the NN model file in *TFLite* format. The model
  is processed and is included in the application axf file. The default value points to one of the
  delivered set of models. Note that the parameter
  `ETHOS_U_NPU_ENABLED` must be aligned with the chosen model. Therefore:
  - if `ETHOS_U_NPU_ENABLED` is set to `On` or `1`, we assume that the NN model is optimized. The
    model naturally falls back to the Arm® Cortex®-M CPU if an unoptimized model is supplied.
  - if `ETHOS_U_NPU_ENABLED` is set to `Off` or `0`, then we assume that the NN model is unoptimized.
    In this case, supplying an optimized model results in a runtime error.

- `noise_reduction_FILE_PATH`: The path to the directory containing WAV files, or a path to single
  WAV file, to be used in the application. The default value points to the
  `resources/noise_reduction/samples` folder containing the delivered set of audio clips.

- `noise_reduction_AUDIO_RATE`: The input data sampling rate. Each audio file from `noise_reduction_FILE_PATH` is
  preprocessed during the build to match the NN model input requirements. The default value is `48000`.

- `noise_reduction_AUDIO_MONO`: If set to `ON`, then the audio data is converted to mono. The default value is `ON`.

- `noise_reduction_AUDIO_OFFSET`: Begins loading audio data and starts from this specified offset, defined in seconds.
  The default value is set to `0`.

- `noise_reduction_AUDIO_DURATION`: The length of the audio data to be used in the application in seconds.
  The default is `0`, meaning that the whole audio file is used.

- `noise_reduction_AUDIO_MIN_SAMPLES`: Minimum number of samples required by the network model. If the audio clip is shorter than
  this number, then it is padded with zeros. The default value is `480`.

- `noise_reduction_ACTIVATION_BUF_SZ`: The intermediate, or activation, buffer size reserved for the
  neural network model. By default, it is set to 2MiB.

To **ONLY** build a `noise_reduction` example application, add `-DUSE_CASE_BUILD=noise_reduction`
  (as specified in [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#Building) to the `cmake` command line).

### Build process

> **Note:** This section describes the process for configuring the build for `MPS3: SSE-300`. To
> configure a different target platform, please see the [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#Building)
> section.

To **only** build the `noise_reduction` example, create a build directory, and then navigate inside.
For example:

```commandline
mkdir build_noise_reduction && cd build_noise_reduction
```

On Linux, when providing only the mandatory arguments for CMake configuration, use the following
command to build the Noise Reduction application to run on the *Ethos-U55* Fast Model:

```commandline
cmake ../ -DUSE_CASE_BUILD=noise_reduction
```

To configure a build that can be debugged using Arm DS, we specify the build type as `Debug` and use
the `Arm Compiler` toolchain file:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake \
    -DCMAKE_BUILD_TYPE=Debug \
    -DUSE_CASE_BUILD=noise_reduction
```

For more notes, please refer to:

- [Configuring with custom TPIP dependencies](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../sections/building.md#configuring-with-custom-tpip-dependencies)
- [Using Arm Compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../sections/building.md#using-arm-compiler)
- [Building for different Ethos-U variants](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../sections/building.md#building-for-different-ethos_u-npu-variants)

> **Note:** If you are rebuilding with changed parameters values, it is highly advised that you
> clean the build directory and rerun the CMake command.

If the CMake command is successful, then build the application as follows:

```commandline
make -j4
```

> **Note:** To see compilation and link details, add `VERBOSE=1`.

The build results are placed under the `build/bin` folder. For example:

```tree
bin
 ├── mlek_noise_reduction.axf
 ├── mlek_noise_reduction.htm
 ├── mlek_noise_reduction.map
 ├── images-noise_reduction.txt
 └── sectors
      └── noise_reduction
           ├── dram.bin
           └── itcm.bin
```

Based on the preceding output, the files contain the following information:

- `mlek_noise_reduction.axf`: The built application binary for the noise reduction use case.

- `mlek_noise_reduction.map`: Information from building the application (for example. The
  libraries used, what was optimized, and location of objects).

- `mlek_noise_reduction.htm`: A human readable file containing the call graph of application
  functions.

- `sectors/`: This folder contains the built application, which is split into files for loading into
  different FPGA memory regions.

- `Images-noise_reduction.txt`: Tells the FPGA which memory regions to use for loading the binaries
  in the `sectors/...` folder.

### Add custom input

To run with inputs different to the ones supplied, the parameter `noise_reduction_FILE_PATH` can be
pointed to a WAV file, or a directory containing WAV files. Once you have a directory with WAV files,
run the following command:

```commandline
cmake .. \
    -DUSE_CASE_BUILD=noise_reduction \
    -Dnoise_reduction_FILE_PATH=/path/to/custom/wav_files
```

### Add custom model

The application performs inference using the model pointed to by the CMake parameter
`noise_reduction_MODEL_PATH`.

> **Note:** If you want to run the model using *Ethos-U* ensure that your custom model has been
> run through the Vela compiler successfully before continuing.

For further information: [Optimize model with Vela compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../sections/building.md#optimize-custom-model-with-vela-compiler).

An example:

```commandline
cmake .. \
    -Dnoise_reduction_MODEL_PATH=<path/to/custom_model_after_vela.tflite> \
    -DUSE_CASE_BUILD=noise_reduction
```

> **Note** Changing the neural network model often also requires the pre-processing implementation
> to be changed. Please refer to:
> [How the default neural network model works](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./noise_reduction.md#how-the-default-neural-network-model-works).
>
> **Note:** Before re-running the CMake command, clean the build directory.

The `.tflite` model file, which is pointed to by `noise_reduction_MODEL_PATH`, is converted
to C++ files during the CMake configuration stage. It is then compiled into the application for
performing inference with.

To see which model path was used, inspect the configuration stage log:

```log
-- User option noise_reduction_MODEL_PATH is set to <path/to/custom_model_after_vela.tflite>
...
-- Using <path/to/custom_model_after_vela.tflite>
++ Converting custom_model_after_vela.tflite to custom_model_after_vela.tflite.cc
-- Generating labels file from <path/to/labels_custom_model.txt>
-- writing to <path/to/build/generated/src/Labels.cc>
...
```

After compiling, your custom model replaces the default one in the application.
