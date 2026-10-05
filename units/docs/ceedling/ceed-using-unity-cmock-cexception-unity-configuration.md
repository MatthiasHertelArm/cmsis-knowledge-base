---
id: "ceed-using-unity-cmock-cexception-unity-configuration"
type: "concept"
domain: "test"
title: "Using Unity, CMock & CException: Unity Configuration"
summary: "Unity is wholly compiled C code. As such, its configuration is entirely controlled by a variety of compilation symbols. These can be configured in Ceedling’s :unity project settings."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@bdc011f:docs/mkdocs/testing-guide/frameworks.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/testing-guide/frameworks/#unity-configuration"
license: "MIT"
mode: "V"
---

Unity is wholly compiled C code. As such, its configuration is entirely 
controlled by a variety of compilation symbols. These can be configured
in Ceedling’s `:unity` project settings.

### Example Unity configurations

#### Itty bitty processor & toolchain with limited test execution options

```yaml
:unity:
  :defines:
    - UNITY_INT_WIDTH=16   # 16 bit processor without support for 32 bit instructions
    - UNITY_EXCLUDE_FLOAT  # No floating point unit
```

#### Great big gorilla processor that grunts and scratches

```yaml
:unity:
  :defines:
    - UNITY_SUPPORT_64                    # Big memory, big counters, big registers
    - UNITY_LINE_TYPE=\"unsigned int\"    # Apparently, we're writing lengthy test files,
    - UNITY_COUNTER_TYPE=\"unsigned int\" # and we've got a ton of test cases in those test files
    - UNITY_FLOAT_TYPE=\"double\"         # You betcha
```

#### Example Unity configuration header file

Sometimes, you may want to funnel all Unity configuration options into a 
header file rather than organize a lengthy `:unity` ↳ `:defines` list. Perhaps your
symbol definitions include characters needing escape sequences in YAML that are 
driving you bonkers.

```yaml
:unity:
  :defines:
    - UNITY_INCLUDE_CONFIG_H
```

```c
// unity_config.h
#ifndef UNITY_CONFIG_H
#define UNITY_CONFIG_H

#include "uart_output.h" // Helper library for your custom environment

#define UNITY_INT_WIDTH 16
#define UNITY_OUTPUT_START() uart_init(F_CPU, BAUD) // Helper function to init UART
#define UNITY_OUTPUT_CHAR(a) uart_putchar(a)        // Helper function to forward char via UART
#define UNITY_OUTPUT_COMPLETE() uart_complete()     // Helper function to inform that test has ended

#endif
```

### Routing Unity’s report output

Unity defaults to using `putchar()` from C’s standard library to 
display test results.

For more exotic environments than a desktop with a terminal — e.g. 
running tests directly on a non-PC target — you have options.

For instance, you could create a routine that transmits a character via 
RS232 or USB. Once you have that routine, you can replace `putchar()` 
calls in Unity by overriding the function-like macro `UNITY_OUTPUT_CHAR`. 

Even though this override can also be defined in Ceedling YAML, most 
shell environments do not handle parentheses as command line arguments
very well. Consult your toolchain and shell documentation.

If redefining the function and macros breaks your command line 
compilation, all necessary options and functionality can be defined in 
`unity_config.h`. Unity will need the `UNITY_INCLUDE_CONFIG_H` symbol in the
`:unity` ↳ `:defines` list of your Ceedling project file (see example above).
