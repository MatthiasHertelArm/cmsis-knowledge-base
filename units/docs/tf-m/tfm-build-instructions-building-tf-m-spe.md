---
id: "tfm-build-instructions-building-tf-m-spe"
type: "concept"
domain: "security"
title: "Build instructions: Building TF-M (SPE)"
summary: "This build generates the SPE binary and artifacts, necessary for Building NSPE."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/building/tfm_build_instruction.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/building/tfm_build_instruction.html#building-tf-m-spe"
license: "BSD-3-Clause"
mode: "V"
---

This build generates the SPE binary and artifacts, necessary for Building NSPE.


### Getting the source code

```bash

cd <base folder>
git clone https://git.trustedfirmware.org/TF-M/trusted-firmware-m.git
```
In this documentation, the cloned `trusted-firmware-m` repository will be referenced as
`<TF-M source dir>`.
Additionally, TF-M depends on several external projects, handled by CMake automatically but
you can alter that behaviour using Dependency management.


- For building with Armclang compiler, please follow the note
  in TF-M getting started.
- For building with the IAR toolchain, please see the notes in
- Please use "/" instead of "\\" for paths when running CMAKE commands under
  Windows Command Prompt.

### Configuring

TF-M has many config options for configuring and fine-tuning. Please check the
tf-m_configuration section for the details. The **base** (default) configuration
contains only essential components such as SPM and HW platform support hence the
only mandatory argument to TF-M build is a platform name, provided via
CMake command-line option `-DTFM_PLATFORM=<platform name>`, it can be:

- A relative path under `<TF-M source dir>/platform/ext/target`, for example `arm/mps2/an521`.
- An absolute path of target platform, mainly used for out-of-tree platform build.
- A basename of the target platform folder, for example `an521`.


#### Essential Directories

There are 3 essential directories used by CMake for building TF-M:

- Source code directory `<TF-M source dir>`
- Build directory `<Build Dir>` - the location of all intermediate files required to produce
  a build target.
- Install directory `<Artifact Dir>` - the location of the build output files.

Note::
```
It's recommended to use absolute paths for all directories. Relative paths may not fully work.
```

#### Toolchains

TF-M supports 4 toolchains for cross-compiling and building the project binaries:

- GNU - **default**
- ArmClang
- IAR
- Arm Toolchain for Embedded (ATfE)

Each toolchain has a configuration file for the compiler and linker.
They are located at the root directory of TF-M.
Use `TFM_TOOLCHAIN_FILE` option to provide the absolute path to the preferred toolchain file,
or relative path to working directory.
The default **toolchain_GNUARM.cmake** is selected by `config_base.cmake`
file if the option is omitted.


#### Build type

By default, a MinSizeRel configuration is built. Alternate build types can be
specified with the `CMAKE_BUILD_TYPE` variable. The possible
types are:

- Debug
- RelWithDebInfo
- Release
- MinSizeRel - **default**

Debug symbols are added by default to all builds, but can be removed from
*Release* and *MinSizeRel* builds by setting `TFM_DEBUG_SYMBOLS` to `OFF`.

*RelWithDebInfo*, *Release* and *MinSizeRel* all have different
optimizations turned on and hence will produce smaller, faster code than
*Debug*. *MinSizeRel* will produce the smallest code and hence is often
a good idea on RAM or flash-constrained systems.


#### Output files

In a successful build, a set of files will be created in the `<Artifact Dir>`.
By default, it is `<Build Dir>\api_ns` subfolder but you can redirect the
output to any location using `CMAKE_INSTALL_PREFIX` option. It can be an
absolute path or relative to your current directory. For the contents of the
artifact directory please refer to Artifacts structure.


#### Other build parameters

The full list of default options is in `config/config_base.cmake` and
explained in tfm_cmake_configuration. Several important options
are listed below.

+----------------------------+------------------------------------------+---------------+
| Parameter                  | Description                              | Default value |
+============================+==========================================+===============+
| BL2                        | Build level 2 secure bootloader.         | ON            |
+----------------------------+------------------------------------------+---------------+
| PROJECT_CONFIG_HEADER_FILE | User defined header file for TF-M config |               |
+----------------------------+------------------------------------------+---------------+
| TFM_ISOLATION_LEVEL        | Set TF-M isolation level.                | 1             |
+----------------------------+------------------------------------------+---------------+
| TFM_PROFILE                | See tf-m_profiles.                |               |
+----------------------------+------------------------------------------+---------------+


#### Project Config Header File

CMake variable `PROJECT_CONFIG_HEADER_FILE` can be set by a user the full path to a
configuration header file, which is used to fine-tune component options. The detailed reference
for the project config header file is in Header_configuration.


### Building binaries


The command below shows a general template for building TF-M as a typical CMake project:

```bash

cmake -S <TF-M source dir> -B <Build Dir> -DTFM_PLATFORM=<platform>
cmake --build <Build Dir> -- install
```
It is recommended to clean up the build directory before re-build if the config
header file is updated. CMake is unable to automatically recognize the
dependency when the header file is defined as a macro.

#### Building default configuration for an521


```bash

cd <TF-M source dir>
cmake -S . -B build -DTFM_PLATFORM=arm/mps2/an521
cmake --build build -- install
```
The command above is intended to do:
  - take TF-M sources in the current `.` folder
  - build SPE in the `build` folder
  - for **an521** platform
  - using GNU toolchain *by default*. Use `-DTFM_TOOLCHAIN_FILE=<toolchain file>`
    for alternatives as described in Toolchains
  - install output files in `build/api_ns` folder *by default*. You can specify
    a different directory using `-DCMAKE_INSTALL_PREFIX=<Artifact dir>`
    as described in Output files

