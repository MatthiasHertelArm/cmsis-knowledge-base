---
id: "zep-assertions-runtime-assertions"
type: "concept"
domain: "rtos"
title: "Assertions: Runtime Assertions"
summary: "The module-aware assertion API is declared in include/zephyr/sys/zassert.h. Each source file opts into an assertion module whose level is a compile-time constant."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/kernel/services/other/assert.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/kernel/services/other/assert.rst"
license: "Apache-2.0"
mode: "V"
---

### ZASSERT()


The module-aware assertion API is declared in `include/zephyr/sys/zassert.h`.
Each source file opts into an assertion *module* whose level is a compile-time constant. Because the
level is known at compile time, the compiler can optimize the footprint of the assertion code based
on the associated assertion level of the module the assert belongs to.


#### Assertion Levels


Every module resolves to one of four levels:

- `ZASSERT_LEVEL_OFF` -- assertions are compiled out entirely.
- `ZASSERT_LEVEL_TERSE` -- assertions are checked; on failure only a fixed
  `ASSERTION FAIL` banner is reported. The location, condition, message and
  arguments are not compiled in.
- `ZASSERT_LEVEL_NORMAL` -- assertions are checked; on failure only the location
  is reported (`ASSERTION FAIL @ file:line`). The condition, message and
  arguments are not compiled in.
- `ZASSERT_LEVEL_VERBOSE` -- assertions are checked; on failure the stringified
  condition, location and optional message are reported.

`CONFIG_ASSERT` is the master switch.
When it is disabled, every module is forced to `ZASSERT_LEVEL_OFF` and all `ZASSERT()` /
`ZASSERT_MODULE()` usage compiles to nothing, regardless of any module's configured level.

:note:
   `ZASSERTS` footprint reduction relies on compiler optimizations to prune unused conditions,
   arguments, and string literals at compile time. Lower optimization levels may prevent dead-code
   elimination, leaving assertion artifacts in the binary despite a low module assertion setting.


#### Selecting a Module


Place `ZASSERT_MODULE` once at file scope, before any use of
`ZASSERT` in the translation unit:

```c

#include <zephyr/sys/zassert.h>

ZASSERT_MODULE(MYMODULE);
```
The module name is an UPPERCASE identifier. Its default level is taken from the
Kconfig symbol `CONFIG_ASSERT_MODULE_<module>_LEVEL` (here `CONFIG_ASSERT_MODULE_MYMODULE_LEVEL`).
A file may override the module default by passing an explicit level as a second argument, for example
`ZASSERT_MODULE(MYMODULE, ZASSERT_LEVEL_VERBOSE)`.

Once a module is selected, use `ZASSERT` like a conditional check with an optional
`printf`-like message:

```c

ZASSERT(x == 3, "x was %d, expected 3", x);
```
If the condition is false and the module's level is at least `ZASSERT_LEVEL_TERSE`, a fatal error
is raised. The location is only compiled in and printed at `ZASSERT_LEVEL_NORMAL` or above, and
the condition, message and its arguments are only compiled in and printed at
`ZASSERT_LEVEL_VERBOSE`.

For headers and inline functions, avoid `ZASSERT_MODULE()` at file scope, as the
selection would leak into every file that includes the header. Use one of the
following instead.

Place `ZASSERT_MODULE` inside the function body. The selection is then
block-scoped and does not escape to the includer, and plain `ZASSERT`
works within that function:

```c

static inline void f(void *ptr)
{
        ZASSERT_MODULE(MYMODULE);

        ZASSERT(ptr != NULL, "ptr must not be NULL");
}
```
For an assertion with a fixed level, use `ZASSERT_TERSE`,
`ZASSERT_NORMAL` or `ZASSERT_VERBOSE`. These forms select the
level at the call site and declare nothing in scope:

```c

ZASSERT_TERSE(ptr != NULL);
ZASSERT_NORMAL(ptr != NULL);
ZASSERT_VERBOSE(ptr != NULL, "ptr must not be NULL");
```
The `ZASSERT_LEVEL_TERSE`, `ZASSERT_LEVEL_NORMAL` and `ZASSERT_LEVEL_VERBOSE`
defines configure module assertion levels, while
`ZASSERT_TERSE()`, `ZASSERT_NORMAL()` and `ZASSERT_VERBOSE()` perform
fixed-level assertions.


**Note:** A few rules apply to `ZASSERT()` and its file-scope module: - `ZASSERT_MODULE()` must appear before the first `ZASSERT()` in the translation unit, and only one module may be selected per file. - Using `ZASSERT()` with no module in scope is a compile error. Select a module first, or use the fixed-level `ZASSERT_TERSE()`, `ZASSERT_NORMAL()` or `ZASSERT_VERBOSE()` form. - `CONFIG_ASSERT` remains the master switch: when it is disabled the module level is forced to `ZASSERT_LEVEL_OFF` regardless of the configured level.


#### Defining a Module's Kconfig Level


The `CONFIG_ASSERT_MODULE_<module>_LEVEL` symbol is generated from the template
`subsys/debug/zassert/Kconfig.template.assert`. Source it from a Kconfig
file, setting the module name and a human-readable description first:

```kconfig

module = MYMODULE
module-str = the MYMODULE assert module
source "subsys/debug/zassert/Kconfig.template.assert"
```
This produces a user-facing `Off` / `Terse` / `Normal` / `Verbose` choice and the derived,
non-assignable integer symbol `CONFIG_ASSERT_MODULE_MYMODULE_LEVEL` consumed by
`ZASSERT_MODULE(MYMODULE)`.
The choice defaults to `Verbose` and stays overridable from `prj.conf`.


#### Example


The assert sample demonstrates enabling
verbose assertions for a single file while the master assertion switch is enabled.
A condensed version:

```c

#include <zephyr/kernel.h>
#include <zephyr/sys/zassert.h>

ZASSERT_MODULE(MYMODULE);

int main(void)
{
        int x = 2;

        ZASSERT(x == 3, "x was %d, expected 3", x);

        return 0;
}
```
With `CONFIG_ASSERT_MODULE_MYMODULE_LEVEL_VERBOSE=y` the failing check produces:

```none

ASSERTION FAIL [x == 3] @ .../src/main.c:...
x was 2, expected 3
```

#### Customizing the Failure Behavior


The entire assertion cold path is consolidated into a small set of weak,
overridable functions declared in `include/zephyr/sys/zassert.h`
and implemented in `subsys/debug/zassert/zassert.c`:

- `zassert_fail` reports a failed assertion (location, and when a
  message is present the message and its arguments) and then invokes
  `zassert_post_action`. Overriding it is the single surface for
  capturing or redirecting the whole assertion output.
- `zassert_post_action` takes the terminal action. The default
  implementation invokes `k_oops` if the failing thread was running in
  user mode, and `k_panic` otherwise.
- `zassert_vprint` is the single primitive through which all assertion
  text flows. Override it to capture or redirect every assertion message from
  one place. `zassert_print` is a variadic convenience wrapper around
  it, used by the legacy `__ASSERT_PRINT()` compatibility shims.

When `CONFIG_ASSERT_TEST` is enabled, the post action handler is
allowed to return (rather than abort) so that tests can validate assertion
behavior by installing a custom hook.
