---
id: "unity-unity-configuration-guide-toolset-customization"
type: "concept"
domain: "test"
title: "Unity Configuration Guide: The Options / Toolset Customization"
summary: "In addition to the options listed above, there are a number of other options which will come in handy to customize Unity's behavior for your specific toolchain. It is possible that you may not need to touch any of these..."
status: "draft"
collection: "unity"
source: "ThrowTheSwitch/Unity@2b80d1a:docs/UnityConfigurationGuide.md"
doc_source: "https://github.com/ThrowTheSwitch/Unity/blob/2b80d1a/docs/UnityConfigurationGuide.md#toolset-customization"
license: "MIT"
mode: "V"
---

_Part of: The Options_

In addition to the options listed above, there are a number of other options which will come in handy to customize Unity's behavior for your specific toolchain.
It is possible that you may not need to touch any of these... but certain platforms, particularly those running in simulators, may need to jump through extra hoops to run properly.
These macros will help in those situations.

#### `UNITY_OUTPUT_CHAR(a)`

#### `UNITY_OUTPUT_FLUSH()`

#### `UNITY_OUTPUT_START()`

#### `UNITY_OUTPUT_COMPLETE()`

By default, Unity prints its results to `stdout` as it runs.
This works perfectly fine in most situations where you are using a native compiler for testing.
It works on some simulators as well so long as they have `stdout` routed back to the command line.
There are times, however, where the simulator will lack support for dumping results or you will want to route results elsewhere for other reasons.
In these cases, you should define the `UNITY_OUTPUT_CHAR` macro.
This macro accepts a single character at a time (as an `int`, since this is the parameter type of the standard C `putchar` function most commonly used).
You may replace this with whatever function call you like.

_Example:_
Say you are forced to run your test suite on an embedded processor with no `stdout` option.
You decide to route your test result output to a custom serial `RS232_putc()` function you wrote like thus:

```C
#include "RS232_header.h"
...
#define UNITY_OUTPUT_CHAR(a)    RS232_putc(a)
#define UNITY_OUTPUT_START()    RS232_config(115200,1,8,0)
#define UNITY_OUTPUT_FLUSH()    RS232_flush()
#define UNITY_OUTPUT_COMPLETE() RS232_close()
```

_Note:_
`UNITY_OUTPUT_FLUSH()` can be set to the standard out flush function simply by specifying `UNITY_USE_FLUSH_STDOUT`.
No other defines are required.

#### `UNITY_OUTPUT_FOR_ECLIPSE`

#### `UNITY_OUTPUT_FOR_IAR_WORKBENCH`

#### `UNITY_OUTPUT_FOR_QT_CREATOR`

When managing your own builds, it is often handy to have messages output in a format which is recognized by your IDE.
These are some standard formats which can be supported.
If you're using Ceedling to manage your builds, it is better to stick with the standard format (leaving these all undefined) and allow Ceedling to use its own decorators.

#### `UNITY_PTR_ATTRIBUTE`

Some compilers require a custom attribute to be assigned to pointers, like `near` or `far`.
In these cases, you can give Unity a safe default for these by defining this option with the attribute you would like.

_Example:_

```C
#define UNITY_PTR_ATTRIBUTE __attribute__((far))
#define UNITY_PTR_ATTRIBUTE near
```

#### `UNITY_PRINT_EOL`

By default, Unity outputs \n at the end of each line of output.
This is easy to parse by the scripts, by Ceedling, etc, but it might not be ideal for YOUR system.
Feel free to override this and to make it whatever you wish.

_Example:_

```C
#define UNITY_PRINT_EOL() { UNITY_OUTPUT_CHAR('\r'); UNITY_OUTPUT_CHAR('\n'); }
```

#### `UNITY_EXCLUDE_DETAILS`

This is an option for if you absolutely must squeeze every byte of memory out of your system.
Unity stores a set of internal scratchpads which are used to pass extra detail information around.
It's used by systems like CMock in order to report which function or argument flagged an error.
If you're not using CMock and you're not using these details for other things, then you can exclude them.

