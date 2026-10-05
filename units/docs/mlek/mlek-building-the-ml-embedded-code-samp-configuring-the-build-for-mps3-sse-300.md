---
id: "mlek-building-the-ml-embedded-code-samp-configuring-the-build-for-mps3-sse-300"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Build process / Configuring the build for MPS3 SSE-300"
summary: "On Linux, if using Arm GNU Toolchain, execute the following command to build the application to run on the Arm® Ethos™-U NPU when providing only the mandatory arguments for CMake configuration:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/building.md#configuring-the-build-for-mps3-sse-300"
license: "Apache-2.0"
mode: "V"
---

_Part of: Build process_

#### Using GNU Arm Embedded toolchain

On Linux, if using `Arm GNU Toolchain`, execute the following command to build the application to run on the
Arm® *Ethos™-U* NPU when providing only the mandatory arguments for CMake configuration:

```commandline
cmake ../
```

The preceding command builds for the default target platform `mps3`, the default subsystem `sse-300`, using the
default toolchain file for the target as `bare-metal-gcc` and the default *Ethos-U55* timing adapter settings.
This is equivalent to running:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-gcc.cmake
    -DTARGET_PLATFORM=mps3 \
    -DTARGET_SUBSYSTEM=sse-300 \
    -DTA_CONFIG_FILE=scripts/cmake/timing_adapter/ta_config_u55_high_end.cmake
```

#### Using Arm Compiler

If using `Arm Compiler` to set the compiler and platform-specific parameters, the toolchain option
`CMAKE_TOOLCHAIN_FILE` can be used to point to the `ARMClang` CMake file, like so:

```commandline
cmake ../ -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake
```

To configure a build that can be debugged using Arm Development Studio, specify the build type as `Debug`. For example:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake \
    -DCMAKE_BUILD_TYPE=Debug
```

#### Using Arm Toolchain for Embedded

Similar to others, for using an LLVM/Clang based toolchain like the Arm Toolchain for Embedded, the toolchain option
`CMAKE_TOOLCHAIN_FILE` can be set as:

```commandline
cmake ../ -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-llvm.cmake
```

#### Configuring applications to run with single sample input

Default CMake configuration behaviour looks for input samples for each use case in the default directory. All these
inputs are baked-in into the application. If the number of files baked in is greater than one the resulting application
will cycle through all the samples before finishing.
[Deploying on an FVP emulating MPS3](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./deployment.md#deploying-on-an-fvp).

To configure the project to use single input for each use case, CMake option `USE_SINGLE_INPUT` can be set to `ON`.


```commandline
cmake ../ -DUSE_SINGLE_INPUT=ON
```

This is useful in quick functional testing scenario or for running tests in a CI environment. To configure automated
testing using the CTest framework:

```commandline
cmake .. \
    -DUSE_SINGLE_INPUT=ON \
    -DBUILD_FVP_TESTS=ON \
    -DFVP_PATH=/home/user/FVP_Corstone_SSE-300/models/Linux64_GCC-6.4/FVP_Corstone_SSE-300_Ethos-U55
```

This will allow the built application to be executed on the FVP in headless mode using:

```commandline
ctest --verbose
```

#### Generating project for Arm Development Studio

To import the project into Arm Development Studio, add the Eclipse project generator and `CMAKE_ECLIPSE_VERSION` in the
CMake command.

It is advisable that the build directory is one level up relative to the source directory. When the build has been
generated, you must follow the Import wizard in Arm Development Studio and import the existing project into the
workspace.

You can then compile and debug the project using Arm Development Studio. Note that the following command is executed one
level up from the source directory:

```commandline
cmake \
    -DTARGET_PLATFORM=mps3 \
    -DTARGET_SUBSYSTEM=sse-300 \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-armclang.cmake \
    -DCMAKE_BUILD_TYPE=Debug \
    -G "Eclipse CDT4 - Unix Makefiles" \
    -DCMAKE_ECLIPSE_VERSION=4.15 \
    ml-embedded-evaluation-kit
```

#### Configuring with custom TPIP dependencies

If the TensorFlow source tree is not in its default expected location, set the path using `TENSORFLOW_SRC_PATH`.
Similarly, if the *Ethos-U* NPU driver and `CMSIS` are not in the default location, then use
`ETHOS_U_NPU_DRIVER_SRC_PATH` and `CMSIS_SRC_PATH` to configure their location.

For example:

```commandline
cmake .. \
    -DTENSORFLOW_SRC_PATH=/my/custom/location/tensorflow \
    -DETHOS_U_NPU_DRIVER_SRC_PATH=/my/custom/location/core-driver \
    -DCMSIS_SRC_PATH=/my/custom/location/cmsis
```

> **Note:** If re-building with changed parameters values, we recommend that you clean the build directory and re-run
> the CMake command.
