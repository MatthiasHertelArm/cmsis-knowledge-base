---
id: "unity-unity-project-bdd-feature-usage"
type: "concept"
domain: "test"
title: "Unity Project - BDD Feature: Usage"
summary: "The provided BDD macros allow you to structure your test scenarios in a descriptive manner. These macros are for descriptive purposes only and do not have functional behavior."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:extras/bdd/readme.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/extras/bdd/readme.md#usage"
license: "MIT"
mode: "V"
---

### BDD Macros

The provided BDD macros allow you to structure your test scenarios in a descriptive manner. These macros are for descriptive purposes only and do not have functional behavior.

- `GIVEN(description)`: Describes the "Given" phase of a test scenario.
- `WHEN(description)`: Describes the "When" phase of a test scenario.
- `THEN(description)`: Describes the "Then" phase of a test scenario.

Example usage:

```c
GIVEN("a valid input") {
    // Test setup and context
    // ...

    WHEN("the input is processed") {
        // Perform the action
        // ...

        THEN("the expected outcome occurs") {
            // Assert the outcome
            // ...
        }
    }
}
```
