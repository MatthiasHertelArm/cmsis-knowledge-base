---
id: "ceed-testing-guide"
type: "concept"
domain: "test"
title: "Testing Guide"
summary: "Testing Guide"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/"
license: "MIT"
mode: "V"
---

!!! danger "Test file naming in Windows"
    **_Test filenames should not include “patch” or “setup”_**.
    Test filenames become test executables. Windows Installer Detection 
    Technology (part of UAC) requires administrator privileges to run 
    executables with this naming.
