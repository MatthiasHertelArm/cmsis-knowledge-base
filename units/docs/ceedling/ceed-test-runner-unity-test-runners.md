---
id: "ceed-test-runner-unity-test-runners"
type: "concept"
domain: "test"
title: "`:test_runner`: Unity & test runners"
summary: "Unity provides a script able to generate a test runner in C for you. It relies on [Ceedling conventions][ceedling-conventions] used in your test files."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/test-runner.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/test-runner/#unity-test-runners"
license: "MIT"
mode: "V"
---

Unity provides a script able to generate a test runner in C for you. It
relies on [Ceedling conventions][ceedling-conventions] used in your test files. 
Ceedling takes this a step further by calling this script for you with all the 
needed parameters.

Test runner generation is configurable. The `:test_runner` section of your
Ceedling project file allows you to pass options to Unity’s runner generation
script. Based on other Ceedling options, Ceedling also sets certain test runner 
generation configuration values for you.

**[Test runner configuration options are documented in the Unity project][unity-runner-options].**
