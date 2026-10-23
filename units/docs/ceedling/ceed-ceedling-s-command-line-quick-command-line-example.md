---
id: "ceed-ceedling-s-command-line-quick-command-line-example"
type: "concept"
domain: "test"
title: "Ceedling’s Command Line: Quick command line example"
summary: "To exercise the Ceedling command line quickly, follow these steps after installing Ceedling:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/getting-started/command-line.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/command-line/#quick-command-line-example"
license: "MIT"
mode: "V"
---

To exercise the Ceedling command line quickly, follow these steps after 
[installing Ceedling](https://throwtheswitch.github.io/Ceedling/getting-started/command-line/installation.md):

1. Open a terminal and chnage directories to a location suitable for
   an example project.
1. Execute `ceedling example temp_sensor` in your terminal. The `example`
   argument is an application command.
1. Change directories into the new _temp_sensor/_ directory.
1. Execute `ceedling test:all` in your terminal. The `test:all` is a
   build task executed by the default `build` application command
   (`build` is an optional keyword for this command line).
1. Take a look at the build and test suite console output as well as 
   the _project.yml_ file in the root of the example project.
