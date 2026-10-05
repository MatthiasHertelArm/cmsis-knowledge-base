---
id: "intr-embedded-c-c-unit-testing-basics-stubs-fakes-and-mocks"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Stubs, Fakes, and Mocks"
summary: "When starting to write unit tests, it is common to write alternate implementations to modules that make sense for a particular unit test."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#stubs-fakes-and-mocks"
license: "CC-BY-SA-4.0"
mode: "V"
---

When starting to write unit tests, it is common to write alternate
implementations to modules that make sense for a particular unit test.

Since unit tests will be run on the host machine, they won't have hardware, such
as an LED. But if a module within a unit test calls `Enable_LED()`, we could
instead have a virtual LED and a state boolean value saving whether the LED is
on or off.

These alternate implementations of modules have different types. Let's explain
them.

- **Fakes** are a working implementation, but will usually substitute their
  dependencies with something simpler and easier for a test environment.
  Example: an in-memory key/value store vs a NOR Flash backed Key/Value store.
- **Stubs** are a trivial implementation that returns canned values, generally
  always returning valid or invalid values.
- **Mocks** are an implementation that is controlled by the unit test. They can
  be pre-programmed with return values, check values of arguments, and help
  verify that functions are called.

After having worked at two software oriented hardware companies with 20+
firmware engineers each, my favorite way to organize the test directory is as
follows:

```
├── header_overrides
│   ├── string.h
│   └── error_codes.h
├── fakes
│   ├── fake_analytics.c
│   ├── fake_analytics.h
│   ├── fake_kv_store.c
│   ├── fake_mutex.c
│   └── fake_mutex.h
├── stubs
│   ├── stub_analytics.h
│   ├── stub_kv_store.h
│   └── stub_mutex.h
├── mocks
│   ├── mock_analytics.h
│   └── mock_kv_store.h
├── src
│   ├── AllTests.cpp
│   ├── test_kv_store.cpp
│   ├── test_littlefs_basic.cpp
│   └── test_littlefs_format.cpp
└── makefiles
    ├── Makefile_littlefs_basic.mk
    ├── Makefile_littlefs_format.mk
    └── Makefile_settings_file.mk
```

where

- **header_overrides/** - headers that override complex, auto-generated, or
  target specific headers.
- **src/** - The unit tests themselves.
- **makefiles/** - Makefiles to build the individual unit tests.

{:.no_toc}

### Stubs

These are used when the implementation of specific functions or their return
values do not matter to the module under test. They are primarily used to fix
the linker's `ld: symbol(s) not found` errors. These should generally have only
a return statement that always returns `true`, `false`, `0`, `NULL`, or whatever
makes sense in the context of the module.

If there is anything more complex than a return statement, consider implementing
a **Fake** instead.

Examples:

- Hardware or peripheral initialization functions since they have little
  relevance in testing on the host (x86 machine).
- A time module which returns the time of day (just return a random time).
- Mutex stubs when the locking or unlocking isn't being tested. (shown below)

```c
#include "mutex/mutex.h"

// Stubs

Mutex *mutex_create(void) {
  return NULL;
}

void mutex_lock(Mutex *mutex) {
  return;
}

void mutex_unlock(Mutex *mutex) {
  return;
}
```

{:.no_toc}

### Fakes

A **Fake** is commonly used in firmware where it is impractical to use the real
implementation for reasons such as:

- It requires specific hardware (flash chip, peripherals, LED's, etc.)

Examples:

- A mutex module which checks at the end of the test that all mutexes were
  properly unlocked (example provided later in the post).
- A RAM based NOR flash implementation, which flips bits from `1` to `0` when
  written to and requires "erasing" (flipping bits back to `1`) before writing
  new data.
- A RAM based key-value store (example shown below).

```c
#include "kv_store.h"

#include <inttypes.h>
#include <stdbool.h>

typedef struct {
  char *key;
  void *val;
  uint32_t len;
} KvEntry;

static KvEntry s_kv_store[256];

bool kv_store_write(const char *key, const void *val, uint32_t len) {
  // Write key/value into RAM store
}

bool kv_store_read(const char *key, void *buf,
                   uint32_t buf_len, uint32_t *len_read) {
  // Read key/value from RAM store into buffer
}

bool kv_store_delete(const char *key) {
  // Delete key/value from RAM store
}
```

{:.no_toc}

### Mocks

Mocks are incredibly useful if you want to declare each and every return value
of a given function. Using many mocks in a single unit test is also the easiest
way to test every single code path of the module under test, as you can force
any function to return error codes, NULL values, and invalid pointers.

These are the most powerful, provide the programmer the most control, and
isolate the module under test the best, but they are also the most cumbersome
and verbose to use, as every return value has to be pre-programmed.

Common mocking frameworks include:

- [CppUMock](https://cpputest.github.io/mocking_manual.html)
- [CMock](http://www.throwtheswitch.org/cmock)
- [Fake Function Framework (fff)](https://github.com/meekrosoft/fff) - _Although
  the name suggests it generates fakes implementations, they are actually mocks_

We are not going to cover examples of mocks and how to implement them (the topic
is big enough for another post), but some pseudo code is shown below to give an
understanding:

> Learn more about mocks in our separate post, [Unit Testing with
> Mocks](https://interrupt.memfault.com/blog/unit-test-mocking).

```c++

TEST(TestKvStore, Test_InitMutexCreated) {
  // On the next call to `my_malloc`, return the value `NULL`.
  MOCK_my_malloc.return_value = NULL;

  // This calls `my_malloc` in its implementation.
  void *buf = allocate_buffer();

  // Ensure that `my_malloc` was called once and only once.
  LONGS_EQUAL(1, MOCK_my_malloc.call_count);
  // Ensure that the buffer returned was indeed `NULL` since `my_malloc` returned `NULL`.
  POINTERS_EQUAL(NULL, buf);
}
```

Examples:

- A malloc implementation that can be pre-programmed with return values (return
  real buffers vs NULL).
- A mock flash driver which returns error codes and forces different paths in a
  higher level module.
- A Bluetooth socket implementation which is fed artfully crafted packed data to
  instrument protocols.

Later in this post, we will go over how to set up CppUTest to run these examples
by downloading the example code, as well as give some short instructions to how
to set up your own project to run unit tests.

For now, the concepts are more important than the framework and process used to
unit test firmware code.
