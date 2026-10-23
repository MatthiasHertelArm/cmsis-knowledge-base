---
id: "cmock-cmock-argumentvalidation-wrapping-our-assertion-in-macros"
type: "concept"
domain: "test"
title: "CMock ArgumentValidation: Wrapping our Assertion in Macros"
summary: "Once you have a function which does the main work, we need to create macros around it so that the assertion can be used conveniently both by CMock and directly in test code."
status: "draft"
collection: "cmock"
source: "ThrowTheSwitch/CMock@34c26e5:docs/CMock_ArgumentValidation.md"
doc_source: "https://github.com/ThrowTheSwitch/CMock/blob/34c26e5/docs/CMock_ArgumentValidation.md#wrapping-our-assertion-in-macros"
license: "MIT"
mode: "V"
---

Once you have a function which does the main work, we need to create
macros around it so that the assertion can be used conveniently both
by CMock and directly in test code.

The macro that CMock **requires** is the `UNITY_TEST_ASSERT_EQUAL_` form.
It starts with exactly that prefix, followed by the type name exactly as
declared, and takes four arguments:

```c
#define UNITY_TEST_ASSERT_EQUAL_MyType(e,a,l,m)  AssertEqualMyType(e,a,l,m)
```

  - `e` - expected value
  - `a` - actual value
  - `l` - line number to report (filled in automatically by CMock)
  - `m` - message to append at the end

CMock scans the helper header for macros matching this pattern and
automatically uses them when it encounters the corresponding type.

It is also useful (though optional) to add the simpler `TEST_ASSERT_EQUAL_`
form so the assertion is easy to call directly inside your own test
functions:

```c
#define TEST_ASSERT_EQUAL_MyType(e,a) \
    UNITY_TEST_ASSERT_EQUAL_MyType(e,a,__LINE__,NULL)

#define TEST_ASSERT_EQUAL_MyType_MESSAGE(e,a,m) \
    UNITY_TEST_ASSERT_EQUAL_MyType(e,a,__LINE__,m)
```

With these in place, you can write `TEST_ASSERT_EQUAL_MyType(expected, actual)`
in your tests just like any built-in Unity assertion.
