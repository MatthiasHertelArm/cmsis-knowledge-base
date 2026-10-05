---
id: "mlek-building-the-ml-embedded-code-samp-configuring-the-build-for-mps3-sse-310"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Build process / Configuring the build for MPS3 SSE-310"
summary: "On Linux, execute the following command to build the application for target platform mps3 and subsystem sse-310, using the default toolchain file for the target as bare-metal-gcc. This is equivalent to running:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/building.md#configuring-the-build-for-mps3-sse-310"
license: "Apache-2.0"
mode: "V"
---

_Part of: Build process_

On Linux, execute the following command to build the application for target platform `mps3` and subsystem `sse-310`,
using the default toolchain file for the target as `bare-metal-gcc`.
This is equivalent to running:

```commandline
cmake .. \
    -DCMAKE_TOOLCHAIN_FILE=scripts/cmake/toolchains/bare-metal-gcc.cmake \
    -DTARGET_PLATFORM=mps3 \
    -DTARGET_SUBSYSTEM=sse-310
```

> **Note:** Timing adapters are not supported for this subsystem.
