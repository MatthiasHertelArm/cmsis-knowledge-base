---
id: "etarm-executorch-arm-backend-directory-layout"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch Arm® Backend: Directory Layout"
summary: "Below is an overview of the key folder and files in this directory:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@6368414:backends/arm/README.md"
doc_source: "https://github.com/pytorch/executorch/blob/6368414/backends/arm/README.md#directory-layout"
license: "BSD-3-Clause"
mode: "V"
---

Below is an overview of the key folder and files in this directory:

```
backends/arm/
│
├── _passes/                       # Graph transformation passes
│   ├── arm_pass_manager.py        # Defines ordering of graph transformations
│   └── *_pass.py                  # Graph transformation implementation
│
├── common/                        # Common functionality used across the backend
│
├── debug/                         # Debugging schema and functionality
│
├── ethosu/                        # Implementations of EthosUPartitioner and EthosUBackend
│
├── operator_support/              # Checks if operators can be partitioned
│
├── operators/                     # ATen → TOSA serialization
│   ├── node_visitor.py            # Defines base class for ATen → TOSA node visitors
│   └── op_*.py                    # Lowering implementations for individual operators
│
├── quantizer/                     # Quantization-related logic
│   ├── arm_quantizer.py           # EthosUQuantizer and VGFQuantizer definitions
│   └── quantization_annotator.py  # Defines how operators are annotated for quantization
│
├── runtime/                       # Backends for running inference on target devices
│   ├── EthosUBackend.cpp          # Common Ethos-U backend implementation
│   ├── EthosUBackend_CoreDriver.cpp
│   ├── EthosUBackend_LinuxDriver.cpp
│   └── VGFBackend.cpp
│
├── scripts/                       # Auxiliary build, dependency installation and utility scripts
│
├── test/                          # Unit tests for the backend
│   ├── ops/                       # Operator level unit tests
│   ├── models/                    # Model level unit tests
│   └── tester/                    # Testing harnesses and utilities
│
├── tosa/                          # Shared TOSA backend implementation and dialect
│
└── vgf/                           # Implementations of VgfPartitioner and VgfBackend
```

### Ethos-U runtime drivers

The common `EthosUBackend.cpp` runtime is paired with one driver-specific
implementation:

- `EthosUBackend_CoreDriver.cpp` calls the Ethos-U core driver directly for
  bare-metal (no-OS) and RTOS targets. CMake selects it when
  `EXECUTORCH_BUILD_ARM_BAREMETAL` is enabled.
- `EthosUBackend_LinuxDriver.cpp` uses the Ethos-U Linux userspace and kernel
  driver stack. CMake selects it when `EXECUTORCH_BUILD_ARM_ETHOSU_LINUX` is
  enabled.

The two implementations provide the same internal platform hooks and are
mutually exclusive in a build.
