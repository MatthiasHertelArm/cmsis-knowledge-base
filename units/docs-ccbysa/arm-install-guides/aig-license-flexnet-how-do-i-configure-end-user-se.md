---
id: "aig-license-flexnet-how-do-i-configure-end-user-se"
type: "concept"
domain: "project"
title: "FlexNet Publisher Floating license setup: How do I configure end-user setup?"
summary: "End-users should set the environment variable ARMLMD_LICENSE_FILE to map to the location of your license server."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/license/flexnet.md"
doc_source: "https://learn.arm.com/install-guides/license/flexnet/#how-do-i-configure-end-user-setup"
license: "CC-BY-SA-4.0"
mode: "V"
---

End-users should set the environment variable `ARMLMD_LICENSE_FILE` to map to the location of your license server.

#### Windows
```console
set ARMLMD_LICENSE_FILE=port@server
```
#### Linux
```console
export ARMLMD_LICENSE_FILE=port@server
```

### How do I activate the license via tools IDE?

The license can also be activated in the various Arm tool IDEs.

For example [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio), via `Help` > `Arm License Manager`.

If `ARMLMD_LICENSE_FILE` is not set, use `Add` > `Add product license`, and specify `port` and `server` information for your license server.

Arm Development Studio will also ask to specify the appropriate [Edition](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio#Editions) as the `Active Product`.

### How do I verify the license setup?

To verify that the license is set up correctly, set the following environment variable:

#### Windows
```console
set FLEXLM_DIAGNOSTICS=3
```
#### Linux
```console
export FLEXLM_DIAGNOSTICS=3
```

and execute an appropriate Arm tool, for example `Arm Compiler for Embedded`:
```command
armclang --version
```

Observe the output, which will be similar to:
```output
Checkout succeeded: ds_suite_rowan/04C6 0E2A CDA4 6344
        License file: port@server
        License Server: port@server
Checkout succeeded: ds_compiler_rowan/141D C968 2E7F 4187
        License file: port@server
        License Server: port@server
Product: Arm Development Studio Gold Edition 2023.1
Component: Arm Compiler for Embedded 6.21
```

**Note:**
Unset the `FLEXLM_DIAGNOSTICS` environment variable afterwards, as this will impact the tools performance.
