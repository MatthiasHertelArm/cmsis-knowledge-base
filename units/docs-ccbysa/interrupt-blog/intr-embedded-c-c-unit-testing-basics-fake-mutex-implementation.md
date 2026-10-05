---
id: "intr-embedded-c-c-unit-testing-basics-fake-mutex-implementation"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Real World Unit Test Example / Fake Mutex Implementation"
summary: "The reason we chose to write a fake implementation for the mutex module is that we want to ensure that equal number of lock and unlock calls are made so that there are no bugs when we actually …"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#fake-mutex-implementation"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

The reason we chose to write a fake implementation for the mutex module is that
we want to ensure that equal number of `lock` and `unlock` calls are made so
that there are no bugs when we actually use the `kv_store` in a real
environment.

This may seem difficult, but it's rather easy. To create a fake, we create two
files, `fake_mutex.h`, and `fake_mutex.c`. The reason for both the `.h` and `.c`
files is because the fake implementation defines new functions that are only
relevant to using the fake in a unit test.

Here is most of the source code for `fake_mutex.c`.

```c
#define NUM_MUTEXES 256

typedef struct Mutex {
  uint8_t lock_count;
} Mutex;

static Mutex s_mutexes[NUM_MUTEXES];
static uint32_t s_mutex_index;

// Fake Helpers

void fake_mutex_init(void) {
  memset(s_mutexes, 0, sizeof(s_mutexes));
}

bool fake_mutex_all_unlocked(void) {
  for (int i = 0; i < NUM_MUTEXES; i++) {
    if (s_mutexes[i].lock_count > 0) {
      return false;
    }
  }
  return true;
}

// Implementation

Mutex *mutex_create(void) {
  assert(s_mutex_index < NUM_MUTEXES);
  return &s_mutexes[s_mutex_index++];
}

void mutex_lock(Mutex *mutex) {
  mutex->lock_count++;
}

void mutex_unlock(Mutex *mutex) {
  mutex->lock_count--;
}
```

Let's go over what the fake is doing.

- We allocate a large number (256) of mutex slots. Since we are running our test
  on a host, large allocations are fine. We have gigabytes of RAM, unlike the
  limited embedded counterparts.
- We define a new `typedef struct Mutex` type which only stores the
  `lock_count`. If the type `Mutex` was properly hidden within a `.c` file in
  the real implementation, this should work.
- `fake_mutex_init` resets the state of this module. This should be called in
  the `setup()` function of every unit test using this module. Otherwise, the
  state will be carried over _between_ tests, which isn't desired.
- `fake_mutex_all_unlocked` ensures that all mutexes are unlocked when called.
  We can call this manually or at the end of every test in the `teardown()`
  function.
- `mutex_create` allocates a slot for a new mutex in our array and returns this
  pointer to the client. Since the client only uses the `Mutex *` as an opaque
  type, it shouldn't matter that it's a fake `Mutex`.
- `mutex_lock` and `mutex_unlock` increment and decrement the lock count
  respectively.

Now we can use this fake in our unit test. After adding the source file to our
compilation scripts, we make the follow changes to the unit test.

```c++
TEST_GROUP(TestKvStore) {
  void setup() {
    fake_mutex_init();
    ...
  }

  void teardown() {
    ...
    CHECK(fake_mutex_all_unlocked());
  }
};
```

If we run our code above with the naive top/bottom mutex additions, we realize
quickly that we have a mistake. Our `fake_mutex_all_unlocked` check failed!

```
complex/tests/src/test_kv_store.cpp:42: error:
  Failure in TEST(TestKvStore, Test_SimpleKvStore)
complex/tests/src/test_kv_store.cpp:38: error:
  CHECK(fake_mutex_all_unlocked()) failed

.
Errors (1 failures, 1 tests, 1 ran, 5 checks, 0 ignored, 0 filtered out, 8 ms)
```

Looking back, hopefully the issue is obvious. We forgot to unlock on our failure
cases within `kv_store_read`. The follow change is necessary:

```c
if (rv < 0) {
    mutex_unlock(s_mutex);  // ADD
    return false;
  }

  uint32_t len = lfs_file_size(s_lfs_ptr, &s_file);
  if (buf_len < len) {
    mutex_unlock(s_mutex);  // ADD
    return false;
  }
```

Thankfully we wrote and used our fake mutex implementation, as deadlocks are the
worst to debug!

> If you do find that deadlocks are a constant issue, do check out
> [Memfault](https://memfault.com/?utm_source=interrupt&utm_medium=link&utm_campaign=unit-test).
> It will help you track them down easily.
