---
id: "ceed-quick-start-command-line-build-tasks"
type: "concept"
domain: "test"
title: "Quick Start: Command Line & Build Tasks"
summary: "Once you have Ceedling installed, you always have access to ceedling help."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/getting-started/quick-start.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/quick-start/#command-line-build-tasks"
license: "MIT"
mode: "V"
---

Once you have Ceedling installed, you always have access to `ceedling help`.

Once you have Ceedling installed, you have options for project creation
using Ceedling’s application commands:

* `ceedling new <name> <destination>`
* `ceedling examples` to list available example projects and 
  `ceedling example <name> <destination>` to create a readymade sample 
   project whose project file you can copy and modify.

Once you have a Ceedling project file and a project directory structure for your
code, Ceedling build tasks go like this:

* `ceedling test:MyCodeModule`, or
* `ceedling test:all`, or
* `ceedling release`, or, if you fancy and have the GCov plugin enabled,
* `ceedling clobber test:all gcov:all release --log --verbosity=obnoxious`
