---
id: "ceed-conventions-behaviors-build-output"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Build output"
summary: "Ceedling requires a top-level build directory for all the stuff that it, the accompanying test tools, and your toolchain generate. That build directory’s location is configured in the top-level :project section of your configuration file (discussed in the configuration reference)."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#build-output"
license: "MIT"
mode: "V"
---

Ceedling requires a top-level build directory for all the stuff
that it, the accompanying test tools, and your toolchain generate.
That build directory’s location is configured in the top-level 
`:project` section of your configuration file (discussed in the
[configuration reference](https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/../configuration/index.md)). There
can be a ton of generated files. By and large, you can live a full
and meaningful life knowing absolutely nothing at all about
the files and directories generated below the root build directory.

As noted already, it’s good practice to add your top-level build
directory to source control but nothing generated beneath it.
you'll spare yourself headache if you let Ceedling delete and
regenerate files and directories in a non-versioned corner
of your project’s filesystem beneath the top-level build directory.

The `artifacts/` directory is the one and only directory you may
want to know about beneath the top-level build directory. The
subdirectories beneath `artifacts` will hold your binary release
target output (if your project is configured for release builds)
and will serve as the conventional location for plugin output.
This directory structure was chosen specifically because it
tends to work nicely with Continuous Integration setups that
recognize and list build artifacts for retrieval / download.
