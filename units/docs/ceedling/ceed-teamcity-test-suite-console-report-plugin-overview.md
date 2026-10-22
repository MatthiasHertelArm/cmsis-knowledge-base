---
id: "ceed-teamcity-test-suite-console-report-plugin-overview"
type: "concept"
domain: "test"
title: "TeamCity Test Suite Console Report: Plugin Overview"
summary: "This plugin is intended to be used within [TeamCity] Continuous Integration (CI) builds. It processes Ceedling test suites and executable output into TeamCity [service messages][service-messages]."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/report-tests-teamcity-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-teamcity-stdout/#plugin-overview"
license: "MIT"
mode: "V"
---

This plugin is intended to be used within [TeamCity] Continuous Integration
(CI) builds. It processes Ceedling test suites and executable output into
TeamCity [service messages][service-messages]. Service messages are a specially
formatted type of log output that a TeamCity build server picks out of build
output to collect progress and metrics of various sorts.

Typically, this plugin is used only in CI builds. Its output is unhelpful in
development builds locally. See the [Configuration](#configuration) section for
options on enabling the build in CI but disabling it locally.

[TeamCity]: https://www.jetbrains.com/teamcity/
[service-messages]:
https://www.jetbrains.com/help/teamcity/service-messages.html
