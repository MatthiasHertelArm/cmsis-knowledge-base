---
id: "zep-test-framework-advanced-features"
type: "concept"
domain: "test"
title: "Test Framework: Advanced features"
summary: "Value-parameterized tests allow a single test body to be executed once for each value in a supplied list, similar to GoogleTest's TEST_P / INSTANTIATE_TEST_SUITE_P pattern."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/test/ztest.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/test/ztest.rst"
license: "Apache-2.0"
mode: "V"
---

### Value-parameterized tests


Value-parameterized tests allow a single test body to be executed once for each
value in a supplied list, similar to GoogleTest's `TEST_P` / `INSTANTIATE_TEST_SUITE_P`
pattern.  The fixture and the parameter are completely independent: the suite's
`setup()` return value is always passed as `data` and is never overwritten by
a parameter value.


#### Declaring a parameterized test body


Use `ZTEST_P` in the same way as `ZTEST`.  Inside the body, the `data`
pointer carries the suite fixture (identical to `ZTEST_F`).  The current
parameter value is retrieved through the run-time accessors:

```C

#include <zephyr/ztest.h>

struct my_suite_fixture {
     int initial_value;
};

static void *my_suite_setup(void) {
     static struct my_suite_fixture f = { .initial_value = 42 };
     return &f;
}

ZTEST_SUITE(my_suite, NULL, my_suite_setup, NULL, NULL, NULL);

ZTEST_P(my_suite, test_multiply)
{
     struct my_suite_fixture *f = (struct my_suite_fixture *)data;
     int factor = ZTEST_GET_PARAM(int);

     /* fixture is always intact, regardless of parameter */
     zassert_equal(f->initial_value, 42, "fixture corrupted");
     zassert_true(f->initial_value * factor > 0, "product must be positive");
}
```

#### Declaring parameter values


Use `ZTEST_DEFINE_PARAM_VALUES` to create a static value set from
literal values:

```C

ZTEST_DEFINE_PARAM_VALUES(small_factors, int, 1, 2, 3);
```
For values already stored in an array use `ZTEST_DEFINE_PARAM_VALUES_ARRAY`:

```C

static const int big_factors[] = { 10, 100, 1000 };
ZTEST_DEFINE_PARAM_VALUES_ARRAY(big_factor_vals, big_factors);
```
For a numeric range use `ZTEST_DEFINE_PARAM_RANGE`, which mirrors
GoogleTest's `testing::Range(begin, end [, step])` semantics.  Values are
`{begin, begin+step, ...}` up to but **not** including `end`.  No backing
array is allocated, so large ranges have zero RAM overhead:

```C

/* {0, 2, 4, 6, 8} — 5 values, step is supplied explicitly */
ZTEST_DEFINE_PARAM_RANGE(even_vals, int, 0, 10, 2);

/* {1, 2, 3, 4, 5} — step=1 is the common case */
ZTEST_DEFINE_PARAM_RANGE(one_to_five, int, 1, 6, 1);
```

**Note:** `ZTEST_DEFINE_PARAM_RANGE` requires `end > begin` and `step > 0`, both enforced at compile time via `BUILD_ASSERT`.

For values that must be **computed at runtime** — for instance random numbers,
hardware sensor readings, or values produced by a custom algorithm — use
`ZTEST_DEFINE_PARAM_GENERATOR` or
`ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP`.  Both accept a
user-provided generator callback with the signature
`void gen(size_t index, void *out)` that writes one value per invocation.
Like ranges, no backing array is allocated.

The `_WITH_SETUP` variant additionally calls a `void setup(void)` hook
**once** before the dispatch loop.  This is the right place to seed a PRNG,
reset a stateful counter, or open any resource needed by the generator:

```C

#include <zephyr/random/random.h>

/* Seed the RNG before the first iteration so failures are reproducible. */
static void seed_rng(void)
{
     sys_rand_seed(MY_FUZZ_SEED);
}

static void rand_u32_gen(size_t idx, void *out)
{
     ARG_UNUSED(idx);
     *(uint32_t *)out = sys_rand32_get();
}

ZTEST_DEFINE_PARAM_GENERATOR_WITH_SETUP(fuzz_vals, uint32_t, MY_FUZZ_ITERATIONS,
                                        seed_rng, rand_u32_gen);
```
When no setup is needed, use the simpler form:

```C

static void deterministic_gen(size_t idx, void *out)
{
     /* Deterministic but computed at runtime (e.g. based on hardware ID). */
     *(uint32_t *)out = get_device_seed() ^ (uint32_t)idx;
}

ZTEST_DEFINE_PARAM_GENERATOR(hw_vals, uint32_t, 16U, deterministic_gen);
```

**Note:** The `count_` argument to both generator macros must be a constant expression (a numeric literal, a `#define`, or a Kconfig symbol such as `MY_FUZZ_ITERATIONS`).  Truly dynamic counts are not supported.

Struct-typed parameters work the same way:

