---
id: "mlek-building-the-ml-embedded-code-samp-building-for-default-configuration"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Build process / Building for default configuration"
summary: "A helper script build_default.py is provided to configure and build all the applications. It configures the project with default settings i.e., for mps3 target, sse-300 subsystem and Ethos-U55 timing-adapter settings."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/building.md#building-for-default-configuration"
license: "Apache-2.0"
mode: "V"
---

_Part of: Build process_

A helper script `build_default.py` is provided to configure and build all the applications. It configures the project
with default settings i.e., for `mps3` target, `sse-300` subsystem and *Ethos-U55* timing-adapter settings.
Under the hood, it invokes all the necessary
CMake commands that are described in the next sections.

If using the `Arm GNU embedded toolchain`, run:

```commandline
./build_default.py
```

If using the `Arm Compiler`, run:

```commandline
./build_default.py --toolchain arm
```

For LLVM/Clang builds, run:

```commandline
./build_default.py --toolchain llvm
```

To build ExecuTorch use cases instead of TensorFlow Lite Micro, run:

```commandline
./build_default.py --ml-framework executorch
```

Additional command line arguments supported by this script are:

- `--skip-download`: Do not download resources: models and test vectors
- `--skip-vela`: Do not run Vela optimizer on downloaded models.
- `--npu-config-name`: Arm Ethos-U configuration to build for. The default value is
    `ethos-u55-128`. Valid values are:
  - `ethos-u55-32`
  - `ethos-u55-64`
  - `ethos-u55-128`
  - `ethos-u55-256`
  - `ethos-u65-256`
  - `ethos-u65-128`
  - `ethos-u85-256`
  - `ethos-u85-512`
  - `ethos-u85-1024`
  - `ethos-u85-2048`
- `--make-jobs`: Specifies the number of concurrent jobs to use for compilation.
  The default value is equal to the number of cores in the system.
  Lowering this value can be useful in case of limited resources.
- `--make-verbose`: Make the compile process verbose. This is equal to run ```make VERBOSE=1```.

To build for *Ethos™-U55* 32 MAC configuration, using `Arm Compiler`, run:

```commandline
./build_default.py --npu-config-name ethos-u55-32 --toolchain arm
```
