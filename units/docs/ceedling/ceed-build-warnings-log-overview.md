---
id: "ceed-build-warnings-log-overview"
type: "concept"
domain: "test"
title: "Build Warnings Log: Overview"
summary: "This plugin collects the warnings that command line tools print as a build preprocesses, compiles, and links, and writes them to a plain text log file when the build ends."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/report-build-warnings-log.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-build-warnings-log/#overview"
license: "MIT"
mode: "V"
---

This plugin collects the warnings that command line tools print as a build preprocesses,
compiles, and links, and writes them to a plain text log file when the build ends. Each
build context — `test`, `release`, or a plugin’s build such as `gcov` — gets its own log
in `<build root>/artifacts/<context>/`, written even when the build ends in an error.

Warnings from Ceedling itself or from code generation do not appear in these logs; only
the output of the preprocessing, compilation, and linking tools is collected.

Each warning keeps the lines that explain it. GCC and Clang print a warning with its
source line and a caret marking the spot, often after an `In function` or
`In file included from` line, and the log holds all of it:

```text
a.c: In function 'a':
a.c:2:21: warning: unused variable ’spare' [-Wunused-variable]
    2 | int a( void ) { int spare; return 0; }
      |                     ^~~~~
```

Each distinct warning is logged once per build context. A warning in a header that many
files include appears once, with the include chain of the first file that reported it.

Output from other toolchains, whose warnings do not follow GCC’s format, is collected a
line at a time.

The same warnings can also be written as [SARIF](#sarif-report) and/or [JSON](#json-report)
reports for other tools to read, such as a CI service that marks each warning on the line
of code it concerns.
