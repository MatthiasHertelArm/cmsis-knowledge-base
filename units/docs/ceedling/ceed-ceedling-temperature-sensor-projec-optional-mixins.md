---
id: "ceed-ceedling-temperature-sensor-projec-optional-mixins"
type: "concept"
domain: "test"
title: "Ceedling Temperature Sensor Project: Optional Mixins"
summary: "Collect and report test coverage (requires gcov and gcovr):"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/snapshot/examples/temp_sensor/README.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/snapshot/examples/temp_sensor/#optional-mixins"
license: "MIT"
mode: "V"
---

### Coverage with gcov

Collect and report test coverage (requires `gcov` and `gcovr`):

```sh
ceedling gcov:all --mixin=mixin/add_gcov.yml
```

### Custom Unity assertions

The project defines a custom assertion for `EXAMPLE_STRUCT_T` in
`test/support/UnityHelper.h`. It is conditionally compiled and activated
by the `add_unity_helper` mixin, which adds the required define and
registers the helper with CMock:

```sh
ceedling test:all --mixin=mixin/add_unity_helper.yml
```
