---
id: "ceed-conventions-behaviors-header-file-preprocessing"
type: "concept"
domain: "test"
title: "Conventions & Behaviors: Test preprocessing / Header file preprocessing"
summary: "When preprocessing is enabled for mocking, Ceedling will expand preprocessor statements in header files before generating mocks from them. CMock requires a clear look at function definitions and types in order to do its work."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/testing-guide/conventions.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/conventions/#header-file-preprocessing"
license: "MIT"
mode: "V"
---

_Part of: Test preprocessing_

When preprocessing is enabled for mocking, Ceedling will expand preprocessor 
statements in header files before generating mocks from them. CMock requires
a clear look at function definitions and types in order to do its work.

Header files with preprocessor directives and conditional macros can easily
obscure details from CMock’s limited C parser. Advanced C projects tend
to rely on preprocessing directives and macros to accomplish everything from
build variants to OS calls to register access to managing proprietary language
extensions.

Mocking is often most useful in complicated codebases. As such Ceedling’s 
preprocessing abilities tend to be quite necessary to properly expand header
files so CMock can parse them.

#### Examples of when Ceedling preprocessing **_is_** needed for mockable headers

Generally, Ceedling preprocessing is needed when:

1. Function signatures are formed by macros
1. Function signatures are conditionaly present due to surrounding `#ifdef` 
   statements
1. Macros expand to become function decorators, return types, or parameters 

**_Important Notes:_**

* Sometimes CMock’s parsing features can be configured to handle scenarios
  that fall within (3) above. CMock can match and remove most text strings,
  match and replace certain text strings, map custom types to mockable 
  alternatives, and be extended with a Unity helper to handle complex and 
  compound types. See [CMock]’s documentation for more.

* Test preprocessing causes any macros or symbols in a mockable header to 
  "disappear" in the generated mock. It’s quite common to have needed symbols
  or macros in a header file that do not directly impact the function 
  signatures to be mocked. This can break compilation of your test suite.

  Possible solutions to this problem include:

    1. Move symbols and macros in your header file that do not impact function 
      signatures to another source header file that will not be filtered
      by Ceedling’s header file preprocessing.
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
