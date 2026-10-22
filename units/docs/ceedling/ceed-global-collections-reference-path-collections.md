---
id: "ceed-global-collections-reference-path-collections"
type: "concept"
domain: "test"
title: "Global Collections Reference: Path collections"
summary: "All configured source and include paths."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/reference/global-collections.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/global-collections/#path-collections"
license: "MIT"
mode: "V"
---

* `COLLECTION_PATHS_INCLUDE`:

    All configured include paths.

* `COLLECTION_PATHS_SOURCE`:

    All configured source paths.

* `COLLECTION_PATHS_SUPPORT`:

    All configured support paths.

* `COLLECTION_PATHS_TEST`:

    All configured test paths.

* `COLLECTION_PATHS_SOURCE_AND_INCLUDE`:

    All configured source and include paths.

* `COLLECTION_PATHS_SOURCE_INCLUDE_VENDOR`:

    All configured source and include paths plus applicable 
    vendor paths (Unity's source path plus CMock and 
    CException's source paths if mocks and exceptions are 
    enabled).

* `COLLECTION_PATHS_TEST_SUPPORT_SOURCE_INCLUDE`:

    All configured test, support, source, and include paths.

* `COLLECTION_PATHS_TEST_SUPPORT_SOURCE_INCLUDE_VENDOR`:

    All test, support, source, include, and applicable 
    vendor paths (Unity's source path plus CMock and 
    CException's source paths if mocks and exceptions are 
    enabled).

* `COLLECTION_PATHS_RELEASE_TOOLCHAIN_INCLUDE`:

    All configured release toolchain include paths.

* `COLLECTION_PATHS_TEST_TOOLCHAIN_INCLUDE`:

    All configured test toolchain include paths.

* `COLLECTION_PATHS_VENDOR`:

    Unity's source path plus CMock and CException's source 
    paths if mocks and exceptions are enabled.
