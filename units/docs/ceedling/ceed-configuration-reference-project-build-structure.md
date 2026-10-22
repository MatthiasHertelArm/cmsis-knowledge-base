---
id: "ceed-configuration-reference-project-build-structure"
type: "concept"
domain: "test"
title: "Configuration Reference: Project & Build Structure"
summary: "Build root, default tasks, parallelism, test preprocessor, release build toggle, crash backtrace, and more."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/configuration/reference/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/#project-build-structure"
license: "MIT"
mode: "V"
---

-   :material-book-open-variant: **[`:project` — Global Project Settings][ref-project]**

    ---

    Build root, default tasks, parallelism, test preprocessor, release build
    toggle, crash backtrace, and more.

-   :material-book-open-variant: **[`:mixins` — Mixins][ref-mixins]**

    ---

    Load and merge additional YAML configuration files into your base project
    configuration for flexible, composable builds.

-   :material-book-open-variant: **[`:test_build` — Test Build Settings][ref-test-build]**

    ---

    Assembly file support for test suite builds.

-   :material-book-open-variant: **[`:partials` — Partials Settings][ref-partials]**

    ---

    Bound how large a single C construct may grow during extraction before
    Partial generation fails outright rather than searching indefinitely.

-   :material-book-open-variant: **[`:release_build` — Release Build Settings][ref-release-build]**

    ---

    Output artifact name, assembly support, and additional artifact file copying.

-   :material-book-open-variant: **[`:environment` — Environment Variables][ref-environment]**

    ---

    Define shell environment variables that are set before tools are invoked,
    with support for inline Ruby string expansion.
