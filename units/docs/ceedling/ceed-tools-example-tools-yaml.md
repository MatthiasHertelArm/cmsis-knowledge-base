---
id: "ceed-tools-example-tools-yaml"
type: "concept"
domain: "test"
title: "`:tools`: Example `:tools` YAML"
summary: "Resulting compiler command line construction from preceding example :tools YAML blurb…"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/tools.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/tools/#example-tools-yaml"
license: "MIT"
mode: "V"
---

```yaml
:tools:
  :test_compiler:
     :executable: compiler              # Exists in system search path
     :name: 'acme test compiler'
     :arguments:
        - -I"${5}"                      # Expands to -I search paths from `:paths` section + build directive path macros
        - -D"${6}"                      # Expands to all -D defined symbols from `:defines` section
        - --network-license             # Simple command line argument
        - -optimize-level 4             # Simple command line argument
        - "#{`args.exe -m acme.prj`}"   # In-line Ruby call to shell out & build string of arguments
        - -c ${1}                       # Source code input file
        - -o ${2}                       # Object file output
  
  :test_linker:
     :executable: /programs/acme/bin/linker.exe  # Full file path
     :name: 'acme test linker'
     :arguments:
        - ${1}               # List of object files to link
        - -l$-lib:           # In-line YAML array substitution to link in foo-lib and bar-lib
           - foo
           - bar
        - -o ${2}            # Binary output artifact
  
  :test_fixture:
     :executable: tools/bin/acme_simulator.exe  # Relative file path to command line simulator
     :name: 'acme test fixture'
     :stderr_redirect: :win                     # Inform Ceedling what model of $stderr capture to use
     :arguments:
        - -mem large         # Simple command line argument
        - -f "${1}"          # Binary executable input file for simulator
```

### `:tools` example blurb notes

* `${#}` is a replacement operator expanded by Ceedling with various strings,
  lists, etc. assembled internally. The meaning of each number is specific to
  each predefined default tool (see documentation above).

* See [search path order][##-search-path-order] to understand how the
  `-I"${5}"` term is expanded.

* At present, `$stderr` redirection is primarily used to capture errors from
  test fixtures so that they can be displayed at the conclusion of a test run.
  For instance, if a simulator detects a memory access violation or a divide by
  zero error, this notice might go unseen in all the output scrolling past in a
  terminal.

* The built-in preprocessing tools _can_ be overridden with non-GCC
  equivalents. However, this is highly impractical to do as preprocessing
  features are quite dependent on the idiosyncrasies and features of the GCC
  toolchain.

* Whatever the tool, preprocessor output must keep its line markers. With
  test preprocessing enabled, Ceedling refuses to start if `-P` or
  `--no-line-commands` appears in the arguments of
  `:test_file_full_preprocessor` or `:test_file_directives_only_preprocessor`.

### Example Test Compiler Tooling

Resulting compiler command line construction from preceding example `:tools`
YAML blurb…

```shell
> compiler -I"/usr/include" -I"project/tests"
  -I"project/tests/support" -I"project/source" -I"project/include"
  -DTEST -DLONG_NAMES -network-license -optimize-level 4 arg-foo
  arg-bar arg-baz -c project/source/source.c -o
  build/tests/out/source.o
```

Notes on compiler tooling example:

- `arg-foo arg-bar arg-baz` is a fabricated example string collected from
  `$stdout` as a result of shell execution of `args.exe`.
- The `-c` and `-o` arguments are fabricated examples simulating a single
  compilation step for a test; `${1}` & `${2}` are single files.

### Example Test Linker Tooling

Resulting linker command line construction from preceding example `:tools`
YAML blurb…

```shell
> \programs\acme\bin\linker.exe thing.o unity.o
  test_thing_runner.o test_thing.o mock_foo.o mock_bar.o -lfoo-lib
  -lbar-lib -o build\tests\out\test_thing.exe
```

Notes on linker tooling example:

- In this scenario `${1}` is an array of all the object files needed to link a
  test fixture executable.

### Example Test Fixture Tooling

Resulting test fixture command line construction from preceding example `:tools`
YAML blurb…

```shell
> tools\bin\acme_simulator.exe -mem large -f "build\tests\out\test_thing.bin 2>&1"
```

Notes on test fixture tooling example:

1. `:executable` could have simply been `${1}` if we were compiling and running
   native executables instead of cross compiling. That is, if the output of the
   linker runs on the host system, then the test fixture _is_ `${1}`.
1. We're using `$stderr` redirection to allow us to capture simulator error
   messages to `$stdout` for display at the run’s conclusion.
