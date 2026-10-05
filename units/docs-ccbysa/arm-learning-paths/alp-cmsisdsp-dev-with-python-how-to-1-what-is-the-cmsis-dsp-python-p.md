---
id: "alp-cmsisdsp-dev-with-python-how-to-1-what-is-the-cmsis-dsp-python-p"
type: "concept"
domain: "project"
title: "Getting started with CMSIS-DSP using Python: CMSIS-DSP Python package: What is the CMSIS-DSP Python package?"
summary: "The CMSIS-DSP Python package provides a Python API for CMSIS-DSP. Its goal is to make it easier to develop a C solution using CMSIS-DSP by bridging the gap between a Python-based design environment and a final C implementation."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/cmsisdsp-dev-with-python/how-to-1.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/cmsisdsp-dev-with-python/how-to-1/#what-is-the-cmsis-dsp-python-package"
license: "CC-BY-SA-4.0"
mode: "V"
---

The CMSIS-DSP Python package provides a Python API for CMSIS-DSP. Its goal is to make it easier to develop a C solution using CMSIS-DSP by bridging the gap between a Python-based design environment  and a final C implementation.

The API is designed to closely mirror the C version in both function and structure.

Fixed-point arithmetic is rarely supported by Python libraries, which generally focus on floating-point operations. The CMSIS-DSP Python package includes the same fixed-point arithmetic functions as the C version: Q31, Q15 and Q7. Support for half-precision floats will be added in a future release, matching the C API.

The package is compatible with NumPy and integrates well with scientific and AI libraries such as SciPy and PyTorch.
