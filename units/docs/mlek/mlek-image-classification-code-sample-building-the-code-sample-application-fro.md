---
id: "mlek-image-classification-code-sample-building-the-code-sample-application-fro"
type: "concept"
domain: "edge-ai"
title: "Image Classification Code Sample: Building the code sample application from sources"
summary: "In addition to the already specified build option in the main documentation, the Image Classification use-case specifies:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/use_cases/img_class.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/img_class.md#building-the-code-sample-application-from-sources"
license: "Apache-2.0"
mode: "V"
---

### Build options

In addition to the already specified build option in the main documentation, the Image Classification use-case
specifies:

- `img_class_MODEL_PATH` - The path to the NN model file in `TFLite` (for TensorFlow Lite Micro) or
  `PTE` (for ExecuTorch) format. The model is then processed and included in the application `axf` file.
  The default value points to one of the delivered set of models.

  When using ExecuTorch, there are two included models: *MobileNet V2* (default) and *DeiT tiny*.
  To use *DeiT tiny*, use this argument to reference the generated `PTE` model for your target platform
  under the `resources_downloaded/img_class/` directory.

    Note that the parameters `img_class_LABELS_TXT_FILE`,`TARGET_PLATFORM`, and `ETHOS_U_NPU_ENABLED` must be aligned with
    the chosen model. In other words:

  - If `ETHOS_U_NPU_ENABLED` is set to `On` or `1`, then the NN model is assumed to be optimized. The model naturally
    falls back to the Arm® *Cortex®-M* CPU if an unoptimized model is supplied.
  - if `ETHOS_U_NPU_ENABLED` is set to `Off` or `0`, the NN model is assumed to be unoptimized. Supplying an optimized
    model in this case results in a runtime error.

