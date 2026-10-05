---
id: "cact-arm-software-cmsis-actions-action-armlm"
type: "concept"
domain: "devops"
title: "ARM-software/cmsis-actions: Action: armlm"
summary: "This action activates an Arm user based license using the armlm license manager."
status: "draft"
collection: "cmsis-actions"
source: "ARM-software/cmsis-actions@f248cd4:README.md"
doc_source: "https://github.com/ARM-software/cmsis-actions/blob/f248cd4/README.md#action-armlm"
license: "Apache-2.0"
mode: "V"
---

This action activates an
[Arm user based license](https://developer.arm.com/documentation/102516/1-2/Activate-and-deactivate-your-product-license/Activate-your-product-using-a-license-server)
using the `armlm` license manager.

```yaml
- name: Activate Arm license
  uses: ARM-software/cmsis-actions/armlm@v1
  with:
    code: <personal product code>
    server: <custom license server>
    product: KEMDK-COM0
```

inputs     | default value | description
-----------|---------------|--------------
`code:`    | n/a           | License activation code (takes precedence over server/product).
`server:`  | n/a           | Get a product license from the server specified by a URL.
`product:` | KEMDK-COM0    | Get a license for the specified product from the server (default MDK Community Edition).

The action can be either called with a
[license activation `code:`](https://developer.arm.com/documentation/102516/1-2/Activate-and-deactivate-your-product-license/Activate-your-product-using-an-activation-code)
or a [license `server:`  with `product:` specification](https://developer.arm.com/documentation/102516/1-2/Activate-and-deactivate-your-product-license/Activate-your-product-using-a-license-server).
Without any `inputs`, it activates a license for the [Keil MDK - Community Edition](https://www.keil.arm.com/keil-mdk/) which is a free-to-use,
non-commercial license which can be used for evaluation.

### Usage examples armlm

- [github.com/Arm-Examples/AVH_CI_Template](https://github.com/Arm-Examples/AVH_CI_Template/blob/main/.github/workflows/basic.yml) actives a
  [Keil MDK - Community Edition](https://www.keil.arm.com/keil-mdk/) as it uses no inputs.

- [github.com/ARM-software/CMSIS_6](https://github.com/ARM-software/CMSIS_6/blob/main/.github/workflows/corevalidation.yml) actives a commerical product using a license activation code
  that is provided via a [GitHub secret](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions).
