---
id: "ceed-flags-contexts-operations-and-matchers"
type: "concept"
domain: "test"
title: "`:flags`: Contexts, Operations, and Matchers"
summary: "The basic layout of :flags involves the concepts of contexts and operations."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/flags.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/flags/#contexts-operations-and-matchers"
license: "MIT"
mode: "V"
---

The basic layout of `:flags` involves the concepts of contexts and operations.

General case:
```yaml
:flags:
  :<context>:      # :test or :release
    :<operation>:  # :preprocess, :compile, :assemble, or :link
      - <flag>
      - ...
```

Advanced matching for **_test_** build handling only:
```yaml
:flags:
  :test:
    :<operation>:  # :preprocess, :compile, :assemble, or :link
      :<matcher>:  # Matches a subset of test executables 
        - <flag>   # List of flags added to that subset’s build operation command line
        - ...
```

A context is the build context you want to modify — `:test` or `:release`.
Plugins can also hook into `:flags` with their own context.

An operation is the build step you wish to modify — `:preprocess`, `:compile`,
`:assemble`, or `:link`.

* The `:preprocess` operation is only used from within the `:test` context.
* The `:assemble` operation is only of use within the `:test` or `:release`
  contexts if assembly support has been enabled in `:test_build` or
  `:release_build`, respectively, and assembly files are a part of the project.

You specify the flags you want to add to a build step beneath `:<context>` ↳
`:<operation>`. In many cases this is a simple YAML list of strings that will
become flags in a tool’s command line.

**_Specifically and only in the `:test` context_** you also have the option to
create test file matchers that apply flags to some subset of your test build.
Note that file matchers and the simpler flags list format cannot be mixed for
`:flags` ↳ `:test`.
