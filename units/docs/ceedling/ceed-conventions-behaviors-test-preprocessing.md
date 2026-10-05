---
id: "ceed-conventions-behaviors-test-preprocessing"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Test preprocessing"
summary: "Ceedling and CMock are advanced tools that both perform fairly sophisticated parsing."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#test-preprocessing"
license: "MIT"
mode: "V"
---

### Background and overview

Ceedling and CMock are advanced tools that both perform fairly sophisticated
parsing.

However, neither of these tools fully understands the entire C language,
especially C's preprocessing statements.

If your test files rely on macros and `#ifdef` conditionals used in certain
ways (see examples below), there's a chance that Ceedling will break on trying
to process your test files, or, alternatively, your test suite will build but 
not execute as expected.

Similarly, generating mocks of header files with macros and `#ifdef`
conditionals around or in function signatures can get weird. Of course, it's 
often in sophisticated projects with complex header files that mocking is most 
desired in the first place.

Ceedling includes an optional ability to preprocess the following files before 
then extracting test cases and functions to be mocked with text parsing.

1. Your test files, or
1. Mockable header files, or
1. Both of the above 

See the [`:project` ↳ `:use_test_preprocessor`][project-settings] project 
configuration setting.

This Ceedling feature uses `gcc`'s preprocessing mode and the `cpp` preprocessor 
tool to strip down / expand test files and headers to their raw code content 
that can then be parsed as text by Ceedling and CMock. These tools must be in 
your search path if Ceedling's preprocessing is enabled.

**Ceedling's test preprocessing abilities are directly tied to the features and 
output of `gcc` and `cpp`. The default Ceedling tool definitions for these should 
not be redefined for other toolchains. It is highly unlikely to work for you. 
Future Ceedling improvements will allow for a plugin-style ability to use your 
own tools in this highly specialized capacity.**

[project-settings]: ../configuration/reference/project.md

### Limitations & gotchas

#### Preprocessing limitations cheatsheet

Ceedling's preprocessing abilities are generally quite useful — especially in 
projects with multiple build configurations for different feature sets or 
multiple targets, legacy code that cannot be refactored, and complex header 
files provided by vendors.

However, best applying Ceedling's preprocessing abilities requires understanding 
how the feature works, when to use it, and its limitations.

At a high level, Ceedling's preprocessing is applicable for cases where macros 
or conditional compilation preprocessing statements (e.g. `#ifdef`):

