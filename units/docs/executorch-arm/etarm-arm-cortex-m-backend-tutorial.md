---
id: "etarm-arm-cortex-m-backend-tutorial"
type: "concept"
domain: "edge-ai"
title: "Arm Cortex-M Backend: Tutorial"
summary: "For cross-compilation and running on simulated hardware: - Arm GNU Toolchain for cross compilation. - Arm® Corstone™ SSE-300 FVP or SSE-320 FVP for simulation."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/docs/source/backends/arm-cortex-m/arm-cortex-m-overview.md#tutorial"
license: "BSD-3-Clause"
mode: "V"
---

### Prerequisites

Install the ExecuTorch pip package:
```bash
./install_executorch.sh
```

For cross-compilation and running on simulated hardware:
- [Arm GNU Toolchain](https://developer.arm.com/Tools%20and%20Software/GNU%20Toolchain) for cross compilation.
- [Arm® Corstone™ SSE-300 FVP](https://developer.arm.com/documentation/100966/1128/Arm--Corstone-SSE-300-FVP) or [SSE-320 FVP](https://developer.arm.com/documentation/109760/0000/SSE-320-FVP) for simulation.

:::{tip}
All cross-compilation tools can be downloaded and added to the path:
```bash
examples/arm/setup.sh --i-agree-to-the-contained-eula
source examples/arm/arm-scratch/setup_path.sh
```
:::

### 1. Export and quantize

Export the model, then quantize using `CortexMQuantizer` with the PT2E quantization flow:

```python
import torch
from torchvision.models import mobilenet_v2, MobileNet_V2_Weights
from executorch.backends.cortex_m.quantizer.quantizer import CortexMQuantizer
from torchao.quantization.pt2e.quantize_pt2e import convert_pt2e, prepare_pt2e

model = mobilenet_v2(weights=MobileNet_V2_Weights.DEFAULT).eval()

example_input = torch.randn(1, 3, 224, 224).to(memory_format=torch.channels_last)
exported_program = torch.export.export(model, (example_input,))
graph_module = exported_program.module()

quantizer = CortexMQuantizer()
prepared = prepare_pt2e(graph_module, quantizer)

# Calibrate with representative data
for calibration_input in calibration_data:
    prepared(calibration_input)

quantized = convert_pt2e(prepared)
quantized_exported_program = torch.export.export(quantized, (example_input,))
```

Calibration observes logical tensor values, so calibration inputs do not need
to use the same memory format as the export example.

### 2. Lower to edge and apply Cortex-M passes

Lower to the edge dialect with the backend's `EdgeCompileConfig`, then apply `CortexMPassManager` through `EdgeProgramManager.transform()` to replace quantized subgraphs with CMSIS-NN operator implementations:

```python
from executorch.exir import ExecutorchBackendConfig, to_edge
from executorch.backends.cortex_m.edge_compile_config import (
    cortex_m_edge_compile_config,
)
from executorch.backends.cortex_m.passes.cortex_m_pass_manager import CortexMPassManager

# Use the backend's own configuration rather than hand-writing one. Ops such as
# silu and hardswish must survive to_edge for the Cortex-M passes to lower them,
# and omitting one does not degrade gracefully: an activation fails the
# AtenToCortexMPass, and linear silently falls back to portable float kernels.
config = cortex_m_edge_compile_config()

edge_program_manager = to_edge(quantized_exported_program, compile_config=config)

edge_program_manager = edge_program_manager.transform(CortexMPassManager())
```

Alternatively, pass `transform_passes=CortexMPassManager()` to
`to_edge_transform_and_lower()` with the same compile configuration.

### 3. Serialize to .pte

```python
executorch_program = edge_program_manager.to_executorch(
    config=ExecutorchBackendConfig(extract_delegate_segments=False)
)

with open("model.pte", "wb") as f:
    f.write(executorch_program.buffer)
```

### 4. Cross-compile and run

Cross-compile the ExecuTorch runtime, Cortex-M kernels, and the example runner application. The first cmake invocation builds the ExecuTorch libraries for Arm baremetal. The second builds the [arm_executor_runner](https://github.com/pytorch/executorch/blob/main/examples/arm/executor_runner/) and links it against those libraries with the `.pte` model baked in.

```bash
# Build ExecuTorch libraries for Arm baremetal
cmake --preset arm-baremetal \
  -DCMAKE_BUILD_TYPE=Release \
  -DEXECUTORCH_BUILD_DEVTOOLS=ON \
  -Bcmake-out-arm
cmake --build cmake-out-arm --target install -j$(nproc)

# Build the executor runner, linking the .pte into the binary
cmake -DCMAKE_TOOLCHAIN_FILE=$(pwd)/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake \
      -DCMAKE_BUILD_TYPE=Release \
      -DET_PTE_FILE_PATH=$(pwd)/model.pte \
      -DTARGET_CPU=cortex-m55 \
      -Bbuild \
      examples/arm/executor_runner
cmake --build build -j$(nproc) -- arm_executor_runner
```

Run on a simulated Cortex-M target:

```bash
backends/arm/scripts/run_fvp.sh --elf=build/arm_executor_runner --target=ethos-u55-128
```

For a complete end-to-end walkthrough including dataset setup, calibration, and result validation, see the [Cortex-M MobileNetV2 notebook](https://github.com/pytorch/executorch/blob/main/examples/arm/cortex_m_mv2_example.ipynb).
