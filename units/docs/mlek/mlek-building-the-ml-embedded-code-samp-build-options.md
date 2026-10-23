---
id: "mlek-building-the-ml-embedded-code-samp-build-options"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Build options"
summary: "The project build system allows you to specify custom neural network models for each use-case along with the network inputs."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/building.md#build-options"
license: "Apache-2.0"
mode: "V"
---

The project build system allows you to specify custom neural network models for each use-case along with the network
inputs.

It also builds the chosen ML framework (TensorFlow Lite for Microcontrollers or ExecuTorch) library,
Arm® *Ethos™-U* NPU driver library, and the CMSIS-DSP library from sources.

The build script is parameterized to support different options (see [common_opts.cmake](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/cmake/configuration_options/common_opts.cmake)).
Default values for these parameters configure the build for all use-cases to be executed on an MPS3 FPGA or the Fixed Virtual
Platform (FVP) implementation of the Arm® *Corstone™-300* design.

The build parameters are:

- `TARGET_PLATFORM`: The target platform to execute the application on:
  - `mps3` (default)
  - `mps4`
  - `native`

- `TARGET_SUBSYSTEM`: The target platform subsystem. Specifies the design implementation for the deployment target.
  - For `mps3` target these sub-systems are available:
    - `sse-300`: this is the default, see [Arm® Corstone™-300](https://developer.arm.com/Processors/Corstone-300)
    - `sse-310`: See [Arm® Corstone™-310](https://developer.arm.com/Processors/Corstone-310)
  - For `mps4` target:
    - `sse-315`: See [Arm® Corstone™-315](https://developer.arm.com/Processors/Corstone-315)

- `CMAKE_TOOLCHAIN_FILE`: This built-in CMake parameter can be used to override the default toolchain file used for the
  build. All the valid toolchain files are located in the scripts directory. For example, see:
  [bare-metal-gcc.cmake](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/cmake/toolchains/bare-metal-gcc.cmake).

- `LINKER_SCRIPT_OVERRIDE_PATH`: Optional path to a custom linker control file that overrides the platform default.
  When left unset, the build uses the standard linker script or scatter file selected by the target platform and
  toolchain. When set, the file must be compatible with the selected toolchain. Use case specific linker script
  overrides take precedence over this global setting.

- `<use_case>_LINKER_SCRIPT_OVERRIDE_PATH`: Optional linker control file override for a specific use case. This is set
  in the use case CMake logic and takes precedence over `LINKER_SCRIPT_OVERRIDE_PATH` for that application target.

  When neither override is set, CMake first looks for a build-type-specific linker control file. The variant must have
  the same filename as the common file and be in a lowercase build-type subdirectory beside it. For example, a Debug
  build whose common file is `sse-300/mps3-sse-300.llvm.ld` uses
  `sse-300/debug/mps3-sse-300.llvm.ld` when it exists. If the variant does not exist, CMake falls back to the common
  file. This convention applies to LLVM and GNU linker scripts and Arm Compiler scatter files. Explicit target and
  global overrides are exact selections and are not searched for build-type variants. Add or remove a variant by
  reconfiguring the build so CMake can select it.

  The SSE-300 LLVM Debug variant executes TensorFlow Lite for Microcontrollers code from BRAM and places the heap in
  DDR to preserve full operators and `-O0` debugging within the available ITCM and BRAM. This placement is slower than
  the common Release layout; use Release builds for performance measurements.

- `ML_FRAMEWORK`: Optional parameter to set the ML framework to be used. Canonical values are `tflm` and
  `executorch`. Default value is `tflm`. The values `TensorFlowLiteMicro`, `ExecuTorch`, and `et` are also accepted
  case-insensitively as aliases. This option will configure the framework build steps and include them in the binary
  tree. All use case examples should advertise which framework they support and only the examples that support the
  framework selected will be included in the binary tree.

- `TENSORFLOW_SRC_PATH`: Path for TensorFlow Lite Micro source tree. Default value points to the
  `dependencies/tensorflow` git submodule. Repository is hosted
  here: [TensorFlow Lite Micro](https://github.com/tensorflow/tflite-micro.git)

- `EXECUTORCH_SRC_PATH`: Path for ExecuTorch source tree. Default value points to
  `dependencies/executorch` git submodule. Repository is hosted
  here: [ExecuTorch](https://github.com/pytorch/executorch)

- `ETHOS_U_NPU_DRIVER_SRC_PATH`: The path to the *Ethos-U* NPU core driver sources. The default value points to the
  `dependencies/core-driver` git submodule. Repository is hosted here:
  [ethos-u-core-driver](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-core-driver).

- `CMSIS_SRC_PATH`, `CMSIS_DSP_SRC_PATH`, `CMSIS_NN_SRC_PATH`: Paths to the CMSIS sources to be used to build TensorFlow
   Lite Micro library. These parameters are optional and are only valid for Arm® *Cortex®-M* CPU targeted
   configurations.  The default values point to the git submodules. Repositories are hosted here:
   [CMSIS-6](https://github.com/ARM-software/CMSIS_6.git), [CMSIS-DSP](https://github.com/ARM-software/CMSIS-DSP)
   and [CMSIS-NN](https://github.com/ARM-software/CMSIS-NN.git).

- `CMSIS_DSP_MIN_REQ_SRC_LIST`: Optional boolean parameter that can toggle whether to compile all CMSIS-DSP sources
   or just a small subset of the whole library. By default, it is set to `ON` to reduce compilation time, but can be
   set to `OFF` if full DSP functionality is required by additions made within this project, or when this project is
   used as a dependency.

- `ETHOS_U_NPU_ENABLED`: Sets whether the use of *Ethos-U* NPU is available for the deployment target. By default, this
  is set and therefore application is built with *Ethos-U* NPU supported.

- `ETHOS_U_NPU_ID`: The *Ethos-U* NPU processor:
  - `U55` (default)
  - `U65`
  - `U85`

- `ETHOS_U_NPU_MEMORY_MODE`:  The *Ethos-U* NPU memory mode:
  - `Shared_Sram` (default for *Ethos-U55* NPU)
  - `Dedicated_Sram` (default for *Ethos-U65* and *Ethos-U85* NPU)
  - `Sram_Only`

  > **Note:** The `Sram_Only` and `Shared_Sram` memory modes are available on
  > *Ethos-U55*, *Ethos-U65* and *Ethos-U85* NPU,
  > and `Dedicated_Sram` only for *Ethos-U65* and *Ethos-U85* NPU.

- `ETHOS_U_NPU_CONFIG_ID`: This parameter is set by default based on the value of `ETHOS_U_NPU_ID`.
  For Ethos-U55, it defaults to the `H128` indicating that the Ethos-U55 128 MAC optimised model
  should be used. For Ethos-U65, it defaults to `Y256` and for Ethos-U85 it defaults to `Z256`.
  However, the user can override these defaults to a configuration ID from `H32`, `H64`, `H256`, `Y512`,
  `Z128`, `Z512`, `Z1024` and `Z2048`.

  > **Note:** This ID is only used to choose which tflite/pte file path is to be used by the CMake
  > configuration for all the use cases. If the user has overridden use-case specific model path
  > parameter `ETHOS_U_NPU_CONFIG_ID` parameter will become irrelevant for that use-case. Also, the
  > model files for the chosen `ETHOS_U_NPU_CONFIG_ID` are expected to exist in the default locations.
  > See [Fetching resource files](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#fetching-resource-files) for details on how to do this for your
  > chosen configuration.

- `ETHOS_U_NPU_CACHE_SIZE`: The *Ethos-U* NPU cache size used if the *Ethos-U* NPU processor selected with the option
  `ETHOS_U_NPU_ID` is `U65` or `U85`.
  Default value is 393216 (see [default_vela.ini](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/vela/default_vela.ini) ).

- `CPU_PROFILE_ENABLED`: Sets whether profiling information for the CPU core should be displayed. By default, this is
  set to false, but can be turned on for FPGA targets. The FVP and the CPU core cycle counts are **not** meaningful and
  are not to be used.

- `MLEK_LOG_ENABLE`: Enables/disables logging for the whole application. Default is set to `ON`, but if this
  project is wrapped as a dependency, the definitions provided by logging interface could be overridden or disabled
  altogether.

- `MLEK_LOG_LEVEL`: Sets the verbosity level for the output of the application over `UART`, or `stdout`. Valid values
  are: `MLEK_LOG_LEVEL_TRACE`, `MLEK_LOG_LEVEL_DEBUG`, `MLEK_LOG_LEVEL_INFO`, `MLEK_LOG_LEVEL_WARN`, and
  `MLEK_LOG_LEVEL_ERROR`. The default is set to: `MLEK_LOG_LEVEL_INFO`.

- `<use_case>_MODEL_PATH`: The path to the model file that is processed and is included into the application
  `axf` file. The default value points to one of the delivered set of models. Make sure that the model chosen is aligned
  with the `ETHOS_U_NPU_ENABLED` setting.

  - When using the *Ethos-U* NPU backend, the NN model is assumed to be optimized by Vela compiler. However, even if
    not, if it is supported by the specified ML framework it falls back on the CPU and is executed.

  - When use of the *Ethos-U* NPU is disabled, and if a Vela optimized model is provided, then the application reports
    a failure at runtime.

- `USE_CASE_BUILD`: Specifies the list of applications to build. By default, the build system scans sources to identify
  available ML applications and produces executables for all detected use-cases. This parameter can accept single value,
  for example: `USE_CASE_BUILD=img_class`, or multiple values. For example: `USE_CASE_BUILD="img_class;kws"`.

- `ETHOS_U_NPU_TIMING_ADAPTER_SRC_PATH`: The path to timing adapter sources. The default value points to the
  `timing_adapter` dependencies folder.

- `ETHOS_U_NPU_TIMING_ADAPTER_ENABLED`: Specifies if the *Ethos-U* timing adapter is enabled.

  > **NOTE**: This setting is set to ON for all platforms if `ETHOS_U_NPU_ENABLED` is set. However, it is overridden
  > to OFF for Arm® Corstone-310 implementation.

- `TA_CONFIG_FILE`: The path to the CMake configuration file that contains the timing adapter parameters. Used only if
  the timing adapter build is enabled. Default for Ethos-U55 NPU is
  [ta_config_u55_high_end.cmake](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/cmake/timing_adapter/ta_config_u55_high_end.cmake),
  for Ethos-U65 NPU is [ta_config_u55_high_end.cmake](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/cmake/timing_adapter/ta_config_u55_high_end.cmake).
  For Ethos-U85 NPU, the default configuration file depends on the MAC configuration.
  The default for 128 and 256 is [ta_config_u85_sys_dram_low.cmake](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/cmake/timing_adapter/ta_config_u85_sys_dram_low.cmake),
  the default for 512 and 1024 is [ta_config_u85_sys_dram_mid.cmake](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/cmake/timing_adapter/ta_config_u85_sys_dram_mid.cmake),
  and the default for 2048 is [ta_config_u85_sys_dram_high.cmake](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/../../scripts/cmake/timing_adapter/ta_config_u85_sys_dram_high.cmake).

- `TENSORFLOW_LITE_MICRO_CLEAN_BUILD`: Optional parameter to enable, or disable, "cleaning" prior to building for the
  TensorFlow Lite Micro library. Enabled by default.

- `TENSORFLOW_LITE_MICRO_CLEAN_DOWNLOADS`: Optional parameter to enable wiping out `TPIP` downloads from TensorFlow
  source tree prior to each build. Disabled by default.

- `USE_SINGLE_INPUT`: Sets whether each use case will use a single default input sample file. This is useful for
   quicker functional testing especially for CI tests. Disabled by default.

- `BUILD_FVP_TESTS`: Specifies whether to generate tests for built applications targeted to run on the FVP. Tests will
  be generated for all use-cases. It is recommended to set `USE_SINGLE_INPUT` to `ON` when using this option.

- `FVP_PATH`: The path to the FVP to be used for testing built applications. This option is available only if
`BUILD_FVP_TESTS` option is switched `ON`.

- `FVP_VSI_ENABLED`: Configures the build for applications to use
  [Virtual Streaming Interface](https://arm-software.github.io/AVH/main/simulation/html/group__arm__vsi.html) (VSI)
  available for FVP targets. Read more about VSI requirements [here](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./deployment.md#vsi-requirements) and about
  deployment [here](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./deployment.md#deployment-with-virtual-streaming-interface). Note that enabling this option will
  conflict with `BUILD_FVP_TESTS`.

- `FVP_VSI_SRC_PATH`: If `FVP_VSI_ENABLED` is `ON`, this cache variable defaults to the git submodule for AVH
   repository. This directory is expected to provide the VSI driver sources and Python scripts.

- `SEMIHOSTING_ENABLED`: Toggles semihosting support. For more information on semihosting, see
  [What is semihosting?](https://developer.arm.com/documentation/dui0203/j/semihosting/about-semihosting/what-is-semihosting-)
  By default, this is set to `OFF` and is only included as an option for `MPS3` and `MPS4` based target platforms.

  > **NOTE**: If semihosting enabled application is used with FVPs, additional command line arguments must be provided.
  > See [semihosting section under deployment](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./deployment.md#semihosting).

- `RESOURCES_PATH`: The path to the resources downloaded by the set_up_default_resources.py script
  and compiled using Vela.  This can be set if this script was run using the `--downloads-dir` flag to
  override the default location for these models.  Defaults to `./resources_downloaded` relative to the
  root of this project.

- `INTERACTIVE_MODE`: Enables or disables interactive mode for the use cases. When set to `ON` (by default `OFF`),
  the program pauses and waits for user input before proceeding to the next inference.
  This flag cannot be used when running the tests.

For details on the specific use-case build options, follow the instructions in the use-case specific documentation.

Also, when setting any of the CMake configuration parameters that expect a directory, or file, path, **use absolute
paths instead of relative paths**.
