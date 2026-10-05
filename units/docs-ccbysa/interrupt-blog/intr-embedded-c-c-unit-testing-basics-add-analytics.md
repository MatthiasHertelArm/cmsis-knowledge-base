---
id: "intr-embedded-c-c-unit-testing-basics-add-analytics"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing Basics: Real World Unit Test Example / Add Analytics"
summary: "Our next requirement was to add analytics tracking how many times key/value pairs were written, read, and deleted. We can do this by simply calling a function analytics_inc which will increment the count of the given key by one."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-10-08-unit-testing-basics.md"
doc_source: "https://interrupt.memfault.com/blog/unit-testing-basics#add-analytics"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

Our next requirement was to add analytics tracking how many times key/value
pairs were written, read, and deleted. We can do this by simply calling a
function `analytics_inc` which will increment the count of the given key by one.
The additions to our source code are shown below:

```c
...
#include "analytics/analytics.h"

bool kv_store_write(const char *key, const void *val, uint32_t len) {
  ...
  analytics_inc(kSettingsFileWrite);
  return (rv == len);
}

bool kv_store_read(const char *key, void *buf,
                   uint32_t buf_len, uint32_t *len_read) {
  ...
  analytics_inc(kSettingsFileRead);
  return len;
}

bool kv_store_delete(const char *key) {
  ...
  analytics_inc(kSettingsFileDelete);
  return true;
}
```

If we run the test now, as usual, we will receive linker errors.

```
Linking build/kv_store/kv_store_tests
Undefined symbols for architecture x86_64:
  "_analytics_inc", referenced from:
      _kv_store_write in libkv_store.a(kv_store.o)
      _kv_store_read in libkv_store.a(kv_store.o)
      _kv_store_delete in libkv_store.a(kv_store.o)
```

Since this isn't a core functionality of the `kv_store` module, and it's likely
something we don't need to verify, we are going to provide a **stub** for this
function, rather than use the real implementation or a **fake**.

We can do that by creating a header called `stub_analytics.h`

```c
// Analytics Stub
#include "analytics/analytics.h"

void analytics_inc(eAnalyticsKey key) {
  return;
}
```

which we include in our unit test as shown below.

```c
extern "C" {
  ...
  #include "stubs/stub_analytics.h"
}
```

{:.no_toc}
