---
id: "unity-unity-fixtures-usage-information"
type: "concept"
domain: "test"
title: "Unity Fixtures: Usage information"
summary: "By default the test executables produced by Unity Fixtures run all tests once, but the behavior can be configured with command-line flags. Run the test executable with the --help flag for more information."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:extras/fixture/readme.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/extras/fixture/readme.md#usage-information"
license: "MIT"
mode: "V"
---

By default the test executables produced by Unity Fixtures run all tests once, but the behavior can be configured with command-line flags.
Run the test executable with the `--help` flag for more information.

It's possible to add a custom line at the end of the help message, typically to point to project-specific or company-specific unit test documentation.
Define `UNITY_CUSTOM_HELP_MSG` to provide a custom message, e.g.:

    #define UNITY_CUSTOM_HELP_MSG "If any test fails see https://example.com/troubleshooting"
