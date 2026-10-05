---
id: "etarm-getting-started-tutorial-build"
type: "concept"
domain: "edge-ai"
title: "Getting Started Tutorial: Build"
summary: "The ExecuTorch Ahead-of-Time (AOT) pipeline takes a PyTorch Model (a torch.nn.Module) and produces a .pte binary file, which is then consumed by the ExecuTorch Runtime."
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md#build"
license: "BSD-3-Clause"
mode: "V"
---

### Ahead-of-Time (AOT) components

The ExecuTorch Ahead-of-Time (AOT) pipeline takes a PyTorch Model (a `torch.nn.Module`) and produces a `.pte` binary file, which is then consumed by the ExecuTorch Runtime. This [document](https://github.com/pytorch/executorch/blob/658390c/docs/source/backends/arm-ethos-u/tutorials/getting-started-architecture.md) goes in much more depth about the ExecuTorch software stack for both AoT as well as Runtime.

The example below shows how to quantize a model consisting of a single addition, and export it it through the AOT flow using the EthosU backend. For more details, see `examples/arm/ethos_u_minimal_example.ipynb`.
```python
import torch

class Add(torch.nn.Module):
    def forward(self, x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
        return x + y

example_inputs = (torch.ones(1,1,1,1),torch.ones(1,1,1,1))

model = Add()
model = model.eval()
exported_program = torch.export.export(model, example_inputs)
graph_module = exported_program.module(check_guards=False)


from executorch.backends.arm.ethosu import EthosUCompileSpec
from executorch.backends.arm.quantizer import (
    EthosUQuantizer,
    get_symmetric_quantization_config,
)
from torchao.quantization.pt2e.quantize_pt2e import convert_pt2e, prepare_pt2e

# Create a compilation spec describing the target for configuring the quantizer
# Some args are used by the Arm Vela graph compiler later in the example. Refer to Arm Vela documentation for an
# explanation of its flags: https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela/-/blob/main/OPTIONS.md
compile_spec = EthosUCompileSpec(
            target="ethos-u55-128",
            system_config="Ethos_U55_High_End_Embedded",
            memory_mode="Shared_Sram",
        )

# Create and configure quantizer to use a symmetric quantization config globally on all nodes
quantizer = EthosUQuantizer(compile_spec)
operator_config = get_symmetric_quantization_config()
quantizer.set_global(operator_config)

# Post training quantization
quantized_graph_module = prepare_pt2e(graph_module, quantizer)
quantized_graph_module(*example_inputs) # Calibrate the graph module with the example input
quantized_graph_module = convert_pt2e(quantized_graph_module)


# Create a new exported program using the quantized_graph_module
quantized_exported_program = torch.export.export(quantized_graph_module, example_inputs)
from executorch.backends.arm.ethosu import EthosUPartitioner
from executorch.exir import (
    EdgeCompileConfig,
    ExecutorchBackendConfig,
    to_edge_transform_and_lower,
)
from executorch.extension.export_util.utils import save_pte_program

# Create partitioner from compile spec
partitioner = EthosUPartitioner(compile_spec)

# Lower the exported program to the Ethos-U backend
edge_program_manager = to_edge_transform_and_lower(
            quantized_exported_program,
            partitioner=[partitioner],
            compile_config=EdgeCompileConfig(
                _check_ir_validity=False,
            ),
        )

# Convert edge program to executorch
executorch_program_manager = edge_program_manager.to_executorch(
            config=ExecutorchBackendConfig(extract_delegate_segments=False)
        )


# Save pte file
save_pte_program(executorch_program_manager, "ethos_u_minimal_example.pte")
```


```{tip}
For a quick test, you can use the script `backends/arm/scripts/aot_arm_compiler.py` to produce the pte.
To produce a pte file equivalent to the one above, run
`python -m backends.arm.scripts.aot_arm_compiler --model_name=add --delegate --quantize --output=ethos_u_minimal_example.pte`.
For production use, you should instead use the stable Python API shown above.
```

### Runtime:

After the AOT compilation flow is done, the runtime can be cross compiled and linked to the produced `.pte`-file using the Arm cross-compilation toolchain. Configure the standalone Arm executor runner CMake project to pull in the ExecuTorch build graph, link the Ethos-U delegate, and generate kernel bindings for any non-delegated ops. This produces the `arm_executor_runner` program that will run on target.

```
# In ExecuTorch top-level, with sourced setup_path.sh
cmake -S examples/arm/executor_runner/standalone \
      -B ethos_u_minimal_example \
      -DEXECUTORCH_ROOT=$(pwd) \
      -DCMAKE_TOOLCHAIN_FILE=$(pwd)/examples/arm/ethos-u-setup/arm-none-eabi-gcc.cmake \
      -DCMAKE_BUILD_TYPE=Release \
      -DET_PTE_FILE_PATH=ethos_u_minimal_example.pte \
      -DTARGET_CPU=cortex-m55 \
      -DETHOSU_TARGET_NPU_CONFIG=ethos-u55-128 \
      -DMEMORY_MODE=Shared_Sram \
      -DSYSTEM_CONFIG=Ethos_U55_High_End_Embedded
cmake --build ethos_u_minimal_example -j$(nproc) -- arm_executor_runner
```

```{tip}
For a quick start, you can use the script `backends/arm/scripts/build_executor_runner.sh` to configure and build the standalone runner.
To build a runner equivalent to the one above, run
`./backends/arm/scripts/build_executor_runner.sh --pte=ethos_u_minimal_example.pte`
```

The block diagram below shows, at the high level, how the various build artifacts are generated and are linked together to generate the final bare-metal executable.


