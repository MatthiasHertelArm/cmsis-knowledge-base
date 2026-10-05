---
id: "alp-alif-image-classification-aws-ec2-setup-transfer-artifacts-to-your-dev"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Compile the model on an Arm cloud instance: Transfer artifacts to your de"
summary: "Run these commands on your development machine, not on the EC2 instance. The paths below use ~/alif/ as the working directory; adjust these to match your own project location:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/aws-ec2-setup/#transfer-artifacts-to-your-development-machine"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run these commands on your development machine, not on the EC2 instance. The paths below use `~/alif/` as the working directory; adjust these to match your own project location:

```bash
mkdir -p ~/alif/models
mkdir -p ~/alif/third_party/executorch/lib

scp alif:/home/ubuntu/alif/models/mv2_ethosu85_256.pte ~/alif/models/
scp alif:/home/ubuntu/alif/et_bundle.tar.gz ~/alif/models/
scp 'alif:/home/ubuntu/alif/executorch/arm_test/cmake-out/lib/*.a' \
  ~/alif/third_party/executorch/lib/
```

Verify the transfer:

```bash
ls -lh ~/alif/models/mv2_ethosu85_256.pte
ls ~/alif/third_party/executorch/lib/*.a | wc -l
```

The output shows the 3.7 MB model file and 13 library files.
