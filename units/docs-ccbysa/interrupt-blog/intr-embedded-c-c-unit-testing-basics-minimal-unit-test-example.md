---
id: "intr-embedded-c-c-unit-testing-basics-minimal-unit-test-example"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Minimal Unit Test Example"
summary: "Let's come up with a bare bones unit test to instrument our simple my_sum module."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#minimal-unit-test-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's come up with a bare bones unit test to instrument our simple `my_sum`
module.

> NOTE: Our examples use the CppUTest framework. If you want to follow along,
> check out the [Setting Up CppUTest](#setting-up-cpputest) section first.

The source code for the `my_sum.c` module is as follows:

```c
#include "my_sum.h"

int my_sum(int a, int b) {
  return (a + b);
}
```

A unit test generally contains the following pieces:

- Setup and Teardown functions, which run before and after each test
  respectively.
- Individual tests that test logical components or paths of a module.
- Many _checks_, such as `LONGS_EQUAL` which compares integer values and
  `STRCMP_EQUAL` which would compare string values.

Our basic unit test is as follows:

```c++
#include "CppUTest/TestHarness.h"

extern "C" {
  #include "my_sum.h"
}

TEST_GROUP(TestMySum) {
  void setup() {
    // This gets run before every test
  }

  void teardown() {
    // This gets run after every test
  }
};

TEST(TestMySum, Test_MySumBasic) {
  LONGS_EQUAL(7, my_sum(3, 4));
}
```

Although the example is basic, let's go over what is happening here.

- We import `my_sum.h` inside of the `extern "C" {}` section so that it is
  compiled as C instead of C++.
- We have empty `setup()` and `teardown()` functions since the modules we are
  testing don't require any initial setup or cleanup routines.
- We have a single `LONGS_EQUAL` state, which compares `<expected> == <actual>`
  after the `my_sum` function is called.
- We did not include any fakes or stubs, as our module didn't have any
  dependencies.

If this test passes, we get something like:

```
Running build/sum/sum_tests
.
OK (1 tests, 1 ran, 1 checks, 0 ignored, 0 filtered out, 0 ms)
```

And if the test fails (for example, change 7 to 6):

```
Running build/sum/sum_tests

src/test_my_sum.cpp:17: error: Failure in TEST(TestMySum, Test_MySumBasic)
  expected <6 0x6>
  but was  <7 0x7>

.
Errors (1 failures, 1 tests, 1 ran, 1 checks, 0 ignored, 0 filtered out, 1 ms)
```

To build and run this unit test, we give the unit test harness the test name,
the list of files to compile into the test binary, and any extra compilation
flags necessary.

```
COMPONENT_NAME=sum

SRC_FILES = \
  $(PROJECT_SRC_DIR)/my_sum.c \

TEST_SRC_FILES = \
  $(UNITTEST_SRC_DIR)/test_my_sum.c
```

Here, we have `SRC_FILES`, which would contain any sources files used by the
test, and `TEST_SRC_FILES` which contains the test files that contain the tests
themselves.
