---
id: "ceed-temp-sensor-optional-mixins"
type: "concept"
domain: "test"
title: "`temp_sensor`: Optional mixins"
summary: "The project ships two mixin files that activate optional features:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/getting-started/example-projects/temp-sensor.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/temp-sensor/#optional-mixins"
license: "MIT"
mode: "V"
---

The project ships two mixin files that activate optional features:

- **`add_gcov`** — enables gcov coverage collection and reporting (requires
  `gcov` and `gcovr`). Run with `ceedling gcov:all --mixin=mixin/add_gcov.yml`.
- **`add_unity_helper`** — activates a custom Unity assertion for
  `EXAMPLE_STRUCT_T`, enabling more detailed failure messages for struct
  comparisons. Run with `ceedling test:all --mixin=mixin/add_unity_helper.yml`.

See the [Mixins](https://throwtheswitch.github.io/Ceedling/getting-started/example-projects/temp-sensor/../../configuration/mixins.md)
documentation for more on how to use and write mixin files.
