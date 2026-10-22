---
id: "unity-unity-configuration-guide-getting-into-the-guts"
type: "concept"
domain: "test"
title: "Unity Configuration Guide: Getting Into The Guts"
summary: "There will be cases where the options above aren't quite going to get everything perfect. They are likely sufficient for any situation where you are compiling and executing your tests with a native toolchain (e.g. clang on Mac)."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@7f1a686:docs/UnityConfigurationGuide.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/7f1a686/docs/UnityConfigurationGuide.md#getting-into-the-guts"
license: "MIT"
mode: "V"
---

There will be cases where the options above aren't quite going to get everything perfect.
They are likely sufficient for any situation where you are compiling and executing your tests with a native toolchain (e.g. clang on Mac).
These options may even get you through the majority of cases encountered in working with a target simulator run from your local command line.
But especially if you must run your test suite on your target hardware, your Unity configuration will
require special help.
This special help will usually reside in one of two places: the `main()` function or the `RUN_TEST` macro.
Let's look at how these work.

### `main()`

Each test module is compiled and run on its own, separate from the other test files in your project.
Each test file, therefore, has a `main` function.
This `main` function will need to contain whatever code is necessary to initialize your system to a workable state.
This is particularly true for situations where you must set up a memory map or initialize a communication channel for the output of your test results.

A simple main function looks something like this:

```C
int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_TheFirst);
    RUN_TEST(test_TheSecond);
    RUN_TEST(test_TheThird);
    return UNITY_END();
}
```

You can see that our main function doesn't bother taking any arguments.
For our most barebones case, we'll never have arguments because we just run all the tests each time.
Instead, we start by calling `UNITY_BEGIN`.
We run each test (in whatever order we wish).
Finally, we call `UNITY_END`, returning its return value (which is the total number of failures).

It should be easy to see that you can add code before any test cases are run or after all the test cases have completed.
This allows you to do any needed system-wide setup or teardown that might be required for your special circumstances.

#### `RUN_TEST`

The `RUN_TEST` macro is called with each test case function.
Its job is to perform whatever setup and teardown is necessary for executing a single test case function.
This includes catching failures, calling the test module's `setUp()` and `tearDown()` functions, and calling `UnityConcludeTest()`.
If using CMock or test coverage, there will be additional stubs in use here.
A simple minimalist RUN_TEST macro looks something like this:

```C
#define RUN_TEST(testfunc) \
    UNITY_NEW_TEST(#testfunc) \
    if (TEST_PROTECT()) { \
        setUp(); \
        testfunc(); \
    } \
    if (TEST_PROTECT() && (!TEST_IS_IGNORED)) \
        tearDown(); \
    UnityConcludeTest();
```

So that's quite a macro, huh?
It gives you a glimpse of what kind of stuff Unity has to deal with for every single test case.
For each test case, we declare that it is a new test.
Then we run `setUp` and our test function.
These are run within a `TEST_PROTECT` block, the function of which is to handle failures that occur during the test.
Then, assuming our test is still running and hasn't been ignored, we run `tearDown`.
No matter what, our last step is to conclude this test before moving on to the next.

Let's say you need to add a call to `fsync` to force all of your output data to flush to a file after each test.
You could easily insert this after your `UnityConcludeTest` call.
Maybe you want to write an xml tag before and after each result set.
Again, you could do this by adding lines to this macro.
Updates to this macro are for the occasions when you need an action before or after every single test case throughout your entire suite of tests.
