---
id: "intr-building-an-on-device-embedded-tes-google-test-integration"
type: "concept"
domain: "debug"
title: "Building an On-Device Embedded Testing Library: Google Test Integration"
summary: "One small win that appeared was that, given the flexibility, it was easy to integrate Google Test and controller. The controller can register each test from the reactor as a test in the google test library."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2022-06-07-testing-library.md"
doc_source: "https://interrupt.memfault.com/blog/testing-library#google-test-integration"
license: "CC-BY-SA-4.0"
mode: "V"
---

One small win that appeared was that, given the flexibility, it was easy to integrate Google Test and controller.
The controller can register each test from the reactor as a test in the google test library.
It can use the Google Test facility on GPOS to provide user-readable output about the execution of the tests, more orchestration logic, and output of the testing in the form of JUnit XML files.
Systems like GitLab can use this.

This shows that it was easy to provide the necessary facility for the testing firmware to be integrated into modern CI with traditional tools.
And yet the integration is not tight. Any integration into Google Test is just a set of a few functions/classes in emlabcpp that can be ignored by anybody not favoring Google Test.

The test output from the project I used this framework the first time can look like this:

```
    ./cmake-build-debug/util/tester --device /dev/ttyACM0
   [==========] Running 1 test from 1 test suite.
   [----------] Global test environment set-up.
   [----------] 1 test from emlabcpp::testing
   [ RUN      ] emlabcpp::testing.basic_control_test
   /home/veverak/Projects/servio/util/src/tester.cpp:32: Failure
   Test produced a failure, stopping
   collected:
    11576 :	0
    11679 :	0
    11782 :	0
    11885 :	0
    11988 :	0
    12091 :	0
    12194 :	0
    12297 :	0
    12400 :	0
    12503 :	0
    12606 :	0
    12709 :	0
    12812 :	0
    12915 :	0
    13018 :	0
    13121 :	0
    13224 :	0
    13327 :	0
    13430 :	0
    13533 :	0
    13636 :	0
    13739 :	0
    13842 :	0
    13945 :	0
    14048 :	0
   [  FAILED  ] emlabcpp::testing.basic_control_test (2597 ms)
   [----------] 1 test from emlabcpp::testing (2597 ms total)

   [----------] Global test environment tear-down
   [==========] 1 test from 1 test suite ran. (2597 ms total)
   [  PASSED  ] 0 tests.
   [  FAILED  ] 1 test, listed below:
   [  FAILED  ] emlabcpp::testing.basic_control_test

    1 FAILED TEST
```

In this example, the controller registered all tests in the firmware (on the device that was connected to the PC and was accessible via the `/dev/ttyACM0` serial device). After that, it executed all of them.

The name of the testing suite `emlabcpp::testing` and the name of the test `basic_control_test` were all extracted on the fly from the testing firmware itself. We can also see values collected by the test during the execution.
