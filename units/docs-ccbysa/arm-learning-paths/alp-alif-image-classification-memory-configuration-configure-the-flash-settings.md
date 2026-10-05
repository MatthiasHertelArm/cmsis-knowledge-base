---
id: "alp-alif-image-classification-memory-configuration-configure-the-flash-settings"
type: "concept"
domain: "edge-ai"
title: "Run image classification on an Alif Ensemble E8 DevKit using ExecuTorch and Ethos-U85: Configure memory layout and flash settings: Configure the flash settings"
summary: "The Security Toolkit needs a JSON configuration file that tells it where to load the binary in MRAM and which CPU should boot it."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/memory-configuration.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/memory-configuration/#configure-the-flash-settings"
license: "CC-BY-SA-4.0"
mode: "V"
---

The Security Toolkit needs a JSON configuration file that tells it where to load the binary in MRAM and which CPU should boot it.

Open (or create) `.alif/M55_HP_cfg.json` and set its contents to:

```json
{
  "DEVICE": {
    "disabled" : false,
    "binary": "app-device-config.json",
    "version" : "0.5.00",
    "signed": true
  },
  "USER_APP": {
    "binary": "alif-img.bin",
    "mramAddress": "0x80000000",
    "version": "1.0.0",
    "cpu_id": "M55_HP",
    "flags": ["boot"],
    "signed": false
  }
}
```

The key fields are:
- **`mramAddress`**: must match `APP_MRAM_HP_BASE` (0x80000000) from `app_mem_regions.h`.
- **`cpu_id`**: `M55_HP` tells the bootloader to start the High-Performance core.
- **`flags: ["boot"]`**: marks this application as the boot image.

You can view the completed versions of these edited files in the [workshop repository](https://github.com/ArmDeveloperEcosystem/workshop-ethos-u) for reference.

The memory layout and flash configuration are complete. The next section covers preparing the test image.