- `img_class_NORM_MEAN` and `img_class_NORM_STD` - These options are available
  when [building with ExecuTorch](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../sections/building.md#build-options) and should be used together.
  They specify the normalisation mean and standard deviation values for each of the three input channels,
  and are used for converting uint8 image data to float32 which is the input type for the ExecuTorch models
  provided with this use case.

  The default values correspond to the *MobileNet V2* ExecuTorch model.
  To use *DeiT tiny*, these options must be provided with values specific to that model:
    - *MobileNet V2* (default):
      - `-Dimg_class_NORM_MEAN="0.485, 0.456, 0.406"`
      - `-Dimg_class_NORM_STD="0.229, 0.224, 0.225"`
    - *DeiT tiny*:
      - `-Dimg_class_NORM_MEAN="0.5, 0.5, 0.5"`
      - `-Dimg_class_NORM_STD="0.5, 0.5, 0.5"`

- `img_class_FILE_PATH`: The path to the directory containing the images, or a path to a single image file, that is to
   be used in the application. The default value points to the `resources/img_class/samples` folder containing the
   delivered set of images.

    For further information, please refer to: [Add custom input data section](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/./img_class.md#add-custom-input).

- `img_class_IMAGE_SIZE`: The NN model requires input images to be of a specific size. This parameter defines the size
  of the image side in pixels. Images are considered squared. The default value is `224`, which is what the supplied
  *MobilenetV2-1.0* model expects.

- `img_class_LABELS_TXT_FILE`: The path to the text file for the label. The file is used to map a classified class index
  to the text label. The default value points to the delivered `labels.txt` file inside the delivery package. Change
  this parameter to point to the custom labels file to map custom NN model output correctly.

  For the included `TFlite` version of *MobileNet V2*, this argument should reference the `labels_mobilenet_v2_1.0_224.txt` file.
  For either of the included ExecuTorch models (*MobileNet V2* or *DeiT tiny*), this argument should reference
  the `labels_mobilenet_v2_1.IMAGENET1K_V2.txt` file.

- `img_class_ACTIVATION_BUF_SZ`: The intermediate, or activation, buffer size reserved for the NN model. By default, it
  is set to 2MiB and is enough for most models.

- `USE_CASE_BUILD`: is set to `img_class` to only build this example.

To build **ONLY** the Image Classification example application, add `-DUSE_CASE_BUILD=img_class` to the `cmake` command
line, as specified in: [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#Building).

### Build process

> **Note:** This section describes the process for configuring the build for the *MPS3: SSE-300*. To build for a
> different target platform, please refer to: [Building](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../documentation.md#Building).

Create a build directory and navigate inside, like so:

```commandline
mkdir build_img_class && cd build_img_class
```

On Linux, when providing only the mandatory arguments for the CMake configuration, execute the following command to
build **only** Image Classification application to run on the *Ethos-U55* Fast Model:

```commandline
cmake ../ -DUSE_CASE_BUILD=img_class
```

To configure a build that can be debugged using Arm DS specify the build type as `Debug` and then use the `Arm Compiler`
toolchain file:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake \
    -DCMAKE_BUILD_TYPE=Debug \
    -DUSE_CASE_BUILD=img_class
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
 ├── mlek_img_class.axf
 ├── mlek_img_class.htm
 ├── mlek_img_class.map
 └── sectors
      ├── images.txt
      └── img_class
           ├── ddr.bin
           └── itcm.bin
```

The `bin` folder contains the following files:

- `mlek_img_class.axf`: The built application binary for the Image Classification use-case.

- `mlek_img_class.map`: Information from building the application. For example: The libraries used, what was
  optimized, and the location of objects.

- `mlek_img_class.htm`: Human readable file containing the call graph of application functions.

- `sectors/img_class`: Folder containing the built application. It is split into files for loading into different FPGA memory
  regions.

- `sectors/images.txt`: Tells the FPGA which memory regions to use for loading the binaries in the `sectors/..`
  folder.

### Add custom input

The application anomaly detection is set up to perform inferences on data found in the folder, or an individual file,
that is pointed to by the parameter `img_class_FILE_PATH`.

To run the application with your own images, first create a folder to hold them and then copy the custom images into the
following folder:

```commandline
mkdir /tmp/custom_images

cp custom_image1.bmp /tmp/custom_images/
```

> **Note:** Clean the build directory before re-running the CMake command.

Next, set `img_class_FILE_PATH` to the location of this folder when building:

```commandline
cmake .. \
    -Dimg_class_FILE_PATH=/tmp/custom_images/ \
    -DUSE_CASE_BUILD=img_class
```

The images found in the `img_class_FILE_PATH` folder are picked up and automatically converted to C++ files during the
CMake configuration stage. They are then compiled into the application during the build phase for performing inference
with.

The log from the configuration stage tells you what image directory path has been used:

```log
-- User option img_class_FILE_PATH is set to /tmp/custom_images
-- User option img_class_IMAGE_SIZE is set to 224
...
-- Generating image files from /tmp/custom_images
++ Converting custom_image1.bmp to custom_image1.cc
...
-- Defined build user options:
...
-- img_class_FILE_PATH=/tmp/custom_images
-- img_class_IMAGE_SIZE=224
```

After compiling, your custom images have now replaced the default ones in the application.

> **Note:** The CMake parameter `IMAGE_SIZE` must match the model input size. When building the application, if the size
of any image does not match `IMAGE_SIZE`, then it is rescaled and padded so that it does.

### Add custom model

The application performs inference using the model pointed to by the CMake parameter `MODEL_PATH`.

> **Note:** If you want to run the model using an *Ethos-U*, ensure that your custom model has been successfully run
> through the Vela compiler *before* continuing.

For further information: [Optimize model with Vela compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/use_cases/../sections/building.md#Optimize-custom-model-with-Vela-compiler).

To run the application with a custom model, you must provide a `labels_<model_name>.txt` file of labels that are
associated with the model. Each line of the file must correspond to one of the outputs in your model.

Refer to the provided `labels_mobilenet_v2_1.0_224.txt` and `labels_mobilenet_v2_1.IMAGENET1K_V2.txt` files for examples.

Then, you must set `img_class_MODEL_PATH` to the location of the Vela processed model file and
`img_class_LABELS_TXT_FILE` to the location of the associated labels file.

For example, a TensorFlow Lite Micro based build tree can be generated by:

```commandline
cmake .. \
    -Dimg_class_MODEL_PATH=<path/to/custom_model_after_vela.tflite> \
    -Dimg_class_LABELS_TXT_FILE=<path/to/labels_custom_model.txt> \
    -DUSE_CASE_BUILD=img_class
```

Or for ExecuTorch, it should be:

```commandline
cmake .. \
    -DML_FRAMEWORK=executorch \
    -Dimg_class_MODEL_PATH=<path/to/custom_model_from_arm_aot_compiler.pte> \
    -Dimg_class_LABELS_TXT_FILE=<path/to/labels_custom_model.txt> \
    -DUSE_CASE_BUILD=img_class
```

> **Note:** Clean the build directory before re-running the CMake command.

The `.tflite` or `.pte` model file pointed to by `img_class_MODEL_PATH`, and the labels text file pointed to by
`img_class_LABELS_TXT_FILE` are converted to C++ files during the CMake configuration stage. They are then compiled into
the application for performing inference with.

The log from the configuration stage tells you what model path and labels file have been used, for example:

```log
-- User option img_class_MODEL_PATH is set to <path/to/custom_model_after_vela.tflite>
...
-- User option img_class_LABELS_TXT_FILE is set to <path/to/labels_custom_model.txt>
...
-- Using <path/to/custom_model_after_vela.tflite>
++ Converting custom_model_after_vela.tflite to\
custom_model_after_vela.tflite.cc
-- Generating labels file from <path/to/labels_custom_model.txt>
-- writing to <path/to/build/generated/src/Labels.cc>
...
```

After compiling, your custom model has now replaced the default one in the application.
