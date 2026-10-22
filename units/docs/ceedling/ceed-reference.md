---
id: "ceed-reference"
type: "concept"
domain: "test"
title: "Reference"
summary: "The Reference section is a quick-lookup companion to Ceedling's narrative documentation. Where the other sections explain concepts and walk you through workflows, these pages collect every command, macro, variable, constant, and configuration section into compact, scannable lists."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/reference/index.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/reference/"
license: "MIT"
mode: "V"
---

The Reference section is a quick-lookup companion to Ceedling's narrative
documentation. Where the other sections explain concepts and walk you through
workflows, these pages collect every command, macro, variable, constant, and
configuration section into compact, scannable lists.




-   :material-console: **[Command Line][command-line]**

    ---

    All application commands and build task syntax.

-   :material-book-open-variant: **[Project Configuration][project-configuration]**

    ---

    Project configuration sections, project loading, and modifying 
    a project configuration with mixins.

-   :material-pound: **[Test Build Directives][build-directives]**

    ---

    Macros for affecting the build configuration for an individual test file.

-   :material-variable: **[Environment Variables][environment-vars]**

    ---

    Environment variables recognized by Ceedling.

-   :material-pound: **[Partials Macros][partials-macros]**

    ---

    All function selection and static variable access macros used with 
    [Partials](https://throwtheswitch.github.io/Ceedling/reference/../testing-guide/partials/index.md)

-   :material-chart-bar: **[Coverage Reporting][coverage-reporting]**

    ---

    All [GCov plugin](https://throwtheswitch.github.io/Ceedling/reference/../plugins/gcov/index.md) configuration options including 
    those for advanced reports with GCovr and ReportGenerator.

-   :material-database: **[Global Collections][global-collections]**

    ---

    All globally-accessible Ruby constants assembled at startup.



[command-line]:          command-line.md
[project-configuration]: project-configuration.md
[build-directives]:      build-directives.md
[environment-vars]:      environment-vars.md
[partials-macros]:       partials-macros.md
[global-collections]:    global-collections.md
[coverage-reporting]:    gcov-plugin.md
