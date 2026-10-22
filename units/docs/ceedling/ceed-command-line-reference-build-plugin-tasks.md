---
id: "ceed-command-line-reference-build-plugin-tasks"
type: "concept"
domain: "test"
title: "Command Line Reference: Build & plugin tasks"
summary: "Build task are loaded from your project configuration. Unlike application commands that are fixed, build tasks vary depending on your project configuration and the files within your project structure."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/reference/command-line.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/command-line/#build-plugin-tasks"
license: "MIT"
mode: "V"
---

Build task are loaded from your project configuration. Unlike 
application commands that are fixed, build tasks vary depending on your
project configuration and the files within your project structure.

Ultimately, build & plugin tasks are executed by the
[`build` application command](#ceedling-build-tasks)
(but the `build` keyword can be omitted — see above).

!!! warning "Quotes in shell command line parsing"
    Quotes may be necessary around any tasks using bracket notation or that
    can make use of wildcards or regexes. Your shell will likely need quotes
    to distinguish the parameter’s characters from shell command line
    operators.

---

### [`ceedling paths:*`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-paths)

* `ceedling paths:header`
* `ceedling paths:source`
* `ceedling paths:support`
* `ceedling paths:test`

List all paths collected from `paths` entries in your YAML config
file where `*` is the name of any section contained in `paths`. This
task is helpful in verifying the expansion of path wildcards / globs
specified in the `paths` section of your config file.

---

### [`ceedling files:*`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-files)

* `ceedling files:header`
* `ceedling files:source`
* `ceedling files:support`
* `ceedling files:test`
* `ceedling files:assembly`

List all files and file counts collected from the relevant search
paths specified by the `paths` entries of your YAML config file.

The `files:assembly` task will only be available if assembly support 
is enabled in the [`:release_build`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../configuration/reference/release-build.md) 
or [`:test_build`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../configuration/reference/test-build.md)
sections of your configuration file.

---

### [`ceedling test:all`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-testall)

Run all unit tests.

---

### [`ceedling test:build_only`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-testbuild_only)

Build the entire test suite but do not execute it. This is a simple 
validation of code and configuration via your toolchain.

---

### [`ceedling test:*`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-test)

Execute the named test file or the named source file that has an
accompanying test. Examples: `ceedling test:foo`, `ceedling test:foo.c`
or `ceedling test:test_foo.c`

!!! tip
    See the full documentation linked in this reference section title for
    details on how to reference test files having the same filename within
    different paths.

#### [`ceedling test:* --test-case=<test_case_name>`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-test-test-casetest_case_name)
Execute individual test cases which match `test_case_name`.

For instance, if you have a test file _test_gpio.c_ containing the following 
test cases (test cases are simply `void test_name(void)`).

- `test_gpio_start`
- `test_gpio_configure_proper`
- `test_gpio_configure_fail_pin_not_allowed`

… and you want to run only _configure_ tests, you can call:

`ceedling test:gpio --test-case=configure`

!!! note
    Test case matching is on sub-strings. `--test_case=configure` matches on
    the test cases including the word _configure_, naturally. 
    `--test-case=gpio` would match all three test cases.

#### [`ceedling test:* --exclude_test_case=<test_case_name>`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-test-exclude_test_casetest_case_name)
Execute test cases which do not match `test_case_name`.

For instance, if you have file test_gpio.c with defined 3 tests:

- `test_gpio_start`
- `test_gpio_configure_proper`
- `test_gpio_configure_fail_pin_not_allowed`

… and you want to run only start tests, you can call:

`ceedling test:gpio --exclude_test_case=configure`

!!! note
    Exclude matching follows the same sub-string logic as discussed in the
    preceding section.

!!! note "Test case filters enable test runner command line arguments"
    Both filters select test cases through command line arguments to the test
    executable. Ceedling enables [`:test_runner` ↳ `:cmdline_args`][cmdline-args]
    for a build using either filter.

[cmdline-args]: ../configuration/reference/test-runner.md#test_runner-cmdline_args

---

### [`ceedling test:pattern[*]`](../getting-started/command-line.md#ceedling-testpattern)

Execute any tests whose name and/or path match the regular expression
pattern (case sensitive). Example: `ceedling "test:pattern[(I|i)nit]"` 
will execute all tests named for initialization testing.

---

### [`ceedling test:path[*]`](../getting-started/command-line.md#ceedling-testpath)

Execute any tests whose path contains the given string (case
sensitive). Example: `ceedling test:path[foo/bar]` will execute all tests
whose path contains foo/bar.

Both directory separator characters `/` and `\` are valid.

---

### [`ceedling gen:mocks:all`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-genmocksall)

Generate the mock files in the project build directory for all tests. The
test build pipeline terminates after the mock generation stage.

---

### [`ceedling gen:mocks:*`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-genmocks)

Generate the mock files in the project build directory for only the given 
test or the named source file that has an accompanying test. The test 
build pipeline terminates after the mock generation stage.
Examples: `ceedling gen:mocks:foo`, `ceedling gen:mocks:foo.c` or 
`ceedling gen:mocks:test_foo.c`

---

### [`ceedling gen:test_runner:all`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-gentest_runnerall)

Generate up through test runners in the project build directory for all 
tests. The test build pipeline terminates after the test runner generation 
stage.

---

### [`ceedling gen:test_runner:*`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-gentest_runner)

Generate the test runner files in the project build directory for only 
the given test or the named source file that has an accompanying test. 
The test build pipeline terminates after the test runner generation stage.
Examples: `ceedling gen:test_runner:foo`, `ceedling gen:test_runner:foo.c`
or `ceedling gen:test_runner:test_foo.c`

---

### [`ceedling release`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-release)

Build all source into a release artifact (if the release build option
is configured).

---

### [`ceedling release:compile:*`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-releasecompile)

Sometimes you just need to compile a single file dagnabit.

Example: `ceedling release:compile:foo.c`

---

### [`ceedling release:assemble:*`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-releaseassemble)

Sometimes you just need to assemble a single file doggonit. Example:
`ceedling release:assemble:foo.s`

---

### [`ceedling summary`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-summary)

If plugins are enabled, this task will execute the summary method of
any plugins supporting it. This task is intended to provide a quick
roundup of build artifact metrics without re-running any part of the
build.

---

### [`ceedling clean`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-clean)

Deletes all toolchain binary artifacts (object files, executables),
test results, and any temporary files. Clean produces no output at the
command line unless verbosity has been set to an appreciable level.

---

### [`ceedling clobber`](https://throwtheswitch.github.io/Ceedling/reference/command-line/../getting-started/command-line.md#ceedling-clobber)

Extends clean task’s behavior to also remove generated files: test
runners, mocks, preprocessor output. Clobber produces no output at the
command line unless verbosity has been set to an appreciable level.
