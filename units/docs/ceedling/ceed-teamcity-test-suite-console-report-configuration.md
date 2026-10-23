---
id: "ceed-teamcity-test-suite-console-report-configuration"
type: "concept"
domain: "test"
title: "TeamCity Test Suite Console Report: Configuration"
summary: "All the report_testsstdout plugins may be enabled in various combinations. But, some combinations may not make a great deal of sense."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/plugins/report-tests-teamcity-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-teamcity-stdout/#configuration"
license: "MIT"
mode: "V"
---

All the `report_tests_*_stdout` plugins may be enabled in various combinations.
But, some combinations may not make a great deal of sense. The TeamCity
plugin “plays nice” with all the others but is generally most appropriate 
running in a CI build on a TeamCity server. Its output will clutter and obscure
console logging at a local development environment command line.

You may enable the TeamCity plugin (above) but disable its operation using the
following.

```YAML
:teamcity:
  :build: FALSE
```

This may seem silly, right? Why enable the plugin and then disable it,
cancelling it out? The answer has to do with _where_ you use the second YAML
blurb configuration setting.

Ceedling provides Mixins for applying configurations settings on top of your
base project configuraiton file. 
See the [Mixins documentation][ceedling-mixins] for full details.

[ceedling-mixins]: ../configuration/mixins.md#base-configuration-mixins-entries

As an example, you might enable the plugin in the main project file that is
committed to your repository while disabling the plugin in your local user
project file that is ignored by your repository. In this way, the plugin would
run on a TeamCity build server but not in your local development environment.
