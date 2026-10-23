---
id: "etarm-introduction-coupling-between-the-aot-compile-specifi"
type: "concept"
domain: "edge-ai"
title: "Introduction: Coupling between the AoT compile specification memory mode, linker script and the application logic"
summary: "It is important to note that when you specify a memory mode in the Python script to generate the pte file, in the runtime, the user is expected to place the scratch buffer and NN in the correct memory location."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@24a6116:examples/arm/ethos-u-porting-guide.md"
doc_source: "https://github.com/pytorch/executorch/blob/24a6116/examples/arm/ethos-u-porting-guide.md#coupling-between-the-aot-compile-specification-memory-mode-linker-script-and-the"
license: "BSD-3-Clause"
mode: "V"
---

It is important to note that when you specify a memory mode in the Python script to generate the pte file, in the runtime, the user is
expected to place the scratch buffer and NN in the correct memory location.

For example, if you generate a pte file with compile specification for Shared Sram, the scratch buffer should be placed in the SRAM and the NN in the external memory in the runtime application code. You can see we are following
this approach in the `examples/arm/executor_runner/arm_executor_runner.cpp` example application. In the linker scripts for the application(`examples/arm/executor_runner/Corstone-320.ld` and
`examples/arm/executor_runner/Corstone-300.ld`) we check the value of `ETHOSU_ARENA` to determine whether the ethos-u scratch buffer is placed in the on-chip memory or in the external memory. In this
way, depending on the `ETHOSU_ARENA` parameter, the linker knows whether the input section is to be placed in the .ddr.bss or .sram.bss sections. The `ETHOSU_ARENA` parameter is set in the `backends/arm/scripts/corstone_utils.cmake` and
its value is derived based on the memory mode parameter that is passed to the `examples/arm/run.sh` shell script. Then, at link time, the .ddr.bss section is always placed in the external memory and the .sram.bss is always placed in the SRAM.
Finally, note that in the `examples/arm/executor_runner/arm_executor_runner.cpp` application code, we place the buffers for the Ethos-u scratch and the neural network in the correct symbol from the linker script. For instance,
the Ethos-u scratch buffer corresponds to the the `.bss.tensor_arena` input section in the linker script, In the application code, when we allocate memory for the Ethos-u scratch buffer, we place this array in the .bss.tensor_arena section in the memory map.
The same runner also supports ExecuTorch memory-planned tensors in `SLOW_MEMORY_REGION` for `mem_id=1` and `mem_id=2`, and in `FAST_MEMORY_REGION` for `mem_id=3`, backed by the `.fast_memory` input section in `.sram.bss` and sized with `ET_ARM_BAREMETAL_PLANNED_FAST_MEMORY_SIZE`.

```
unsigned char __attribute__((
    section(".bss.tensor_arena"),
    aligned(16))) temp_allocation_pool[temp_allocation_pool_size];
```
and the `.bss.tensor_arena` input section is placed in the correct location in the memory map thanks to
the `ETHOSU_ARENA` parameter.

There is a tight coupling between the memory mode for the Ethos-U and the placement of the ethos-u scratch buffer,
ethos-u-fast scratch buffer (only applicable for Dedicated_Sram) and the neural network in the memory map of the
SoC. The `arm_executor_runner.cpp` application built with the `examples/arm/run.sh` shell script and corresponding linker scripts are aimed to serve as
example implementation for the correct placement of the various objects in memory.

It's also worth mentioning that in the AoT Python flow, by default the input to the pte file is in FP32. Therefore, the pte file contains a Quantize node, an Ethos-U custom delegate and a Dequantize node.
Sometimes, you may want to feed quantized input to the Ethos-U custom delegate straight away, for example if you have a camera input outputting RGB data in (u)int8. You can apply the `QuantizeInputs` and
`QuantizeOutputs` passes in the AoT flow for that purpose. Here is a snippet showing how to achieve it:
```
edge_program_manager = to_edge_transform_and_lower(...)
from executorch.exir.passes.quantize_io_pass import QuantizeInputs
from executorch.exir.passes.quantize_io_pass import QuantizeOutputs
# Apply the QuantizeInputs & QuantizeOutputs passes to input & output tensor 0
edge_program_manager.transform(passes=[QuantizeInputs(edge_program_manager, [0]),
                      QuantizeOutputs(edge_program_manager, [0])])
# Convert edge program to executorch
executorch_program_manager = edge_program_manager.to_executorch(
            config=ExecutorchBackendConfig(extract_delegate_segments=False)
        )
```
If you apply  the `QuantizeInputs` pass in the AoT flow, when you populate the input tensor in the runtime application logic, you need to use int8 numbers and not FP32. In the `examples/arm/executor_runner/arm_executor_runner.cpp` application, you can see
how we populate the input tensor depending on its data type.
