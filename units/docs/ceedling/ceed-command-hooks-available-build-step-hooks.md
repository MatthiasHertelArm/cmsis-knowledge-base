---
id: "ceed-command-hooks-available-build-step-hooks"
type: "concept"
domain: "test"
title: "Command Hooks: Available Build Step Hooks"
summary: "Define any of the following entries within a top-level :command_hooks: section of your Ceedling project file to automagically connect utilities or scripts to build process steps."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/command-hooks.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/command-hooks/#available-build-step-hooks"
license: "MIT"
mode: "V"
---

Define any of the following entries within a top-level `:command_hooks:` section of your Ceedling project file to automagically connect utilities or scripts to build process steps.

Some hooks are called for every file-related operation for which the hook is named. Other hooks are triggered by the single build step for which the hook is named.

As an example, consider a Ceedling project with ten test files and seventeen mocks. The command line `ceedling test:all` would trigger:

* 1 occurrence of the `:pre_build` hook.
* 1 occurrence of the `:pre_test_build` hook.
* 10 occurrences of the `:pre_test` and `:post_test` hooks.
* 17 occurrences of the `:pre_mock_generate` and `:post_mock_generate` hooks.
* 10 occurrences of the `:pre_test_runner_generate` and `:post_test_runner_generate` hooks.
* 27(+) occurrences of the `:pre_compile` and `:post_compile` hooks. These hooks would be called 27 times for test file and mock file compilation. A test suite build will also include compilation of the source files under tests, Unity’s source, CMock’s source, and generated test runner C files -- easily more than another two dozen compilation hook calls.
* 10 occurrences of the `:pre_link` and `:post_link` hooks for test executable creation.
* 10 occurrences of the `:pre_test_fixture_execute` and `:post_test_fixture_execute` hooks for running test executables and gathering the results of the tests cases they contain.
* 1 occurrence of the `:post_test_build` hook.
* 1 occurrence of the `:post_build` hook unless a build error occurred (`:post_error` would be called instead).

### `:pre_build`

Called once just before Ceedling executes any tasks.

The parameter available to a tool (`${1}`) when the hook is called is a floating-point stopwatch value in seconds. This value and the corresponding `post_build` value can be used to compute the total build duration.

### `:post_build`

Called once just before Ceedling terminates after a successful build.

The parameter available to a tool (`${1}`) when the hook is called is a floating-point stopwatch value in seconds. This value and the corresponding `pre_build` value can be used to compute the total build duration.

### `:post_error`

Called once just after any build failure and just before Ceedling terminates.

The parameter available to a tool (`${1}`) when the hook is called is a floating-point stopwatch value in seconds at the moment the error is handled.

### `:pre_test`

Called just before each test begins its build pipeline and just after all context for that build has been gathered.

The parameter available to a tool (`${1}`) when the hook is called is the test’s filepath.

### `:post_test`

Called just after each test completes its build and execution.

The parameter available to a tool (`${1}`) when the hook is called is the test’s filepath.

### `:pre_test_build`

Called once just before the full test build pipeline begins (before any individual test’s configure, preprocess, compile, link, or execute steps).

Two parameters are available to a tool when the hook is called:

* `${1}` — the build context as a string (e.g. `"test"`, `"gcov"`).
* `${2}` — a floating-point stopwatch value in seconds. This value and the corresponding `post_test_build` value can be used to compute the total test build duration.

### `:post_test_build`

Called once just after the full test build pipeline completes or terminates (including on error).

Two parameters are available to a tool when the hook is called:

* `${1}` — the build context as a string (e.g. `"test"`, `"gcov"`).
* `${2}` — a floating-point stopwatch value in seconds. This value and the corresponding `pre_test_build` value can be used to compute the total test build duration.

### `:pre_release_build`

Called once just before a release build begins.

The parameter available to a tool (`${1}`) when the hook is called is a floating-point stopwatch value in seconds. This value and the corresponding `post_release_build` value can be used to compute the total release build duration.

### `:post_release_build`

Called once just after a release build finishes or terminates (including on error).

The parameter available to a tool (`${1}`) when the hook is called is a floating-point stopwatch value in seconds. This value and the corresponding `pre_release_build` value can be used to compute the total release build duration.

### `:pre_mock_preprocess`

If mocks are enabled and preprocessing is in use, this is called just before each header file to be mocked is preprocessed.

The parameter available to a tool (`${1}`) when the hook is called is the filepath of the header file to be mocked.

See [_Conventions & Behaviors_][preprocessing] for details on how Ceedling preprocessing operates.

[preprocessing]: ../testing-guide/conventions.md#test-preprocessing

### `:post_mock_preprocess`

If mocks are enabled and preprocessing is in use, this is called just after each header file to be mocked is preprocessed.

The parameter available to a tool (`${1}`) when the hook is called is the filepath of the header file to be mocked.

### `:pre_mock_generate`

If mocks are enabled, this is called just before each header file to be mocked is processed by mock generation.

The parameter available to a tool (`${1}`) when the hook is called is the filepath of the header file to be mocked.

### `:post_mock_generate`

If mocks are enabled, this is called just after each mock generation.

The parameter available to a tool (`${1}`) when the hook is called is the filepath of the header file to be mocked.

### `:pre_test_preprocess`

If preprocessing is in use, this is called just before each test file is preprocessed before runner generation.

The parameter available to a tool (`${1}`) when the hook is called is the test’s filepath.

See [_Conventions & Behaviors_][preprocessing] for details on how Ceedling preprocessing operates.

### `:post_test_preprocess`

If preprocessing is in use, this is called just after each test file is preprocessed.

The parameter available to a tool (`${1}`) when the hook is called is the test’s filepath.

See [_Conventions & Behaviors_][preprocessing] for details on how Ceedling preprocessing operates.

### `:pre_runner_generate`

Called just before each test file is processed by test runner generation.

The parameter available to a tool (`${1}`) when the hook is called is the test’s filepath.

### `:post_runner_generate`

Called just after each test runner is generated.

The parameter available to a tool (`${1}`) when the hook is called is the test’s filepath.

### `:pre_compile_execute`

Called just before each C or assembly file is compiled.

The parameter available to a tool (`${1}`) when the hook is called is the filepath of the file to be compiled.

### `:post_compile_execute`

Called just after each file compilation.

The parameter available to a tool (`${1}`) when the hook is called is the filepath of the input file that was compiled.

### `:pre_link_execute`

Called just before any binary artifact—test or release—is linked.

The parameter available to a tool (`${1}`) when the hook is called is the binary output artifact’s filepath.

### `:post_link_execute`

Called just after a binary artifact is linked.

The parameter available to a tool (`${1}`) when the hook is called is the binary output artifact’s filepath.

### `:pre_test_fixture_execute`

Called just before each test is executed in its corresponding test fixture.

The parameter available to a tool (`${1}`) when the hook is called is the filepath of the binary artifact to be executed by the fixture.

### `:post_test_fixture_execute`

Called just after each test’s fixture is executed and test results are collected.

The parameter available to a tool (`${1}`) when the hook is called is the filepath of the binary artifact that was executed by the fixture.