* Generate or hide/reveal your test files' `#include` statements.
* Generate or hide/reveal your test files' test case function signatures 
  (e.g. `void test_foo()`.
* Generate or hide/reveal mockable header files' `#include` statements.
* Generate or hide/reveal header files' mockable function signatures.

**_NOTE:_ You do not necessarily need to enable Ceedling's preprocessing only
because you have preprocessing statements in your test files or mockable header 
files. The feature is only truly needed if your project meets the conditions 
above.**

The sections that follow flesh out the details of the bulleted list above.

#### Preprocessing gotchas

##### `TEST_INCLUDE_PATH()` incompatibe with `#ifdef`

!!! note
    The build directive macro `TEST_INCLUDE_PATH()`, available as of Ceedling 
    1.0.0, is incompatible with enclosing conditional compilation C preprocessing 
    statements.

Wrapping `TEST_INCLUDE_PATH()` in conditional compilation statements 
(e.g. `#ifdef`) will not behave as you expect. This macro is used as a marker
for advanced abilities discovered by Ceedling parsing a test file as plain text.
Whether or not Ceedling preprocessing is enabled, Ceedling will always discover 
this marker macro in the plain text of a test file.

Why is `TEST_INCLUDE_PATH()` incompatible with `#ifdef`? Well, it's because of
a cyclical dependency that cannot be resolved. In order to perform test 
preprocessing, we need a full complement of `#include` search paths. These 
could be provided, in part, by `TEST_INCLUDE_PATH()`. But, if we allow 
`TEST_INCLUDE_PATH()` to be placed within conditional compilation C 
preprocessing statements, our search paths may be different after test 
preprocessing! The only solution is to disallow this and scan a test file as
plain text looking for this macro at the beginning of a test build.

**_Notes:_**

* `TEST_SOURCE_FILE()` _can_ be placed within conditional compilation
  C preprocessing statements.
* `TEST_INCLUDE_PATH()` & `TEST_SOURCE_FILE()` can be “hidden” from Ceedling's
  text scanning with traditional C comments.

### Test file preprocessing

When preprocessing is enabled for test files, Ceedling will expand preprocessor
statements in test files before extracting `#include` conventions and test case 
signatures. That is, preprocessing output is used to generate test runners 
and assemble the components of a test executable build.

!!! tip "Preprocessing Not Needed Inside Test Functions"
    Conditional directives _inside_ test case functions generally do not require
    Ceedling's test preprocessing ability. Assuming your code is correct, the C
    preprocessor within your toolchain will do the right thing for you in your
    test build. Read on for more details and the other cases of interest.

Test file preprocessing by Ceedling is applicable primarily when conditional
preprocessor directives generate the `#include` statements for your test file
and/or generate or enclose full test case functions. Ceedling will not be able 
to properly discover your `#include` statements or test case functions unless 
they are plainly available in an expanded, raw code version of your test file. 
Ceedling's preprocessing abilities provide that expansion.

#### Examples of when Ceedling preprocessing **_is_** needed for test files

Generally, Ceedling preprocessing is needed when:

1. `#include` statements are generated by macros
1. `#include` statements are conditionally present due to `#ifdef` statements
1. Test case function signatures are generated by macros
1. Test case function signatures are conditionaly present due to `#ifdef` statements

```c
// #include conventions are not recognized for anything except #include "..." statements
INCLUDE_STATEMENT_MAGIC("header_file")
```
```c
// Test file scanning will always see this #include statement
#ifdef BUILD_VARIANT_A
#include "mock_FooBar.h"
#endif
```
```c
// Test runner generation scanning will see the test case function signature and think this test case exists in every build variation
#ifdef MY_SUITE_BUILD
void test_some_test_case(void) {
   TEST_ASSERT_EQUALS(...);
}
#endif
```
```c
// Test runner generation will not recognize this as a test case when scanning the file
void TEST_CASE_MAGIC("foo_bar_case") {
   TEST_ASSERT_EQUALS(...);
}
```

#### Examples of when test preprocessing is **_not_** needed for test files

```c
// Code inside a test case is simply code that your toolchain will expand and build as you desire
// You can manage your compile time symbols with the :defines section of your project configuration file
void test_some_test_case(void) {
#ifdef BUILD_VARIANT_A
   TEST_ASSERT_EQUALS(...);
#endif

#ifdef BUILD_VARIANT_B
   TEST_ASSERT_EQUALS(...);
#endif
}
```

### Header file preprocessing

When preprocessing is enabled for mocking, Ceedling will expand preprocessor 
statements in header files before generating mocks from them. CMock requires
a clear look at function definitions and types in order to do its work.

Header files with preprocessor directives and conditional macros can easily
obscure details from CMock's limited C parser. Advanced C projects tend
to rely on preprocessing directives and macros to accomplish everything from
build variants to OS calls to register access to managing proprietary language
extensions.

Mocking is often most useful in complicated codebases. As such Ceedling's 
preprocessing abilities tend to be quite necessary to properly expand header
files so CMock can parse them.

#### Examples of when Ceedling preprocessing **_is_** needed for mockable headers

Generally, Ceedling preprocessing is needed when:

1. Function signatures are formed by macros
1. Function signatures are conditionaly present due to surrounding `#ifdef` 
   statements
1. Macros expand to become function decorators, return types, or parameters 

**_Important Notes:_**

* Sometimes CMock's parsing features can be configured to handle scenarios
  that fall within (3) above. CMock can match and remove most text strings,
  match and replace certain text strings, map custom types to mockable 
  alternatives, and be extended with a Unity helper to handle complex and 
  compound types. See [CMock]'s documentation for more.

* Test preprocessing causes any macros or symbols in a mockable header to 
  "disappear" in the generated mock. It's quite common to have needed symbols
  or macros in a header file that do not directly impact the function 
  signatures to be mocked. This can break compilation of your test suite.

  Possible solutions to this problem include:

    1. Move symbols and macros in your header file that do not impact function 
      signatures to another source header file that will not be filtered
      by Ceedling's header file preprocessing.
    1. If (1) is not possible, you may duplicate the needed symbols and macros
      in a header file that is only available in your test build search paths
      and include it in your test file.

```c
// Header file scanning will see this function signature but mistakenly mock the name of the macro
void FUNCTION_SIGNATURE_MAGIC(...);
```

```c
// Header file scanning will always see this function signature
#ifdef BUILD_VARIANT_A
unsigned int someFunction(void);
#endif
```

```c
// Header file scanning will either fail for this function signature or extract erroneous type names
INLINE_MAGIC RETURN_TYPE_MAGIC someFunction(PARAMETER_MAGIC);
```
