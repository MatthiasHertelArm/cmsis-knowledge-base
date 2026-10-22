---
id: "mlek-automatic-speech-recognition-code-building-the-code-sample-application-fro"
type: "concept"
domain: "edge-ai"
title: "Automatic Speech Recognition Code Sample: Building the code sample application from sources"
summary: "In addition to the already specified build option in the main documentation, the Automatic Speech Recognition use-case adds:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/asr.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/asr.md#building-the-code-sample-application-from-sources"
license: "Apache-2.0"
mode: "V"
---

### Build options

In addition to the already specified build option in the main documentation, the Automatic Speech Recognition use-case
adds:

- `asr_MODEL_PATH` - The path to the NN model file in `TFLite` (for TensorFlow Lite Micro) or
  `PTE` (for ExecuTorch) format. The model is processed and then included into the application `axf` file.
  The default value points to one of the delivered set of models. Note that the parameters
  `asr_LABELS_TXT_FILE`,`TARGET_PLATFORM`, and `ETHOS_U_NPU_ENABLED` must be aligned with the chosen model.
  In other words:
  - If `ETHOS_U_NPU_ENABLED` is set to `On` or `1`, then the NN model is assumed to be optimized. The model naturally
    falls back to the Arm® *Cortex®-M* CPU if an unoptimized model is supplied.
  - If `ETHOS_U_NPU_ENABLED` is set to `Off` or `0`, then the NN model is assumed to be unoptimized. Supplying an
    optimized model in this case results in a runtime error.

- `asr_FILE_PATH`: The path to the directory containing audio files, or a path to single WAV file, to be used in the
  application. The default value points to the `resources/asr/samples` folder that contains the delivered set of audio
  clips.

- `asr_LABELS_TXT_FILE`: The path to the text file for the label. The file is used to map token class index to the text
  label. The default value points to the delivered `labels.txt` file inside the delivery package for *wav2letter*,
  or to `librispeech_sp.pieces` for the labels of the SentencePiece tokeniser trained on the LibriSpeech test-clean
  dataset that was used to train the *Conformer* model.

- `asr_AUDIO_RATE`: The input data sampling rate. Each audio file from `asr_FILE_PATH` is preprocessed during the build
  to match the NN model input requirements. The default value is `16000`.

- `asr_AUDIO_MONO`: If set to `ON`, then the audio data is converted to mono. The default value is `ON`.

- `asr_AUDIO_OFFSET`: Begins loading audio data and starts from this specified offset, defined in seconds. the default
  value is set to `0`.

- `asr_AUDIO_DURATION`: The length of the audio data to be used in the application in seconds. The default is `0`,
  meaning that the whole audio file is used.

- `asr_AUDIO_MIN_SAMPLES`: Minimum number of samples required by the network model. If the audio clip is shorter than
  this number, then it is padded with zeros. The default value is `16000`.

- `asr_MODEL_SCORE_THRESHOLD`: Threshold value that must be applied to the inference results for a label to be deemed
  valid. The default is `0.5`.

- `asr_ACTIVATION_BUF_SZ`: The intermediate, or activation, buffer size reserved for the NN model. By default, it is set
  to 2MiB and is enough for most models.

