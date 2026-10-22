---
id: "ceed-test-runner-example-test-runner-yaml"
type: "concept"
domain: "test"
title: "`:test_runner`: Example `:test_runner` YAML"
summary: "[ceedling-conventions]: ../../testing-guide/conventions.md [unity-runner-options]: https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityHelperScriptsGuide.md#options-accepted-by-generate_test_runnerrb [unity-shuffle-tests]: unity.md#shuffle_tests"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/test-runner.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/test-runner/#example-test-runner-yaml"
license: "MIT"
mode: "V"
---

```yaml
:test_runner:
  # Insert additional #include statements in a generated runner
  :includes:
    - Foo.h
    - Bar.h
```

[ceedling-conventions]: ../../testing-guide/conventions.md
[unity-runner-options]: https://github.com/ThrowTheSwitch/Unity/blob/master/docs/UnityHelperScriptsGuide.md#options-accepted-by-generate_test_runnerrb
[unity-shuffle-tests]: unity.md#shuffle_tests
