---
id: "etarm-getting-started-tutorial-set-up-the-developer-environment"
type: "concept"
domain: "edge-ai"
title: "Getting Started Tutorial: Set Up the Developer Environment"
summary: "The setup.sh script generates a setup_path.sh script that you need to source whenever you restart your shell. Run:"
status: "draft"
collection: "executorch-arm"
source: "pytorch/executorch@658390c:docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md"
doc_source: "https://github.com/pytorch/executorch/blob/658390c/docs/source/backends/arm-ethos-u/tutorials/ethos-u-getting-started.md#set-up-the-developer-environment"
license: "BSD-3-Clause"
mode: "V"
---

The setup.sh script generates a setup_path.sh script that you need to source whenever you restart your shell. Run:

```{bash}
source  examples/arm/arm-scratch/setup_path.sh
```

As a simple check that your environment is set up correctly, run `which FVP_Corstone_SSE-320` and make sure that the executable is located where you expect, in the `examples/arm` tree.
