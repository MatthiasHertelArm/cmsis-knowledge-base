---
id: "csx-simple-trustzone-application-use-an-existing-secure-image"
type: "concept"
domain: "project"
title: "Simple TrustZone Application: Use an Existing Secure Image"
summary: "The AVH-NS-only target demonstrates the CMSIS-Toolbox concept Use a Prebuilt Secure Image. It builds only CM33ns and reuses two outputs previously generated for the AVH target:"
status: "draft"
collection: "csolution-examples"
source: "Open-CMSIS-Pack/csolution-examples@02f71b2:SimpleTrustZone/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/csolution-examples/blob/02f71b2/SimpleTrustZone/README.md#use-an-existing-secure-image"
license: "Apache-2.0"
mode: "V"
---

The `AVH-NS-only` target demonstrates the CMSIS-Toolbox concept [Use a Prebuilt Secure Image](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/#use-a-prebuilt-secure-image). It builds only `CM33_ns` and reuses two outputs previously generated for the `AVH` target:

- `CM33_s.hex`, which is loaded together with the non-secure application.
- `CM33_s_CMSE_Lib.o`, which provides the secure callable interface used to link the non-secure application.

The existing secure outputs must match the selected build type and compiler. Build the `AVH` target before building the corresponding `AVH-NS-only` target:

```txt
> cbuild SimpleTZ.csolution.yml --packs --active AVH@Debug --toolchain AC6
> cbuild SimpleTZ.csolution.yml --context CM33_ns.Debug+AVH-NS-only --toolchain AC6
```

When using VS Code, first select and build `AVH@Debug` or `AVH@Release` in the Manage Solution view. Then select the matching `AVH-NS-only` target set and build or run it. Building `AVH-NS-only` first in a clean workspace fails because the secure HEX file and CMSE library do not yet exist.

The non-secure executable is listed before the secure HEX file in the target set and FVP invocation. This load order lets the executable configure the debug session before the prebuilt secure image is overlaid.
