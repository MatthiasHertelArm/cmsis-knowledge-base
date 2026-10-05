---
id: "ceed-project-configuration-reference-configuration-sections"
type: "concept"
domain: "test"
title: "Project Configuration Reference: Configuration sections"
summary: "Each top-level key in your project YAML file corresponds to one configuration section. All sections are optional; Ceedling supplies defaults for anything left unset."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/reference/project-configuration.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/project-configuration/#configuration-sections"
license: "MIT"
mode: "V"
---

Each top-level key in your project YAML file corresponds to one configuration
section. All sections are optional; Ceedling supplies defaults for anything
left unset.

| Section | Description |
|---|---|
| **[`:project`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/project.md)** | Build root, build modes, version info, and global project switches |
| **[`:mixins`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/mixins.md)** | Load and merge additional YAML configuration files into the base project configuration |
| **[`:test_build`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/test-build.md)** | Test-specific build options: assembly support, mock generation, preprocessor use, and more |
| **[`:release_build`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/release-build.md)** | Release artifact build options and output settings |
| **[`:paths`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/paths.md)** | Source, test, include, support, library, and vendor path globs |
| **[`:files`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/files.md)** | Explicit file inclusion and exclusion overrides |
| **[`:environment`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/environment.md)** | Set and export environment variables from within the project configuration |
| **[`:extension`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/extension.md)** | File extension strings for source, header, object, binary, and other file types |
| **[`:defines`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/defines.md)** | Per-context, per-file preprocessor symbol definitions |
| **[`:flags`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/flags.md)** | Compiler, linker, assembler, and preprocessor flags per build context |
| **[`:libraries`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/libraries.md)** | Test and release libraries plus linker search paths |
| **[`:unity`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/unity.md)** | Unity test framework configuration (defines, helper file paths, etc.) |
| **[`:cmock`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/cmock.md)** | CMock mock generation configuration |
| **[`:test_runner`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/test-runner.md)** | Test runner generation configuration |
| **[`:cexception`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/cexception.md)** | CException configuration |
| **[`:plugins`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/plugins.md)** | Enable built-in plugins and configure custom plugin load paths |
| **[`:tools`](https://throwtheswitch.github.io/Ceedling/reference/project-configuration/../configuration/reference/tools.md)** | Define or override compiler, linker, and other tool invocations |
