---
id: "ceed-which-ceedling-background"
type: "concept"
domain: "test"
title: "Which Ceedling: Background"
summary: "Ceedling is usually packaged and installed as a Ruby Gem. This gem ends up installed in an appropriate place by the gem package installer. Inside the gem installation is the entire Ceedling project."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/configuration/which-ceedling.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/configuration/which-ceedling/#background"
license: "MIT"
mode: "V"
---

Ceedling is usually packaged and installed as a Ruby Gem. This gem ends
up installed in an appropriate place by the `gem` package installer.
Inside the gem installation is the entire Ceedling project. The `ceedling`
command line launcher lives in `bin/` while the Ceedling application lives
in `lib/`. The code in `/bin` manages lots of startup details and base
configuration. Ultimately, it then launches the main application code from
`lib/`.

The features and conventions controlling _which ceedling_ dictate which
application code the `ceedling` command line handler launches.

!!! note "Ceedling development in `bin/`"
    Working on the code in Ceedling’s `bin/` and need to run it while a gem is 
    installed? You must take the additional step of specifying the path to the 
    `ceedling` launcher in your filesystem.

    In Unix-like systems:
    `> my/ceedling/changes/bin/ceedling <args>`.

    On Windows systems:
    `> ruby my\ceedling\changes\bin\ceedling <args>`.
