---
id: "ceed-module-generator-overview"
type: "concept"
domain: "test"
title: "Module Generator: Overview"
summary: "With a single call, Ceedling can generate a source, header, and test file for a new module. If given a pattern, it can even create a series of submodules to support specific design patterns."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/module-generator.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/module-generator/#overview"
license: "MIT"
mode: "V"
---

With a single call, Ceedling can generate a source, header, and test file for a new 
module. If given a pattern, it can even create a series of submodules to support 
specific design patterns. Finally, it can just as easily remove related modules, 
avoiding the need to delete each individually.

Let's say, for example, that you want to create a single module named `MadScience`.

```sh
ceedling module:create[MadScience]
```

It says we're speaking to the module plugin, and we want to create a new module. The
name of that module is between the brackets. It will keep this case, unless you have
specified a different default (see configuration). It will create three files:
`MadScience.c`, `MadScience.h`, and `TestMadScience.c`. *NOTE* that it is important that
there are no spaces between the brackets. We know, it's annoying... but it's the rules.
