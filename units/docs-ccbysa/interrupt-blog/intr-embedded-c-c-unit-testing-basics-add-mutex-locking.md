---
id: "intr-embedded-c-c-unit-testing-basics-add-mutex-locking"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Real World Unit Test Example / Add Mutex Locking"
summary: "Almost done! We've also been advised to add locking around our filesystem calls to ensure that only one client can read and write to the /kv directory at one time."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#add-mutex-locking"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

Almost done! We've also been advised to add locking around our filesystem calls
to ensure that only one client can read and write to the `/kv` directory at one
time.

In our implementation, we add `mutex_lock()` and a `mutex_unlock()` at the start
of the function and just before the `analytics_inc` calls respectively.

```c
#include "mutex/mutex.h"

static Mutex *s_mutex;

void kv_store_init(lfs_t *lfs) {
  ...
  s_mutex = mutex_create();
}

bool kv_store_write(const char *key, const void *val, uint32_t len) {
  mutex_lock(s_mutex); // New
  ...
  mutex_unlock(s_mutex); // New
  analytics_inc(kSettingsFileWrite);
  return (rv == len);
}

bool kv_store_read(const char *key, void *buf,
                   uint32_t buf_len, uint32_t *len_read) {
  mutex_lock(s_mutex); // New

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

  mutex_unlock(s_mutex); // New
  analytics_inc(kSettingsFileRead);
  return true;
}

bool kv_store_delete(const char *key) {
  mutex_lock(s_mutex); // New
  ...
  mutex_unlock(s_mutex); // New
  analytics_inc(kSettingsFileDelete);
  return true;
}
```

If we run our test now, we'll receive linker errors for the missing `mutex_*`
symbols. Since mutexes are rather important to this module, and we wouldn't want
to forget to unlock a mutex, we are going to try writing a **fake** mutex
implementation instead of a **stub**.

{:.no_toc}
