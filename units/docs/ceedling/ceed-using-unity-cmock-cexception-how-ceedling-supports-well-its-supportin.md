---
id: "ceed-using-unity-cmock-cexception-how-ceedling-supports-well-its-supportin"
type: "concept"
domain: "test"
title: "Using Unity, CMock & CException: How Ceedling supports, well, its supporting frameworks"
summary: "If you are using Ceedling for unit testing, this means you are using Unity, the C testing framework. Unity is fully built-in and enabled for test builds. It cannot be disabled."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/frameworks.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/frameworks/#how-ceedling-supports-well-its-supporting-frameworks"
license: "MIT"
mode: "V"
---

If you are using Ceedling for unit testing, this means you are using Unity,
the C testing framework. Unity is fully built-in and enabled for test builds.
It cannot be disabled.

If you want to use mocks in your test cases, you'll need to enable mocking 
and configure CMock with `:project` ↳ `:use_mocks` and the `:cmock` section 
of your project configuration respectively. CMock is fully supported by 
Ceedling but generally requires some set up for your project’s needs.

If you are incorporating CException into your release artifact, you'll need 
to enable exceptions and configure CException with `:project` ↳ 
`:use_exceptions` and the `:cexception` section of your project 
configuration respectively. Enabling CException makes it available in both 
release builds and test builds.

This section provides a high-level view of how the various tools become
part of your builds and fit into Ceedling’s configuration file. Ceedling’s 
configuration file is discussed in detail in the next section.

See [Unity], [CMock], and [CException]’s project documentation for all 
your configuration options. Ceedling offers facilities for providing these
frameworks their compilation and configuration settings. Discussing 
these tools and all their options in detail is beyond the scope of Ceedling 
documentation.
