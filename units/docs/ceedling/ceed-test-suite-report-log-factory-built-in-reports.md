---
id: "ceed-test-suite-report-log-factory-built-in-reports"
type: "concept"
domain: "test"
title: "Test Suite Report Log Factory: Built-in Reports"
summary: "Each report is populated with a name, using :project ↳ :name from your configuration if set."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/report-tests-log-factory.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/report-tests-log-factory/#built-in-reports"
license: "MIT"
mode: "V"
---

Each report is populated with a name, using `:project` ↳ `:name` from your configuration if set.

Those reports that support build time or test suite execution time “stopwatch” values include them.

### Execution duration values

Some test reporting formats include the execution time (duration) for aspects of a test suite run. Various granularities exist from the total time for all tests to the time of each suite (per the relevant definition of a suite) to the time required to run individual test cases. See _CeedlingPacket_ for the details on time duration values.

Ceedling automatically gathers all the relevant durations. In fact, Ceedling itself performs the needed timing and arithmetic in all cases, except one. Individual test case execution time tracking is specifically a [Unity] feature (see its documentation for more details). If enabled and if your platform supports the time mechanism Unity relies on, Ceedling will automatically collect test case time values and make them available to reports.

To enable test case duration measurements, they must be enabled as a Unity compilation option. Add `UNITY_INCLUDE_EXEC_TIME` to Unity’s compilation symbols (`:unity` ↳ `:defines`) in your Ceedling project file (below). This plugin and the core of Ceedling take care of the rest. Unity test case durations as reported by Ceedling default to 0 if this Unity compilation option is not configured.

```yaml
:unity:
  :defines:
    - UNITY_INCLUDE_EXEC_TIME
```

_Note:_ Most test cases are quite short, and most computers are quite fast. As such, Unity test case execution time is often reported as 0 milliseconds as the CPU execution time for a test case typically remains in the microseconds range. Unity would require special rigging that is inconsistently available across platforms to measure test case durations at a finer resolution.

[Unity]: https://github.com/ThrowTheSwitch/Unity

### JSON Format

[JSON] is “a lightweight data-interchange format.” JSON serializes common data structures into a human readable form. The format has several pros, including the ability for entirely different programming languages to ingest JSON and recreate these data structures. As such, this makes JSON a good report generation option as the result can be easily programmatically manipulated and put to use.

Something like XML is a general purpose structure for, well, structuring data. XML has enough formality that XML formats can be validated with general purpose tools plus much more. JSON is much more flexible but is rather tied to the data it encodes. Small changes to a data structure can have big impacts.

The JSON this plugin generates uses an ad hoc set of data structures following no standard — though any other test framework outputting test results in JSON may look fairly similar.

#### Example JSON configuration YAML

```yaml
:plugins:
  :enabled:
    - report_tests_log_factory

:report_tests_log_factory:
  :reports:
    - json
  # Default filename shown for completeness
  # `:json` block only needed to override default
  :json:
    :filename: tests_report.json
```

[JSON]: https://www.json.org/

#### Example JSON test report

In the following example a single test file _TestUsartModel.c_ exercised four test cases. Two test cases passed, one test case failed, and one test case was ignored.

```sh
 > ceedling test:UsartModel
```

```json
{
  "Name": "Ceedling Test Suite",
  "BuildDuration": 123.4,
  "FailedTests": [
    {
      "file": "test/TestUsartModel.c",
      "test": "testGetFormattedTemperatureFormatsTemperatureFromCalculatorAppropriately",
      "line": 25,
      "message": "Function TemperatureFilter_GetTemperatureInCelcius() called more times than expected."
    }
  ],
  "PassedTests": [
    {
      "file": "test/TestUsartModel.c",
      "test": "testGetBaudRateRegisterSettingShouldReturnAppropriateBaudRateRegisterSetting"
    },
    {
      "file": "test/TestUsartModel.c",
      "test": "testShouldReturnErrorMessageUponInvalidTemperatureValue"
    }
  ],
  "IgnoredTests": [
    {
      "file": "test/TestUsartModel.c",
      "test": "testShouldReturnWakeupMessage"
    }
  ],
  "Summary": {
    "total_tests": 4,
    "passed": 2,
    "ignored": 1,
    "failures": 1
  }
}
```

### JUnit XML Format

[JUnit] holds a certain position among testing tools. While it is an xUnit-style framework specific to unit testing Java, it has influenced how Continuous Integration build tools operate, and its [JUnit XML report format][junit-xml-format] has become something of a de facto standard for test reports in any language. The JUnit XML format has been revised in various ways over time but generally has more available documentation than some other formats.

[JUnit]: https://junit.org/
[junit-xml-format]: https://docs.getxray.app/display/XRAY/Taking+advantage+of+JUnit+XML+reports

#### Example JUnit configuration YAML

```yaml
:plugins:
  :enabled:
    - report_tests_log_factory

:report_tests_log_factory:
  :reports:
    - junit
  # Defaults shown for completeness
  # `:junit` block only needed to override defaults
  :junit:
    :filename: junit_tests_report.xml
    :file_line_anchor: FALSE
```

#### JUnit test locations

Each `<testcase>` names where its test lives, so CI tools can group results and
link to the code.

