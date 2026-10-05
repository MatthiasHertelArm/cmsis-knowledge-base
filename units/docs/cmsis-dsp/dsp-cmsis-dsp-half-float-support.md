---
id: "dsp-cmsis-dsp-half-float-support"
type: "concept"
domain: "optimization"
title: "CMSIS-DSP: Half float support"
summary: "f16 data type (half float) has been added to the library. It is useful only if your Cortex has some half float hardware acceleration (for instance with Helium extension)."
status: "draft"
collection: "cmsis-dsp"
source: "ARM-software/CMSIS-DSP@83a2d7b:README.md"
doc_source: "https://github.com/ARM-software/CMSIS-DSP/blob/83a2d7b/README.md#half-float-support"
license: "Apache-2.0"
mode: "V"
---

`f16` data type (half float) has been added to the library. It is useful only if your Cortex has some half float hardware acceleration (for instance with Helium extension). If you don't need `f16`, you should disable it since it may cause compilation problems. Just define `-DDISABLEFLOAT16` when building.
