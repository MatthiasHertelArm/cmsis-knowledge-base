---
id: "mlek-implementing-custom-ml-application-adding-custom-ml-use-case"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Adding custom ML use-case"
summary: "This section describes how to implement additional use-case and then compile it into the binary executable to run with Fast Model or MPS3 FPGA board."
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/customizing.md#adding-custom-ml-use-case"
license: "Apache-2.0"
mode: "V"
---

This section describes how to implement additional use-case and then compile it into the binary executable to run with
Fast Model or MPS3 FPGA board.

It covers common major steps: The application main loop creation, a description of the NN model, and inference
execution.

In addition, some useful examples are provided: Printing into console, and drawing images into MPS3 LCD.

For example:

```tree
source/app/use_case
   └── hello_world
         ├── include
         └── src
```

Start with creation of a subdirectory under the `source/app/use_case` directory and two additional directories `src` and
`include` as described in the [Software project description](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./customizing.md#software-project-description) section.
