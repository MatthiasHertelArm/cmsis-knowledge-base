---
id: "mlek-implementing-custom-ml-application-application-context"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Application context"
summary: "Application context can be used as a holder for a state between main loop iterations. Include AppContext.hpp to use ApplicationContext class."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/customizing.md#application-context"
license: "Apache-2.0"
mode: "V"
---

Application context can be used as a holder for a state between main loop iterations. Include `AppContext.hpp` to use
`ApplicationContext` class.

| Method name | Description                                                     |
|-------------|-----------------------------------------------------------------|
| `Set`       | Saves given value as a named attribute in the context.          |
| `Get`       | Gets the saved attribute from the context by the given name.    |
| `Has`       | Checks if an attribute with a given name exists in the context. |

For example:

```C++
#include "hal.h"
#include "AppContext.hpp"

void MainLoop()
{
    /* Instantiate application context */
    arm::app::ApplicationContext caseContext;
    caseContext.Set<uint32_t>("counter", 0);

    /* loop */
    while (true) {
        // do something, pass application context down the call stack
    }
}
```
