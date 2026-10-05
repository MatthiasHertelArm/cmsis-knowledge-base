---
id: "mlek-implementing-custom-ml-application-implementing-main-loop"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Implementing main loop"
summary: "The use-case main loop is the place to put use-case main logic. It is an infinite loop that triggers use-case conditional logic based on the input and present results back to the user."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/customizing.md#implementing-main-loop"
license: "Apache-2.0"
mode: "V"
---

The use-case main loop is the place to put use-case main logic. It is an infinite loop that
triggers use-case conditional logic based on the input and present results back to the user.

However, it could also be a simple logic that runs a single inference and then exits.

Main loop has knowledge about the platform and has access to the platform components through the Hardware Abstraction
Layer (HAL).

Start by creating a `MainLoop.cc` file in the `src` directory (the one created under
[Adding custom ML use-case](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#adding-custom-ml-use-case)).  The name used is not important.

Now define the `MainLoop` function with the signature described in [Main loop function](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#main-loop-function):

```C++
#include "hal.h"
#include "mlek/log/log_macros.h"

void MainLoop()
{
    printf("Hello world!");
}
```

The preceding code is already a working use-case. If you compile and run it (see [Building custom use-case](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./customizing.md#building-custom-use_case)),
then the application starts and prints a message to console and exits straight away.

You can now start filling this function with logic.
