---
id: "intr-embedded-c-c-unit-testing-basics-basic-implementation-of-key-value-store"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Real World Unit Test Example / Basic Implementation of Key/Value Store"
summary: "Below is our first attempt at kv_store.c which is the skeleton of our file."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#basic-implementation-of-key-value-store"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

Below is our first attempt at `kv_store.c` which is the skeleton of our file.

```c
#include "kv_store.h"
#include <inttypes.h>
#include "lfs.h"

void kv_store_init(lfs_t *lfs) {
}

bool kv_store_write(const char *key, const void *val, uint32_t len) {
  return true;
}

bool kv_store_read(const char *key, void *buf,
                   uint32_t buf_len, uint32_t *len_read) {
  return true;
}

bool kv_store_delete(const char *key) {
  return true;
}
```

Believe it or not, we are ready to create a unit test to test that things are
working. It's usually easier to write a unit test earlier rather than later
since the number of dependencies can grow out of hand quickly.

Below is a unit test which we mainly create to test compilation and the harness.

```c++
#include "CppUTest/TestHarness.h"

extern "C" {
  #include "kv_store/kv_store.h"
}

TEST_GROUP(TestKvStore) {
  void setup() {
  }

  void teardown() {
  }
};

TEST(TestKvStore, Test_SimpleKvStore) {
  // Just make sure that our file is hooked up
  LONGS_EQUAL(true, kv_store_read(NULL, NULL, 0, NULL));
}
```

Let's run the test and see what prints!

```
$ cd complex/tests
$ make
compiling kv_store.c
Building archive build/kv_store/lib/libkv_store.a
Linking build/kv_store/kv_store_tests
Running build/kv_store/kv_store_tests
.
OK (1 tests, 1 ran, 1 checks, 0 ignored, 0 filtered out, 1 ms)
```

Looks like our test passes and we are ready to move onto a (more) realistic
test.

{:.no_toc}
