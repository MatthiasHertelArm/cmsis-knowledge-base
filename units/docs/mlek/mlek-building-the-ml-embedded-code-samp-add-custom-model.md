---
id: "mlek-building-the-ml-embedded-code-samp-add-custom-model"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Add custom model"
summary: "The application performs inference using the model pointed to by the CMake parameter MODEL_PATH."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/building.md#add-custom-model"
license: "Apache-2.0"
mode: "V"
---

The application performs inference using the model pointed to by the CMake parameter `MODEL_PATH`.

> **Note:** If you want to run the model using *Ethos-U* NPU, ensure that your custom model has been run through the
> Vela compiler successfully before continuing.

To run the application with a custom model, you must provide a `labels_<model_name>.txt` file of labels that are
associated with the model.

Each line of the file should correspond to one of the outputs in your model. See the provided
`labels_mobilenet_v2_1.0_224.txt` file in the `img_class` use-case for an example.

Then, you must set `<use_case>_MODEL_PATH` to the location of the Vela processed model file and
`<use_case>_LABELS_TXT_FILE` to the location of the associated labels file (if necessary), like so:

```commandline
cmake .. \
    -D<use_case>_MODEL_PATH=<path/to/custom_model_after_vela.tflite> \
    -D<use_case>_LABELS_TXT_FILE=<path/to/labels_custom_model.txt> \
    -DTARGET_PLATFORM=mps3 \
    -DTARGET_SUBSYSTEM=sse-300 \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake
```

> **Note:** For the specific use-case command, refer to the relative section in the use-case documentation.
>
> **Note:** Clean the build directory before re-running the CMake command.

The TensorFlow Lite for Microcontrollers model pointed to by `<use_case>_MODEL_PATH` and the labels text file
pointed to by `<use_case>_LABELS_TXT_FILE` are converted to C++ files during the CMake configuration stage. They are
then compiled into the application for performing inference with.

The log from the configuration stage tells you what model path and labels file have been used. For example:

```log
-- User option TARGET_PLATFORM is set to mps3
-- User option <use_case>_MODEL_PATH is set to
<path/to/custom_model_after_vela.tflite>
...
-- User option <use_case>_LABELS_TXT_FILE is set to
<path/to/labels_custom_model.txt>
...
-- Using <path/to/custom_model_after_vela.tflite>
++ Converting custom_model_after_vela.tflite to custom_model_after_vela.tflite.cc
-- Generating labels file from <path/to/labels_custom_model.txt>
-- writing to <path/to/build>/generated/include/Labels.hpp and <path/to/build>/generated/src/Labels.cc
...
```

After compiling, your custom model has now replaced the default one in the application.
