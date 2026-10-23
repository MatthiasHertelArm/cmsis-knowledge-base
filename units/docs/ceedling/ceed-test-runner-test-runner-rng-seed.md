---
id: "ceed-test-runner-test-runner-rng-seed"
type: "concept"
domain: "test"
title: "`:test_runner`: `:test_runner` ↳ `:rng_seed`"
summary: "Seeds the randomization used by [:unity ↳ :shuffle_tests][unity-shuffle-tests] to shuffle the Unity runner test case execution order. :rng_seed has no effect unless :shuffle_tests is enabled."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/reference/test-runner.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/test-runner/#test-runner-rng-seed"
license: "MIT"
mode: "V"
---

Seeds the randomization used by [`:unity` ↳ `:shuffle_tests`][unity-shuffle-tests]
to shuffle the Unity runner test case execution order. `:rng_seed` has no 
effect unless `:shuffle_tests` is enabled.

Left at its default of `0`, Unity seeds the shuffle from the current time 
causing a different execution order every time a test runner executes. Set 
a fixed, nonzero value for a reproducible shuffled order (e.g. to debug 
an order-dependent failure without test case order moving around run to run).

**Default**: 0
