---
id: "cet-executorch-on-ethos-u-prerequisites"
type: "concept"
domain: "edge-ai"
title: "ExecuTorch on Ethos-U: Prerequisites"
summary: "Keil Studio manages the required license; the free Keil MDK Community edition can be used for evaluation."
status: "draft"
collection: "cmsis-executorch"
source: "Arm-Examples/CMSIS-Executorch@0a243f1:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Executorch/blob/0a243f1/README.md#prerequisites"
license: "Apache-2.0"
mode: "V"
---

- [Git](https://git-scm.com/) to clone the repository created from this template.
- [Keil Studio for VS Code](https://marketplace.visualstudio.com/items?itemName=Arm.keil-studio-pack) from the VS Code marketplace.
- [Python extension for VS Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
- [Astral's uv](https://docs.astral.sh/uv/getting-started/installation/) on `PATH` for the
  recommended environment task, or an installed Python `>=3.10,<3.14` for pip.
- On macOS, follow [FVPs on macOS](https://github.com/Arm-Examples/FVPs-on-Mac)
  to install Docker Desktop and configure the FVP environment.

Keil Studio manages the required license; the free Keil MDK Community edition
can be used for evaluation.

> [!NOTE]
> On Windows, enable [long-path support](https://learn.microsoft.com/windows/win32/fileio/maximum-file-path-limitation#enable-long-paths-in-windows-10-version-1607-and-later).
