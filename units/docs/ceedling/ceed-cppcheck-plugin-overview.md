---
id: "ceed-cppcheck-plugin-overview"
type: "concept"
domain: "test"
title: "Cppcheck: Plugin overview"
summary: "The Cppcheck plugin runs [Cppcheck] over your project and writes reports to the build artifacts directory. It provides two analysis modes."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/cppcheck.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/cppcheck/#plugin-overview"
license: "MIT"
mode: "V"
---

The Cppcheck plugin runs [Cppcheck] over your project and writes reports to the
build artifacts directory. It provides two analysis modes.

- **Whole project analysis**: `ceedling cppcheck:all` analyzes all project
  sources with every check enabled (`--enable=all`) and writes the reports you
  configure.
- **Single file analysis**: `ceedling cppcheck:<filename>` analyzes one source
  file using the checks in [`:enable_checks:`](#enable_checks), and prints
  findings to the console.

Reports are available in HTML, SARIF, text, and XML. The plugin also exposes
most of Cppcheck's configuration surface, including platform, language
standard, preprocessor defines, include and exclude paths, addons such as
MISRA, library configuration files, regular expression rules, and suppression
management.

A build can be failed on findings. See [`:fail_build:`](#fail_build).

!!! note "Analysis runs once per report format"
    Cppcheck emits one format per invocation, so each entry in
    [`:reports:`](#reports) costs its own full analysis pass. Cppcheck's own
    `--cppcheck-build-dir` cache reduces the cost of passes after the first.
