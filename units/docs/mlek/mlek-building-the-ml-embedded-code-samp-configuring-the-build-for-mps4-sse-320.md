---
id: "mlek-building-the-ml-embedded-code-samp-configuring-the-build-for-mps4-sse-320"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Build process / Configuring the build for MPS4 SSE-320"
summary: "On Linux, execute the following command to build the application for target platform mps4 and subsystem sse-320, using the default toolchain file for the target as bare-metal-gcc. This is equivalent to running:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/building.md#configuring-the-build-for-mps4-sse-320"
license: "Apache-2.0"
mode: "V"
---

_Part of: Build process_

On Linux, execute the following command to build the application for target platform `mps4` and subsystem `sse-320`,
using the default toolchain file for the target as `bare-metal-gcc`.
This is equivalent to running:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-gcc.cmake \
    -DTARGET_PLATFORM=mps4 \
    -DTARGET_SUBSYSTEM=sse-320
```

To build for Corstone™-320 FPGA (for MPS4 board), an additional flag must be supplied:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-gcc.cmake \
    -DTARGET_PLATFORM=mps4 \
    -DTARGET_SUBSYSTEM=sse-320 \
    -DFPGA_PLATFORM_SSE_320=ON
```

The flag `-DFPGA_PLATFORM_SSE_320=ON` is needed for the binaries to work on the MPS4 board, and the binaries produced by this
build will not work on FVP.  Omit `FPGA_PLATFORM_SSE_320` to produce binaries that can run on Corstone™-320 FVP.
