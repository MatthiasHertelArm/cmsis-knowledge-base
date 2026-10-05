---
id: "mlek-anomaly-detection-code-sample-building-the-code-sample-application-fro"
type: "concept"
domain: "edge-ai"
title: "Anomaly Detection Code Sample: Building the code sample application from sources"
summary: "In addition to the already specified build option in the main documentation, the Anomaly Detection use-case adds:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/use_cases/ad.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/ad.md#building-the-code-sample-application-from-sources"
license: "Apache-2.0"
mode: "V"
---

### Build options

In addition to the already specified build option in the main documentation, the Anomaly Detection use-case adds:

- `ad_MODEL_PATH` - Path to the NN model file in the `TFLite` format. The model is then processed and included in
  the application `axf` file. The default value points to one of the delivered set of models.

    Note that the parameters `ad_LABELS_TXT_FILE`, `TARGET_PLATFORM`, and `ETHOS_U_NPU_ENABLED` must be aligned with the
    chosen model. In other words:

  - If `ETHOS_U_NPU_ENABLED` is set to `On` or `1`, then the NN model is assumed to be optimized. The model naturally
    falls back to the Arm® *Cortex®-M* CPU if an unoptimized model is supplied.
  - if `ETHOS_U_NPU_ENABLED` is set to `Off` or `0`, the NN model is assumed to be unoptimized. Supplying an optimized
    model in this case results in a runtime error.

- `ad_FILE_PATH`: Path to the directory containing audio files, or a path to single WAV file, to be used in the
  application. The default value points to the `resources/ad/samples` folder containing the delivered set of audio
  clips.

- `ad_AUDIO_RATE`: The input data sampling rate. Each audio file from `ad_FILE_PATH` is preprocessed during the build to
  match the NN model input requirements. The default value is `16000`.

- `ad_AUDIO_MONO`: If set to `ON`, then the audio data is converted to mono. The default value is `ON`.

- `ad_AUDIO_OFFSET`: begin loading the audio data, while starting from this offset amount, defined in seconds. The
  default value is set to `0`.

- `ad_AUDIO_DURATION`: Length of the audio data to be used in the application in seconds. Default is `0`, meaning that
  the whole audio file is used.

- `ad_AUDIO_MIN_SAMPLES`: Minimum number of samples required by the network model. If the audio clip is shorter than
  this number, then it is padded with zeros. The default value is `16000`.

- `ad_MODEL_SCORE_THRESHOLD`: Threshold value to be applied to average Softmax score over the clip, if larger than this
  value, then there is an anomaly.

- `ad_ACTIVATION_BUF_SZ`: The intermediate, or activation, buffer size reserved for the NN model. By default, it is set
  to 2MiB and is enough for most models.

