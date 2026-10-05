---
id: "alp-zephyr-ml-cs320-mps4-how-to-1-pre-process-the-pytorch-model"
type: "concept"
domain: "edge-ai"
title: "Deploy a Zephyr-based machine learning application on Arm Corstone-320 MPS4 with ExecuTorch: Set up the Zephyr and ExecuTorch development environment: Pre-proce"
summary: "The ExecuTorch Ahead-of-Time (AOT) pipeline takes a PyTorch model (a torch.nn.Module) and produces a .pte binary file. The ExecuTorch runtime uses this file for inference."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/zephyr_ml_cs320_mps4/how-to-1.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/zephyr_ml_cs320_mps4/how-to-1/#pre-process-the-pytorch-model-for-npu-delegation"
license: "CC-BY-SA-4.0"
mode: "V"
---

The ExecuTorch [Ahead-of-Time (AOT)](https://github.com/pytorch/executorch/blob/main/examples/arm/aot_arm_compiler.py) pipeline takes a PyTorch model (a `torch.nn.Module`) and produces a `.pte` binary file. The ExecuTorch runtime uses this file for inference.

The following example shows a PyTorch model, `add.py`, that performs a single addition:

```python
import torch

b = 2

class myModelAdd(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x + x + b


ModelUnderTest = myModelAdd()
ModelInputs = (torch.ones(5),)
```
Run the following commands from the `modules/lib/executorch` directory to quantize the model and export it through the AOT flow using the Ethos-U backend:

```bash
source ~/zephyrproject/.venv/bin/activate
python3 -m executorch.backends.arm.scripts.aot_arm_compiler \
  --model_name=examples/arm/example_modules/add.py \
  -t ethos-u85-1024 \
  --delegate \
  --quantize \
  --memory_mode=Sram_Only \
  -o add_u85_1024_sram_only.pte
```
The following are key parameters used in the commands:

| Parameter | Value | Notes |
|-----------|-------|-------|
| `--model_name` | path to `.py` model file | Use absolute or workspace-relative path |
| `-t` / `--target` | `ethos-u85-1024` | Must match `CONFIG_ETHOS_U85_1024=y` in Kconfig |
| `--delegate` | (flag) | Enables Ethos-U NPU delegation via ArmBackend |
| `--quantize` | (flag) | Applies INT8 symmetric quantisation |
| `--memory_mode` | `Shared_Sram` or `Sram_Only` | Vela memory layout that must match the runtime build |
| `--system_config` | `Ethos_U85_SYS_DRAM_Mid` | (Optional) Selects Vela system config from `vela.ini` |
| `-o` | output filename | Saved in the project root by default |

The `add_u85_1024_sram_only.pte` file contains the model graph, quantized weights, and a Vela-compiled command stream. The Ethos-U85 executes the command stream directly.

Verify the model file was created:

```bash
ls -la add_u85_1024_sram_only.pte
```
