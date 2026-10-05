---
id: "aig-license-cloud-how-do-i-refresh-the-license"
type: "concept"
domain: "project"
title: "UBL Cloud server setup: How do I refresh the license?"
summary: "Your license is cached on your local machine, and is valid for 7 days."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/license/cloud.md"
doc_source: "https://learn.arm.com/install-guides/license/cloud/#how-do-i-refresh-the-license"
license: "CC-BY-SA-4.0"
mode: "V"
---

Your license is cached on your local machine, and is valid for 7 days.

There will be an automatic attempt to refresh this timer on the first usage of a UBL enabled tool in a day. If it fails to communicate to the server (see [Network requirements for user-based licensing](https://developer.arm.com/documentation/102516/latest/User-based-licensing-overview/Network-requirements-for-user-based-licensing) for the most common reasons) the tools can still be used provided there is still time on the locally cached license.

To manually refresh the cached license, you can deactivate and reactivate your license (assuming above network requirements are fulfilled):
```command
armlm deactivate --code xxxxxxxx-xxxx-xxxx-xxxxxxxx
armlm reactivate --code xxxxxxxx-xxxx-xxxx-xxxxxxxx
```
Verify that you have refreshed successfully with:
```command
armlm inspect
```
