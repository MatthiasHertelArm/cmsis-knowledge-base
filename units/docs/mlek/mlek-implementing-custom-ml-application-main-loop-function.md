---
id: "mlek-implementing-custom-ml-application-main-loop-function"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Main loop function"
summary: "Code samples application main function delegates the use-case logic execution to the main loop function that must be implemented for each custom ML scenario."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/customizing.md#main-loop-function"
license: "Apache-2.0"
mode: "V"
---

Code samples application main function delegates the use-case logic execution to the main loop function that must be
implemented for each custom ML scenario.

The main loop function has external linkage and the main executable for the use-case references the function defined in
the use-case code.

```C++
void MainLoop()
{

...

}
```
