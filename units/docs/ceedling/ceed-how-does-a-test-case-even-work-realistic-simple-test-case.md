---
id: "ceed-how-does-a-test-case-even-work-realistic-simple-test-case"
type: "concept"
domain: "test"
title: "How Does a Test Case Even Work?: Realistic simple test case"
summary: "In reality, we're probably not testing the static value of an integer against itself. Instead, we're calling functions in our source code and making assertions against return values."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/test-cases.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/test-cases/#realistic-simple-test-case"
license: "MIT"
mode: "V"
---

In reality, we're probably not testing the static value of an integer 
against itself. Instead, we're calling functions in our source code
and making assertions against return values.

```c
#include "unity.h"
#include "my_math.h"

void test_some_sums(void) {
   TEST_ASSERT_EQUALS(   5, mySum(  2,   3) );
   TEST_ASSERT_EQUALS(   6, mySum(  0,   6) );
   TEST_ASSERT_EQUALS( -12, mySum( 20, -32) );
}
```

If an assertion fails, the test case fails. As soon as an assertion
fails, execution within that test case stops.

Multiple test cases can live in the same test file. When all the
test cases are run, their results are tallied into simple pass
and fail metrics with a bit of metadata for failing test cases such 
as line numbers and names of test cases.

Ceedling and Unity work together to both automatically run your test
cases and tally up all the results.
