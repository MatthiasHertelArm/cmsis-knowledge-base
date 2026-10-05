---
id: "cmock-cmock-argumentvalidation-creating-a-custom-assertion"
type: "concept"
domain: "test"
title: "CMock ArgumentValidation: Creating a Custom Assertion"
summary: "A custom assertion is a function which accepts a standard set of inputs, and then uses Unity's assertion macros to verify any details required for the types involved."
status: "draft"
collection: "cmock"
source: "ThrowTheSwitch/CMock@f2a70b4:docs/CMock_ArgumentValidation.md"
doc_source: "https://github.com/ThrowTheSwitch/CMock/blob/f2a70b4/docs/CMock_ArgumentValidation.md#creating-a-custom-assertion"
license: "MIT"
mode: "V"
---

A custom assertion is a function which accepts a standard set of 
inputs, and then uses Unity's assertion macros to verify any details
required for the types involved. 

The inputs:

  - the `expected` value (as a `const` version of type being verified)
  - the `actual` value (also as a `const` version of the desired type)
  - the `line` this function was called from (as type `UNITY_LINE_TYPE`)
  - an optional `message` to be appended (as type `const char*`)

Inside the function, we use the *internal* versions of Unity's assertions
to validate any details that need validating.

Let's look at an example! Let's say we have the following type:

```
typedef struct MyType_t
{
    int a;
    const char* b;
} MyType;
```

In our application, the length of `b` is supposed to be specified by `a`,
and `b` is therefore allowed to have any value (including `0x00`). 

Our custom assertion might look something like this:

```
void AssertEqualMyType(const MyType expected, const MyType actual, UNITY_LINE_TYPE line, const char* message)
{
    //It's common to override the default message with our own 
    (void)message; 

    // Verify the lengths are the same, or they're clearly not matched
    UNITY_TEST_ASSERT_EQUAL_INT(expected.a, actual.a, line, "Data length mismatch");

    // Verify we're dealing with actual pointers
    UNITY_TEST_ASSERT_NOT_NULL(expected.b, line, "Expected value should not be NULL");
    UNITY_TEST_ASSERT_NOT_NULL(actual.b, line, "Actual value should not be NULL");

    // Verify the string contents
    UNITY_TEST_ASSERT_EQUAL_MEMORY(expected.b, actual.b, expected.a, line, "Data not equal");
}
```

There are a few things to note about this. First, notice we're using the 
`UNITY_TEST_ASSERT_` assertions? That's because these allow us to pass 
on the specific line number. Second, notice we override the message with our
own more helpful messages? You don't need to do this, but anything you can do
to help a developer find a bug is a good thing.

What if there isn't an assertion that is right for your needs? You can 
always do whatever operations are necessary yourself, and use `UNITY_TEST_FAIL()`
directly.

One final note: It's best to only test the things that are hard rules about
how a type is supposed to work in your system. Anything else should be left to
the test code.

For example, let's say that in our example above, there are situations where
it IS valid for the pointers to be `NULL`. Perhaps the pointers are ignored
completely when the `a` field is `0`. In that case, we could drop those 
assertions completely, or add logic to only check when necessary.

Similarly, should our assertion check that the length is positive? In this
case, it's dangerous if it's negative, because the memory check wouldn't like it.

Updating for these concerns:


```
void AssertEqualMyType(const MyType expected, const MyType actual, UNITY_LINE_TYPE line, const char* message)
{
    //It's common to override the default message with our own 
    (void)message; 

    // Verify the lengths are the same, or they're clearly not matched
    UNITY_TEST_ASSERT_EQUAL_INT(expected.a, actual.a, line, "Data length mismatch");

    // Verify the lengths are non-negative
    UNITY_TEST_ASSERT_GREATER_OR_EQUAL_INT(0, expected.a, line, "Data length must be positive");

    if (expected.a > 0)
    {
        // Verify we're dealing with actual pointers
        UNITY_TEST_ASSERT_NOT_NULL(expected.b, line, "Expected value should not be NULL");
        UNITY_TEST_ASSERT_NOT_NULL(actual.b, line, "Actual value should not be NULL");

        // Verify the string contents
        UNITY_TEST_ASSERT_EQUAL_MEMORY(expected.b, actual.b, expected.a, line, "Data not equal");
    }
}
```
