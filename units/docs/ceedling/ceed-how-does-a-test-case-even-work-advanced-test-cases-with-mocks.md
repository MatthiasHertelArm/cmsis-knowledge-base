---
id: "ceed-how-does-a-test-case-even-work-advanced-test-cases-with-mocks"
type: "concept"
domain: "test"
title: "How Does a Test Case Even Work?: Advanced test cases with mocks"
summary: "Often you want to test not just what a function returns but how it interacts with other functions."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@cee146d:docs/mkdocs/testing-guide/test-cases.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/test-cases/#advanced-test-cases-with-mocks"
license: "MIT"
mode: "V"
---

Often you want to test not just what a function returns but how
it interacts with other functions.

The simple test cases above work well at the "edges" of a 
codebase (libraries, state management, some kinds of I/O, etc.). 
But, in the messy middle of your code, code calls other code. 
One way to handle testing this is with [mock functions][mocks] and
[interaction-based testing][interaction-based-tests].

Mock functions are functions with the same interface as the real 
code the mocks replace. A mocked function allows you to control 
how it behaves and wrap up assertions within a higher level idea 
of expectations.

What is meant by an expectation? Well… We _expect_ a certain 
function is called with certain arguments and that it will return
certain values. With the appropriate code inside a mocked function 
all of this can be managed and checked.

You can write your own mocks, of course. But, it's generally better 
to rely on something else to do it for you. Ceedling uses the [CMock] 
framework to perform mocking for you.

Here's some sample code you might want to test:

```c
#include "other_code.h"

void doTheThingYo(mode_t input) {
   mode_t result = processMode(input);
   if (result == MODE_3) {
      setOutput(OUTPUT_F);
   }
   else {
      setOutput(OUTPUT_D);
   } 
}
```

And, here's what test cases using mocks for that code could look 
like:

```c
#include "mock_other_code.h"

void test_doTheThingYo_should_enableOutputF(void) {
   // Mocks
   processMode_ExpectAndReturn(MODE_1, MODE_3);
   setOutput_Expect(OUTPUT_F);

   // Function under test
   doTheThingYo(MODE_1);
}

void test_doTheThingYo_should_enableOutputD(void) {
   // Mocks
   processMode_ExpectAndReturn(MODE_2, MODE_4);
   setOutput_Expect(OUTPUT_D);

   // Function under test
   doTheThingYo(MODE_2);
}
```

Remember, the generated mock code you can't see here has a whole bunch 
of smarts and Unity assertions inside it. CMock scans header files and
then generates mocks (C code) from the function signatures it finds in
those header files. It's kinda magical.
