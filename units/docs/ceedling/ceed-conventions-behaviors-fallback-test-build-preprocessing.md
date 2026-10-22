---
id: "ceed-conventions-behaviors-fallback-test-build-preprocessing"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Test preprocessing / Fallback test build preprocessing"
summary: "Ceedling depends on the GNU Compiler Collection (gcc) for many of its advanced features (such as in the preceding sections)."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#fallback-test-build-preprocessing"
license: "MIT"
mode: "V"
---

_Part of: Test preprocessing_

Ceedling depends on the GNU Compiler Collection (`gcc`) for many of its advanced 
features (such as in the preceding sections).

Older versions of `gcc` or `clang` standins may not support certain preprocessing
features Ceedling requires. Ceedling probes for those features; if they are not 
found then Ceedling falls back to a simpler, best-effort
[fallback preprocessing][fallback-preprocessing].

Fallback preprocessing is a best effort with no guarantees. It is not as capable 
as full preprocessing, but it can usually handle the most common preprocessing 
needs (i.e. conditional compilation). Ceedling does what it can to find and log 
issues related to inadequate preprocessing before you get to mysterious 
compilation errors.

!!! tip "Fallback preprocessing for faster test builds"
    Ceedling’s internal [fallback preprocessing mode can be forced][fallback-preprocessing],
    and, for **_some_** projects this can be a shortcut to running advanced 
    Ceedling features such as Partials with faster builds.

    **_If using Partials, there’s a good chance your code is too complex for fallback preprocessing._**

[project-settings]: ../configuration/reference/project.md
[partials]: partials/index.md
[fallback-preprocessing]: ../configuration/reference/test-build.md#preprocess_force_fallback
