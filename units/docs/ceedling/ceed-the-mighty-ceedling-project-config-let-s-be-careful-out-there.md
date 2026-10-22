---
id: "ceed-the-mighty-ceedling-project-config-let-s-be-careful-out-there"
type: "concept"
domain: "test"
title: "The Mighty Ceedling Project Configuration File: Let’s Be Careful Out There"
summary: "Ceedling performs validation of the values you set in your configuration file (this assumes your YAML is correct and will not fail format parsing, of course)."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/project-file.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/project-file/#let-s-be-careful-out-there"
license: "MIT"
mode: "V"
---

Ceedling performs validation of the values you set in your 
configuration file (this assumes your YAML is correct and will 
not fail format parsing, of course).

That said, validation is limited to only those settings Ceedling
uses and those that can be reasonably validated. Ceedling does
not limit what can exist within your configuration file. In this
way, you can take full advantage of YAML as well as add sections
and values for use in your own custom plugins (documented later).

The consequence of this is simple but important. A misspelled
configuration section or value name is unlikely to cause Ceedling 
any trouble. Ceedling will happily process that section
or value and simply use the properly spelled default maintained
internally — thus leading to unexpected behavior without warning.

[example-config-file]: ../snapshot/assets/features/project.yml
