---
id: "nn-cmsis-nn-python-bindings-optional"
type: "concept"
domain: "optimization"
title: "CMSIS NN: Python bindings (optional)"
summary: "The Python helpers are built as a cmsis_nn extension module using pybind11."
status: "draft"
collection: "cmsis-nn"
source: "ARM-software/CMSIS-NN@71cbe3d:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-NN/blob/71cbe3d/README.md#python-bindings-optional"
license: "Apache-2.0"
mode: "V"
---

The Python helpers are built as a `cmsis_nn` extension module using pybind11.

The purpose is to expose the CMSIS-NN host buffer size getter functions so they can be accessed and used from Python.

Build the extension with CMake:
```
cmake -S . -B build -DCMSISNN_BUILD_PYBIND=ON
cmake --build build
```

This produces a `cmsis_nn` shared library in the build tree. For a pip-installable wheel, use:
```
pip wheel . -w dist
pip install dist/cmsis_nn-*.whl
```

Example usage:
```
import cmsis_nn

backend = cmsis_nn.Backend.MVE

buf_size = cmsis_nn.convolve_wrapper_buffer_size(
    backend,
    cmsis_nn.DataType.A8W8,
    input_nhwc=[1, 8, 8, 16],
    filter_nhwc=[8, 3, 3, 16],
    output_nhwc=[1, 6, 6, 8],
    padding_hw=[0, 0],
    stride_hw=[1, 1],
    dilation_hw=[1, 1],
)
```

Optionally backend can be derived, e.g.:
```
backend = cmsis_nn.resolve_backend(cmsis_nn.CortexM.M55)
```


### Compiler Options
Default optimization level is set at Ofast. This can be overwritten with CMake on command line by using *"-DCMSIS_OPTIMIZATION_LEVEL"*. Please change according to project needs.
Just bear in mind this can impact performance. With only optimization level -O0, *ARM_MATH_AUTOVECTORIZE* needs to be defined for processors with Helium
Technology.

The compiler option *'-fomit-frame-pointer'* is enabled by default at -O and higher. When no optimization level is specified,
you may need to specify '-fomit-frame-pointer'.

The compiler option *'-fno-builtin'* does not utilize optimized implementations of e.g. memcpy and memset, which are heavily used by CMSIS-NN. It can significantly downgrade performance. So this should be avoided. The compiler option *'-ffreestanding'* should also be avoided as it enables '-fno-builtin' implicitly.

For processors with DSP extension, int4 and int8 convolutions make use of the restrict keyword for the output pointer. This can allow the compiler to make optimizations but the actual performance result depends on the Arm(R) Cortex(R)-M processor, the compiler and the model. This optimization can be enabled by providing the compiler with a defition of OPTIONAL_RESTRICT_KEYWORD=__restrict . In general Arm Cortex-M7 will benefit from this. Similar Arm Cortex-M4 and Cortex-M33, will generally not benefit from it, but it may still bring an uplift depending on the model and compiler. It is recommended to enable this for Cortex-M7.

Experimental float support is disabled by default. This is intentional to keep the library code size and public API surface small for integer-only builds. Enable the float options only when the application strictly needs them.

For performance reasons, the current floating-point kernels do not
specifically target IEEE edge cases such as `NaN`, `Inf`,
denormals/subnormals, or signed zero. The intended use is that the neural
network pre-processing stage provides finite, numerically safe input data and
that the model weights and biases do not contain aberrant values.

For the scalar floating-point softmax path, the LUT-based exp approximation is
enabled by default for performance. This improves speed on supported targets,
but it adds one 257-entry lookup table per enabled float precision:

- float16: 257 half-words, about 514 bytes
- float32: 257 words, about 1028 bytes

Define `ARM_NN_USE_EXP_TAYLOR` to avoid the extra lookup-table storage. Do not
define both `ARM_NN_USE_EXP_LUT` and `ARM_NN_USE_EXP_TAYLOR` at the same time.

Further compile-time options:

| Name | Explanation | Affects headers(*) |
|------|-----|-----|
| ARM_NN_ENABLE_F32 | Enable experimental float32 operator support. Leave disabled unless the application needs float32 kernels. | Yes |
| ARM_NN_ENABLE_F16 | Enable experimental float16 operator support. Leave disabled unless the application needs float16 kernels and the toolchain/target support them. | Yes |
| NN_DISABLE_SPECIALIZATION | Disable optional shape/layout-specific fast paths and force the corresponding generic implementations. Useful for debugging or validating specialized kernels against the generic path. | No |
| ARM_NN_USE_EXP_LUT | Select the LUT-based scalar float softmax exp approximation. This is the default if no softmax exp macro is defined. | No |
| ARM_NN_USE_EXP_TAYLOR | Select the Taylor/Estrin scalar float softmax exp approximation to avoid the extra LUT storage. | No |
| CMSIS_NN_USE_SINGLE_ROUNDING | Use a single instead of double rounding in requantizazion. This may affect the output. | Yes |
| CMSIS_NN_USE_REQUANTIZE_INLINE_ASSEMBLY | Use inline assembly for `arm_nn_requantize`. This code branch is faster on Cortex-M4, but slower on others. Results should be bit-identical, but was observed to cause differences with Arm Compiler and Cortex-M7. | Yes |

(*) If you enable an option that affects headers, also enable the equivalent option in TFL/TFLM.


### Supported Compilers
* CMSIS-NN is tested on Arm Compiler 6 and on Arm GNU Toolchain.
* IAR compiler is not tested and there can be compilation and/or performance issues.
* Compilation for Host is not supported out of the box. It should be possible to use the C implementation and compile for host with minor stubbing effort.
