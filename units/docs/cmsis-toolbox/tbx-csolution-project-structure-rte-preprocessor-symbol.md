---
id: "tbx-csolution-project-structure-rte-preprocessor-symbol"
type: "concept"
domain: "project"
title: "CSolution Project Structure: Directory Structure / \\_RTE\\_ Preprocessor Symbol"
summary: "The preprocessor symbol RTE is added to the compiler invocation when a CMSIS build system manages the file RTE_Components.h. This symbol can be used as follows:"
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/build-overview.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#rte-preprocessor-symbol"
license: "Apache-2.0"
mode: "V"
---

_Part of: Directory Structure_

The preprocessor symbol `_RTE_` is added to the compiler invocation when a CMSIS build system manages the file `RTE_Components.h`. This symbol can be used as follows:

```c
#ifdef _RTE_                           // Is a CMSIS build system used?
#include "RTE_Components.h"            // Include Run-Time-Environment symbols
#else                                  // Otherwise, use different ways to supply required symbols
#define CMSIS_device_header "stm32f10x.h"
#endif
```
