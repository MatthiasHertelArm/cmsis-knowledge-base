---
id: "ceed-global-collections-reference-options-and-artifacts"
type: "concept"
domain: "test"
title: "Global Collections Reference: Options and artifacts"
summary: "Unity plus CMock, and CException's .c filenames (without paths) if mocks and exceptions are enabled."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/reference/global-collections.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/global-collections/#options-and-artifacts"
license: "MIT"
mode: "V"
---

* `COLLECTION_VENDOR_FRAMEWORK_SOURCES`:

    Unity plus CMock, and CException's .c filenames (without 
    paths) if mocks and exceptions are enabled.

* `COLLECTION_RELEASE_ARTIFACT_EXTRA_LINK_OBJECTS`:

    If exceptions are enabled, CException's .c filenames 
    (without paths) remapped to configured object file 
    extension.

* `COLLECTION_TEST_FIXTURE_EXTRA_LINK_OBJECTS`:

    All test support source filenames (without paths) 
    remapped to configured object file extension.
