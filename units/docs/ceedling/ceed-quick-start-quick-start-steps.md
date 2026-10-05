---
id: "ceed-quick-start-quick-start-steps"
type: "concept"
domain: "test"
title: "Quick Start: Quick Start Steps"
summary: "Below is a quick overview of how to get started from Ceedling installation through running build tasks."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/getting-started/quick-start.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/quick-start/#quick-start-steps"
license: "MIT"
mode: "V"
---

Below is a quick overview of how to get started from Ceedling installation 
through running build tasks. Jump down just a teeny bit to see what the Ceedling 
command line looks like and navigate to all the documentation for the steps 
listed immediately below.

!!! warning "C toolchain requirement"
    Ceedling requires a command line C toolchain be available in your path and is
    flexible enough to work with most anything. By default, Ceedling is ready to 
    work with [GCC] out of the box (we recommend [MinGW] on Windows).

1. [Install Ceedling](https://throwtheswitch.github.io/Ceedling/getting-started/quick-start/installation.md)
1. Create a project
    * Use Ceedling to generate an example project (see next section), or
    * Add a Ceedling project file to the root of an existing project, or
    * Create a project from scratch:
        1. Create a project directory.
        1. Add source code and optionally test code however you’d like it organized.
        1. Create a Ceedling project file in the root of your project directory.
1. Run Ceedling tasks (see next section) from the working directory of your project.

A common build strategy is to use your target toolchain for release builds—with or 
without Ceedling—but rely on Ceedling + GCC for test builds (more on this 
[here][overview]).

!!! tip "Ceedling VS Code extension"
    If you are a Visual Studio Code user, you may want to install the
    [Ceedling extension](https://marketplace.visualstudio.com/items?itemName=throw-the-switch.vscode-ceedling).

[GCC]: https://gcc.gnu.org
[MinGW]: http://www.mingw.org/
[overview]: ../overview/index.md
