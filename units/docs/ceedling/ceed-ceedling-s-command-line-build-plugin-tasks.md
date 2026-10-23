---
id: "ceed-ceedling-s-command-line-build-plugin-tasks"
type: "concept"
domain: "test"
title: "Ceedling’s Command Line: Build & plugin tasks"
summary: "Build task are loaded from your project configuration. Unlike application commands that are fixed, build tasks vary depending on your project configuration and the files within your project structure."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/getting-started/command-line.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/command-line/#build-plugin-tasks"
license: "MIT"
mode: "V"
---

Build task are loaded from your project configuration. Unlike 
application commands that are fixed, build tasks vary depending on your
project configuration and the files within your project structure.

Ultimately, build & plugin tasks are executed by the `build` application
command (but the `build` keyword can be omitted — see above).

### `ceedling paths:*`

Variants:

* `ceedling files:header`
* `ceedling files:source`
* `ceedling files:support`
* `ceedling files:test`

List all paths collected from `:paths` entries in your project configuration
where `*` is the name of any section contained in `:paths`.

This task is helpful in verifying the expansion of path wildcards / globs
specified in the `:paths` section of your configuration.

---

### `ceedling files:*`

Variants:

* `ceedling files:header`
* `ceedling files:source`
* `ceedling files:support`
* `ceedling files:test`
* `ceedling files:assembly`

List all files and file counts collected from the relevant search
paths specified by the `:paths` entries of your project configuration.

The `files:assembly` task will only be available if assembly support is
enabled in the `:release_build` or `:test_build` sections of your 
configuration file.

---

### `ceedling test:all`

Run all unit tests.

---

### `ceedling test:build_only`

Build the entire test suite but do not execute it. This is a simple 
validation of code and configuration via your toolchain.

---

### `ceedling test:*`

Build and execute the named test executable or the named source file that has an
accompanying test file. Examples: `ceedling test:foo`, `ceedling test:foo.c`
or `ceedling test:test_foo.c`

!!! tip "Disambiguating test files with the same name"
    If more than one test file shares that filename in different test
    directories, add enough of the trailing path to identify the file you
    want. `/` and `\` are both acceptable path separators.
    
    For example, given _test/unit/test_foo.c_ and _test/integration/test_foo.c_, 
    run `ceedling test:unit/test_foo.c` at the command line to identify
    the first test file.
    
    When Ceedling is unable to uniquely identify a file path, it raises 
    an error naming every matching file.

---

### `ceedling test:* --test-case=<test_case_name>`

Execute individual test cases which match `test_case_name`.

For instance, if you have a test file _test_gpio.c_ containing the following 
test cases (test cases are simply `void test_name(void)`):

- `test_gpio_start`
- `test_gpio_configure_proper`
- `test_gpio_configure_fail_pin_not_allowed`

… and you want to run only `configure` tests, you can call:

  `ceedling test:gpio --test-case=configure`

**Test case matching notes**

* Test case matching is on sub-strings. `--test_case=configure` matches on
  the test cases including the word _configure_, naturally. 
  `--test-case=gpio` would match all three test cases.

---

### `ceedling test:* --exclude_test_case=<test_case_name>`

Execute test cases which do not match `test_case_name`.

For instance, if you have file _test_gpio.c_ with 3 tests:

- `test_gpio_start`
- `test_gpio_configure_proper`
- `test_gpio_configure_fail_pin_not_allowed`

… and you want to run only `start` tests, you can call:

  `ceedling test:gpio --exclude_test_case=configure`

**Test case exclusion matching notes**

* Exclude matching follows the same sub-string logic as discussed in the
  preceding section.

---

### `ceedling test:pattern[*]`

Execute any tests whose name and/or path match the regular expression
pattern between the brackets (case sensitive).

Example: `ceedling "test:pattern[(I|i)nit]"` will execute all tests named for 
initialization testing.

!!! note
    Quotes are likely necessary around the regex characters or 
    entire task to distinguish characters from shell command line operators.

---

### `ceedling test:path[*]`

Execute any tests whose path contains the given string (case
sensitive). Example: `ceedling test:path[foo/bar]` will execute all tests
whose path contains foo/bar. _Notes:_

1. Both directory separator characters `/` and `\` are valid.
1. Quotes may be necessary around the task to distinguish the parameter’s
   characters from shell command line operators.

---

### `ceedling gen:mocks:all`

Generate the mock files in the project build directory for all tests. The
test build pipeline terminates after the mock generation stage.

---

### `ceedling gen:mocks:*`

Generate the mock files in the project build directory for only the given 
test or the named source file that has an accompanying test. The test 
build pipeline terminates after the mock generation stage.
Examples: `ceedling gen:mocks:foo`, `ceedling gen:mocks:foo.c` or 
`ceedling gen:mocks:test_foo.c`

Like the `test:` tasks, the test specifier for duplicate test filenames
can be disambiguated with a trailing path before the test name.

---

### `ceedling gen:test_runner:all`

Generate up through test runners in the project build directory for all 
tests. The test build pipeline terminates after the test runner generation 
stage.

---

### `ceedling gen:test_runner:*`

Generate the test runner files in the project build directory for only 
the given test or the named source file that has an accompanying test. 
The test build pipeline terminates after the test runner generation stage.
Examples: `ceedling gen:test_runner:foo`, `ceedling gen:test_runner:foo.c`
or `ceedling gen:test_runner:test_foo.c`

Like the `test:` tasks, the test specifier for duplicate test filenames
can be disambiguated with a trailing path before the test name.

---

### `ceedling release`

Build all source into a release artifact (if the release build option
is configured).

---

### `ceedling release:compile:*`

Sometimes you just need to compile a single file dagnabit. Example:
`ceedling release:compile:foo.c`

---

### `ceedling release:assemble:*`

Sometimes you just need to assemble a single file doggonit. Example:
`ceedling release:assemble:foo.s`

---

### `ceedling summary`

If plugins are enabled, this task will execute the summary method of
any plugins supporting it. This task is intended to provide a quick
roundup of build artifact metrics without re-running any part of the
build.

---

### `ceedling clean`

Deletes all toolchain binary artifacts (object files, executables),
test results, and any temporary files. Clean produces no output at the
command line unless verbosity has been set to an appreciable level.

---

### `ceedling clobber`

Extends clean task’s behavior to also remove generated files: test
runners, mocks, preprocessor output. Clobber produces no output at the
command line unless verbosity has been set to an appreciable level.

---
