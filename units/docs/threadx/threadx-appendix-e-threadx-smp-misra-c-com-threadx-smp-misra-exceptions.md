---
id: "threadx-appendix-e-threadx-smp-misra-c-com-threadx-smp-misra-exceptions"
type: "concept"
domain: "rtos"
title: "Appendix E - ThreadX SMP MISRA C compliance: MISRA C Overview / ThreadX SMP MISRA Exceptions"
summary: "ThreadX SMP conforms with almost all \"required\" and \"mandatory\" MISRA-C:2004 and MISRA C:2012 rules/directives. The only exceptions to this are several \"advisory\" and \"lower priority\" required rules/directives, as follows:"
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/appendix-e.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/appendix-e.md#threadx-smp-misra-exceptions"
license: "MIT"
mode: "V"
---

_Part of: MISRA C Overview_

ThreadX SMP conforms with almost all "required" and "mandatory"
MISRA-C:2004 and MISRA C:2012 rules/directives. The only exceptions to
this are several "advisory" and "lower priority" required
rules/directives, as follows:

**MISRA Exception(s):**

MISRA-C:2004 5.6 (advisory)  
MISRA C:2012 Dir 4.5 (advisory)

**_"No identifier in one name space should have the same spelling as an identifier in another name space, with the exception of structure member and union member names."_**

There are handful of structure member names associated with the notify callbacks that are the same in their first 31 characters. In addition, there are macro parameters that are problematic with regard to this directive.

MISRA C:2012 Dir 5.1 (Required)

**_"External identifiers shall be distinct. This is a link analysis check."_**

Several global variables are the same in their first 31 characters.

MISRA-C:2004 16.7 (advisory)

**_"A pointer parameter in a function prototype should be declared as pointer to const if the pointer is not used to modify the addressed object."_**

ThreadX SMP has an established API from before this MISRA rule so changing this in the ThreadX SMP API is not practical. In addition, some services in ThreadX SMP are conditionally enabled or disabled and therefore some cases supplied pointers to the API are not used to modify the addressed object.

MISRA-C:2004 19.7 (advisory)  
MISRA C:2012 4.9 (advisory)

**_"A function should be used in preference to a function-like macro."_**

ThreadX SMP uses function-like macros to make the ThreadX SMP code base
more portable across the many different processors that are supported by
ThreadX SMP.

MISRA C:2012 Dir-4.6_b (advisory)

**_"typedefs that indicate size and signedness should be used in place of the basic numerical types."_**

ThreadX SMP uses basic typedefs without sign or size information, such as UINT and ULONG.

MISRA C:2012 Dir-4.8 (advisory)

**_"If a pointer to a structure or union is never dereference within a translation unit, then the implementation of the object should be hidden."_**

ThreadX SMP objects have a structure name and a typedef name. Since the structure name is not used directly by the ThreadX SMP code, this advisory directive is not met.

MISRA C:2012 2.3 (advisory)

**_"A project should not contain unused type declarations."_**

ThreadX SMP defines a few typedefs that are not used in the standard ThreadX SMP configuration, but are used in some configurations and in the middleware supported by ThreadX SMP.

MISRA C:2012 2.4 (advisory)

"**_A project should not contain unused tag declarations_**."

ThreadX SMP uses some structures only once while defining a typedef.

MISRA C:2012 2.5 (advisory)

**_"A project should not contain unused macro declarations."_**

ThreadX SMP defines a few typedefs that are not used in the standard ThreadX SMP configuration, but are used in some configurations and in the middleware supported by ThreadX SMP.

MISRA C:2012 2.7 (advisory)

**_"There should be no unused parameters in functions."_**

By default, ThreadX SMP conforms to this advisory rule. However, when ThreadX is built with **_TX_DISABLE_NOTIFY_CALLBACKS_**, Four functions in the ThreadX SMP library are flagged as not meeting this advisory rule, as follows:

**_tx_event_flags_set_notify.c  
tx_queue_send_notify.c  
tx_semaphore_put_notify.c  
tx_thread_entry_exit_notify.c_**

In addition, when **_TX_TIMER_PROCESS_IN_ISR_** is defined, the file **_tx_timer_thread_entry.c_** is flagged as not meeting this advisory rule.

MISRA C:2012 3.1 (required)

**_"The character sequences /\* and // shall not be used within a comment."_**

"//" is used in the copyright as part of the URL. 

MISRA C:2012 8.7 (advisory)

**_"Functions and objects should not be defined with external linkage if they are referenced in only one translation unit."_**

Internal functions and variables in ThreadX SMP are not always referenced from more than one external translation unit.

MISRA C:2012 8.9_b (advisory)

**_"An object should be defined at block scope if its identifier only appears in a single function."_**

Some global data elements of ThreadX SMP are only referenced in one function, necessitating an exception to this rule.

MISRA C:2012 8.13 (advisory)

**_"A pointer should point to a const-qualified type whenever
possible."_**

The ThreadX SMP API has input parameters that are not modified but the
pointer does not have the const qualifier.

MISRA C:2012 17.8 (advisory)

**_"A function parameter should not be modified."_**

In several files the input parameter to a ThreadX SMP API is used as a
local variable within the API itself. There are no side effects since
in C the parameters are passed as value.

MISRA-C:2004 20.1 (required, low priority)  
MISRA C:2012 21.1

"**Reserved identifiers, macros and functions in the standard library,
shall not be defined, redefined or undefined**"

ThreadX SMP utilizes much of the field proven ThreadX single core
source code. However, to enable the reuse, macros are used to replace
data structures specific to each core with function calls or an array
indexed by core, like the following:

(figure: Image that shows an array indexed by core.)

Technically, this isn't replacing a reserved identifier, but the
MISRA-C:2004 specification indicates that anything with an underscore
cannot be redefined.

MISRA C:2012 5.2 (required, low priority)

"**Identifiers declared in the same scope and name space shall be
distinct**"

This is the same situation as the previous issue, the macro
re-definition of **_"\_tx_thread_system_state_**" matches the default
definition of the actual data structure, which is expected since
ThreadX SMP needs to override the standard, single core data structure
usage.

MISRA C:2012 18.1 (required)

"**_A pointer resulting from arithmetic on a pointer operand shall
address an element of the same array as that pointer operand_**."

C-STAT generates six messages when building the Thread SMP library,
however, these are all false positives, i.e., this version of C-STAT
is erroneously reporting this error.
