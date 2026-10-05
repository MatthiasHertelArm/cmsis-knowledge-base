---
id: "ceed-configuring-partials-enabling-partials"
type: "concept"
domain: "test"
title: "Configuring Partials: Enabling Partials"
summary: "Enable Partials in your project YAML under the :project: block:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/partials/configuration.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/partials/configuration/#enabling-partials"
license: "MIT"
mode: "V"
---

Enable Partials in your project YAML under the `:project:` block:

```yaml
:project:
  :use_partials: true
```

See the [:project: configuration reference](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/configuration/../../configuration/reference/project.md#use_partials)
for the full setting description.

Enabling `:use_partials:` automatically:

- Enables `:use_mocks` as Partials depend on CMock’s mocking infrastructure.
- Supersedes CMock’s `:treat_inlines` setting. With Partials, Ceedling manages 
  inline function exposure directly.
