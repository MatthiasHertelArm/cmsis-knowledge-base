---
id: "unity-unity-configuration-guide-miscellaneous"
type: "concept"
domain: "test"
title: "Unity Configuration Guide: The Options / Miscellaneous"
summary: "Unity uses the NULL macro, which defines the value of a null pointer constant, defined in stddef.h by default."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityConfigurationGuide.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityConfigurationGuide.md#miscellaneous"
license: "MIT"
mode: "V"
---

_Part of: The Options_

#### `UNITY_EXCLUDE_STDDEF_H`

Unity uses the `NULL` macro, which defines the value of a null pointer constant, defined in `stddef.h` by default.
If you want to provide your own macro for this, you should exclude the `stddef.h` header file by adding this define to your configuration.

_Example:_

```C
#define UNITY_EXCLUDE_STDDEF_H
```

#### `UNITY_INCLUDE_PRINT_FORMATTED`

Unity provides a simple (and very basic) printf-like string output implementation, which is able to print a string modified by the following format string modifiers:

- __%d__ - signed value (decimal)
- __%i__ - same as __%d__
- __%u__ - unsigned value (decimal)
- __%f__ - float/Double (if float support is activated)
- __%g__ - same as __%f__
- __%b__ - binary prefixed with "0b"
- __%x__ - hexadecimal (upper case) prefixed with "0x"
- __%X__ - same as __%x__
- __%p__ - pointer (same as __%x__ or __%X__)
- __%c__ - a single character
- __%s__ - a string (e.g. "string")
- __%%__ - The "%" symbol (escaped)

Length specifiers are also supported. If you are using long long types, make sure UNITY_SUPPORT_64 is true to ensure they are printed correctly.

- __%ld__ - signed long value (decimal)
- __%lld__ - signed long long value (decimal)
- __%lu__ - unsigned long value (decimal)
- __%llu__ - unsigned long long value (decimal)
- __%lx__ - unsigned long value (hexadecimal)
- __%llx__ - unsigned long long value (hexadecimal)

_Example:_

```C
#define UNITY_INCLUDE_PRINT_FORMATTED

int a = 0xfab1;
TEST_PRINTF("Decimal   %d\n", -7);
TEST_PRINTF("Unsigned  %u\n", 987);
TEST_PRINTF("Float     %f\n", 3.1415926535897932384);
TEST_PRINTF("Binary    %b\n", 0xA);
TEST_PRINTF("Hex       %X\n", 0xFAB);
TEST_PRINTF("Pointer   %p\n", &a);
TEST_PRINTF("Character %c\n", 'F');
TEST_PRINTF("String    %s\n", "My string");
TEST_PRINTF("Percent   %%\n");
TEST_PRINTF("Unsigned long long %llu\n", 922337203685477580);
TEST_PRINTF("Color Red \033[41mFAIL\033[0m\n");
TEST_PRINTF("\n");
TEST_PRINTF("Multiple (%d) (%i) (%u) (%x)\n", -100, 0, 200, 0x12345);
```
