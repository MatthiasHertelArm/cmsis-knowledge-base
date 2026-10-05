---
id: "ceed-environment-special-case-path-handling"
type: "concept"
domain: "test"
title: "`:environment:`: Special case: `PATH` handling"
summary: "In the specific case of specifying an environment key named :path, an array of string values will be concatenated with the appropriate platform-specific path separation character (i.e. : on Unix-variants, ; on Windows)."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/reference/environment.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/reference/environment/#special-case-path-handling"
license: "MIT"
mode: "V"
---

In the specific case of specifying an environment key named `:path`, an array 
of string values will be concatenated with the appropriate platform-specific 
path separation character (i.e. `:` on Unix-variants, `;` on Windows).

All other instances of environment keys assigned a value of a YAML array use 
simple concatenation.
