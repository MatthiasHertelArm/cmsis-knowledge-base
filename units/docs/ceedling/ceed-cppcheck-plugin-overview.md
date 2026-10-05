---
id: "ceed-cppcheck-plugin-overview"
type: "concept"
domain: "test"
title: "Cppcheck: Plugin overview"
summary: "The Cppcheck plugin integrates Cppcheck static analysis into Ceedling, facilitating automated code quality checks as part of your development workflow. It provides two analysis modes:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/cppcheck.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/cppcheck/#plugin-overview"
license: "MIT"
mode: "V"
---

The Cppcheck plugin integrates [Cppcheck](https://cppcheck.sourceforge.io)
static analysis into Ceedling, facilitating automated code quality checks as
part of your development workflow. It provides two analysis modes:

- **Whole project analysis**: By running `ceedling cppcheck:all`, all project
source files will be analyzed with all checks enabled (`--enable=all`) and
configurable reports can be generated in multiple formats.
- **Single file analysis**: By running `ceedling cppcheck:<filename>`, an
individual source file will be analyzed using the checks configured in the
`:enable_checks` list (defaults to `style`).

The plugin supports extensive Cppcheck configuration options such as platform,
language standard, preprocessor defines, include/exclude paths, and suppression
management. It also integrates with advanced features like MISRA addons, custom
check levels, library configuration files, and regular expression rules. All of
these can be configured in your `project.yml` file.

The plugin can produce reports in HTML, SARIF, text, and XML (v2 and v3)
formats, all stored under the build artifacts directory.

It also suppoprts using a project file (such as `compile_commands.json` or a
Cppcheck GUI project), in which case, the plugin delegates source and include
path discovery to Cppcheck rather than using Ceedling's own file collection.