It is recommended to build each different build configuration in a separate
build directory.
CMake can generate code for many native build systems. TF-M is tested with
`Unix Makefiles` (default) and `Ninja`. The `-G` option can specify
alternative generators. For example for building with Ninja in the Debug
Build type using ArmClang Toolchains you can use the following:

```bash

cd <TF-M source dir>
cmake -S . -B build -DTFM_PLATFORM=arm/mps2/an521 -GNinja -DTFM_TOOLCHAIN_FILE=toolchain_ARMCLANG.cmake -DCMAKE_BUILD_TYPE=Debug
cmake --build build -- install
```

### Dependency management


The TF-M build system will fetch all dependencies by default with appropriate
versions and store them inside the build tree. In this case, the build tree
location is `<build_dir>/lib/ext`.

If you have local copies already and wish to avoid having the libraries
downloaded every time the build directory is deleted, then the following
variables can be set to the paths to the root directories of the local repos.
This will disable the automatic downloading for that dependencies and speed up
development iterations or allow usage of a dependency version different from the
current one.
Additionally, these path variables can be set in `localrepos.cmake`
file which will be included in a build if it exists.
This file is ignored in TF-M git settings.

The following table lists the commonly used repos. For others, you can refer to `lib/ext`.

+----------------+---------------------+-----------------------------------------------------+
| Dependency     | Cmake variable      | Git repo URL                                        |
+================+=====================+=====================================================+
| TF-PSA-Crypto  | TF_PSA_CRYPTO_PATH  | https://github.com/Mbed-TLS/TF-PSA-Crypto           |
+----------------+---------------------+-----------------------------------------------------+
| MCUboot        | MCUBOOT_PATH        | https://github.com/mcu-tools/mcuboot                |
+----------------+---------------------+-----------------------------------------------------+
| QCBOR          | QCBOR_PATH          | https://github.com/laurencelundblade/QCBOR.git      |
+----------------+---------------------+-----------------------------------------------------+

The recommended versions of the dependencies are listed in `config/config_base.cmake`.


- Some repositories might need patches to allow building it as a part of TF-M.
  While these patches are being upstreamed they are stored in a
  dependency folder under `lib/ext/`.
  In order to use local repositories those patches shall be applied to original source.
  An alternative is to copy out the auto-downloaded repos under the `<build_dir>/lib/ext`.
  They have been applied with patches and can be used directly.

#### Example: building TF-M with local TF-PSA-Crypto repo


Preparing a local repository consists of 2 steps: cloning and patching.
This is only required to be done once. For dependencies without `.patch`
files in their `lib/ext` directory the only required step is
cloning the repo and checking out the correct branch.

```bash

cd <TF-PSA-Crypto base folder>
git clone https://github.com/Mbed-TLS/TF-PSA-Crypto
cd TF-PSA-Crypto
git checkout <TF_PSA_CRYPTO_VERSION> from <TF-M source dir>/config/config_base.cmake>
git apply <TF-M source dir>/lib/ext/tf-psa-crypto/*.patch
```

`<TF-PSA-Crypto base folder>` does not need to have any fixed position related
to the TF-M repo so alternative method to get prepared dependency repos is to
let TF-M download it once and then copy them out of the `build/lib/ext` folder.
Now build TF-M binaries

```bash

cd <TF-M source dir>
cmake -S . -B build -DTFM_PLATFORM=arm/mps2/an521 -DTF_PSA_CRYPTO_PATH=<TF-PSA-Crypto base folder>
cmake --build build -- install

## Building Application (NSPE)


As a result of Building SPE you will get a set of Output files in
`<Artifact Dir>` required for building TF-M application. Essentially, SPE
exports a binary and a set of C source files for PSA interface and platform.
Please note that NSPE and SPE are independent projects and can be built using
different toolchains and toolchain options.


### SPE artifacts structure


SPE components prepared and installed for NSPE usage in `<Artifact Dir>`
will have the following structure:

```none

<Artifact Dir>
├── bin
├── cmake
├── config
├── image_signing
├── initial_attestation
├── interface
├── platform
└── CMakeLists.txt
```
With certain configurations, additional folders may also be installed.
These folders have the following content:

- **bin** - binary images of SPE, Bootloader(optional) and combined.
- **cmake** - CMake scripts like SPE configuration and NSPE toolchains.
- **config** - Configuration files
- **image_signing** - binary image signing tool and keys.
- **initial_attestation** - attestation interface APIs.
- **interface** - PSA interface exposed by SPE.
- **platform** - source code for a selected hardware platform.
- **CMakeLists.txt** - CMake script for the artifacts integration in NSPE.

The content of `<Artifact Dir>` is an exported directory for integration with CMake projects.

Attempting to change any file in `<Artifact Dir>` may cause incompatibility issues.
Instead, please change the corresponding file in the `<TF-M source dir>`.

### NSPE toolchains


SPE prepares and exports CMake toolchain files for building NSPE in all
supported Toolchains in `<Artifact Dir>/cmake` folder.
Toolchain used to build NSPE can be different from what is used to build SPE.


### Basic SPE integration

Refer to the
[example](https://git.trustedfirmware.org/TF-M/tf-m-extras.git/+/refs/heads/main/examples/tf-m-example-ns-app/)
of TF-M applications in **tf-m-extras** repository.

--------------

*Copyright (c) 2017-2024, Arm Limited. All rights reserved.*
*Copyright (c) 2022, Cypress Semiconductor Corporation. All rights reserved.*
