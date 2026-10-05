---
id: "dsp-cmsis-dsp-about"
type: "concept"
domain: "optimization"
title: "CMSIS-DSP: About"
summary: "CMSIS-DSP is an optimized compute library for embedded systems (DSP is in the name for legacy reasons)."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/README.md#about"
license: "Apache-2.0"
mode: "V"
---

CMSIS-DSP is an optimized compute library for embedded systems (DSP is in the name for legacy reasons).

It provides optimized compute kernels for Cortex-M and for Cortex-A.

Different variants are available according to the core and most of the functions are using a vectorized version when the Helium or Neon extension is available.

This repository contains the CMSIS-DSP library and several other projects:

* Test framework for bare metal Cortex-M or Cortex-A
* Examples for bare metal Cortex-M
* PythonWrapper

You don't need any of the other projects to build and use CMSIS-DSP library. Building the other projects may require installation of other libraries (CMSIS), other tools (Arm Virtual Hardware) or CMSIS build tools.


### CMSIS-DSP Kernels

Kernels provided by CMSIS-DSP (list not exhaustive):

* Basic mathematics (real, complex, quaternion, linear algebra, fast math functions)
* DSP (filtering)
* Transforms (FFT, MFCC, DCT)
* Statistics 
* Classical ML (Support Vector Machine, Distance functions for clustering ...)

Kernels are provided with several datatypes : f64, f32, f16, q31, q15, q7.

### C++ API (DSP++)

DSP++ provides a higher-level C++ API for combining existing CMSIS-DSP kernels into new algorithms while keeping good performance. Its loop fusion feature can combine several operations into a single loop, avoiding temporary arrays and repeated passes over the data.

DSP++ is entirely optional and header-only: it requires no separate library build. Applications using only the C API are unaffected: no code or build changes are needed, and the extension adds no code size, memory or runtime overhead.

**DSP++ is currently unsupported in builds with `ARM_MATH_NEON` enabled.** On Cortex-A, enabling this macro to benefit from Neon in the C API also affects DSP++: its incomplete Neon implementation can cause compilation errors, with no automatic scalar fallback. Applications using only the C API can continue to use Neon normally.

The C++ API headers are in `dsppp/Include` and are included in the CMSIS-DSP pack starting with version 1.18.0. See the [DSP++ introduction](https://arm-software.github.io/CMSIS-DSP/dsppp_intro.html) for an example.

### Experimental autodiff extension

Built on DSP++, the automatic differentiation (autodiff) extension is **experimental** and is not a new ML framework. Its focus is on-device fine-tuning using a subset of existing CMSIS-DSP kernels. See the [autodiff introduction](https://arm-software.github.io/CMSIS-DSP/autodiff_introduction.html) to learn more.

### Python wrapper

A [PythonWrapper](https://pypi.org/project/cmsisdsp/) is also available and can be installed with:

`pip install cmsisdsp`

With this wrapper you can design your algorithm in Python using an API as close as possible to the C API. The wrapper is compatible with NumPy. The wrapper is supporting fixed point arithmetic. This wrapper works in google colab.

The goal is to make it easier to move from a design to a final implementation in C.