_Example:_

```C
#define UNITY_EXCLUDE_DETAILS
```

#### `UNITY_PRINT_TEST_CONTEXT`

This option allows you to specify your own function to print additional context as part of the error message when a test has failed.
It can be useful if you want to output some specific information about the state of the test at the point of failure, and `UNITY_SET_DETAILS` isn't flexible enough for your needs.

_Example:_

```C
#define UNITY_PRINT_TEST_CONTEXT PrintIterationCount

extern int iteration_count;

void PrintIterationCount(void)
{
  UnityPrintFormatted("At iteration #%d: ", iteration_count);
}
```

#### `UNITY_EXCLUDE_SETJMP`

If your embedded system doesn't support the standard library setjmp, you can exclude Unity's reliance on this by using this define.
This dropped dependence comes at a price, though.
You will be unable to use custom helper functions for your tests, and you will be unable to use tools like CMock.
Very likely, if your compiler doesn't support setjmp, you wouldn't have had the memory space for those things anyway, though... so this option exists for those situations.

_Example:_

```C
#define UNITY_EXCLUDE_SETJMP
```

#### `UNITY_TEST_PROTECT`

#### `UNITY_TEST_ABORT`

Unity handles test failures via `setjmp`/`longjmp` pair by default. As mentioned above, you can disable this with `UNITY_EXCLUDE_SETJMP`. You can also customise what happens on every `TEST_PROTECT` and `TEST_ABORT` call. This can be accomplished by providing user-defined `UNITY_TEST_PROTECT` and `UNITY_TEST_ABORT` macros (and these may be defined independently).

`UNITY_TEST_PROTECT` is used as an `if` statement expression, and has to evaluate to `true` on the first call (when saving stack environment with `setjmp`), and to `false` when it returns as a result of a `TEST_ABORT` (when restoring the stack environment with `longjmp`).

Whenever an assert macro fails, `TEST_ABORT` is used to restore the stack environment previously set by `TEST_PROTECT`. This part may be overriden with `UNITY_TEST_ABORT`, e.g. if custom failure handling is needed.

_Example 1:_

Calling `longjmp` on your target is possible, but has a platform-specific (or implementation-specific) set of prerequisites, e.g. privileged access level. You can extend the default behaviour of `TEST_PROTECT` and `TEST_ABORT` as:

`unity_config.h`:

```C
#include "my_custom_test_handlers.h"

#define UNITY_TEST_PROTECT() custom_test_protect()
#define UNITY_TEST_ABORT()   custom_test_abort()
```

`my_custom_test_handlers.c`:

```C
int custom_test_protect(void) {
  platform_specific_code();
  return setjmp(Unity.AbortFrame) == 0;
}

UNITY_NORETURN void custom_test_abort(void) {
  more_platform_specific_code();
  longjmp(Unity.AbortFrame, 1);
}
```

_Example 2:_

Unity is used to provide the assertion macros only, and an external test harness/runner is used for test orchestration/reporting. In this case you can easily plug your code by overriding `TEST_ABORT` as:

`unity_config.h`:

```C
#include "my_custom_test_handlers.h"

#define UNITY_TEST_PROTECT() 1
#define UNITY_TEST_ABORT()   custom_test_abort()
```

`my_custom_test_handlers.c`:

```C
void custom_test_abort(void) {
  if (Unity.CurrentTestFailed == 1) {
    custom_failed_test_handler();
  } else if (Unity.CurrentTestIgnored == 1) {
    custom_ignored_test_handler();
  }
}
```

#### `UNITY_OUTPUT_COLOR`

If you want to add color using ANSI escape codes you can use this define.

_Example:_

```C
#define UNITY_OUTPUT_COLOR
```

#### `UNITY_INCLUDE_EXEC_TIME`

Define this to measure and report execution time for each test in the suite. When enabled, Unity will do
it's best to automatically find a way to determine the time in milliseconds. On most Windows, macos, or 
Linux environments, this is automatic. If not, you can give Unity more information.

