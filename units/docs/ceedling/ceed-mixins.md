---
id: "ceed-mixins"
type: "concept"
domain: "test"
title: "Mixins"
summary: "Once you have a base configuration loaded, you may want to modify it for any number of reasons. Some example scenarios:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/configuration/mixins.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/mixins/"
license: "MIT"
mode: "V"
---

Once you have a [base configuration loaded](https://throwtheswitch.github.io/Ceedling/configuration/mixins/loading.md), you may want to 
modify it for any number of reasons. Some example scenarios:

* A single project actually contains mutiple build variations. You would
  like to maintain a common configuration that is shared among build
  variations with each build variation’s differences maintained separately.
* Your repository contains the configuration needed by your Continuous
  Integration server setup, but this is not fun to run locally. You would
  like to modify the configuration locally with configuration details 
  maintained by you external to your locally cloned repository.
* Ceedling’s default `gcc` tools do not work for your project needs. You
  would like the complex tooling configurations you most often need to
  be maintained separately and shared among projects. Ceedling includes
  a collection of ready-made toolchain target mixins (e.g. `clang`,
  `iar_arm`) that can be selected by name without any extra
  configuration — see [Built-in toolchain targets](#built-in-toolchain-targets).

Mixins allow you to merge configuration with your project configuration
just after the base project file is loaded. The merge is so low-level
and generic that you can, in fact, load an empty base configuration 
and merge in entire project configurations through mixins.

Mixins may be merged per a priority scheme:

1. `mixins:` section in your base configuration file that loads mixin 
   YAML files.
1. Environment variables that point to mixin files.
1. Command line `--mixin` flags that point to mixin files or provide
   inline YAML.

!!! tip
    The [`cipher_quest` example project](https://throwtheswitch.github.io/Ceedling/configuration/mixins/../getting-started/example-projects/cipher-quest.md)
    illustrates the use of Mixins for build variants.
