---
id: "cmock-cmock-argumentvalidation"
type: "concept"
domain: "test"
title: "CMock ArgumentValidation"
summary: "CMock: Argument Validation =========================="
status: "draft"
collection: "cmock"
source: "ThrowTheSwitch/CMock@f2a70b4:docs/CMock_ArgumentValidation.md"
doc_source: "https://github.com/ThrowTheSwitch/CMock/blob/f2a70b4/docs/CMock_ArgumentValidation.md"
license: "MIT"
mode: "V"
---

CMock: Argument Validation
==========================

Much of the power of CMock comes from its ability to automatically
validate that the arguments passed to mocked functions are the
values that were expected to be passed. CMock puts a lot of effort
into guessing how the user would most like to see those values
compared, and then represented when failures are encountered.

Like Unity, CMock follows a philosophy of making its best guesses,
and then allowing the user to explicitly specify any features that
they would like to change or customize.

Quick Reference: Which Option Should I Use?
-------------------------------------------

| Situation | Recommended Option |
|-----------|-------------------|
| Built-in C types (`int`, `uint8_t`, `float`, …) | Nothing — Option 1 handles these automatically |
| Simple typedef or `#define` alias of a known type | Option 2: add a `:treat_as` entry |
| Small `enum` type | Option 2: map to `INT8`, `INT16`, or `INT` |
| Opaque handle / function pointer where only identity matters | Option 2: map to `PTR` |
| `typedef`'d fixed-size array | Option 2: `:treat_as_array` |
| Legacy `typedef void MY_VOID` | Option 2: `:treat_as_void` |
| `struct` or `union` needing field-level comparison | Option 3: custom assertion + `:unity_helper_path` |
| Pointer to a `struct` with a custom assertion | Option 2 + 3: custom assertion, then `:treat_as` the pointer |
| Type that changes meaning per test, or one-off complex logic | Option 4: Callback |
| Last resort — type is unknown and rough equality is enough | Option 1b: memcmp fallback (automatic) |

Option 1: Common Types
----------------------

First, if you're dealing with C's standard types, there is nothing
further you need to do. CMock will choose an appropriate assertion
from Unity's list of assertions and will perform the comparison and
display using that. For example, if you specify a `short`, then it's 
very likely CMock will compare using `TEST_ASSERT_EQUAL_INT16`. For
unsigned values, it assumes you'd like them displayed in hex. Are you
interested in comparing a `const char*`? That would be Unity's 
string comparison. 

What if you have some other type of pointer? If you've instructed
CMock to compare pointers, it'll use `TEST_ASSERT_EQUAL_PTR`. 
Otherwise it'll use dereference the value being pointed at and 
compare that for you. (Read more about the Array plugin for more
details on how this all works). The TYPE being pointed to follows the
same rules as the those above... so if they're common types, for example 
`unsigned char*`, then CMock will choose to compare using the 
logical assertion (in this case `TEST_ASSERT_EQUAL_HEX8`).

A quick note about floating point types: we're calling the assertions
`TEST_ASSERT_EQUAL_FLOAT` (for example), but don't worry... these 
assertions are actually checking to make sure that the values are
"incredibly close" to the desired value instead of identical. This
is because many numbers can be represented in multiple ways when
using floating point. These differences are out of the control of 
the user, for the most part. You can ready more about this in the
Unity documentation if you're interested in the details.

Option 1b: The Fallback Plan
----------------------------

So what happens when CMock doesn't recognize the type being used?
This will happen for any custom types being used. What constitutes
a custom type?

  - You've used `#define` to create an alias for a standard type
  - You've used `typedef` to create an alias for a standard type
  - You've created an `enum` type
  - You've created a `union` type
  - You've created a `struct` type
  - You're working with a function pointer

 When CMock doesn't recognize the type as a standard type, (and 
 assuming you don't have a better option specified, as any of the
 options below), it will fall back to performing a memory 
 comparison using `TEST_ASSERT_EQUAL_MEMORY`. For the most part,
 this is effective, but the reported failures are not terribly
 descriptive.

 **WARNING:** There is one important instance where this fallback method
 doesn't work at all. If the custom type is a `struct` and that 
 struct isn't packed, then it's possible you can get false failures
 when the unused bytes between fields differ. For an unpacked struct,
 it's important that you either use option 3 or 4 below, or ignore that
 particular argument (and possibly test it manually yourself).

Option 2: Treat-As
------------------

CMock maintains a list of non-standard types which are basically
aliases of standard types. For example, a common shorthand for
a single-byte unsigned integer might be `u8` or `U8` or `UINT8`.
Any of these can simply be mapped to the standard
`TEST_ASSERT_EQUAL_HEX8`.