* **`classname`** is the test file’s path without its extension, the same as the
  enclosing `<testsuite>` name. Keeping the path matters because Ceedling can build
  two test files of the same name in different folders, each with a test case of
  the same name. CI tools identify a test case by its class and name together, and
  the path keeps the two apart.
* **`file`** is the test file’s path.
* **`line`** is the line Unity reported for the test, when it reports one.
* A failure’s message starts with the file and line in the form compilers use,
  such as `test/TestUsartModel.c:62: Expected 8 Was 9`.

Some tools follow a `file` attribute written as `path#line` to the line itself.
Set `:file_line_anchor` to `TRUE` to write `file` that way for each test case that
has a line, such as `test/TestUsartModel.c#62`. It defaults to `FALSE`, which
writes the plain path that tools such as GitLab turn into a link.

#### Example JUnit test report

In the following example a single test file _TestUsartModel.c_ exercised four test cases. Two test cases passed, one test case failed, and one test case was ignored (a.k.a. “skipped” in JUnit lingo).

In mapping a Ceedling test suite to JUnit conventions, a Ceedling _test file_ becomes a JUnit _test suite_.

```sh
 > ceedling test:UsartModel
```

```xml
<?xml version="1.0" encoding="utf-8" ?>
<testsuites name="Ceedling Test Suite" tests="4" failures="1" time="0.331">
  <testsuite name="test/TestUsartModel" tests="4" failures="1" skipped="1" errors="0" time="0.331">
    <testcase name="testGetBaudRateRegisterSettingShouldReturnAppropriateBaudRateRegisterSetting" classname="test/TestUsartModel" file="test/TestUsartModel.c" line="25" time="0.000"/>
    <testcase name="testShouldReturnErrorMessageUponInvalidTemperatureValue" classname="test/TestUsartModel" file="test/TestUsartModel.c" line="33" time="0.000"/>
    <testcase name="testGetFormattedTemperatureFormatsTemperatureFromCalculatorAppropriately" classname="test/TestUsartModel" file="test/TestUsartModel.c" line="44" time="0.000">
      <failure message="test/TestUsartModel.c:44: Function TemperatureFilter_GetTemperatureInCelcius() called more times than expected." />
    </testcase>
    <testcase name="testShouldReturnWakeupMessage" classname="test/TestUsartModel" file="test/TestUsartModel.c" line="51" time="0.000">
      <skipped />
    </testcase>
  </testsuite>
</testsuites>
```

### CppUnit XML Format

[CppUnit] is an xUnit-style port of the JUnit framework to C/C++. Documentation for its XML test report is scattered and not easily linked.

[CppUnit]: https://freedesktop.org/wiki/Software/cppunit/

#### Example CppUnit configuration YAML

```yaml
:plugins:
  :enabled:
    - report_tests_log_factory

:report_tests_log_factory:
  :reports:
    - cppunit
  # Default filename shown for completeness
  # `:cppunit` block only needed to override default
  :cppunit:
    :filename: cppunit_tests_report.xml
```

#### Example CppUnit test report

In the following example a single test file _TestUsartModel.c_ exercised four test cases. Two test cases passed, one test case failed, and one test case was ignored.

In mapping a Ceedling test suite to CppUnit conventions, a CppUnit test name is the concatenation of a Ceedling test filename and a test case function name. As such, a test filename will appear in the report a number of times equal to the number of test cases it holds. Test IDs are merely an incrementing count useful to uniquely identifying tests by number; no ordering or convention is enforced in generating them.

```sh
 > ceedling test:UsartModel
```

```xml
<?xml version="1.0" encoding="utf-8" ?>
<TestRun name="Ceedling Test Suite">
  <FailedTests>
    <Test id="1">
      <Name>test/TestUsartModel.c::testGetFormattedTemperatureFormatsTemperatureFromCalculatorAppropriately</Name>
      <FailureType>Assertion</FailureType>
      <Location>
        <File>test/TestUsartModel.c</File>
        <Line>25</Line>
      </Location>
      <Message>Function TemperatureFilter_GetTemperatureInCelcius() called more times than expected.</Message>
    </Test>
  </FailedTests>
  <SuccessfulTests>
    <Test id="2">
      <Name>test/TestUsartModel.c::testGetBaudRateRegisterSettingShouldReturnAppropriateBaudRateRegisterSetting</Name>
    </Test>
    <Test id="3">
      <Name>test/TestUsartModel.c::testShouldReturnErrorMessageUponInvalidTemperatureValue</Name>
    </Test>
  </SuccessfulTests>
  <IgnoredTests>
    <Test id="4">
      <Name>test/TestUsartModel.c::testShouldReturnWakeupMessage</Name>
    </Test>
  </IgnoredTests>
  <Statistics>
    <Tests>4</Tests>
    <Ignores>1</Ignores>
    <FailuresTotal>1</FailuresTotal>
    <Errors>0</Errors>
    <Failures>1</Failures>
  </Statistics>
</TestRun>
```

### HTML Format

This plugin creates an adhoc HTML page in a single file.

#### Example HTML configuration YAML

```yaml
:plugins:
  :enabled:
    - report_tests_log_factory

:report_tests_log_factory:
  :reports:
    - html
  # Default filename shown for completeness
  # `:html` block only needed to override default
  :html:
    :filename: tests_report.html
```

#### Example HTML test report


