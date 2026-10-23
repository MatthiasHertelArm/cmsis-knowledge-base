---
id: "ceed-ceedling-packet-new-goodness"
type: "concept"
domain: "test"
title: "Ceedling Packet: New goodness"
summary: "And, the headlining feature of Ceedling 1.1.0 was Partials. A Partial is your C code sliced and diced to expose functional elements for testing that you could not otherwise access without rewriting your source code."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/#new-goodness"
license: "MIT"
mode: "V"
---

!!! feature "Ceedling 1.2.0 adds the most requested features and improvements"
    👀 See the [Changelog](https://github.com/ThrowTheSwitch/Ceedling/blob/master/docs/Changelog.md).

Ceedling 1.2.0 includes:

* [**Delta builds**](https://throwtheswitch.github.io/Ceedling/getting-started/builds.md) have been restored so that file regeneration and build actions only occur because of changed files or configuration.
* **`#include` relative paths & duplicate filename disambiguation**. Ceedling now fully [supports relative paths everywhere](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions.md#distinguishing-same-named-files) and offers options to distinguish files of the same name.
* **Multiple file extensions per file type.** You may now provide a list of file types (e.g. `.c` and `.cc`) via [`:extension`](https://throwtheswitch.github.io/Ceedling/configuration/reference/extension.md) to gather files into your project’s build.
* **Shuffled test order.** Ceedling now supports [Unity’s](https://throwtheswitch.github.io/Ceedling/overview/tools-and-frameworks.md#unity) randomized test case ordering (via a [`:unity` configuration setting](https://throwtheswitch.github.io/Ceedling/configuration/reference/unity.md#shuffle_tests)). [Delta builds](https://throwtheswitch.github.io/Ceedling/getting-started/builds.md) automatically adjust to always rerun test executables so test case ordering is shuffled.
* The **[`TEST_SOURCE_FILE()` build directive macro](https://throwtheswitch.github.io/Ceedling/testing-guide/build-directives.md#test_source_file-subtractive-notation)** can now be used to remove source files from a test executable build. This can be handy in overriding [Ceedling’s conventions](https://throwtheswitch.github.io/Ceedling/testing-guide/build-directives.md#test_source_file-the-headersource-convention) for associating source files with a test executable if your project structure does not match up with Ceedling’s conventions.
* The **new [Sanitize plugin](https://docs.throwtheswitch.org/Ceedling/1.2.0/plugins/sanitize/)** builds and runs tests with ASan, UBSan, and LeakSanitizer, naming each finding where a test fails and writing text, JSON, and SARIF reports.
* The **[build warnings](https://throwtheswitch.github.io/Ceedling/plugins/report-build-warnings-log.md)**, **[JUnit report](https://throwtheswitch.github.io/Ceedling/plugins/report-tests-log-factory.md#junit-xml-format)**, **[IDE integration](https://throwtheswitch.github.io/Ceedling/plugins/report-tests-ide-stdout.md), [GoogleTest report](https://throwtheswitch.github.io/Ceedling/plugins/report-tests-gtestlike-stdout.md)**, **[module generator](https://throwtheswitch.github.io/Ceedling/plugins/module-generator.md)**, and **[dependencies](https://throwtheswitch.github.io/Ceedling/plugins/dependencies.md)** plugins all received numerous bug fixes and feature expansions.
* **[Bullseye code coverage plugin](https://throwtheswitch.github.io/Ceedling/plugins/bullseye/index.md)** re-enabled and modernized (disabled since 1.0.0).
* **Dedicated mocks and test runner generation [build tasks](https://throwtheswitch.github.io/Ceedling/getting-started/command-line.md#build-plugin-tasks).** You may now run the test build pipeline only up through generating mocks or test runners with no compilation or test runs.
* Ceedling prerelease and release builds now automatically **[generate Software Bills of Material](https://throwtheswitch.github.io/Ceedling/project/sbom.md)** (SBOMs) and attach them to GitHub pre/releases along with the final Ruby gem.

And, the headlining feature of Ceedling 1.1.0 was [_Partials_](https://throwtheswitch.github.io/Ceedling/testing-guide/partials/index.md). A Partial is your C code sliced and diced to expose functional elements for testing that you could not otherwise access without rewriting your source code. Think of Partials as a scalpel for testing your code.

---
