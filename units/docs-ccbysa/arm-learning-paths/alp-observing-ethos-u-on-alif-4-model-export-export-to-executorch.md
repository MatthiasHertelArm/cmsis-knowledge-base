---
id: "alp-observing-ethos-u-on-alif-4-model-export-export-to-executorch"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: (Optional) Export PyTorch model to ExecuTorch format: Export to ExecuTorch"
summary: "Export the trained model to .pte format for Ethos-U85:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/4-model-export.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/4-model-export/#export-to-executorch"
license: "CC-BY-SA-4.0"
mode: "V"
---

Export the trained model to `.pte` format for Ethos-U85:

```bash
cd $ET_HOME
MNIST_LOAD_CHECKPOINT=1 python3 -m examples.arm.aot_arm_compiler --model_name=/home/developer/models/mnist_model.py --delegate --quantize --target=ethos-u85-256 --system_config=Ethos_U85_SYS_DRAM_Mid --memory_mode=Shared_Sram --output=/home/developer/output/mnist_ethos_u85.pte
```
**Important:**
Use full paths such as `/home/developer/models/mnist_model.py`. Don't use `~` in the export command.


The following are the arguments passed in the export command:
- `MNIST_LOAD_CHECKPOINT=1`: loads the trained weights from `/home/developer/models/mnist_model.pth`.
- `--model_name`: points to the PyTorch model definition.
- `--delegate`: partitions supported operators for execution on the Ethos-U NPU.
- `--quantize`: converts the model for int8 inference.
- `--target=ethos-u85-256`: targets an Ethos-U85 configuration with 256 MACs per cycle.
- `--system_config` and `--memory_mode`: select the Vela memory configuration used when compiling the NPU command stream.
- `--output`: writes the exported ExecuTorch program.

Vela is Arm’s compiler for Ethos-U NPUs. During export, it prints information about the selected Ethos-U target, memory use, and NPU performance estimates. Review this output to confirm that the model was compiled for the expected `ethos-u85-256` target. 

At the end, you should see confirmation of the saved `.pte` file as follows:

```output
PTE file saved as /home/developer/output/mnist_ethos_u85.pte
```
