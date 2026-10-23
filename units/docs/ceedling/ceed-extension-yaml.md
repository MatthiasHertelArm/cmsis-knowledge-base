---
id: "ceed-extension-yaml"
type: "concept"
domain: "test"
title: "`:extension`: `:yaml`"
summary: "Mixin files (see Mixins)"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/extension.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/extension/#yaml"
license: "MIT"
mode: "V"
---

Mixin files (see [Mixins](https://throwtheswitch.github.io/Ceedling/configuration/reference/extension/../mixins.md))

Ceedling uses this setting only to find a mixin given by name, as _<name>_ plus
each extension, in each mixin load path. It reads the setting from your project
file before processing configuration, so it cannot come from a mixin. Ceedling's
own YAML files always use _.yml_.

**Default**: .yml
