---
id: "unity-unity-helper-scripts-unity-test-summary-rb"
type: "concept"
domain: "test"
title: "Unity Helper Scripts: With a Little Help From Our Friends / `unity_test_summary.rb`"
summary: "Part of: With a Little Help From Our Friends"
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityHelperScriptsGuide.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityHelperScriptsGuide.md#unity-test-summary-rb"
license: "MIT"
mode: "V"
---

_Part of: With a Little Help From Our Friends_

A Unity test file contains one or more test case functions.
Each test case can pass, fail, or be ignored.
Each test file is run individually producing results for its collection of test cases.
A given project will almost certainly be composed of multiple test files.
Therefore, the suite of tests is comprised of one or more test cases spread across one or more test files.
This script aggregates individual test file results to generate a summary of all executed test cases.
The output includes how many tests were run, how many were ignored, and how many failed. In addition, the output includes a listing of which specific tests were ignored and failed.
A good example of the breadth and details of these results can be found in the `examples` directory.
Intentionally ignored and failing tests in this project generate corresponding entries in the summary report.

If you're interested in other (prettier?) output formats, check into the [Ceedling][] build tool project that works with Unity and CMock and supports xunit-style xml as well as other goodies.

This script assumes the existence of files ending with the extensions `.testpass` and `.testfail`.
The contents of these files includes the test results summary corresponding to each test file executed with the extension set according to the presence or absence of failures for that test file.
The script searches a specified path for these files, opens each one it finds, parses the results, and aggregates and prints a summary.
Calling it from the command line looks like this:

```Shell
ruby unity_test_summary.rb build/test/
```

You can optionally specify a root path as well.
This is really helpful when you are using relative paths in your tools' setup, but you want to pull the summary into an IDE like Eclipse for clickable shortcuts.

```Shell
ruby unity_test_summary.rb build/test/ ~/projects/myproject/
```

Or, if you're more of a Windows sort of person:

```Shell
ruby unity_test_summary.rb build\test\ C:\projects\myproject\
```

When configured correctly, you'll see a final summary, like so:

```Shell
--------------------------
UNITY IGNORED TEST SUMMARY
--------------------------
blah.c:22:test_sandwiches_should_HaveBreadOnTwoSides:IGNORE

-------------------------
UNITY FAILED TEST SUMMARY
-------------------------
blah.c:87:test_sandwiches_should_HaveCondiments:FAIL:Expected 1 was 0
meh.c:38:test_soda_should_BeCalledPop:FAIL:Expected "pop" was "coke"

--------------------------
OVERALL UNITY TEST SUMMARY
--------------------------
45 TOTAL TESTS 2 TOTAL FAILURES 1 IGNORED
```

How convenient is that?

*Find The Latest of This And More at [ThrowTheSwitch.org][]*

[ruby-lang.org]: https://ruby-lang.org/
[YAML]: http://www.yaml.org/
[Ceedling]: http://www.throwtheswitch.org/ceedling
[ThrowTheSwitch.org]: https://throwtheswitch.org