To **ONLY** build the automatic speech recognition example application, add `-DUSE_CASE_BUILD=asr` to the `cmake`
command line, as specified in: [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#Building).

### Build process

> **Note:** This section describes the process for configuring the build for the *MPS3: SSE-300*. To build for a
> different target platform, please refer to: [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#Building).

To build **only** the automatic speech recognition example, create a build directory and navigate inside, like so:

```commandline
mkdir build_asr && cd build_asr
```

On Linux, when providing only the mandatory arguments for CMake configuration, execute the following command to build
**only** Automatic Speech Recognition application to run on the *Ethos-U55* Fast Model:

```commandline
cmake ../ -DUSE_CASE_BUILD=asr
```

To configure a build that can be debugged using Arm DS specify the build type as `Debug` and then use the `Arm Compiler`
toolchain file:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake \
    -DCMAKE_BUILD_TYPE=Debug \
    -DUSE_CASE_BUILD=asr
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
 ├── mlek_asr.axf
 ├── mlek_asr.htm
 ├── mlek_asr.map
 └── sectors
      ├── images.txt
      └── asr
          ├── ddr.bin
          └── itcm.bin
```

The `bin` folder contains the following files:

- `mlek_asr.axf`: The built application binary for the Automatic Speech Recognition use-case.

- `mlek_asr.map`: Information from building the application. For example: The libraries used, what was optimized, and
  the location of objects.

- `mlek_asr.htm`: Human readable file containing the call graph of application functions.

- `sectors/asr`: Folder containing the built application. It is split into files for loading into different FPGA memory
  regions.

- `sectors/images.txt`: Tells the FPGA which memory regions to use for loading the binaries in the `sectors/..` folder.

### Add custom input

The application anomaly detection is set up to perform inferences on data found in the folder, or an individual file,
that is pointed to by the parameter `asr_FILE_PATH`.

To run the application with your own audio clips, first create a folder to hold them and then copy the custom clips into
the following folder:

```commandline
mkdir /tmp/custom_wavs

cp my_clip.wav /tmp/custom_wavs/
```

> **Note:** Clean the build directory before re-running the CMake command.

Next, when building, set `asr_FILE_PATH` to the location of the following folder:

```commandline
cmake .. \
    -Dasr_FILE_PATH=/tmp/custom_wavs/ \
    -DUSE_CASE_BUILD=asr
```

The audio flies found in the `asr_FILE_PATH` folder are picked up and automatically converted to C files during the
CMake configuration stage. They are then compiled into the application during the build phase for performing inference
with.

The log from the configuration stage tells you what audio directory path has been used:

```log
-- User option asr_FILE_PATH is set to /tmp/custom_wavs
-- Generating audio files from /tmp/custom_wavs
++ Converting my_clip.wav to my_clip.cc
++ Generating build/generated/asr/samples/sample_files.h
++ Generating build/generated/asr/samples/sample_files.c
```

After compiling, your custom inputs have now replaced the default ones in the application.

> **Note:** The CMake parameter `asr_AUDIO_MIN_SAMPLES` determines the minimum number of input samples. When building
> the application, if the size of the audio clips is less than `asr_AUDIO_MIN_SAMPLES`, then it is padded until it
> matches.

### Add custom model

The application performs inference using the model pointed to by the CMake parameter `MODEL_PATH`.

> **Note:** If you want to run the model using an *Ethos-U*, ensure that your custom model has been successfully run
> through the Vela compiler *before* continuing.

For further information: [Optimize model with Vela compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../sections/building.md#Optimize-custom-model-with-Vela-compiler).

To run the application with a custom model, you must provide a `labels_<model_name>.txt` file of labels that are
associated with the model. Each line of the file must correspond to one of the outputs in your model. Refer to the
provided `labels_wav2letter.txt` or `librispeech_sp.pieces` files for an example.

Then, you must set `asr_MODEL_PATH` to the location of the Vela processed model file and `asr_LABELS_TXT_FILE`to
the location of the associated labels file.

For example:

```commandline
cmake .. \
    -Dasr_MODEL_PATH=<path/to/custom_model_after_vela.tflite> \
    -Dasr_LABELS_TXT_FILE=<path/to/labels_custom_model.txt> \
    -DUSE_CASE_BUILD=asr
```

> **Note:** Clean the build directory before re-running the CMake command.

The `.tflite` model file pointed to by `asr_MODEL_PATH`, and the labels text file pointed to by
`asr_LABELS_TXT_FILE` are converted to C++ files during the CMake configuration stage. They are then compiled into the
application for performing inference with.

The log from the configuration stage tells you what model path and labels file have been used, for example:

```log
-- User option TARGET_PLATFORM is set to mps3
-- User option asr_MODEL_PATH is set to <path/to/custom_model_after_vela.tflite>
...
-- User option asr_LABELS_TXT_FILE is set to <path/to/labels_custom_model.txt>
...
-- Using <path/to/custom_model_after_vela.tflite>
++ Converting custom_model_after_vela.tflite to\
custom_model_after_vela.tflite.cc
-- Generating labels file from <path/to/labels_custom_model.txt>
-- writing to <path/to/build/generated/src/Labels.cc>
...
```

After compiling, your custom model has now replaced the default one in the application.
