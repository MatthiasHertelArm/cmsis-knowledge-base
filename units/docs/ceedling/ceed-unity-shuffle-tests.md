---
id: "ceed-unity-shuffle-tests"
type: "concept"
domain: "test"
title: "`:unity`: `:shuffle_tests`"
summary: "Configures the Unity test runner to shuffle (randomize) the order in which test cases run within a test executable."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/unity.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/unity/#shuffle-tests"
license: "MIT"
mode: "V"
---

Configures the Unity test runner to shuffle (randomize) the order in which 
test cases run within a test executable. This is useful for surfacing bugs 
caused by tests that depend on execution order or on state left behind by 
an earlier test.

The randomization seed can be pinned to a fixed value for reproducible
ordering — see [`:test_runner` ↳ `:rng_seed`][test-runner-rng-seed].

Ceedling’s [delta builds][delta-builds] also work together with shuffled test.

**Default**: `false`





[test-runner-rng-seed]: test-runner.md#test_runner-rng_seed
[delta-builds]: ../../getting-started/builds.md
