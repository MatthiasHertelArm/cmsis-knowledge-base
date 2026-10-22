---
id: "tbx-pyocd-debugger-minimal-setup"
type: "concept"
domain: "debug"
title: "pyOCD Debugger: Minimal Setup"
summary: "pyOCD uses the information from the CMSIS system as explained under Build Information Files: Run and Debug Management. The following section shows a minimal setup for configuring pyOCD using a .cbuild-run.yml file."
status: "draft"
collection: "cmsis-toolbox"
source: "Open-CMSIS-Pack/cmsis-toolbox@3ce8307:docs/pyOCD-Debugger.md"
doc_source: "https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/#minimal-setup"
license: "Apache-2.0"
mode: "V"
---

pyOCD uses the information from the CMSIS system as explained under [Build Information Files: Run and Debug Management](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/YML-CBuild-Format.md#run-and-debug-management). The following section shows a minimal setup for configuring pyOCD using a `*.cbuild-run.yml` file.

**Example:** MySetup.csolution.yml

```yml
solution:
  packs:
    - pack: Infineon::PSE8xxx_DFP@1.0.1     # Device Family Pack (DFP)

  target-types:
    - type: PSE8_Target                     # Target name
      device: PSE812GOS2DFNC4B              # Device name from DFP
      target-set:
        - set:
          images:
            - image: out/MyFile.hex         # Image files used
          debugger:
            name: CMSIS-DAP@pyOCD           # Debugger configuration
            clock: 10000000
            protocol: swd
```

To generate the related `*.cbuild-run.yml` file for pyOCD run the following CMSIS-Toolbox commands:

```bash
cpackget add Infineon::PSE8xxx_DFP@1.0.1
cbuild setup MySetup.csolution.yml --active PSE8_Target
```

This creates the file `out/MySetup+PSE8_Target.cbuild-run.yml` that can be used for the [command line invocation](#command-line-invocation).
