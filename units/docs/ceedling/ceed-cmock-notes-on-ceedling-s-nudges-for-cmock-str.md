---
id: "ceed-cmock-notes-on-ceedling-s-nudges-for-cmock-str"
type: "concept"
domain: "test"
title: "`:cmock`: Notes on Ceedling’s nudges for CMock strict ordering"
summary: "The preceding settings are tied to other Ceedling settings; hence, why they are documented here."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/cmock.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/cmock/#notes-on-ceedling-s-nudges-for-cmock-strict-ordering"
license: "MIT"
mode: "V"
---

The preceding settings are tied to other Ceedling settings; hence, why they are
documented here.

The first setting above, `:enforce_strict_ordering`, defaults to `FALSE` within
CMock. However, it is set to `TRUE` by default in Ceedling as our way of
encouraging you to use strict ordering.

Strict ordering is teeny bit more expensive in terms of code generated, test
execution time, and complication in deciphering test failures. However, it’s
good practice. And, of course, you can always disable it by overriding the
value in the Ceedling project configuration file.

[cmock-docs]: https://github.com/ThrowTheSwitch/CMock/blob/master/docs/CMock_Summary.md
