---
id: "etarm-getting-started-tutorial"
type: "concept"
domain: "edge-ai"
title: "Getting Started Tutorial"
summary: ":::{grid-item-card} Tutorials we recommend you complete before this: :class-card: card-prerequisites  Introduction to ExecuTorch  Getting Started  Building ExecuTorch with CMake :::"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md"
license: "BSD-3-Clause"
mode: "V"
---

<!----This will show a grid card on the page----->
::::{grid} 2

:::{grid-item-card}  Tutorials we recommend you complete before this:
:class-card: card-prerequisites
* [Introduction to ExecuTorch](https://github.com/pytorch/executorch/blob/658390c/docs/source/backends/arm-ethos-u/tutorials/intro-how-it-works.md)
* [Getting Started](https://github.com/pytorch/executorch/blob/658390c/docs/source/backends/arm-ethos-u/tutorials/getting-started.md)
* [Building ExecuTorch with CMake](https://github.com/pytorch/executorch/blob/658390c/docs/source/backends/arm-ethos-u/tutorials/using-executorch-building-from-source.md)
:::

:::{grid-item-card}  What you will learn in this tutorial:
:class-card: card-prerequisites
In this tutorial you will learn how to export a simple PyTorch model for the ExecuTorch Ethos-U backend.
:::

::::

```{tip}
If you are already familiar with this delegate, you may want to jump directly to the examples:
* [Examples in the ExecuTorch repository](https://github.com/pytorch/executorch/tree/main/examples/arm)
* [A commandline compiler for quick tests and example models](https://github.com/pytorch/executorch/blob/main/backends/arm/scripts/aot_arm_compiler.py)
```

This tutorial serves as an introduction to using ExecuTorch to deploy PyTorch models on Arm® Ethos™-U targets. It is based on `ethos_u_minimal_example.ipynb`, provided in Arm’s examples folder.
