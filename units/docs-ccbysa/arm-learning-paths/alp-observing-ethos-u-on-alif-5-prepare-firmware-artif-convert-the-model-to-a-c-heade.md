---
id: "alp-observing-ethos-u-on-alif-5-prepare-firmware-artif-convert-the-model-to-a-c-heade"
type: "concept"
domain: "edge-ai"
title: "Run MNIST on an Alif E8 Ensemble DevKit using ExecuTorch and Ethos-U85: Prepare the ExecuTorch model and static libraries for the Alif E8 CMSIS project: Convert"
summary: "The firmware embeds the .pte model as a byte array in flash memory. Use xxd to generate a C header:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/5-prepare-firmware-artifacts/#convert-the-model-to-a-c-header"
license: "CC-BY-SA-4.0"
mode: "V"
---

The firmware embeds the `.pte` model as a byte array in flash memory. Use `xxd` to generate a C header:


  **macOS and Linux:**
  cd ~/mnist_alif/executorch-alif/output
  xxd -i mnist_ethos_u85.pte > mnist_model_data.h
  

  **Windows (PowerShell):**
  cd ~\mnist_alif\executorch-alif\output
  & "$env:ProgramFiles\Git\usr\bin\xxd.exe" -i mnist_ethos_u85.pte | Set-Content -Encoding ascii mnist_model_data.h
  


Open the generated header (`mnist_model_data.h`) and change the first array declaration to the following:

```c
#include <stdint.h>
const uint8_t __attribute__((aligned(16))) mnist_ethos_u85_pte[] = {
```

**Important:**
The `aligned(16)` attribute is required because the Ethos-U85 needs the Vela command stream data aligned to 16 bytes. Without `aligned(16)`, the NPU driver will report an alignment error at runtime.