```C

struct point { int x; int y; };

static const struct point corners[] = { {0,0}, {1,0}, {0,1}, {1,1} };
ZTEST_DEFINE_PARAM_VALUES_ARRAY(corner_vals, corners);

ZTEST_P(my_suite, test_in_unit_square)
{
     const struct point *p = ZTEST_GET_PARAM_PTR(struct point);
     zassert_true(p->x >= 0 && p->x <= 1 && p->y >= 0 && p->y <= 1,
                 "point (%d, %d) outside unit square", p->x, p->y);
}
```

#### Instantiating a parameterized test


`ZTEST_INSTANTIATE_TEST_SUITE_P` binds a value set to a test body.  Each
call creates a separate named instantiation; the same test body may be
instantiated multiple times with different value sets:

```C

ZTEST_INSTANTIATE_TEST_SUITE_P(small, my_suite, test_multiply, small_factors);
ZTEST_INSTANTIATE_TEST_SUITE_P(big,   my_suite, test_multiply, big_factor_vals);
```
The first argument (`small` / `big`) is an arbitrary unique identifier within
the compilation unit; it is recorded in the test metadata but does not affect test
naming as reported by Twister.


#### Retrieving the current parameter


Inside a `ZTEST_P` body the following helpers are available:


* - Helper
  - Description
* - `ztest_has_current_param()`
  - Returns `true` when called inside a parameterized invocation.
* - `ztest_get_current_param()`
  - Returns a `const void *` pointer to the current value.
* - `ZTEST_GET_PARAM_PTR(type)`
  - Returns a `const type *` pointer to the current value.
* - `ZTEST_GET_PARAM(type)`
  - Dereferences and returns the current value as `type`.
* - `ztest_get_current_param_index()`
  - Returns the zero-based index of the current value within its set.
* - `ztest_get_current_param_size()`
  - Returns the size in bytes of one parameter element.
Non-parameterized tests (`ZTEST`, `ZTEST_F`) always see
`ztest_has_current_param()` return `false` and `ztest_get_current_param()`
return `NULL`.


### Test result expectations


Some tests were made to be broken. In cases where the test is expected to fail or skip due to the
nature of the code, it's possible to annotate the test as such. For example:

```C

#include <zephyr/ztest.h>

ZTEST_SUITE(my_suite, NULL, NULL, NULL, NULL, NULL);

ZTEST_EXPECT_FAIL(my_suite, test_fail);
ZTEST(my_suite, test_fail)
{
  /** This will fail the test */
  zassert_true(false, NULL);
}

ZTEST_EXPECT_SKIP(my_suite, test_skip);
ZTEST(my_suite, test_skip)
{
  /** This will skip the test */
  zassume_true(false, NULL);
}
```
In this example, the above tests should be marked as failed and skipped respectively. Instead,
Ztest will mark both as passed due to the expectation.


### Test rules


Test rules are a way to run the same logic for every test and every suite. There are a lot of cases
where you might want to reset some state for every test in the binary (regardless of which suite is
currently running). As an example, this could be to reset mocks, reset emulators, flush the UART,
etc.:

```C

#include <zephyr/fff.h>
#include <zephyr/ztest.h>

#include "test_mocks.h"

DEFINE_FFF_GLOBALS;

DEFINE_FAKE_VOID_FUN(my_weak_func);

static void fff_reset_rule_before(const struct ztest_unit_test *test, void *fixture)
{
     ARG_UNUSED(test);
     ARG_UNUSED(fixture);

     RESET_FAKE(my_weak_func);
}

ZTEST_RULE(fff_reset_rule, fff_reset_rule_before, NULL);
```

### A custom `test_main`


While the Ztest framework provides a default `test_main` function, it's possible that some
applications will want to provide custom behavior. This is particularly true if there's some global
state that the tests depend on and that state either cannot be replicated or is difficult to
replicate without starting the process over. For example, one such state could be a power sequence.
Assuming there's a board with several steps in the power-on sequence a test suite can be written
using the `predicate` to control when it would run. In that case, the `test_main`
function can be written as follows:

```C

#include <zephyr/ztest.h>

#include "my_test.h"

void test_main(void)
{
     struct power_sequence_state state;

     /* Only suites that use a predicate checking for phase == PWR_PHASE_0 will run. */
     state.phase = PWR_PHASE_0;
     ztest_run_all(&state, false, 1, 1);

     /* Only suites that use a predicate checking for phase == PWR_PHASE_1 will run. */
     state.phase = PWR_PHASE_1;
     ztest_run_all(&state, false, 1, 1);

     /* Only suites that use a predicate checking for phase == PWR_PHASE_2 will run. */
     state.phase = PWR_PHASE_2;
     ztest_run_all(&state, false, 1, 1);

     /* Check that all the suites in this binary ran at least once. */
     ztest_verify_all_test_suites_ran();
}
```
The signature of `ztest_run_all` is
`ztest_run_all(const void *state, bool shuffle, int suite_iter, int case_iter)`:

* `state` - Pointer to the global state passed to each suite's `predicate`.
* `shuffle` - When `true`, randomize the order in which suites and tests run
  (requires `CONFIG_ZTEST_SHUFFLE`); `false` keeps the default
  alphanumerical order.
* `suite_iter` - Number of times to repeat each test suite.
* `case_iter` - Number of times to repeat each test case.

In the example above each call runs the matching suites once, in order, without
shuffling.
