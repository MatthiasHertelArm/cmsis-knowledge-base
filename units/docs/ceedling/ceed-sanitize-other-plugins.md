---
id: "ceed-sanitize-other-plugins"
type: "concept"
domain: "test"
title: "Sanitize: Other plugins"
summary: "A test executable built with sanitizers cannot run under Valgrind. Valgrind builds are never instrumented by this plugin."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/sanitize.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/sanitize/#other-plugins"
license: "MIT"
mode: "V"
---

A test executable built with sanitizers cannot run under Valgrind. Valgrind
builds are never instrumented by this plugin. A `valgrind:` build whose own
flags carry `-fsanitize`, such as flags it uses from `:flags` ↳ `:test`, stops
with a message naming them.

Coverage builds from the Gcov and Bullseye plugins are not instrumented either.
Sanitizers and coverage instrumentation each alter the code they build, and are
kept apart in their own builds.

[AddressSanitizer]: https://clang.llvm.org/docs/AddressSanitizer.html
[UndefinedBehaviorSanitizer]: https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html
[LeakSanitizer]: https://clang.llvm.org/docs/LeakSanitizer.html
[SARIF]: https://sarifweb.azurewebsites.net
