---
id: "ceed-parallel-build-steps-operating-system-restrictions"
type: "concept"
domain: "test"
title: "Parallel Build Steps: Operating System restrictions"
summary: "Modern versions of macOS and Windows both include security gatekeeping that can limit Ceedling’s ability to achieve speedups and true parallelism. These products can:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/parallel-builds.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/parallel-builds/#operating-system-restrictions"
license: "MIT"
mode: "V"
---

!!! warning "Operating Systems security protections can limit parallelism"

Modern versions of macOS and Windows both include security gatekeeping that can
limit Ceedling’s ability to achieve speedups and true parallelism. These
products can:

1. Execute first-run security checks on newly built, unsgined executables
(such as components of a test suite) that greatly slow down execution.
1. Force one-at-a-time execution for any unsigned software attempting to 
spawn multiple processes simultaneously.

Signing the executables Ceedling generates is wildly complex and maybe even
practically impossible.

A current limitation of Ceedling since 1.0.0 also contributes to these
bottlenecks. Namely, with the release of 1.0.0 Ceedling lost “delta” builds —
the ability to only regenerate components of a test suite that have changed.
This means Ceedling’s test suites are fully rebuilt each time with OS first-run
security checks to fire at run time. Future versions of Ceedling will restore
this ability.

!!! tip "Configuring OS security restrictions"
    Read up on your Operating System’s options for configuring the restrictions 
    noted above. For instance, you may be able to configure certain exceptions 
    for your terminal application that cascade to benefit Ceedling’s parallelism.
