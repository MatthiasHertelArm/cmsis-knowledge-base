---
id: "intr-embedded-c-c-unit-testing-basics-add-littlefs-implementation"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Real World Unit Test Example / Add littlefs Implementation"
summary: "Our requirement was that our kv_store implementation must use littlefs to store its data. At first, the task seems daunting! How are we supposed to write to a filesystem that doesn't exist on our host machine?"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#add-littlefs-implementation"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

Our requirement was that our `kv_store` implementation must use `littlefs` to
store its data. At first, the task seems daunting! How are we supposed to write
to a filesystem that doesn't exist on our host machine? Also, a filesystem is a
complicated piece of software!

Thankfully, `littlefs` includes an _emulated_ version of its filesystem which
runs directly on a PC. These source files are under `littlefs/emubd`, and we can
add them to our unit test to make a fully functional `littlefs` filesystem. In
this example, we can imagine that the `emubd` portion of `littlefs` is a fake.

The strategy we use to store various key/value pairs is that each `key` will be
a new filename under the `/kv` directory, and the value will be written as the
file data.

Let's try writing the source code!

```c
#define SETTINGS_DIR "/kv"

static char s_fname[256];
static lfs_file_t s_file;
static lfs_t *s_lfs_ptr;

static const char *prv_prefix_fname(const char *key) {
  snprintf(s_fname, sizeof(s_fname), "%s/%s", SETTINGS_DIR, key);
  return s_fname;
}

void kv_store_init(lfs_t *lfs) {
  s_lfs_ptr = lfs;
  lfs_mkdir(s_lfs_ptr, "/kv");
}

bool kv_store_write(const char *key, const void *val, uint32_t len) {
  lfs_file_open(s_lfs_ptr, &s_file, prv_prefix_fname(key), LFS_O_WRONLY | LFS_O_CREAT);
  uint32_t rv = lfs_file_write(s_lfs_ptr, &s_file, val, len);
  lfs_file_close(s_lfs_ptr, &s_file);
  return (rv == len);
}

bool kv_store_read(const char *key, void *buf,
                   uint32_t buf_len, uint32_t *len_read) {
  int rv = lfs_file_open(s_lfs_ptr, &s_file, prv_prefix_fname(key), LFS_O_RDONLY);
  if (rv < 0) {
    return false;
  }

  uint32_t len = lfs_file_size(s_lfs_ptr, &s_file);
  if (buf_len < len) {
    return false;
  }

  len = lfs_file_read(s_lfs_ptr, &s_file, buf, buf_len);
  lfs_file_close(s_lfs_ptr, &s_file);
  *len_read = len;
  return len;
}

bool kv_store_delete(const char *key) {
  lfs_remove(s_lfs_ptr, prv_prefix_fname(key));
  return true;
}
```

This is a reasonable start for our module. It could use more error checking, but
the basics are there. Let's test things out. One thing to note is that we'll
have to add the source files for `littlefs`, so we add those in our Makefile as
shown below. If we try to run the unit test without adding the source files, we
run into linker errors telling us that symbols are missing.

```
$ make
Linking build/kv_store/kv_store_tests
Undefined symbols for architecture x86_64:
  "_lfs_file_close", referenced from:
      _kv_store_write in libkv_store.a(kv_store.o)
      _kv_store_read in libkv_store.a(kv_store.o)
  "_lfs_file_open", referenced from:
      _kv_store_write in libkv_store.a(kv_store.o)
      _kv_store_read in libkv_store.a(kv_store.o)
  ...
```

We can simply add these source files to our compilation and then all should be
well. If these new files had dependencies of their own, we'd have to fix those
linker errors as well.

```
COMPONENT_NAME=kv_store

SRC_FILES = \
  $(PROJECT_SRC_DIR)/littlefs/lfs.c \
  $(PROJECT_SRC_DIR)/littlefs/lfs_util.c \
  $(PROJECT_SRC_DIR)/littlefs/emubd/lfs_emubd.c \
  $(PROJECT_SRC_DIR)/kv_store/kv_store.c \

TEST_SRC_FILES = \
  $(UNITTEST_SRC_DIR)/test_kv_store.c

include $(CPPUTEST_MAKFILE_INFRA)

```

{:.no_toc}
