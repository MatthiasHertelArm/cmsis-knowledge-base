---
id: "intr-exploring-printf-on-cortex-m-printf"
type: "concept"
domain: "debug"
title: "Exploring printf on Cortex-M: `printf`"
summary: "Ah, the first and last of debugging techniques!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-09-20-printf-on-embedded.md"
doc_source: "https://interrupt.memfault.com/blog/printf-on-embedded#printf"
license: "CC-BY-SA-4.0"
mode: "V"
---

Ah, the first and last of debugging techniques!

Let's first explore what happens when printf runs. Here's a simplified flowchart
showing what happens when `printf` is called:

 blockdiag { A [label = "printf"]; B [label =
"vprintf"]; C [label = "_write syscall"]; A -> B -> C; } 

Going call by call:

1. `printf` is called by the application, for example:

   ```c
   printf("hello world! today is %d-%d-%d\n", 2021, 2, 16);
   ```

2. `printf` calls `vprintf`, the variadic version of `printf` (simplifying a bit
   for this example). `vprintf` processes the format string and consumes the
   "variadic args" (here the date components), and then calls `_write` to output
   the formatted data.

3. `_write` is a libc function responsible for writing bytes to a file
   descriptor. It's called with the file descriptor for stdout (1), and a
   pointer to the formatted string. It executes the necessary system call to
   write the data to the appropriate file descriptor. On hosted platforms (eg
   Linux, macOS, Windows), this is usually a `write` syscall. On embedded
   platforms, this might be a call to a UART driver.

### Using `printf` in a bare-metal application

On unhosted platforms (eg bare-metal or minimal RTOS), you may not have built-in
support for `printf`/`scanf`/`fprintf`. Fear not, you can get some printf in
your life by using newlib-nano's support:

```bash
# add these to your linker command line
LDFLAGS += --specs=nano.specs --specs=nosys.specs
```

That adds libc and "nosys" support to your application, which provide the
implementations for the various libc functions like `printf`, `sprintf`, etc.
This means you can add `printf` calls and your application will link! But we're
not quite done.

### Redirecting `_write`

`_write()` is the function eventually called by `printf`/`fprintf` responsible
for emitting the bytes formatted by those functions to the appropriate file
descriptor.

If you want to redirect the output of your `printf`/`fprintf` calls, you might
want to implement your own copy of `_write()`. By default, newlib libc doesn't
provide an implementation for `_write()`: you might see an error like this when
linking:

```log
arm-none-eabi/lib/thumb/v7e-m/nofp/libg_nano.a(libc_a-writer.o): in function `_write_r':
newlib/libc/reent/writer.c:49: warning: _write is not implemented and will always fail
```

See a thorough explanation here[^0].

The minimal implementation might look like this:

```c
// stderr output is written via the 'uart_write' function
#include <stddef.h>  // for size_t
#include <unistd.h>  // for STDERR_FILENO
int _write (int file, const void * ptr, size_t len) {
  if (file == STDERR_FILENO) {
    uart_write(ptr, len);
  }

  // return the number of bytes passed (all of them)
  return len;
}
```

Note that the libc `setbuf` API controls I/O buffering for newlib. By default
`_write` will be called for every byte. You might want to instead buffer up to
line ends, by:

```c
#include <stdio.h>
setvbuf(stout, NULL, _IOLBF, 0);
```

See `man setvbuf` or <http://www.cplusplus.com/reference/cstdio/setvbuf/> for
details.

### Reentrancy

Fancy word for if a function can be safely premepted and called simultaneously
from multiple (interrupt) contexts.

Some libc functions in newlib share a context structure that contains global
data structures. If you want to safely use them in multiple threads, you have a
couple of options:

- only use these functions in one thread in your program
- disable interrupts when using non-reentrant functions
- only use the reentrant versions of the functions (denoted by `_xxx_r()`, eg
  `_printf_r` in newlib)
- recompile newlib with `__DYNAMIC_REENT__` to have the non-reentrant functions
  call a user-defined function to get the current thread's reentrancy structure
- override the default global reentrancy structure as necessary

See the header file here for some detailed information:

<https://github.com/bminor/newlib/blob/6226bad0eafe762b811c62d1dc096bc0858b0d1a/newlib/libc/include/reent.h>

And great explanations here- especially if using FreeRTOS, there's built-in
support for managing reentrancy structures:

- <https://www.codeinsideout.com/blog/freertos/reentrant/>
- <https://mcuoneclipse.com/2020/11/15/steps-to-use-freertos-with-newlib-reentrant-memory-allocation/>

Let's go on a small side adventure into reentrancy approaches for
newlib\[-nano\]!

#### One thread only

It might not be necessary to use the non-reentrant functions in small interrupt
handlers (and is probably a reasonable idea to prohibit them).

Here's an approach that will cause a runtime error if a non-reentrant function
is called in an interrupt context. Unfortunately it requires rebuilding newlib,
so it's really only for curiosity or the very paranoid.

First, rebuild newlib (or build it as part of your project build; this is
probably only practical if you're using a compiler cache like ccache), setting
`__DYNAMIC_REENT__` when building.

Then, when building your application source, define a `__getreent()` function
with the following contents:

```c
#include <reent.h>
// Function to check if in interrupt context
int isInInterruptContext(void) {
    // Read the CONTROL register
    uint32_t control_reg;
    asm volatile ("MRS %0, CONTROL" : "=r" (control_reg));

    // Check the nPRIV bit (bit 0)
    return (control_reg & 1) != 0;
}
struct _reent * __getreent(void) {
  if (isInInterruptContext()) {
    __asm__ ("bkpt 0");
  }
  // return the built in global reentrancy context
  return _impure_ptr;
}
```

Also be sure to define `__DYNAMIC_REENT__` in your CFLAGS when building your
application source.

This example trips a software breakpoint if a non-reentrant function is called
from an interrupt context, to catch the error condition. Alternatively, the
function could return `NULL`, and libc calls using the reentrancy structure
_should_ return with no effect, but in practice this may not always be handled
in newlib.

Note that the same trap can be set up (applying to `printf` only though) by
adding a similar snippet to `_write()` (or using linker `--wrap` to inject the
check), without requiring rebuilding newlib 🥹.

#### Disable interrupts

This approach requires that every lower-priority thread enclose any
non-reentrant calls in a critical section, eg:

```c
__disable_irq();
printf("phew!\n");
__enable_irq();
```

This can add latency to interrupts (on cortex parts, typically interrupts will
pend until enabled after the call), particularly bad if your printf output is
relatively slow, eg 115200 baud UART for example.

It also requires you to be diligent about where you are using non-reentrant
functions.

#### Only use reentrant libc functions

This approach requires only calling the reentrant versions of the libc
functions. See an example below.

```c
#include <reent.h>
#include <stdio.h>

