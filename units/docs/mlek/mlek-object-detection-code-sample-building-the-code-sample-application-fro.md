---
id: "mlek-object-detection-code-sample-building-the-code-sample-application-fro"
type: "concept"
domain: "edge-ai"
title: "Object Detection Code Sample: Building the code sample application from sources"
summary: "In addition to the already specified build option in the main documentation, the Object Detection use-case specifies:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/use_cases/object_detection.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/object_detection.md#building-the-code-sample-application-from-sources"
license: "Apache-2.0"
mode: "V"
---

### Build options

In addition to the already specified build option in the main documentation, the Object Detection use-case
specifies:

- `object_detection_MODEL_PATH` - The path to the NN model file in the *TFLite* format. The model is then processed and
  included in the application `axf` file. The default value points to one of the delivered set of models.
  Note that the parameters `TARGET_PLATFORM`, and `ETHOS_U_NPU_ENABLED` must be aligned with
  the chosen model. In other words:
  - If `ETHOS_U_NPU_ENABLED` is set to `On` or `1`, then the NN model is assumed to be optimized. The model naturally
    falls back to the Arm® *Cortex®-M* CPU if an unoptimized model is supplied.
  - if `ETHOS_U_NPU_ENABLED` is set to `Off` or `0`, the NN model is assumed to be unoptimized. Supplying an optimized
    model in this case results in a runtime error.

- `object_detection_FILE_PATH`: The path to the directory containing the images, or a path to a single image file, that is to
   be used in the application. The default value points to the `resources/object_detection/samples` folder containing the
   delivered set of images.
   For further information, please refer to: [Add custom input data section](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/./object_detection.md#add-custom-input).

- `object_detection_IMAGE_SIZE`: The NN model requires input images to be of a specific size. This parameter defines the size
  of the image side in pixels. Images are considered squared. The default value is `192`, which is what the supplied
  *YOLO Fastest* model expects.

- `object_detection_ANCHOR_1`: First anchor  array estimated during *YOLO Fastest* model training.

- `object_detection_ANCHOR_2`: Second anchor array estimated during *YOLO Fastest* model training.

- `object_detection_CHANNELS_IMAGE_DISPLAYED`: The user can decide if display the image on the LCD screen in grayscale or RGB.
  This parameter defines the number of channel to use: 1 for grayscale, 3 for RGB. The default value is `3`.

- `object_detection_ACTIVATION_BUF_SZ`: The intermediate, or activation, buffer size reserved for the NN model.
  By default, it is set to 2MiB and is enough for most models.

To build **ONLY** the Object Detection example application, add `-DUSE_CASE_BUILD=object_detection` to the `cmake` command
line, as specified in: [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../documentation.md#Building).

### Build process

> **Note:** This section describes the process for configuring the build for the *MPS3: SSE-300*. To build for a
> different target platform, please refer to: [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../documentation.md#Building).

To **only** build the `object_detection` example, create a build directory, and then navigate inside.

```commandline
mkdir build_object_detection && cd build_object_detection
```

On Linux, when providing only the mandatory arguments for the CMake configuration, execute the following command to
build **only** Object Detection application to run on the *Ethos-U55* Fast Model:

```commandline
cmake ../ -DUSE_CASE_BUILD=object_detection
```

To configure a build that can be debugged using Arm DS, we specify the build type as `Debug` and use the `Arm Compiler`
toolchain file:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake \
    -DCMAKE_BUILD_TYPE=Debug \
    -DUSE_CASE_BUILD=object_detection
```

For further information, please refer to:

- [Configuring with custom TPIP dependencies](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../sections/building.md#configuring-with-custom-tpip-dependencies)
- [Using Arm Compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../sections/building.md#using-arm-compiler)
- [Building for different Ethos-U NPU variants](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../sections/building.md#building-for-different-ethos_u-npu-variants)

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
 ├── mlek_object_detection.axf
 ├── mlek_object_detection.htm
 ├── mlek_object_detection.map
 └── sectors
      ├── images.txt
      └── object_detection
           ├── ddr.bin
           └── itcm.bin
```

The `bin` folder contains the following files:

- `mlek_object_detection.axf`: The built application binary for the Object Detection use-case.

- `mlek_object_detection.map`: Information from building the application. For example: The libraries used, what was
  optimized, and the location of objects.

- `mlek_object_detection.htm`: Human readable file containing the call graph of application functions.

- `sectors/object_detection`: Folder containing the built application. It is split into files for loading into different FPGA memory
  regions.

- `Images-object_detection.txt`: Tells the FPGA which memory regions to use for loading the binaries
  in the `sectors/...` folder.

### Add custom input

The application object detection is set up to perform inferences on data found in the folder, or an individual file,
that is pointed to by the parameter `object_detection_FILE_PATH`.

To run the application with your own images, first create a folder to hold them and then copy the custom images into the
following folder:

```commandline
mkdir /tmp/custom_images

cp custom_image1.bmp /tmp/custom_images/
```

> **Note:** Clean the build directory before re-running the CMake command.

Next, set `object_detection_FILE_PATH` to the location of this folder when building:

```commandline
cmake .. \
    -Dobject_detection_FILE_PATH=/tmp/custom_images/ \
    -DUSE_CASE_BUILD=object_detection
```

The images found in the `object_detection_FILE_PATH` folder are picked up and automatically converted to C++ files during the
CMake configuration stage. They are then compiled into the application during the build phase for performing inference
with.

The log from the configuration stage tells you what image directory path has been used:

```log
-- User option object_detection_FILE_PATH is set to /tmp/custom_images
-- User option object_detection_IMAGE_SIZE is set to 192
...
-- Generating image files from /tmp/custom_images
++ Converting custom_image1.bmp to custom_image1.cc
...
-- Defined build user options:
...
-- object_detection_FILE_PATH=/tmp/custom_images
-- object_detection_IMAGE_SIZE=192
```

After compiling, your custom images have now replaced the default ones in the application.

> **Note:** The CMake parameter `IMAGE_SIZE` must match the model input size. When building the application, if the size
of any image does not match `IMAGE_SIZE`, then it is rescaled and padded so that it does.

### Add custom model

The application performs inference using the model pointed to by the CMake parameter `object_detection_MODEL_PATH`.

> **Note:** If you want to run the model using an *Ethos-U*, ensure that your custom model has been successfully run
> through the Vela compiler *before* continuing.

For further information: [Optimize model with Vela compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/use_cases/../sections/building.md#Optimize-custom-model-with-Vela-compiler).

For example:

```commandline
cmake .. \
    -Dobject_detection_MODEL_PATH=<path/to/custom_model_after_vela.tflite> \
    -DUSE_CASE_BUILD=object_detection
```

> **Note:** Clean the build directory before re-running the CMake command.

The `.tflite` model file pointed to by `object_detection_MODEL_PATH` is converted to
C++ files during the CMake configuration stage. They are then compiled into
the application for performing inference with.

The log from the configuration stage tells you what model path and labels file have been used, for example:

```log
-- User option object_detection_MODEL_PATH is set to <path/to/custom_model_after_vela.tflite>
...
-- Using <path/to/custom_model_after_vela.tflite>
++ Converting custom_model_after_vela.tflite to custom_model_after_vela.tflite.cc
...
```

After compiling, your custom model has now replaced the default one in the application.
