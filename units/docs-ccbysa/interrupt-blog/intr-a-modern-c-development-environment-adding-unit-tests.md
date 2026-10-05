---
id: "intr-a-modern-c-development-environment-adding-unit-tests"
type: "concept"
domain: "debug"
title: "A Modern C Development Environment: Adding unit tests"
summary: "We're already able to build our library, analyze it and have a formatter in place. One more thing that we need in our development environment is a unit test framework."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-08-09-a-modern-c-dev-env.md"
doc_source: "https://interrupt.memfault.com/blog/a-modern-c-dev-env#adding-unit-tests"
license: "CC-BY-SA-4.0"
mode: "V"
---

We're already able to build our library, analyze it and have a formatter in place. One more thing that we need in our development environment is a unit test framework.

For this article, I've chosen the [Unity](https://www.throwtheswitch.org/unity) test framework, executed on the host via [Ceedling](https://www.throwtheswitch.org/ceedling). I'm using this framework since it is quite easy to extend the integration to also execute tests on an actual target hardware in case you're developing an embedded system.

### Installing `Unity` and `Ceedling` in the builder image

In the first step of our builder image we already installed `ruby`, so installing our unit test tools is very straightforward:

```dockerfile
# install unity cmock and ceedling (unit test environment)
RUN gem install ceedling
# set standard encoding to UTF-8 for ruby (and thus ceedling)
ENV RUBYOPT "-KU -E utf-8:utf-8"
```

After rebuilding our image we're good to go!

```bash
make builder-build
```

### Configuring `Unity` and running unit tests

Lots of resources exist on how to set up `Unity` and `Ceedling`, including an [excellent article on Embedded Artistry](https://embeddedartistry.com/blog/2019/2/25/unit-testing-and-reporting-on-a-build-server-using-ceedling-and-unity/) or the [*ThrowTheSwitch's* own articles](https://www.throwtheswitch.org/articles). In short, you set the configuration switches for `Unity` in a dedicated [`unity_config.h`](https://github.com/lmapii/cproject/blob/main/tests/unittest/support/unity_config.h) file, and configure `Ceedling` with the [`project.yml`](https://github.com/lmapii/cproject/blob/main/tests/unittest/project.yml). `Ceedling` is a neat little helper that generates all the test runners for you, so all you need to do is add your test files and tell `Ceedling` how to detect them. Have a look at the files in the [example project on GitHub](https://github.com/lmapii/cproject) in case you need details!

In the [`project.yml`](https://github.com/lmapii/cproject/blob/main/tests/unittest/project.yml) we told `Ceedling` that our tests will be located in the `tests/unittest/test` directory and all test file names have the prefix `test`. So all we need to do is to add our [`test_dummy.c`](https://github.com/lmapii/cproject/blob/main/tests/unittest/test/test_dummy.c) file to test our implementation, leading to the following files added:

```bash
$ tree --charset=utf-8 --dirsfirst -- tests
tests
└── unittest
    ├── support
    │   └── unity_config.h
    ├── test
    │   └── test_dummy.c
    └── project.yml
```

We can then create our first unit test `tests/unittest/test/test_dummy.c`:

```c
#include "dummy/dummy.h"
#include "unity.h"

void setUp(void) {}
void tearDown(void) {}

void test_dummy(void)
{
    TEST_ASSERT_EQUAL(4U, dummy_random());
}
```

If you're in your `vscode` development container, you can run the following straight from the integrated terminal. Otherwise, spin up the container using `make builder-run` to execute your tests:

```bash
$ ceedling test:all

Test 'test_dummy.c'
-------------------
Generating runner for test_dummy.c...
Compiling test_dummy_runner.c...
Compiling test_dummy.c...
Compiling unity.c...
Compiling dummy.c...
Compiling cmock.c...
Linking test_dummy.out...
Running test_dummy.out...

--------------------
OVERALL TEST SUMMARY
--------------------
TESTED:  1
PASSED:  1
FAILED:  0
IGNORED: 0
```

### Bonus: Coverage reports

The previously mentioned [article on Embedded Artistry](https://embeddedartistry.com/blog/2019/2/25/unit-testing-and-reporting-on-a-build-server-using-ceedling-and-unity/) also shows how to configure coverage reports. This is already set up in the [`project.yml` of the GitHub example project](https://github.com/lmapii/cproject/blob/main/tests/unittest/project.yml), and since we included `gcovr` in the `apt` packages of our image, we are good to run our unit tests with coverage:

```bash
$ ceedling gcov:all

Test 'test_dummy.c'
-------------------
Compiling test_dummy_runner.c...
Compiling test_dummy.c...
Compiling dummy.c with coverage...
Compiling unity.c...
Compiling cmock.c...
Linking test_dummy.out...
Running test_dummy.out...

--------------------------
GCOV: OVERALL TEST SUMMARY
--------------------------
TESTED:  1
PASSED:  1
FAILED:  0
IGNORED: 0

---------------------------
GCOV: CODE COVERAGE SUMMARY
---------------------------
dummy.c Lines executed:100.00% of 2
dummy.c No branches
dummy.c No calls
```

The [`project.yml`](https://github.com/lmapii/cproject/blob/main/tests/unittest/project.yml) also sets up a utility for generating coverage reports. In this demo project we can generate a `gcovr` HTML report with the following command:

```bash
$ ceedling utils:gcov
Creating gcov results report(s) in 'build/artifacts/gcov'... Done in 1.359 seconds.
```

You'll now find the HTML report in `tests/unittest/build/artifacts/gcov/GcovCoverageResults.html`.


