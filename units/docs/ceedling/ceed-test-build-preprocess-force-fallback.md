---
id: "ceed-test-build-preprocess-force-fallback"
type: "concept"
domain: "test"
title: "`:test_build`: `:preprocess_force_fallback`"
summary: "This option is primarily used to enable certain Ceedling self-tests, but it may be valuable is a tool chain’s preprocessor somehow falsely indicates that directives-only preprocessing is available."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/test-build.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/test-build/#preprocess-force-fallback"
license: "MIT"
mode: "V"
---

This option is primarily used to enable certain Ceedling self-tests,
but it may be valuable is a tool chain’s preprocessor somehow falsely
indicates that directives-only preprocessing is available.

At startup, if test preprocessing is enabled, Ceedling probes the 
C preprocessor tool for indications that it support directives-only
mode. If it does not, Ceedling uses less capable text-only scanning
of C files when directives-only C preprocessing is preferred. Some 
toolchains, particularly older variations, may not support this mode.

This flag forces Ceedling to use text-scanning fallback mechanisms
regardless of preprocessor capabilities (the start up probe is 
entirely skipped.)

**Default**: FALSE
