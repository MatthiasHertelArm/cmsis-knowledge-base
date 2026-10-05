---
id: "dsp-overview-related-projects"
type: "concept"
domain: "optimization"
title: "Overview: Related projects"
summary: "A Python wrapper is also available with a Python API as close as possible to the C one. It can be used to start developing and testing an algorithm with NumPy and SciPy before writing the C version."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:Documentation/Doxygen/src/mainpage.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/Documentation/Doxygen/src/mainpage.md#related-projects"
license: "Apache-2.0"
mode: "V"
---

### Python wrapper

A Python wrapper is also available with a Python API as close as possible to the C one. It can be used to start developing and testing an algorithm with NumPy and SciPy before writing the C version. Is is available on [PyPI.org](https://pypi.org/project/cmsisdsp/). It can be installed with: `pip install cmsisdsp`.

### C++ template extension

This extension is a set of C++ headers using templates.
To use this C++ API, just include the headers.
The C++ API is a higher-level API that provides automatic vectorized loop fusion for better performance.

More documentation about the @ref dsppp_main "DSP++" extension.
