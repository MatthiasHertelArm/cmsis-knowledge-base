---
id: "ceed-test-suite-report-log-factory-user-beware"
type: "concept"
domain: "test"
title: "Test Suite Report Log Factory: _User Beware_"
summary: "Test reports often lack well managed standards or even much documentation at all. Different revisions of the formats exist as do different flavors of the same version produced by different tools."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/report-tests-log-factory.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-log-factory/#user-beware"
license: "MIT"
mode: "V"
---

Test reports often lack well managed standards or even much documentation at all. Different revisions of the formats exist as do different flavors of the same version produced by different tools.

If a test report produced by this plugin does not work for your needs or is not recognized by your report processing tool of choice, well, sadly, this is not all that uncommon. You have at least two options:

1. Use a script or other tool to post-process the report into a format that works for you. You might be surprised how many of these hacks are commonly necessary and exist peppered throughout online forums. You can incorporate any such post-processing step by enabling the `command_hooks` Ceedling plugin (lower in the plugin list than this plugin) and configuring a Ceedling tool to run the needed transformation.
1. Use Ceedling’s abilities plus features of this plugin (documented below) to generate your own test report with a minimal amount of Ruby code.
