---
id: "armsw-cmsis-cv-about"
type: "concept"
domain: "edge-ai"
title: "CMSIS-CV: About"
summary: "CMSIS-CV is an optimized computer vision library for embedded systems."
status: "draft"
collection: "arm-software-readmes"
source: "ARM-software/CMSIS-CV@25c6c11:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-CV/blob/25c6c11/README.md#about"
license: "Apache-2.0"
mode: "V"
---

CMSIS-CV is an optimized computer vision library for embedded systems.

It provides optimized compute kernels for Cortex-M.

Different variants are available according to the core and most of the functions are using a vectorized version when the Helium or Neon extension is available.

CMSIS-CV is licensed under [Apache License 2.0](https://github.com/ARM-software/CMSIS-CV/blob/25c6c11/LICENSE).

**It is a work in progress and has just started.**

# Testing

Two kind of tests are provided:

* web : You can test the scalar versions of the kernels in the browser and compare with OpenCV.
* board: Test framework to run on a FVP or MPS3 board

For the web version, clone the repository and just open `Testing/browser/web/index.html` with your browser.
