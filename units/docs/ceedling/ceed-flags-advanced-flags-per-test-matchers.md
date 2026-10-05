---
id: "ceed-flags-advanced-flags-per-test-matchers"
type: "concept"
domain: "test"
title: "`:flags`: Advanced `:flags` per-test matchers"
summary: "Ceedling treats each test executable as a mini project. As a reminder, each test file, together with all C sources and frameworks, becomes an individual test executable of the same name."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/flags.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/flags/#advanced-flags-per-test-matchers"
license: "MIT"
mode: "V"
---

Ceedling treats each test executable as a mini project. As a reminder, each
test file, together with all C sources and frameworks, becomes an individual
test executable of the same name.

_In the `:test` context only_, flags can be applied to build step operations —
preprocessing, compilation, and linking — for only those test executables that
match file name criteria. Matchers match on test filenames only, and the
specified flags are added to the build step for all files that are components
of matched test executables.

In short, for instance, this means your compilation of _TestA_ can have
different flags than compilation of _TestB_. And, in fact, those flags will be
applied to every C file that is compiled as part those individual test
executable builds.

### `:flags` per-test matcher examples with YAML

Before detailing matcher capabilities and limits, here are examples to
illustrate the basic ideas of test file name matching.

```yaml
:flags:
  :test:
    :compile:
      :*:              #  Wildcard: Add '-foo' for all files compiled for all test executables
        - -foo         
      :Model:          # Substring: Add '-Wall' for all files compiled for any test executable with 'Model' in its filename
        - -Wall
      :/M(ain|odel)/:  #     Regex: Add 🏴‍☠️ flag for all files compiled for any test executable with 'Main' or 'Model' in its filename
        - -🏴‍☠️
      :Comms*Model:
        - --freak      #  Wildcard: Add your `--freak` flag for all files compiled for any test executable with zero or more
                       #            characters between 'Comms' and 'Model'
    :link:
      :tests/comm/TestUsart.c:  # Substring: Add '--bar --baz' to the link step of the TestUsart executable
        - --bar
        - --baz
```

### Using `:flags` per-test matchers

These matchers are available:

1. Wildcard (`*`)
    1. If specified in isolation, matches all tests.
    1. If specified within a string, matches any test filename with that 
      wildcard expansion.
1. Substring — Matches on part of a test filename (up to all of it, including
   full path).
1. Regex (`/.../`) — Matches test file names against a regular expression.

Notes:

* Substring filename matching is case sensitive.
* Wildcard matching is effectively a simplified form of regex. That is, 
  multiple approaches to matching can match the same filename.

Flags by matcher are cumulative. This means the flags from multiple matchers
can be applied to all files processed by the named build operation for any
single test executable.

Referencing the example above, here are the extra compilation flags for a
handful of test executables:

* _test_Something_: `-foo`
* _test_Main_: `-foo -🏴‍☠️`
* _test_Model_: `-foo -Wall -🏴‍☠️`
* _test_CommsSerialModel_: `-foo -Wall -🏴‍☠️ --freak`

The simple `:flags` list format remains available for the `:test` context. Of
course, this format is limited in that it applies flags to all C files processed
by the named build operation for all test executables.

This simple list format for the `:test` context…

```yaml
:flags:
  :test:
    :compile:
      - -foo
```

…is equivalent to this matcher version:

```yaml
:flags:
  :test:
    :compile:
      :*:
        - -foo
```

### Distinguishing similar / identical filenames

You may find yourself needing to distinguish test files with the same name or
test files with names whose base naming is identical.

Of course, identical test filenames have a natural distinguishing feature in
their containing directory paths. Files of the same name can only exist in
different directories. As such, your matching must include the path.

```yaml
:flags:
  :test:
    :compile:
      # Match any test names beginning with 'test_startup' in hardware/ directory
      :hardware/test_startup:
        - A                 
      # Match any test names beginning with 'test_startup' in network/ directory 
      :network/test_startup:
        - B
```

It’s common in C file naming to use the same base name for multiple files.
Given the following example list, care must be given to matcher construction to
single out test_comm_startup.c.

* tests/test_comm_hw.c
* tests/test_comm_startup.c
* tests/test_comm_startup_timers.c

```yaml
:flags:
  :test:
    :compile:
      # Full filename with extension distinguishes this file test_comm_startup_timers.c
      :test_comm_startup.c:
        - FOO
```

The preceding examples use substring matching, but, regular expression matching
could also be appropriate.

### YAML anchors & aliases

See the short but helpful article on [YAML anchors & aliases][yaml-anchors-aliases]
to understand these features of YAML.

Particularly in testing complex projects, per-test file matching may only get
you so far in meeting your build step flag needs. For instance, you may need to
set various flags for operations across many test files, but no convenient name
matching scheme works. Advanced YAML features can help you copy the same flags
into multiple `:flags` test file matchers.

Please see the discussion in [`:defines`][defines] for a complete example.

[yaml-anchors-aliases]: https://support.atlassian.com/bitbucket-cloud/docs/yaml-anchors/
[defines]: defines.md
