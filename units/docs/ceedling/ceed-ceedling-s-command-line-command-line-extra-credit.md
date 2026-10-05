---
id: "ceed-ceedling-s-command-line-command-line-extra-credit"
type: "concept"
domain: "test"
title: "Ceedling’s Command Line: Command line extra credit"
summary: "Multiple build tasks can be executed at the command line."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/getting-started/command-line.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/getting-started/command-line/#command-line-extra-credit"
license: "MIT"
mode: "V"
---

### Combining tasks

Multiple build tasks can be executed at the command line.

For example, `ceedling clobber test:all release` will remove all generated
files; build and run all tests; and then build all source — in that order. If
any task fails along the way, execution halts before the next task.

Task order is executed as provided and can be important! Running `clobber` after
a `test:` or `release:` task will not accomplish much.

### Builds & Revision Control

The `clobber` task removes certain build directories in the course of 
deleting generated files.

In general, it’s best not to add to source control any Ceedling generated 
directories below the root of your top-level project build directory. That is, 
leave anything Ceedling & its accompanying tools generate out of source control.

[inline-ruby-string-expansion]: ../configuration/project-file.md#inline-ruby-string-expansion
