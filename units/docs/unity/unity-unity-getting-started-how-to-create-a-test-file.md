---
id: "unity-unity-getting-started-how-to-create-a-test-file"
type: "concept"
domain: "test"
title: "Unity - Getting Started: How to Create A Test File"
summary: "Test files are C files. Most often you will create a single test file for each C module that you want to test. The test file should include unity.h and the header for your C module to be tested."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityGettingStartedGuide.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityGettingStartedGuide.md#how-to-create-a-test-file"
license: "MIT"
mode: "V"
---

Test files are C files.
Most often you will create a single test file for each C module that you want to test.
The test file should include unity.h and the header for your C module to be tested.

Next, a test file will include a `setUp()` and `tearDown()` function.
The setUp function can contain anything you would like to run before each test.
The tearDown function can contain anything you would like to run after each test.
Both functions accept no arguments and return nothing.
You may leave either or both of these blank if you have no need for them.

If you're using Ceedling or the test runner generator script, you may leave these off completely.
Not sure?
Give it a try.
If your compiler complains that it can't find setUp or tearDown when it links, you'll know you need to at least include an empty function for these.

The majority of the file will be a series of test functions.
Test functions follow the convention of starting with the word "test_" or "spec_".
You don't HAVE to name them this way, but it makes it clear what functions are tests for other developers.
Also, the automated scripts that come with Unity or Ceedling will default to looking for test functions to be prefixed this way.
Test functions take no arguments and return nothing. All test accounting is handled internally in Unity.

Finally, at the bottom of your test file, you will write a `main()` function.
This function will call `UNITY_BEGIN()`, then `RUN_TEST` for each test, and finally `UNITY_END()`.
This is what will actually trigger each of those test functions to run, so it is important that each function gets its own `RUN_TEST` call.

Remembering to add each test to the main function can get to be tedious.
If you enjoy using helper scripts in your build process, you might consider making use of our handy [generate_test_runner.rb][] script.
This will create the main function and all the calls for you, assuming that you have followed the suggested naming conventions.
In this case, there is no need for you to include the main function in your test file at all.

When you're done, your test file will look something like this:

```C
#include "unity.h"
#include "file_to_test.h"

void setUp(void) {
    // set stuff up here
}

void tearDown(void) {
    // clean stuff up here
}

void test_function_should_doBlahAndBlah(void) {
    //test stuff
}

void test_function_should_doAlsoDoBlah(void) {
    //more test stuff
}

// not needed when using generate_test_runner.rb
int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_function_should_doBlahAndBlah);
    RUN_TEST(test_function_should_doAlsoDoBlah);
    return UNITY_END();
}
```

It's possible that you will need more customization than this, eventually.
For that sort of thing, you're going to want to look at the configuration guide.
This should be enough to get you going, though.

### Running Test Functions

When writing your own `main()` functions, for a test-runner.
There are two ways to execute the test.

The classic variant

``` c
RUN_TEST(func, linenum)
```

Or its simpler replacement that starts at the beginning of the function.

``` c
RUN_TEST(func)
```

These macros perform the necessary setup before the test is called and handles clean-up and result tabulation afterwards.

### Ignoring Test Functions

There are times when a test is incomplete or not valid for some reason.
At these times, TEST_IGNORE can be called.
Control will immediately be returned to the caller of the test, and no failures will be returned.
This is useful when your test runners are automatically generated.

``` c
TEST_IGNORE()
```

Ignore this test and return immediately

```c
TEST_IGNORE_MESSAGE (message)
```

Ignore this test and return immediately.
Output a message stating why the test was ignored.

### Aborting Tests

There are times when a test will contain an infinite loop on error conditions, or there may be reason to escape from the test early without executing the rest of the test.
A pair of macros support this functionality in Unity.
The first `TEST_PROTECT` sets up the feature, and handles emergency abort cases.
`TEST_ABORT` can then be used at any time within the tests to return to the last `TEST_PROTECT` call.

```c
    TEST_PROTECT()
```

Setup and Catch macro

```c
    TEST_ABORT()
```

Abort Test macro

Example:

```c
    main()
    {
        if (TEST_PROTECT())
        {
            MyTest();
        }
    }
```

If MyTest calls `TEST_ABORT`, program control will immediately return to `TEST_PROTECT` with a return value of zero.
