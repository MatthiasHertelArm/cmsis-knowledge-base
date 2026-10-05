---
id: "ceed-build-warnings-log-overview"
type: "concept"
domain: "test"
title: "Build Warnings Log: Overview"
summary: "This plugin captures warning messages output by command line tools throughout a build. At the end of a build, any collected warning messages are written to one or more plain text log files."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/report-build-warnings-log.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-build-warnings-log/#overview"
license: "MIT"
mode: "V"
---

This plugin captures warning messages output by command line tools throughout a
build. At the end of a build, any collected warning messages are written to one 
or more plain text log files.

Warning messages are collected for all compilation-related builds and
differentiated by build context — `test`, `release`, or plugin-modified build 
(e.g. `gcov`).

Ceedling warning messages or warning messages from code generation will not
appear in log files; warnings are only collected from build step command line
tools for the predefined build steps of preprocessing, compilation, and
linking.

Log files are written to `<build root>/artifacts/<context>/`.
