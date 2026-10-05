---
id: "aig-license-cloud-how-do-i-generate-an-activatio"
type: "concept"
domain: "project"
title: "UBL Cloud server setup: How do I generate an activation code?"
summary: "Access to the Arm user-based licensing portal with the account that the licenses were assigned to. This is likely to be an assigned license administrator rather than the end-user."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/license/cloud.md"
doc_source: "https://learn.arm.com/install-guides/license/cloud/#how-do-i-generate-an-activation-code"
license: "CC-BY-SA-4.0"
mode: "V"
---

Access to the Arm user-based licensing portal with the account that the licenses were assigned to. This is likely to be an assigned license administrator rather than the end-user.

```url
https://developer.arm.com/support/licensing/user-based
```
Click on `View Details` of the product of interest, and then navigate to `Cloud Server` > `Generate Activation Code`.

This code can be shared with the end-user to [activate](#activate).

Once activated, the user information will be visible on the licensing portal dashboard along side the activation code.

### How do I activate the license?
On the end-user machine, open a command prompt, and navigate to the `bin` directory of any UBL enabled product.

Use the following command with your assigned activation code.
```console
armlm activate --code xxxxxxxx-xxxx-xxxx-xxxxxxxx
```

### How do I activate the license via tools IDE?

The license can also be activated in the various Arm tool IDEs.

For example [Arm Development Studio](https://developer.arm.com/Tools%20and%20Software/Arm%20Development%20Studio), via `Help` > `Arm License Manager` > `Manage Arm User-Based Licenses`.

Select `Activate with` > `Activation Code`, and enter your product activation code. Click `Activate`.
