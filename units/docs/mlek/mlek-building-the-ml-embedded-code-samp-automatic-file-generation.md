---
id: "mlek-building-the-ml-embedded-code-samp-automatic-file-generation"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Automatic file generation"
summary: "As mentioned in the previous sections, some files such as neural network models, network inputs, and output labels are automatically converted into C/C++ arrays during the CMake project configuration stage."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/building.md#automatic-file-generation"
license: "Apache-2.0"
mode: "V"
---

As mentioned in the previous sections, some files such as neural network models, network inputs, and output labels are
automatically converted into C/C++ arrays during the CMake project configuration stage.

Also, some code is generated to allow access to these arrays.

For example:

```log
-- Found sources for use-case img_class
-- User option img_class_FILE_PATH is set to /tmp/samples
-- User option img_class_IMAGE_SIZE is set to 224
-- User option img_class_LABELS_TXT_FILE is set to /tmp/labels/labels_mobilenet_v2_1.0_224.txt
-- Generating image files from /tmp/samples
++ Converting cat.bmp to cat.c
++ Converting dog.bmp to dog.c
-- Skipping file /tmp/samples/files.md due to unsupported image format.
++ Converting kimono.bmp to kimono.c
++ Converting tiger.bmp to tiger.c
++ Generating /tmp/build/generated/img_class/samples/sample_files.h
-- Generating labels file from /tmp/labels/labels_mobilenet_v2_1.0_224.txt
-- writing to /tmp/build/generated/img_class/include/Labels.hpp and /tmp/build/generated/img_class/src/Labels.cc
-- User option img_class_ACTIVATION_BUF_SZ is set to 0x00200000
-- User option img_class_MODEL_PATH is set to /tmp/models/mobilenet_v2_1.0_224_INT8.tflite
-- Using /tmp/models/mobilenet_v2_1.0_224_INT8.tflite
++ Converting mobilenet_v2_1.0_224_INT8.tflite to    mobilenet_v2_1.0_224_INT8.tflite.cc
...
```

In particular, the building options pointing to the input files `<use_case>_FILE_PATH`, the model
`<use_case>_MODEL_PATH`, and labels text file `<use_case>_LABELS_TXT_FILE` are used by Python scripts in order to
generate not only the converted array files, but also some headers with utility functions.

> **Note**: The utility functions generated for `labels` and the `tflite` files are used directly at application level.
> The sample images and audio, however, are linked to HAL camera and audio component interfaces. There is no restriction
> on direct use of the generated functions, we have chosen to wire it via HAL to make it easier to understand the flow
> if we were using a real peripheral device streaming (or strobing) data.

For example, the generated utility functions for image classification are:

- Snippet from `build/generated/img_class/generated/samples/samples_files.h`

    ```C++
    #ifndef GENERATED_IMAGES_H
    #define GENERATED_IMAGES_H

    #if defined(__cplusplus)
    extern "C" {
    #endif /* defined(__cplusplus) */

    #include <stdint.h>

    #define NUMBER_OF_FILES (4U)   /**< Total number of files data is available for */
    #define IMAGE_DATA_SIZE (150528U)     /**< Size (bytes) for each image */
    #define IMAGE_DATA_W    (224)     /**< Width of each image in pixels */
    #define IMAGE_DATA_H    (224)    /**< Height of each image pixels */

    extern const uint8_t im0[IMAGE_DATA_SIZE];
    extern const uint8_t im1[IMAGE_DATA_SIZE];
    extern const uint8_t im2[IMAGE_DATA_SIZE];
    extern const uint8_t im3[IMAGE_DATA_SIZE];

    /**
    * @brief       Gets the filename for the baked-in input array
    * @param[in]   idx     Index of the input.
    * @return      const C string pointer to the name.
    **/
    const char* get_sample_data_filename(const uint32_t idx);

    /**
    * @brief       Gets the pointer to image data.
    * @param[in]   idx     Index of the input.
    * @return      Pointer to the 8-bit unsigned integer data.
    **/
    const uint8_t* get_sample_data_ptr(const uint32_t idx);
    ```

  - Snippet from `build/generated/img_class/generated/samples/sample_files.c`

      ```C++

      #include "sample_files.h"
      #include <stddef.h>

      static const char* imgFilenames[] = {
          "cat.bmp",
          "dog.bmp",
          "kimono.bmp",
          "tiger.bmp",
      };

      static const uint8_t* imgArrays[] = {
          im0,
          im1,
          im2,
          im3
      };

      const char* get_sample_data_filename(const uint32_t idx)
      {
        if (idx < NUMBER_OF_FILES) {
            return imgFilenames[idx];
        }
        return NULL;
      }

      const uint8_t* get_sample_data_ptr(const uint32_t idx)
      {
        if (idx < NUMBER_OF_FILES) {
            return imgArrays[idx];
        }
        return NULL;
      }
      ```

