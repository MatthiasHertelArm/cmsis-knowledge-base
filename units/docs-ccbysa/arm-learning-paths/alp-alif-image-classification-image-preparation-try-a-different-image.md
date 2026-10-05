---
id: "alp-alif-image-classification-image-preparation-try-a-different-image"
type: "concept"
domain: "edge-ai"
title: "image preparation: Try a different image"
summary: "To classify a different image, change the filename in prepare_image.py:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/alif-image-classification/image-preparation.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/alif-image-classification/image-preparation/#try-a-different-image"
license: "CC-BY-SA-4.0"
mode: "V"
---

To classify a different image, change the filename in `prepare_image.py`:

```python
img = Image.open("dog.jpg").convert("RGB")
```

Re-run the script and copy the updated header to the project. Rebuild and flash to see the new classification result.

The model classifies among 1000 ImageNet categories. Some common class ranges:
- **Cats**: 281-285 (281=tabby, 282=tiger cat, 283=Persian cat, 284=Siamese, 285=Egyptian cat)
- **Dogs**: 151-268 (various breeds)
- **Birds**: 7-23
- **Vehicles**: 407=ambulance, 436=beach wagon, 511=convertible, 609=jeep, 817=sports car

For a complete list, search for "ImageNet 1000 class labels" online.

The test image is ready. The next section covers building, flashing, and verifying the inference output.
