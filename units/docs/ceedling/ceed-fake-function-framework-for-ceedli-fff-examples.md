---
id: "ceed-fake-function-framework-for-ceedli-fff-examples"
type: "concept"
domain: "test"
title: "Fake Function Framework for Ceedling: FFF examples"
summary: "See the [FFF example project][fff-example-project]. This project illustrates how to use the plugin with full-size examples."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/fff.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/fff/#fff-examples"
license: "MIT"
mode: "V"
---

See the [FFF example project][fff-example-project]. This project illustrates how to use the plugin with full-size examples.

!!! warning "Versioning"
    The example project link is to the latest in the repository.
    It is not explicitly versioned to correspond to this documentation.
    That said, FFF and the plugin are relatively stable.

### Running example tests

Unit and integration tests exist for the plugin itself.

These tests are run with the default `rake` task packaged in the [FFF plugin][fff-plugin].

The integration test runs the FFF-based unit tests within the [example project][fff-example-project].
That is, the FFF examples are executed as part of Ceedling continuous integration.

[fff-example-project]: https://github.com/ThrowTheSwitch/Ceedling/tree/master/plugins/fff/examples/fff_example
[fff-plugin]:          https://github.com/ThrowTheSwitch/Ceedling/tree/master/plugins/fff
