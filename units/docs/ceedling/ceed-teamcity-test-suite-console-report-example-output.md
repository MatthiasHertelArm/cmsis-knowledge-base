---
id: "ceed-teamcity-test-suite-console-report-example-output"
type: "concept"
domain: "test"
title: "TeamCity Test Suite Console Report: Example Output"
summary: "TeamCity's convention for identifying tests uses the naming convention of the underlying Java language in which TeamCity is written, package_or_namespace.ClassName.TestName."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/plugins/report-tests-teamcity-stdout.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-teamcity-stdout/#example-output"
license: "MIT"
mode: "V"
---

TeamCity's convention for identifying tests uses the naming convention of the
underlying Java language in which TeamCity is written,
`package_or_namespace.ClassName.TestName`.

This plugin maps Ceedling conventions to TeamCity test service messages as
`context.TestFilepath.TestCaseName`.

* `context` Your build's context defaults to `test`. Certain other test build 
  plugins (e.g. GCov) provide a different context (`gcov`) for test builds, 
  generally named after themselves.
* `TestFilepath` This identifier is the relative filepath of the relevant test
  file without a file extension (e.g. no `.c`).
* `TestCaseName` This identifier is a test case function name within a Ceedling test file.

```sh
 > ceedling test:UsartModel
```

```
##teamcity[testSuiteStarted name='TestUsartModel' flowId='15']
##teamcity[testStarted name='test.test/TestUsartModel.testGetBaudRateRegisterSettingShouldReturnAppropriateBaudRateRegisterSetting' flowId='15']
##teamcity[testFinished name='test.test/TestUsartModel.testGetBaudRateRegisterSettingShouldReturnAppropriateBaudRateRegisterSetting' duration='81' flowId='15']
##teamcity[testStarted name='test.test/TestUsartModel.testShouldReturnErrorMessageUponInvalidTemperatureValue' flowId='15']
##teamcity[testFinished name='test.test/TestUsartModel.testShouldReturnErrorMessageUponInvalidTemperatureValue' duration='81' flowId='15']
##teamcity[testStarted name='test.test/TestUsartModel.testGetFormattedTemperatureFormatsTemperatureFromCalculatorAppropriately' flowId='15']
##teamcity[testFailed name='test.test/TestUsartModel.testGetFormattedTemperatureFormatsTemperatureFromCalculatorAppropriately' message='Function TemperatureFilter_GetTemperatureInCelcius() called more times than expected.' details='File: test/TestUsartModel.c Line: 25' flowId='15']
##teamcity[testFinished name='test.test/TestUsartModel.testGetFormattedTemperatureFormatsTemperatureFromCalculatorAppropriately' duration='81' flowId='15']
##teamcity[testIgnored name='test.test/TestUsartModel.testShouldReturnWakeupMessage' flowId='15']
##teamcity[testSuiteFinished name='TestUsartModel' flowId='15']
```
