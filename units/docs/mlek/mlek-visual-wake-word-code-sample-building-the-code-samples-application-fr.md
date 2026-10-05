---
id: "mlek-visual-wake-word-code-sample-building-the-code-samples-application-fr"
type: "concept"
domain: "edge-ai"
title: "Visual Wake Word Code Sample: Building the Code Samples application from sources"
summary: "In addition to the already specified build option in the main reference manual, Visual Wake Word use case specifies:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/use_cases/visual_wake_word.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/visual_wake_word.md#building-the-code-samples-application-from-sources"
license: "Apache-2.0"
mode: "V"
---

### Build options

In addition to the already specified build option in the main reference manual, Visual Wake Word use case specifies:

- `vww_MODEL_PATH` - Path to the NN model file in the `TFLite` format. The model is then processed and included in
  the application `axf` file. The default value points to one of the delivered set of models.
  Note that the parameters `vww_LABELS_TXT_FILE`, `TARGET_PLATFORM`, and `ETHOS_U_NPU_ENABLED` must be aligned with the
  chosen model. In other words:
  - If `ETHOS_U_NPU_ENABLED` is set to `On` or `1`, then the NN model is assumed to be optimized. The model naturally
      falls back to the Arm® *Cortex®-M* CPU if an unoptimized model is supplied.
  - if `ETHOS_U_NPU_ENABLED` is set to `Off` or `0`, the NN model is assumed to be unoptimized. Supplying an optimized
      model in this case results in a runtime error.

- `vww_FILE_PATH`: Path to directory or file to be used as custom image file(s) to use in the evaluation
    application. The default value points to the resources/vww/samples folder containing the delivered set
    of images. See more in the Running custom input data section.

- `vww_IMAGE_SIZE`: The NN model requires input images to be of a specific size. This parameter defines the
    size of the image side in pixels. Images are considered squared. Default value is 128, which is what the supplied
    visual wake word model expects.

- `vww_LABELS_TXT_FILE`: Path to the labels' text file to be baked into the application. The file is used
    to map classified classes index to the text label. Change this parameter to point to the custom labels file to map
    custom NN model output correctly.\
    The default value points to the delivered labels.txt file inside the delivery package.

- `vww_ACTIVATION_BUF_SZ`: The intermediate/activation buffer size reserved for the NN model. By default,
    it is set to 2MiB and should be enough for most models.

### Build process

> **Note:** This section describes the process for configuring the build for `MPS3: SSE-300` for different target
> platform see [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../documentation.md#Building) section.

Create a build directory and navigate inside:

```commandline
mkdir build_visual_wake_word && cd build_visual_wake_word
```

On Linux, execute the following command to build **only** Visual Wake Word application to run on the Ethos-U55 Fast
Model when providing only the mandatory arguments for CMake configuration:

```commandline
cmake ../ -DUSE_CASE_BUILD=vww
```

To configure a build that can be debugged using Arm-DS, we can just specify the build type as `Debug` and use the `Arm
Compiler` toolchain file:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake \
    -DCMAKE_BUILD_TYPE=Debug \
    -DUSE_CASE_BUILD=vww
```

Also see:

- [Configuring with custom TPIP dependencies](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../sections/building.md#configuring-with-custom-tpip-dependencies)
- [Using Arm Compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../sections/building.md#using-arm-compiler)
- [Building for different Ethos-U NPU variants](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../sections/building.md#building-for-different-ethos-u-npu-variants)

> **Note:** If re-building with changed parameters values, it is highly advised to clean the build directory and re-run
>the CMake command.

If the CMake command succeeded, build the application as follows:

```commandline
make -j4
```

Add VERBOSE=1 to see compilation and link details.

Results of the build will be placed under `build/bin` folder:

```tree
bin
 ├── mlek_vww.axf
 ├── mlek_vww.htm
 ├── mlek_vww.map
 ├── images-vww.txt
 └── sectors
      └── vww
           ├── ddr.bin
           └── itcm.bin
```

Where:

- `mlek_vww.axf`: The built application binary for the Visual Wake Word use case.

- `mlek_vww.map`: Information from building the application (e.g. libraries used, what was optimized,
    location of objects)

- `mlek_vww.htm`: Human readable file containing the call graph of application functions.

- `sectors/`: Folder containing the built application, split into files for loading into different FPGA memory regions.

- `Images-vww.txt`: Tells the FPGA which memory regions to use for loading the binaries in sectors/**
  folder.

### Add custom input

The application performs inference on image data found in the folder set by the CMake parameter
`vww_FILE_PATH`.

To run the application with your own images first create a folder to hold them and then copy the custom images into this
folder:

```commandline
mkdir /tmp/custom_images

cp custom_image1.bmp /tmp/custom_images/
```

> **Note:** Clean the build directory before re-running the cmake command.

Next set `vww_FILE_PATH` to the location of this folder when building:

```commandline
cmake .. \
    -Dvww_FILE_PATH=/tmp/custom_images/ \
    -DUSE_CASE_BUILD=vww
```

The images found in the `vww_FILE_PATH` folder will be picked up and automatically converted to C++ files
during the CMake configuration stage and then compiled into the application during the build phase for performing
inference with.

The log from the configuration stage should tell you what image directory path has been used:

```log
-- User option vww_FILE_PATH is set to /tmp/custom_images
-- User option vww_IMAGE_SIZE is set to 128
...
-- Generating image files from /tmp/custom_images
++ Converting custom_image1.bmp to custom_image1.cc
...
-- Defined build user options:
...
-- vww_FILE_PATH=/tmp/custom_images
-- vww_IMAGE_SIZE=128
```

After compiling, your custom images will have now replaced the default ones in the application.

> **Note:** The CMake parameter vww_IMAGE_SIZE should match the model input size. When building the
> application, if the size of any image does not match IMAGE_SIZE then it will be rescaled and padded so that it does.

### Add custom model

The application performs inference using the model pointed to by the CMake parameter
`vww_MODEL_PATH`.

> **Note:** If you want to run the model using Ethos-U, ensure your custom model has been run through the Vela compiler
> successfully before continuing.

To run the application with a custom model you will need to provide a labels_<model_name>.txt file of labels associated
with the model. Each line of the file should correspond to one of the outputs in your model. See the provided
visual_wake_word_labels.txt file for an example.

Then, you must set `vww_MODEL_PATH` to the location of the Vela processed model file and
`vww_LABELS_TXT_FILE` to the location of the associated labels file.

An example:

```commandline
cmake \
    -Dvww_MODEL_PATH=<path/to/custom_model_after_vela.tflite> \
    -Dvww_LABELS_TXT_FILE=<path/to/labels_custom_model.txt> \
    -DUSE_CASE_BUILD=vww ..
```

> **Note:** Clean the build directory before re-running the cmake command.

The TFLite model pointed to by `vww_MODEL_PATH` and labels text file pointed to by
`vww_LABELS_TXT_FILE` will be converted to C++ files during the CMake configuration stage and then compiled
into the application for performing inference with.

The log from the configuration stage should tell you what model path and labels file have been used:

```log
-- User option vww_MODEL_PATH is set to <path/to/custom_model_after_vela.tflite>
...
-- User option vww_LABELS_TXT_FILE is set to <path/to/labels_custom_model.txt>
...
-- Using <path/to/custom_model_after_vela.tflite>
++ Converting custom_model_after_vela.tflite to custom_model_after_vela.tflite.cc
-- Generating labels file from <path/to/labels_custom_model.txt>
-- writing to <path/to/build/generated/src/Labels.cc>
...
```

After compiling, your custom model will have now replaced the default one in the application.