// call printf from an interrupt without breaking other threads
void Foo_Interrupt_Handler(void) {
  struct _reent my_impure_data = _REENT_INIT(my_impure_data);
  _printf_r(&my_impure_data, "hey!\n");
}
```

This is a pretty manual technique but it is relatively simple, and doesn't
require disabling interrupts or knowing the relative preemption priority of the
current call site.

#### Dynamic reentrancy

See the section above about building newlib; we need to enable
`__DYNAMIC_REENT__` in the library build to have the non-reentrant functions
call `__getreent()` (i.e. enable it in the `crosstool-ng` configuration if
you're building a whole toolchain). Then we can implement a version that
provides the correct reentrancy structure depending on our thread context:

```c
// this system only needs 1 reentrancy context
static struct _reent isr_impure_structs[] = {
  _REENT_INIT(isr_impure_structs[0]),
};

struct _reent * __getreent (void) {
  struct _reent *isr_impure_ptr;

  // this might use NVIC calls to figure out which ISR is active, or if there is
  // an OS, return current executing thread
  int thread_id = get_thread_id();

  switch thread_id {
    case 0:
      isr_impure_ptr = isr_impure_structs[0];
    default:
      // crash
      __asm__("bkpt 0");
  }

  return isr_impure_ptr;
}
```

Note that if you're using an RTOS, this may already be handled in some way or
there might be a hook when switching thread contexts (see [above](#reentrancy))
where we can move `__impure_ptr`, and we don't even need to recompile newlib!

For example, Zephyr RTOS
[handles logging from interrupts](https://docs.zephyrproject.org/3.4.0/services/logging/index.html#default-frontend)
or multiple preemptible thread contexts, so there's no need to fiddle with the
low-level libc reentrancy structures.

#### Overriding `__impure_ptr`

Another option is to override the global reentrancy structure when inside
interrupts; a little trickier but can be useful in certain systems.

The global reentrant structure is referenced by the pointer `__impure_ptr`,
defined here:

<https://sourceware.org/git/?p=newlib-cygwin.git;a=blob;f=newlib/libc/reent/impure.c;h=76f67459e48d3efc20698f8fda39620b1359f63f;hb=HEAD#l27>

You can instantiate your own copy of the structure:

```c
#include <reent.h>
struct _reent my_impure_data = _REENT_INIT(my_impure_data);
```

And then temporarily override `_impure_ptr`:

```c
_impure_ptr = &my_impure_data;
printf("yolo\n");
// restore default global reentrancy struct
_impoure_ptr = &impure_data;
```

This makes it safe to call the above snippet in an interrupt handler, because it
won't stomp on the global reentrancy data if it preempted an in-progress
non-reentrant function!

Note that you'll need to do the same thing in every preemption context, i.e. any
call site that can interrupt another thread that is using non-reentrant
functions. So this approach would be primarily useful in cases with only a small
number of threads, or a well-considered preemption hierarchy where we know
exactly where to move the pointer and where we don't need to.