These are generated using Python templates located in `scripts/py/mlek_tools/gen/templates`.

```tree
scripts
└── py
    ├── requirements.txt
    └── mlek_tools
        └── gen
            ├── <generation scripts>
            └── templates
                  ├── header_template.txt
                  ├── labels
                  │   ├── Labels.cc.template
                  │   └── Labels.hpp.template
                  ├── sample-data
                  │   ├── audio
                  │   │   ├── audio_clips.c.template
                  │   │   ├── audio_clips.h.template
                  │   │   └── audio.c.template
                  │   └── images
                  │       ├── image.c.template
                  │       ├── images.c.template
                  │       └── images.h.template
                  ├── tests
                  │   ├── iofmdata.cc.template
                  │   ├── TestData.cc.template
                  │   └── TestData.hpp.template
                  └── tflite.cc.template
```

Based on the type of use-case, the correct conversion is called in the use-case CMake file. Or, audio or image
respectively, for voice, or vision use-cases.

For example, the generations call for image classification, `source/app/use_case/img_class/usecase.cmake`, looks like:

```c++
# Generate input files
generate_images_code("${${use_case}_FILE_PATH}"
                     ${SAMPLES_GEN_DIR}
                     "${${use_case}_IMAGE_SIZE}")

# Generate labels file
set(${use_case}_LABELS_CPP_FILE Labels)
generate_labels_code(
    INPUT           "${${use_case}_LABELS_TXT_FILE}"
    DESTINATION_SRC ${SRC_GEN_DIR}
    DESTINATION_HDR ${INC_GEN_DIR}
    OUTPUT_FILENAME "${${use_case}_LABELS_CPP_FILE}"
)

...

# Generate model file
generate_model_code(
    MODEL_PATH ${${use_case}_MODEL_PATH}
    DESTINATION ${SRC_GEN_DIR}
    NAMESPACE   "arm" "app" "img_class")
```

> **Note:** When required, for models and labels conversion, it is possible to add extra parameters such as extra code
> to put in `<model>.cc` file or namespaces.
>
> ```c++
> set(${use_case}_LABELS_CPP_FILE Labels)
> generate_labels_code(
>     INPUT           "${${use_case}_LABELS_TXT_FILE}"
>     DESTINATION_SRC ${SRC_GEN_DIR}
>     DESTINATION_HDR ${INC_GEN_DIR}
>     OUTPUT_FILENAME "${${use_case}_LABELS_CPP_FILE}"
>     NAMESPACE       "namespace1" "namespace2"
> )
>
> ...
>
> set(EXTRA_MODEL_CODE
>     "/* Model parameters for ${use_case} */"
>     "extern const int   g_myvariable2     = value1"
>     "extern const int   g_myvariable2     = value2"
> )
>
> generate_model_code(
>     MODEL_PATH ${${use_case}_MODEL_PATH}
>     DESTINATION ${SRC_GEN_DIR}
>     EXPRESSIONS ${EXTRA_MODEL_CODE}
>     NAMESPACE   "namespace1" "namespace2"
> )
> ```

After the build, the files generated in the build folder are:

```tree
build/generated/
├── <use_case_name1>
│   ├── include
│   │   └── Labels.hpp
│   │
│   ├── samples
│   │   ├── <uc1_input_file1>.cc
│   │   ├── <uc1_input_file2>.cc
│   │   ├── sample_files.c
│   │   └── sample_files.h
│   │
│   └── src
│       ├── Labels.cc
│       └── <uc1_model_name>.tflite.cc
└──  <use_case_name2>
    ├── include
    │   ├── InputFiles.hpp
    │   └── Labels.hpp
    │
    ├── samples
    │   ├── <uc2_input_file1>.cc
    │   ├── <uc2_input_file2>.cc
    │   ├── sample_files.c
    │   └── sample_files.h
    │
    └── src
        ├── Labels.cc
        └── <uc2_model_name>.tflite.cc
```

The next section of the documentation details: [Deployment](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/deployment.md).
