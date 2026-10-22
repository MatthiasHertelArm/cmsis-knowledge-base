---
id: "mlek-troubleshooting-missing-libpython-when-running-fvp"
type: "concept"
domain: "edge-ai"
title: "Troubleshooting: Missing libpython when running FVP"
summary: "When running an FVP, you may encounter the following error:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/troubleshooting.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/troubleshooting.md#missing-libpython-when-running-fvp"
license: "Apache-2.0"
mode: "V"
---

When running an FVP, you may encounter the following error:

```commandline
FVP_Corstone_SSE-320: error while loading shared libraries: libpython3.9.so.1.0: cannot open shared object file: No such file or directory
```
This occurs when the `libpython3.9-dev` is missing on your system.  To resolve the issue, install the library as per the instructions [here](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/./deployment.md#arm_corstone_320-fvp).