In order to **ONLY** build the Anomaly Detection example application, add `-DUSE_CASE_BUILD=ad` to the `cmake` command
line that is specified in: [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../documentation.md#Building).

### Build process

> **Note:** This section describes the process for configuring the build for the `MPS3: SSE-300` for a different target
> platform. Additional information can be found at: [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../documentation.md#Building).

Create a build directory folder and then navigate inside using:

```commandline
mkdir build_ad && cd build_ad
```

On Linux, when providing only the mandatory arguments for CMake configuration, execute the following command to **only**
build the Anomaly Detection application to run on the *Ethos-U55* Fast Model:

```commandline
cmake ../ -DUSE_CASE_BUILD=ad
```

To configure a build that can be debugged using Arm DS, specify the build type as `Debug` and use the `Arm Compiler`
toolchain file, like so:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake \
    -DCMAKE_BUILD_TYPE=Debug \
    -DUSE_CASE_BUILD=ad
```

For additional information, please refer to:

- [Configuring with custom TPIP dependencies](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../sections/building.md#configuring-with-custom-tpip-dependencies)
- [Using Arm Compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../sections/building.md#using-arm-compiler)
- [Building for different Ethos-U NPU variants](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../sections/building.md#building-for-different-ethos_u-npu-variants)

> **Note:** If re-building with changed parameters values, we recommend that you clean the build directory and then
> re-run the CMake command.

If the CMake command succeeded, build the application as follows:

```commandline
make -j4
```

To see compilation and link details, add `VERBOSE=1`.

Results of the build are placed under `build/bin` folder. For example:

```tree
bin
 ├── mlek_ad.axf
 ├── mlek_ad.htm
 ├── mlek_ad.map
 └── sectors
      ├── images.txt
      └── ad
          ├── ddr.bin
          └── itcm.bin
```

The bin folder contains the following files and folders:

- `mlek_ad.axf`: The built application binary for the Anomaly Detection use-case.

- `mlek_ad.map`: Information from building the application. For example, the libraries used, what was optimized, and
  the location of objects.

- `mlek_ad.htm`: Human readable file containing the call graph of application functions.

- `sectors/ad`: Folder containing the built application. is split into files for loading into different FPGA memory
  regions.

- `sectors/images.txt`: Tells the FPGA which memory regions to use for loading the binaries in the `sectors/..` folder.

### Add custom input

The application anomaly detection is set up to perform inferences on data found in the folder, or an individual file,
that is pointed to by the parameter `ad_FILE_PATH`.

To run the application with your own audio clips, first create a folder to hold them and then copy the custom clips into
the following folder:

```commandline
mkdir /tmp/custom_files

cp custom_id_00.wav /tmp/custom_files/
```

> **Note:** The data used for this example comes from
> [https://zenodo.org/record/3384388\#.X6GILFNKiqA](https://zenodo.org/record/3384388\#.X6GILFNKiqA) and the model
> included in this example is trained on the "Slider" part of the dataset.\
> The machine ID for the clip, so: `00`, `02`, `04`, `06`, comes from must be in the file name for the application to
> work.\
> The file name must have a pattern that matches. For example: `<any>_<text>_00_<here>.wav` if the audio was from machine
> ID `00`, or `<any>_<text>_02_<here>.wav` if it was from machine ID `02`, and so on.
>
> **Note:** Clean the build directory before re-running the CMake command.

Next, set `ad_FILE_PATH` to the location of the following folder when building:

```commandline
cmake .. \
    -Dad_FILE_PATH=/tmp/custom_files/ \
    -DUSE_CASE_BUILD=ad
```

The audio flies found in the `ad_FILE_PATH` folder are picked up and automatically converted to C++ files during the
CMake configuration stage. They are then compiled into the application during the build phase for performing inference
with.

The log from the configuration stage tells you what image directory path has been used:

```log
-- User option ad_FILE_PATH is set to /tmp/custom_files
```

After compiling, your custom inputs have now replaced the default ones in the application.

### Add custom model

The application performs inference using the model pointed to by the CMake parameter ``ad_MODEL_PATH``.

> **Note:** If you want to run the model using an *Ethos-U*, ensure that your custom model has been successfully run
> through the Vela compiler *before* continuing. Please refer to this section for more help:
> [Optimize model with Vela compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../sections/building.md#Optimize-custom-model-with-Vela-compiler).

For example:

```commandline
cmake .. \
    -Dad_MODEL_PATH=<path/to/custom_ad_model_after_vela.tflite> \
    -DUSE_CASE_BUILD=ad
```

> **Note:** Clean the build directory before re-running the CMake command.

The `.tflite` model file pointed to by `ad_MODEL_PATH` is converted to C++ files during the CMake configuration
stage and is then compiled into the application for performing inference with.

The log from the configuration stage tells you what model path has been used. For example:

```log
-- User option TARGET_PLATFORM is set to fastmodel
-- User option ad_MODEL_PATH is set to <path/to/custom_ad_model_after_vela.tflite>
...
-- Using <path/to/custom_ad_model_after_vela.tflite>
++ Converting custom_ad_model_after_vela.tflite to custom_ad_model_after_vela.tflite.cc
...
```

After compiling, your custom model has now replaced the default one in the application.

 >**Note:** To successfully run the model, the NPU must be enabled and the platform `TARGET_PLATFORM` is set to `mps3`
 >and `TARGET_SUBSYSTEM` is `SSE-300`.
