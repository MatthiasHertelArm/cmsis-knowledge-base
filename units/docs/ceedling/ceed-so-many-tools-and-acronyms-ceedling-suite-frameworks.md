---
id: "ceed-so-many-tools-and-acronyms-ceedling-suite-frameworks"
type: "concept"
domain: "test"
title: "So Many Tools and Acronyms: Ceedling suite frameworks"
summary: "[Unity] is a [unit test framework][unit-testing] for C. It provides facilities for test assertions, executing tests, and collecting / reporting test results."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/overview/tools-and-frameworks.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/overview/tools-and-frameworks/#ceedling-suite-frameworks"
license: "MIT"
mode: "V"
---

### Unity

[Unity] is a [unit test framework][unit-testing] for C. It provides facilities
for test assertions, executing tests, and collecting / reporting test
results. Unity derives its name from its implementation in a single C
source file (plus two C header files) and from the nature of its
implementation - Unity will build in any C toolchain and is configurable
for even the very minimalist of processors.

[Unity]: http://github.com/ThrowTheSwitch/Unity
[unit-testing]: http://en.wikipedia.org/wiki/Unit_testing

### CMock

[CMock]† is a tool written in Ruby able to generate [function mocks & stubs][test-doubles] 
in C code from a given C header file. Mock functions are invaluable in 
[interaction-based unit testing][interaction-based-tests].
CMock's generated C code uses Unity.

† Through a [plugin][FFF-plugin], Ceedling also supports
[FFF], _Fake Function Framework_, for [fake functions][test-doubles] as an
alternative to CMock's mocks and stubs.

[CMock]: http://github.com/ThrowTheSwitch/CMock
[test-doubles]: https://blog.pragmatists.com/test-doubles-fakes-mocks-and-stubs-1a7491dfa3da
[FFF]: https://github.com/meekrosoft/fff
[FFF-plugin]: ../plugins/fff.md
[interaction-based-tests]: http://martinfowler.com/articles/mocksArentStubs.html

### CException

[CException] is a C source and header file that provide a simple
[exception mechanism][exn] for C by way of wrapping up the
[setjmp / longjmp][setjmp] standard library calls. Exceptions are a much
cleaner and preferable alternative to managing and passing error codes
up your return call trace.

[CException]: http://github.com/ThrowTheSwitch/CException
[exn]: http://en.wikipedia.org/wiki/Exception_handling
[setjmp]: http://en.wikipedia.org/wiki/Setjmp.h
