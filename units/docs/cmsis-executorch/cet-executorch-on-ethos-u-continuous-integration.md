---
id: "cet-executorch-on-ethos-u-continuous-integration"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch on Ethos-U: Continuous integration"
summary: "Two GitHub Actions workflows validate the supplied Ethos-U configurations on every push and pull request to main."
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/README.md#continuous-integration"
license: "Apache-2.0"
mode: "V"
---

Two GitHub Actions workflows validate the supplied Ethos-U configurations on
every push and pull request to `main`. They create the Python environment,
generate the target-specific AI layer, build the Corstone-320/Ethos-U85-256 and
Corstone-300/Ethos-U55-128 solutions with AC6, GCC, and Clang, run each
application on its FVP simulation model, verify the reported test result, and
upload the build artifacts. A separate workflow verifies the Python environment
setup on Linux, macOS, and Windows. The badges at the top of this README show
the current status of all three workflows.
