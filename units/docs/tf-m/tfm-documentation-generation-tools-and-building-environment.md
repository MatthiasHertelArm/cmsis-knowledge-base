---
id: "tfm-documentation-generation-tools-and-building-environment"
type: "concept"
domain: "security"
title: "Documentation generation: Tools and building environment"
summary: "These tools are used to generate TF-M documentation:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/building/documentation_generation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/building/documentation_generation.html#tools-and-building-environment"
license: "BSD-3-Clause"
mode: "V"
---

These tools are used to generate TF-M documentation:

    - Doxygen v1.8.0 or later
    - Graphviz dot v2.38.0 or later
    - PlantUML v1.2018.11 or later
    - Java runtime environment v1.8 or later (for running PlantUML)
    - (Optional) `uv <https://docs.astral.sh/uv/getting-started/installation/#standalone-installer>`

Additionally, for PDFs format:

    - LaTeX
    - PdfLaTeX

There are two ways of building TF-M reference manual:

    1. As a custom target of TF-M CMake build system
    2. Directly, using the command line tools


To prepare your building environment execute the following steps:
