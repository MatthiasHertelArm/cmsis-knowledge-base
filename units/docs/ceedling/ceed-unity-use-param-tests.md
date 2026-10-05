---
id: "ceed-unity-use-param-tests"
type: "concept"
domain: "test"
title: "`:unity`: `:use_param_tests`"
summary: "Configures Unity test runner generation and #defines for test compilation to support Unity’s parameterized test cases."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/unity.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/unity/#use-param-tests"
license: "MIT"
mode: "V"
---

Configures Unity test runner generation and `#define`s for test compilation to
support Unity’s parameterized test cases.

Example parameterized test case:

```c
TEST_RANGE([5, 100, 5])
void test_should_handle_divisible_by_5_for_parameterized_test_range(int num) {
  TEST_ASSERT_EQUAL(0, (num % 5));
}
```

See Unity documentation for more on parameterized test cases.

**Default**: false
