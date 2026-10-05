---
id: "mlek-arm-ml-embedded-evaluation-kit-repository-structure"
type: "concept"
domain: "edge-ai"
title: "Arm® ML embedded evaluation kit: Repository structure"
summary: "The repository has the following structure:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/documentation.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/documentation.md#repository-structure"
license: "Apache-2.0"
mode: "V"
---

The repository has the following structure:

```tree
├── CMakeLists.txt
├── dependencies
├── docs
├── model_conditioning_examples
├── resources
├── /resources_downloaded/
├── scripts
│     ├── cmake
│     │    ├── platforms
│     │    │      ├── mps3
│     │    │      ├── mps4
│     │    │      └── native
│     │    └── ...
│     └── ...
├── source
│     ├── app
│     │    ├── main
│     │    ├── profiler
│     │    └── use_case
│     ├── hal
│     │    ├── include
│     │    └── source
│     ├── lib
│     │    └── mlek
│     │         ├── common
│     │         ├── fwk
│     │         │    ├── executorch
│     │         │    ├── iface
│     │         │    └── tflm
│     │         ├── log
│     │         ├── math
│     │         └── use_case
│     └── readme.md
└── tests
```

What these folders contain:

- `dependencies`: All the third-party dependencies for this project. These are either populated by `git submodule` or by
    downloading packages in the required hierarchy. See `scripts/py/download_dependencies.py`.

- `docs`: Detailed documentation for this repository.

- `model_conditioning_examples`: short example scripts that demonstrate some methods available in TensorFlow
    to condition your model in preparation for deployment on Arm Ethos NPU.

- `resources`: contains ML use-cases applications resources such as input data, label files, etc.

- `resources_downloaded`: created by `set_up_default_resources.py`, contains downloaded resources for ML use-cases
    applications such as models, test data, etc. It also contains a Python virtual environment with all the required
    packages installed.

- `scripts`: Build and source generation scripts.

- `scripts/cmake/platforms`: Platform build configuration scripts `build_configuration.cmake` are located here.
   These scripts are adding platform sources into the application build stream. The script has 2 functions:
  - `set_platform_global_defaults` - to set platform source locations and other build options.
  - `platform_custom_post_build` - to execute specific post build steps. For example, MPS3 and MPS4 board related script adds
                                    board specific `images.txt` file creation and calls bin generation command.
                                    Native profile related script compiles unit-tests.

- `source`: C/C++ sources for the platform and ML applications.

  - `app`: Application entry points and platform-aware use-case implementations that orchestrate the reusable
    libraries.

    - `main`: Contains the main function and calls to platform initialization logic to set up things before launching
      the main loop. Also contains sources common to all use-case implementations.

    - `profiler`: Profiling utilities used by the applications, built as a static library.

    - `use_case`: Contains the ML use-case specific logic. Stored as a separate subfolder, it helps isolate the
      ML-specific application logic. With the assumption that the `app` layer performs the required setup for logic to
      run. It also makes it easier to add a new use-case block.

  - `lib`: Platform-agnostic MLEK libraries that can be reused independently of the provided applications.

    - `mlek/common`: Contains functionality that is common across ML use cases, including pre- and post-processing
        methods for image and audio data, as well as some data structures for conveniently handling intermediate
        data and results.
        It depends on the math functionality exposed by the `math` and the ML framework abstraction layer.

    - `mlek/fwk`: ML framework abstraction layer.  This library contains generic classes representing models and tensors
      that are independent of the underlying ML framework used (TensorFlow Lite Micro or ExecuTorch).
      This allows use case application logic to work with either framework with no changes.

      This library contains implementations of the abstraction layer for TensorFlow Lite Micro and ExecuTorch,
      and one of these implementations will be used at build time depending on the ML framework selected (see [available build options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/./sections/building.md#build-options) for details).

    - `mlek/log`: Common to all code logging macros managing log levels.

    - `mlek/math`: Math functions to be used in ML pipelines. Some of them use CMSIS DSP for optimized execution on Arm CPUs.
      It is a separate CMake project that is built into a static library `libarm_math.a`.

    - `mlek/use_case`: This contains "model" and "processing" APIs for each individual use case. For example, KWS use case
      contains a class for a generic KWS neural network model and the "processing" API give user an easier way to drive
      the MFCC calculations.

    > **NOTE:** The API here is also used to export a CMSIS-pack from this repository and therefore, it is imperative to
    > that the sources here do not depend on any HAL component or drive any platform dependent logic. If you are looking to
    > reuse components from this repository for your application level logic, this directory should be the prime candidate.

  - `hal`: Contains Hardware Abstraction Layer (HAL) sources, providing a platform-agnostic API to access hardware
    platform-specific functions.

    > **Note:** Common code related to the `Arm Ethos-U NPU` software framework resides in *hal/components* sub-folder.

- `tests`: Contains the x86 tests for the use-case applications.

The HAL has the following structure:

```tree
hal
├── CMakeLists.txt
├── include
│   ├── hal.h
│   └── hal_pmu.h
├── readme.md
└── source
    ├── components
    │   ├── audio
    │   ├── camera
    │   ├── cmsis_device
    │   ├── display
    │   ├── npu
    │   ├── npu_ta
    │   ├── platform_pmu
    │   ├── readme.md
    │   └── stdout
    ├── hal.c
    ├── hal_pmu.c
    └── platform
        ├── mps3
        ├── mps4
        ├── native
        └── simple
```

HAL is built as a separate project into a static library `libhal.a`. It is linked with use-case executable.

What these folders contain:

- The folders `include` and `source/hal.c` contain the HAL top-level platform API with PMU interfaces.

> **Note:** the files here and lower in the hierarchy have been written in C and this layer is a clean C/C++ boundary
> in the sources.

- `source/components` directory contains API and implementations for different modules that can be reused for different
  platforms. These contain common functions for Arm Ethos-U NPU initialization, timing adapter block helpers and others.
  Each component produces a static library that could potentially be linked into the platform library to enable
  usage of corresponding modules from the platform sources. For example, most of the use-cases use NPU and
  timing adapter initialization. Similarly, the LCD component provides a standard LCD API used by HAL and propagated
  up the hierarchy. Two static library targets are provided for the LCD module - one with stubbed implementation and the
  other which can drive the LCD on an Arm MPS3 target. If you want to run default ML use-cases on a custom platform, you
  could re-use existing code from this directory provided it is compatible with your platform.

- `source/components/cmsis_device` has a common startup code for Cortex-M based systems. The package defines interrupt
   vector table and handlers. Reset handler - starting point of our application - is also defined here. This entry
   point is responsible for the set-up before calling the user defined "main" function in the higher-level `application`
   logic. It is a separate CMake project that is built into a static library `libcmsis_device.a`. It depends on a CMSIS
   repo through `CMSIS_SRC_PATH` variable. The static library is used by platform code.

- `source/platform/*`: These folders contain platform specific declaration and defines, such as platform initialisation
  code, peripheral memory map, system registers, system specific timer implementation and other.
  Platform is built from selected components and configured cmsis device. It is a separate CMake project, and is
  built into a static library `libplatform-drivers.a`. It is linked into HAL library.
