---
id: "aig-license-flexnet-how-do-i-set-up-a-license-serv"
type: "concept"
domain: "project"
title: "FlexNet Publisher Floating license setup: How do I set up a license server?"
summary: "License Administrators should download and install the latest FlexNet Publisher software to your internal license server."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/license/flexnet.md"
doc_source: "https://learn.arm.com/install-guides/license/flexnet/#how-do-i-set-up-a-license-server"
license: "CC-BY-SA-4.0"
mode: "V"
---

### How do I download the FlexNet Publisher software?

License Administrators should download and install the latest FlexNet Publisher software to your internal license server.
```url
https://support.arm.com/downloads/view/LLSFL
```
### How do I generate a license file?

Access the [Software Licensing Portal](https://developer.arm.com/support/licensing) to generate your license. You will need the `HOSTID` of the license server and your product license key from Arm.

Optionally add license server names and network port to the `SERVER` line of the license file:
```output
SERVER HOSTNAME HOSTID PORT
```
### How do I launch the license server?

Start the license server with:
```command
lmgrd -c license_file
```
See the [FlexNet for Arm Tools License Management Guide](https://developer.arm.com/documentation/dui0209) for full options.
