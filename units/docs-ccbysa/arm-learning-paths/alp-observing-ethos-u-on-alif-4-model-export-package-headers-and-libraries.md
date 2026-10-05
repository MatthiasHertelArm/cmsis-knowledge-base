---
id: "alp-observing-ethos-u-on-alif-4-model-export-package-headers-and-libraries"
type: "concept"
domain: "edge-ai"
title: "4 model export: Package headers and libraries"
summary: "Bundle the ExecuTorch headers and libraries into et_bundle.tar.gz:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/4-model-export.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-alif/4-model-export/#package-headers-and-libraries"
license: "CC-BY-SA-4.0"
mode: "V"
---

Bundle the ExecuTorch headers and libraries into `et_bundle.tar.gz`:

```bash
rm -rf /home/developer/output/et_bundle
mkdir -p /home/developer/output/et_bundle
cp -a arm_test/cmake-out/include /home/developer/output/et_bundle/
cp -a arm_test/cmake-out/lib /home/developer/output/et_bundle/
CMSIS_NN_LIB=$(find arm_test/cmake-out -type f -name "libcmsis-nn.a" | head -n 1)
cp "$CMSIS_NN_LIB" /home/developer/output/et_bundle/lib/
tar -C /home/developer/output -czf /home/developer/output/et_bundle.tar.gz et_bundle
```

Because `/home/developer/output` is mounted from your host machine, `et_bundle.tar.gz` is now available on your host at `~/mnist_alif/executorch-alif/output/et_bundle.tar.gz`.

Exit Docker:

```bash
exit
```
