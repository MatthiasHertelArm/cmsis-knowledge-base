---
id: "ceed-valgrind-configuration"
type: "concept"
domain: "test"
title: "Valgrind: Configuration"
summary: "The plugin ships with sensible defaults that enable full leak checking. By default the build runs all test binaries to completion and is marked as failed if any memory errors are found."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/valgrind.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/valgrind/#configuration"
license: "MIT"
mode: "V"
---

The plugin ships with sensible defaults that enable full leak checking. By
default the build runs all test binaries to completion and is marked as failed
if any memory errors are found. Set `:fail_build: false` to log errors without
failing the build.

You can change the Valgrind configuration in your project configuration 
under an optional `:valgrind` section.

### Default configuration

In the default configuration, the Valgrind plugin will run the entire test 
suite, collecting Valgrind reports for each test fixture executable.

By default, the plugin runs with these command line arguments for `valgrind`:

- `--leak-check=full`
- `--show-leak-kinds=all`
- `--track-origins=yes`
- `--errors-for-leak-kinds=all`

### `:arguments:`

The list of flags passed to Valgrind for every test binary. To override the
defaults, redefine the argument list in your project configuration:

```yaml
:valgrind:
  :arguments:
    # A subset of the default arguments
    - "--leak-check=full"
    - "--show-leak-kinds=all"
```

### `:fail_build:`

When `true` (the default), any memory errors are logged immediately after 
running a test executable. After all test binaries complete execution, if 
any memory errors were found across the run, the build is marked as failed 
with a total count of memory errors and test files processed.

When `false`, memory errors are still logged per test binary but the build is
not marked as failed.

```yaml
:valgrind:
  :fail_build: false
```

!!! note "Detection uses log parsing, not Valgrind’s exit code"
    Valgrind’s `--error-exitcode` flag is not used because its exit code would
    overlap with Unity’s own exit code, which equals the number of failing test
    cases. Instead, the plugin parses the `ERROR SUMMARY: N errors` line written
    to the Valgrind log file.
