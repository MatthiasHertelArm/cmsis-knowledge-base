---
id: "mlek-implementing-custom-ml-application-hardware-abstraction-layer-api"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Hardware Abstraction Layer API"
summary: "The HAL is represented by the following interfaces. To access them, include the hal.h header."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/customizing.md#hardware-abstraction-layer-api"
license: "Apache-2.0"
mode: "V"
---

The HAL is represented by the following interfaces. To access them, include the `hal.h` header.

- `hal_platform_init` function: Initializes the HAL platform and every module on the platform that the application
  requires to run.

  |  Parameter name | Description                             |
  |-----------------|-----------------------------------------|
  | `return`        | true if successful, false otherwise.    |

- `hal_platform_release` function Releases the HAL platform and any acquired resources.

An example of the API initialization in the main function:

```C++
#include "hal.h"

int main ()

{
  /* Initialise the HAL and platform */
  hal_platform_init();

  ...

  hal_platform_release();
  return 0;
}
```
