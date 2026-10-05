---
id: "alp-alif-dual-npu-vision-build-application-optional-regenerate-the-pte-mo"
type: "concept"
domain: "edge-ai"
title: "Run parallel vision inference on an Alif Ensemble E8 with Zephyr: Build the dual-NPU application: (Optional) Regenerate the PTE models"
summary: "Skip this section unless you want to reproduce or modify the model artifacts. Use a Linux development host for the optional model-generation flow."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/build-application.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-dual-npu-vision/build-application/#optional-regenerate-the-pte-models"
license: "CC-BY-SA-4.0"
mode: "V"
---

Skip this section unless you want to reproduce or modify the model artifacts. Use a Linux development host for the optional model-generation flow.

The pinned Vela 5.0.0 and TOSA Tools 2026.2.1 packages declare different FlatBuffers versions. Install the validated combination with the supplied helper. It keeps Vela's FlatBuffers 24.3.25 and installs TOSA Tools without resolving its conflicting FlatBuffers dependency:

```bash
"$APP/tools/install_model_export_deps.sh"
```

Create a directory for the source weights:

```bash
cd $HOME/alif-dual-npu
mkdir -p model-weights
```

Download the trained [SSD-Slim int8 model](https://github.com/emza-vs/ModelZoo/blob/59fcdb2aab865a8a8d93a9d419b3c5490a5508e4/Models/Object_detection/SSD/ssd_slim_120x160x1_v1_int8.tflite) and the official [torchvision MobileNetV2 checkpoint](https://download.pytorch.org/models/mobilenet_v2-7ebf99e0.pth). The SSD URL is pinned to the commit that added the model:

```bash
curl -L \
  https://raw.githubusercontent.com/emza-vs/ModelZoo/59fcdb2aab865a8a8d93a9d419b3c5490a5508e4/Models/Object_detection/SSD/ssd_slim_120x160x1_v1_int8.tflite \
  -o model-weights/ssd_slim_120x160x1_v1_int8.tflite
curl -L \
  https://download.pytorch.org/models/mobilenet_v2-7ebf99e0.pth \
  -o model-weights/mobilenet_v2-7ebf99e0.pth
```

Verify both downloads before using them:

```bash
echo "64fcc31aa517798d0e798551418c85bc0a5ed03a75c45c4e47fc7ee41e5ea51f  model-weights/ssd_slim_120x160x1_v1_int8.tflite" | shasum -a 256 -c -
echo "7ebf99e03e254b273379b23edca7ec0da9f48273b23a332b93c1c99d49e86e8f  model-weights/mobilenet_v2-7ebf99e0.pth" | shasum -a 256 -c -
```

The SSD source repository doesn't publish a PyTorch checkpoint. Use the sample's importer to convert the trained, quantized constants into the common PyTorch checkpoint:

```bash
.venv-executorch/bin/python \
  "$APP/tools/import_ssd_slim_tflite.py" \
  --source model-weights/ssd_slim_120x160x1_v1_int8.tflite \
  --output model-weights/ssd_slim_common.pth
```

Generate both PTE files with the Alif Vela configuration included in the SDK:

```bash
"$APP/tools/generate_pte_models.sh" \
  "$PWD/sdk-alif/samples/modules/executorch/ensemble_vela.ini" \
  "$PWD/model-weights/ssd_slim_common.pth" \
  "$PWD/model-weights/mobilenet_v2-7ebf99e0.pth"
```

The script emits `comparable_ssd_slim_u55.pte` and `mobilenet_v2_imagenet_u85.pte` in the sample's `models` directory. The export uses PT2E quantization, deterministic representative inputs, the ExecuTorch Ethos-U partitioner, and Vela. Both programs expose `int8` tensors and require complete delegation, with no Cortex-M fallback operators. The SSD checkpoint is produced by the supplied offline weight-import tool. Both deployed files are native ExecuTorch PTE programs.
