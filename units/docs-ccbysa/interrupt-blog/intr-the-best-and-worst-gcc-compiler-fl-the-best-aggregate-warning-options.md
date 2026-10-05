---
id: "intr-the-best-and-worst-gcc-compiler-fl-the-best-aggregate-warning-options"
type: "concept"
domain: "debug"
title: "The Best and Worst GCC Compiler Flags For Embedded: The Best Aggregate Warning Options"
summary: "Compiler warnings are the first line of defense against catching various errors that could arise at runtime and enforcing conventions that lead to a more readable codebase."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-22-best-and-worst-gcc-clang-compiler-flags.md"
doc_source: "https://interrupt.memfault.com/blog/best-and-worst-gcc-clang-compiler-flags#the-best-aggregate-warning-options"
license: "CC-BY-SA-4.0"
mode: "V"
---

Compiler warnings are the first line of defense against catching various errors that could arise at
runtime and enforcing conventions that lead to a more readable codebase. It is _a lot_ easier to fix
issues at compilation time than when unexpected behavior is encountered on your platform.

GCC and Clang have several warning flags which will enable a collection of useful checks which we
will explore in more detail below.

> NOTE: When enabling warning flags for a project that hasn't used them previously, there will likely be _a
> ton_ of warnings. I'd recommend taking an incremental approach when transitioning the project by only compiling parts of your
> system (i.e new files) with a more stringent set of warning flags or enabling and fixing sets of
> warnings at a time. Trying to fix thousands of warnings all at the same time is a recipe for
> introducing regressions or upsetting fellow developers trying to review your change.

### -Wall & -Wextra

The compiler flag `-Wall` enables a base set of warnings generally agreed upon as being useful and easy to fix. `-Wextra` enables an additional set of flags not covered by `-Wall`

The exact list of flags varies between compiler versions but can easily be found by consulting the GCC documentation for the compiler version you are using[^1].

Here's a c snippet that will happily compile but has a couple unfortunate bugs.

```c
static void prv_various_memset_bugs(void) {
  #define NUM_ITEMS 10
  uint32_t buf[NUM_ITEMS];
  memset(buf, NUM_ITEMS, 0x0);
  memset(buf, 0x0, NUM_ITEMS);
}
```

The issues can easily be caught at compile time by using the `-Wall` flag.

```bash
$ EXTRA_CFLAGS=-Wall make
main.c: In function 'prv_various_memset_bugs':
main.c:19:3: warning: 'memset' used with constant zero length parameter; this could be due to transposed parameters [-Wmemset-transposed-args]
   memset(buf, NUM_ITEMS, 0x0);
   ^~~~~~
main.c:20:3: warning: 'memset' used with length equal to number of elements without multiplication by element size [-Wmemset-elt-size]
memset(buf, 0x0, NUM_ITEMS);
```

### -Werror

`-Werror` causes all enabled warnings to cause compilation errors. This can be _incredibly_
useful to ensure that no new warnings slip into a codebase. When working with a team,
not everyone may be as excited about fixing compiler warnings as you. I really consider this flag a
must have to prevent code with warnings from being merged to master.

Enabling `-Werror` does mean that when the compiler version changes, new compilation errors may
appear (since new sets of warnings are usually added to flags like `-Wall` and pre-existing checks
are improved and can catch new errors). Typically, it's a very small set of changes required to fix
the new issues detected.

> NOTE: I'd recommend enforcing a certain compiler version be used in your build system (for local
> development and in CI). That way everyone will see the exact same errors and behavior. As new versions become available, one team
> member can update to the new version, fix up any new issues, and then merge an update requiring
> that compiler version be used by the rest of the team.

Sometimes, there may be warnings you do not wish to trigger an error or even a warning. These can
easily be controlled with the following compiler options:

- `-Wno-<warning>` to disable the warning altogether
- `-Wno-error=<warning>` to keep the warning enabled but not trigger an error.

Let's try it out for our example above! For example:

```bash
# Warn about memset-elt-size but don't error on it
$ EXTRA_CFLAGS="-Wall -Werror -Wno-error=memset-elt-size" make
main.c: In function 'prv_various_memset_bugs':
main.c:47:3: error: 'memset' used with constant zero length parameter; this could be due to transposed parameters [-Werror=memset-transposed-args]
   memset(buf, NUM_ITEMS, 0x0);
   ^~~~~~
main.c:48:3: warning: 'memset' used with length equal to number of elements without multiplication by element size [-Wmemset-elt-size]
memset(buf, 0x0, NUM_ITEMS);

# Don't enable any warnings for memset-elt-size
$ EXTRA_CFLAGS="-Wall -Werror -Wno-memset-elt-size" make
main.c: In function 'prv_various_memset_bugs':
main.c:47:3: error: 'memset' used with constant zero length parameter; this could be due to transposed parameters [-Werror=memset-transposed-args]
   memset(buf, NUM_ITEMS, 0x0);
   ^~~~~~
```

### -Weverything (Clang only)

By design, Clang generally matches the set of compiler flag options available in the GNU toolchain, but there are a few that are different.

For embedded projects, it's useful to cross-compile the source code with Clang to surface additional
issues that GCC may have missed.

One flag there are some _strong opinions_[^2] about is `-Weverything` which literally enables every
single warning available to Clang! Many suggest you should _never_ flip on this flag in a
build. The strategy I prefer, followed by other projects such as CppUTest[^3], is to enable the
warning but liberally disable warnings from it that are not useful.

I've found this to be a pretty neat way to discover new warning flags built into clang, such as
`-Wdocumentation`, which can catch errors in comments! For example,

```c
//! A bad docstring that clang can identify issues with using -Wdocumentation
//!
//! @param a The first value of the summation
//! @param c The second value of the summation
//!
//! @return the sum of a & b
int simple_math_get_sum(int a, int b);
```

```bash
$ USE_CLANG=1 EXTRA_CFLAGS=-Weverything make
[...]
./simple_math.h:6:12: warning: parameter 'c' not found in the function declaration [-Wdocumentation]
//! @param c The second value of the summation
           ^
./simple_math.h:6:12: note: did you mean 'b'?
//! @param c The second value of the summation
           ^
           b
```
