---
id: "ceed-which-ceedling-settings"
type: "concept"
domain: "test"
title: "Which Ceedling: Settings"
summary: "The environment variable and configuration entry for Which Ceedling can contain two values:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/which-ceedling.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/which-ceedling/#settings"
license: "MIT"
mode: "V"
---

The environment variable and configuration entry for _Which Ceedling_ can
contain two values:

1. The value `gem` indicates that the command line `ceedling` launcher 
   should run the application packaged alongside it in `lib/` (these 
   paths are typically found in the gem installation location).
1. A relative or absolute path in your file system. Such a path should 
   point to the top-level directory that contains Ceedling’s `bin/` and 
   `lib/` sub-directories.
