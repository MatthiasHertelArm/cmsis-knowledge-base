---
id: "ceed-a-build-system-for-all-your-c-mad-simple-sample-project-file"
type: "concept"
domain: "test"
title: "A Build System for All Your C Mad Scientisting Needs: Simple Sample Project File"
summary: "For a project including Unity/CMock unit tests and using the default toolchain gcc, the configuration file could be as simple as this:"
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/overview/build-system.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/overview/build-system/#simple-sample-project-file"
license: "MIT"
mode: "V"
---

For a project including Unity/CMock unit tests and using the default 
toolchain `gcc`, the configuration file could be as simple as this:

```yaml
:project:
  :build_root: project/build/
  :release_build: TRUE

:paths:
  :test:
    - tests/**
  :source:
    - source/**
  :include:
    - inc/**
```

From the command line, to run all your unit tests, you would run 
`ceedling test:all`. To build the release version of your project,
you would simply run `ceedling release`. That's it!

!!! tip "Want to see a real world project configuration?"
    See this [commented project file][example-config-file] 
    for a much more complete and sophisticated example of a project 
    configuration.

Of course, many more advanced options allow you to configure
your project with a variety of features to meet a variety of needs.
Ceedling can work with practically any command line toolchain
and directory structure – all by way of the configuration file.

See the later [configuration section][project-configuration] for 
way more details on your project configuration options.

A facility for [plugins](https://throwtheswitch.github.io/Ceedling/overview/build-system/../plugins/index.md) also allows you to 
extend Ceedling's capabilities for needs such as custom code metrics 
reporting, build artifact packaging, and much more. A variety of 
built-in plugins come with Ceedling.

[example-config-file]: ../snapshot/assets/project.yml
[project-configuration]: ../configuration/index.md