On Unix and macOS, the default uses POSIX `clock_gettime(CLOCK_MONOTONIC)` when that clock is available.
If it is not (strict ISO C with no POSIX clocks in `<time.h>`), it falls back to the standard `clock()` function,
which is also the Windows default.

#### `UNITY_CLOCK_MS`

If you're working on a system (embedded or otherwise) which has an accessible millisecond timer. You can
define `UNITY_CLOCK_MS` to be the name of the function which returns the millisecond timer. It will then
attempt to use that function for timing purposes.

#### `UNITY_EXEC_TIME_START`

Define this hook to start a millisecond timer if necessary.

#### `UNITY_EXEC_TIME_STOP`

Define this hook to stop a millisecond timer if necessary.

#### `UNITY_PRINT_EXEC_TIME`

Define this hook to print the current execution time. Used to report the milliseconds elapsed.

#### `UNITY_TIME_TYPE`

Finally, this can be set to the type which holds the millisecond timer.

#### `UNITY_SHORTHAND_AS_INT`

#### `UNITY_SHORTHAND_AS_MEM`

#### `UNITY_SHORTHAND_AS_RAW`

#### `UNITY_SHORTHAND_AS_NONE`

These options give you control of the `TEST_ASSERT_EQUAL` and the `TEST_ASSERT_NOT_EQUAL` shorthand assertions.
Historically, Unity treated the former as an alias for an integer comparison.
It treated the latter as a direct comparison using `!=`.
This asymmetry was confusing, but there was much disagreement as to how best to treat this pair of assertions.
These four options will allow you to specify how Unity will treat these assertions.

- AS INT - the values will be cast to integers and directly compared.
  Arguments that don't cast easily to integers will cause compiler errors.
- AS MEM - the address of both values will be taken and the entire object's memory footprint will be compared byte by byte.
  Directly placing constant numbers like `456` as expected values will cause errors.
- AS_RAW - Unity assumes that you can compare the two values using `==` and `!=` and will do so.
  No details are given about mismatches, because it doesn't really know what type it's dealing with.
- AS_NONE - Unity will disallow the use of these shorthand macros altogether, insisting that developers choose a more descriptive option.

#### `UNITY_SUPPORT_VARIADIC_MACROS`

This will force Unity to support variadic macros when using its own built-in RUN_TEST macro.
This will rarely be necessary. Most often, Unity will automatically detect if the compiler supports variadic macros by checking to see if it's C99+ compatible.
In the event that the compiler supports variadic macros, but is primarily C89 (ANSI), defining this option will allow you to use them.
This option is also not necessary when using Ceedling or the test runner generator script.

#### `UNITY_SUPPORT_TEST_CASES`

Unity can automatically define all supported parameterized tests macros.
That feature is disabled by default.
To enable it, use the following example:

```C
#define UNITY_SUPPORT_TEST_CASES
```

You can manually provide required `TEST_CASE`, `TEST_RANGE` or `TEST_MATRIX` macro definitions
before including `unity.h`, and they won't be redefined.
If you provide one of the following macros, some of default definitions will not be
defined:
| User defines macro | Unity will _not_ define following macro |
|---|---|
| `UNITY_EXCLUDE_TEST_CASE` | `TEST_CASE` |
| `UNITY_EXCLUDE_TEST_RANGE` | `TEST_RANGE` |
| `UNITY_EXCLUDE_TEST_MATRIX` | `TEST_MATRIX` |
| `TEST_CASE` | `TEST_CASE` |
| `TEST_RANGE` | `TEST_RANGE` |
| `TEST_MATRIX` | `TEST_MATRIX` |

`UNITY_EXCLUDE_TEST_*` defines is not processed by test runner generator script.
If you exclude one of them from definition, you should provide your own definition
for them or avoid using undefined `TEST_*` macro as a test generator.
Otherwise, compiler cannot build source code file with provided call.

_Note:_
That feature requires variadic macro support by compiler. If required feature
is not detected, it will not be enabled, even though preprocessor macro is defined.
