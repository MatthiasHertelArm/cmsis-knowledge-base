---
id: "mlek-implementing-custom-ml-application-building-custom-use-case"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Building custom use-case"
summary: "There is one last thing to do before building and running a use-case application. You must create a usecase.cmake file in the root of your use-case. However, the name of the file is not important."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/customizing.md#building-custom-use-case"
license: "Apache-2.0"
mode: "V"
---

There is one last thing to do before building and running a use-case application. You must create a `usecase.cmake` file
in the root of your use-case. However, the name of the file is not important.

> **Convention:**  The build system searches for CMake file in each use-case directory and includes it into the build
> flow. This file can be used to specify additional application-specific build options, add custom build steps, or
> override standard compilation and linking flags. Use the `USER_OPTION` function to add further build options. Prefix
> the variable name with `${use_case}`, the use-case name, to avoid names collisions with other CMake variables. Here
> are some useful variable names visible in use-case CMake file:
>
> - `DEFAULT_MODEL_PATH` – The default model path to use if use-case specific `${use_case}_MODEL_PATH` is not set
>  in the build arguments.
>- `TARGET_NAME` – The name of the executable.
> - `use_case` – The name of the current use-case.
> - `UC_SRC` – A list of use-case sources.
> - `UC_INCLUDE` – The path to the use-case headers.
> - `ETHOS_U_NPU_ENABLED` – The flag indicating if the current build supports *Ethos™-U* NPU.
> - `TARGET_PLATFORM` – The target platform being built for.
> - `TARGET_SUBSYSTEM` – If target platform supports multiple subsystems, this is the name of the subsystem.
> - All standard build options.
>   - `CMAKE_CXX_FLAGS` and `CMAKE_C_FLAGS` – The compilation flags.
>   - `CMAKE_EXE_LINKER_FLAGS` – The linker flags.

For the hello world use-case, create a `helloworld.cmake` file and add the following:

```cmake
# Specify the ML frameworks the use case supports
set(${use_case}_ML_FRAMEWORK "tflm")
if (NOT ${use_case}_ML_FRAMEWORK STREQUAL ${ML_FRAMEWORK})
    set(${use_case}_supports_${ML_FRAMEWORK} OFF)
    return()
endif ()

set(${use_case}_supports_${ML_FRAMEWORK} ON)
```

If your use case uses ExecuTorch instead of TensorFlow Lite Micro,
set the value of `${use_case}_ML_FRAMEWORK` to `executorch`.

Next, set the `DEFAULT_MODEL_PATH`:

**TensorFlow Lite Micro**

```cmake
if (ETHOS_U_NPU_ENABLED)
  set(DEFAULT_MODEL_PATH  ${DEFAULT_MODEL_DIR}/helloworldmodel_vela_${DEFAULT_NPU_CONFIG_ID}.tflite)
else()
  set(DEFAULT_MODEL_PATH  ${DEFAULT_MODEL_DIR}/helloworldmodel.tflite)
endif()
```

**ExecuTorch**

```cmake
if (ETHOS_U_NPU_ENABLED)
    string(TOLOWER ${ETHOSU_TARGET_NPU_CONFIG} _NPU_CFG_ID)
    set(DEFAULT_MODEL_PATH  ${DEFAULT_MODEL_DIR}/helloworldmodel_arm_delegate_${_NPU_CFG_ID}.pte)
else()
    set(DEFAULT_MODEL_PATH  ${DEFAULT_MODEL_DIR}/helloworldmodel_arm_TOSA-1.0+FP.pte)
endif()
```

This can be used in subsequent section, for example:

```cmake
USER_OPTION(${use_case}_MODEL_PATH "Neural network model in tflite or pte format."
    ${DEFAULT_MODEL_PATH}
    FILEPATH
    )

generate_model_code(
    MODEL_PATH ${${use_case}_MODEL_PATH}
    DESTINATION ${SRC_GEN_DIR}
    NAMESPACE   "arm" "app" "hello_world"
    )
```

This ensures that the model path pointed to by `${use_case}_MODEL_PATH` is converted to a C++ array and is picked
up by the build system. More information on auto-generations is available under section:
[Automatic file generation](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#automatic-file-generation).

To build you application, follow the general instructions from [Add Custom inputs](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#add-custom-inputs) and
then specify the name of the use-case in the build command, like so:

**TensorFlow Lite Micro**

```commandline
cmake .. \
  -DTARGET_PLATFORM=mps3 \
  -DTARGET_SUBSYSTEM=sse-300 \
  -DUSE_CASE_BUILD=hello_world \
  -DML_FRAMEWORK="tflm" \
  -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake
```

**ExecuTorch**

```commandline
cmake .. \
  -DTARGET_PLATFORM=mps3 \
  -DTARGET_SUBSYSTEM=sse-300 \
  -DUSE_CASE_BUILD=hello_world \
  -DML_FRAMEWORK="executorch" \
  -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake
```


As a result, the file `mlek_hello_world.axf` is created. The MPS3 build also produces the `sectors/hello_world`
directory with binaries and the file `sectors/images.txt` to be copied to the MicroSD card on the board.

The next section of the documentation covers: [Testing and benchmarking](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/testing_benchmarking.md).
