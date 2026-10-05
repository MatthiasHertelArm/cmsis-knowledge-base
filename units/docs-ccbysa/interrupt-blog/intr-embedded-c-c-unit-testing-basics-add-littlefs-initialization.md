---
id: "intr-embedded-c-c-unit-testing-basics-add-littlefs-initialization"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Real World Unit Test Example / Add littlefs Initialization"
summary: "Just because we got the files to compile in our unit test does not mean littlefs will magically work. We need to initialize the filesystem and set up and tear it down before and after each test respectively."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#add-littlefs-initialization"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

Just because we got the files to compile in our unit test does not mean
`littlefs` will magically work. We need to initialize the filesystem and set up
and tear it down before and after each test respectively.

To learn how to do this, we can go to the existing `littlefs` tests directory
and take inspiration from the template and a basic file test, both linked below.

- [Template](https://github.com/ARMmbed/littlefs/blob/master/scripts/template.fmt)
- [Basic File Test](https://github.com/ARMmbed/littlefs/blob/master/tests/test_files.sh#L17-L34)

This ultimately results in the following changes necessary for the unit test
file.

```c++
extern "C" {
  ...
  #include "lfs.h"
  #include "emubd/lfs_emubd.h"

  // Contains lfs, cfg, variables with default configuration.
  #include "defs/lfs_default_config.h"
}

TEST_GROUP(TestKvStore) {
  void setup() {
    lfs_emubd_create(&cfg, "blocks");
    lfs_format(&lfs, &cfg);
    lfs_mount(&lfs, &cfg);

    kv_store_init(&lfs);
  }

  void teardown() {
    lfs_emubd_destroy(&cfg);
    lfs_unmount(&lfs);
  }
};
```

The unit test will now, at the _start_ of every test, create a directory called
`blocks/`, format and mount the filesystem there, and initialize the key/value
store, and at the end of the test, destroy and unmount the filesystem so the
next test starts with a clean environment.

Since we now have a filesystem backing our key/value store, we can write a
simple test!

```c++
TEST(TestKvStore, Test_SimpleKvStore) {
  bool success;

  const char *key = "hello";
  const char *val = "world";
  success = kv_store_write(key,  (void *)val, sizeof(val));
  CHECK(success);

  char buf[16];
  uint32_t read_len;
  success = kv_store_read(key, buf, sizeof(buf), &read_len);
  CHECK(success);
  STRCMP_EQUAL(val, buf);

  // Buffer length too short. Should return false.
  success = kv_store_read(key, buf, 0, &read_len);
  CHECK_FALSE(success);
}
```

This test writes a key "hello" with the value "world", reads the value stored at
key "hello" into a buffer, and compares it against the expected value "world".

We also check the failure case of `kv_store_read` by passing in a buffer that is
too small.

It passes! This means our `littlefs` was set up correctly, and that our initial
logic in `kv_store.c` was (mostly) correct.

{:.no_toc}
