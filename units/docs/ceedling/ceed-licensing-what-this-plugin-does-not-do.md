---
id: "ceed-licensing-what-this-plugin-does-not-do"
type: "concept"
domain: "test"
title: "Licensing: What this plugin does not do"
summary: "This plugin invokes Bullseye's tools with the coverage and license environment variables described here. It also reports license status on request."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/bullseye/licensing.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/bullseye/licensing/#what-this-plugin-does-not-do"
license: "MIT"
mode: "V"
---

This plugin invokes Bullseye's tools with the coverage and license environment
variables described here. It also reports license status on request.

Installing and activating Bullseye is a host or CI setup concern. The plugin
never creates a license manager file, adds a key, or releases a license.
Ceedling's generic
[`:environment`](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/licensing/../../configuration/reference/environment.md) configuration
can set any other environment variable a given Bullseye installation needs.

[bullseye-download]:         https://www.bullseye.com/cgi-bin/download
[bullseye-license-manager]:  https://www.bullseye.com/help/licenseManager.html
