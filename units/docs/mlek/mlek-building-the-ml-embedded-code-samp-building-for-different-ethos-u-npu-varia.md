---
id: "mlek-building-the-ml-embedded-code-samp-building-for-different-ethos-u-npu-varia"
type: "concept"
domain: "edge-ai"
title: "Building the ML embedded code sample applications from sources: Building for different Ethos-U NPU variants"
summary: "The building process described in the previous paragraphs assumes building for the default Ethos-U55 NPU with 128 MACs, using the Ethos-U55 High End timing adapter system configuration."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/building.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/building.md#building-for-different-ethos-u-npu-variants"
license: "Apache-2.0"
mode: "V"
---

The building process described in the previous paragraphs assumes building for the default *Ethos-U55* NPU with 128 MACs,
using the *Ethos-U55* High End timing adapter system configuration.

To build for a different *Ethos-U* NPU variant:

- Optimize the model with Vela compiler with the correct parameters. See [Optimize custom model with Vela compiler](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#optimize-custom-model-with-vela-compiler).
- Use the correct `ETHOS_U_NPU_ID`: `U55` for *Ethos-U55* NPU, `U65` for *Ethos-U65* NPU or `U85` for *Ethos-U85*.
- Use the Vela model as custom model in the building command. See [Add custom model](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#add-custom-model)
- Use the correct timing adapter settings configuration. See [Building timing adapter with custom options](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./building.md#building-timing-adapter-with-custom-options)

For example, when building for *Ethos-U65* High End system configuration and 512 MACs/cc, the Vela command will be:

```commandline
vela \
    <model_file>.tflite \
    --accelerator-config ethos-u65-512 \
    --optimise Performance \
    --memory-mode=Dedicated_Sram \
    --system-config=Ethos_U65_High_End \
    --config=../scripts/vela/default_vela.ini
```

And the cmake command:

```commandline
cmake .. \
    -DETHOS_U_NPU_ID=U65 \
    -D<use_case>_MODEL_PATH=<path/to/ethos_u65_vela_model.tflite>
```
