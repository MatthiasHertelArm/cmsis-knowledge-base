---
id: "mlek-building-the-ml-embedded-code-samp-build-process"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Build process"
summary: "The build process uses three major steps:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/building.md#build-process"
license: "Apache-2.0"
mode: "V"
---

The build process uses three major steps:

1. Prepare the build environment by downloading third-party sources required, see
   [Preparing build environment](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#preparing-build-environment).

2. Configure the build for the platform chosen. This stage includes:
    - CMake options configuration
    - When `<use_case>_MODEL_PATH` build options are not provided, the default neural network models can be
      downloaded from [Arm ML-Zoo](https://github.com/ARM-software/ML-zoo). For native builds, the network input and
      output data for tests are downloaded.
    - Some files such as neural network models, network inputs, and output labels are automatically converted into C/C++
      arrays, see: [Automatic file generation](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#automatic-file-generation).

3. Build the application.
   Application and third-party libraries are now built. For further information, see:
   [Building the configured project](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#building-the-configured-project).
