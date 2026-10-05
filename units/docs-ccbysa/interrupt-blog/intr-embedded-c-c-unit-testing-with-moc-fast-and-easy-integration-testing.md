---
id: "intr-embedded-c-c-unit-testing-with-moc-fast-and-easy-integration-testing"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: Fast and Easy Integration Testing"
summary: "In this post, we've taken extreme measures to ensure that we are only testing a single module's source code, with every other dependency being a stub, fake, or a mock, instead of the real implementation."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#fast-and-easy-integration-testing"
license: "CC-BY-SA-4.0"
mode: "V"
---

In this post, we've taken extreme measures to ensure that we are only testing a
single module's source code, with every other dependency being a stub, fake, or
a mock, instead of the real implementation. This is useful for testing the
correctness of each specific module, but it does not give us confidence that all
the modules will correctly work linked together.

The type of test that tests many modules as a group for interoperability is
called an **integration test**. These tests are usually left to QA or developer
self-testing. Another approach would be to do automated testing with an emulator
like [Renode](https://interrupt.memfault.com/blog/intro-to-renode).

However, wouldn't it be nice if we could do similar tests within our unit test
infrastructure? Yes it would!

Recall our protocol diagram which takes data from a remote device, writes
key/value pairs to flash, and provides responses.



Let's try to create a test that tests this end-to-end within a unit test
environment. Since we've already written unit tests for the Key/Value store with
LittleFS in our [previous post](https://interrupt.memfault.com/blog/unit-testing-basics),
we can use the same initialization routines and copy them into a new test.

The way I usually go about writing these tests is I first include all of the
source files in the Makefile that I think I'll need to include. In our
particular case, it looks something like:

```
COMPONENT_NAME=integration_protocol_kv_store

SRC_FILES = \
  $(PROJECT_SRC_DIR)/littlefs/lfs.c \
  $(PROJECT_SRC_DIR)/littlefs/lfs_util.c \
  $(PROJECT_SRC_DIR)/littlefs/emubd/lfs_emubd.c \
  $(PROJECT_SRC_DIR)/kv_store/kv_store.c \
  $(PROJECT_SRC_DIR)/protocol/protocol.c \
  $(PROJECT_SRC_DIR)/protocol/registry.c \
  $(PROJECT_SRC_DIR)/kv_store/kv_store_protocol_handlers.c \
  $(UNITTEST_ROOT)/fakes/fake_mutex.c \

TEST_SRC_FILES = \
  $(UNITTEST_SRC_DIR)/test_integration_protocol_kv_store.cpp

include $(CPPUTEST_MAKFILE_INFRA)
```

Note that I've included real implementations for everything my module needs
except for `fake_mutex.c`, since I do not want to include any RTOS primitives
into the unit test. It's not worth the hassle.

After including all of these, it's time to get everything initialized correctly,
since most of the modules will need some sort of `_init()` routine called.
Thankfully, this is was mostly done for us in our previous `test_kv_store.cpp`.

```c++
TEST_GROUP(TestIntegrationProtocolKvStore) {
  void setup() {
    fake_mutex_init();

    lfs_emubd_create(&cfg, "blocks");
    lfs_format(&lfs, &cfg);
    lfs_mount(&lfs, &cfg);

    kv_store_init(&lfs);
  }

  void teardown() {
    lfs_emubd_destroy(&cfg);
    lfs_unmount(&lfs);

    CHECK(fake_mutex_all_unlocked());
  }
};
```

Now it's time to write the real meat of the integration test. We'll test only
the protocol's **K/V Read** command.

```c++
static uint8_t s_resp_buffer[1024];
static const size_t s_resp_buffer_len = sizeof(s_resp_buffer);


TEST(TestIntegrationProtocolKvStore, Read) {
  // Raw input into the protocol
  const uint8_t in_bytes[] = {
      0xE8, 0x03, 0x00, 0x00,       // Code (1000)
      0x06, 0x00, 0x00, 0x00,       // Payload Size (6)
      'h', 'e', 'l', 'l', 'o', '\0' // Payload ("hello")
  };

  const uint8_t val_bytes[] = {
      'w', 'o', 'r', 'l', 'd'       // Payload
  };

  // Initialize the value in the K/V store
  bool success = kv_store_write("hello", val_bytes, sizeof(val_bytes));
  CHECK_TRUE(success);

  // Push the raw bytes into our protocol
  size_t len = s_resp_buffer_len;
  eProtocolCode rv = protocol_handle(
      in_bytes, sizeof(in_bytes),
      s_resp_buffer, &len);

  // Ensure we receive the correct response!
  CHECK_EQUAL(kProtocolCode_Ok, rv);
  MEMCMP_EQUAL(val_bytes, s_resp_buffer, sizeof(val_bytes));
}
```

We are passing in a set of raw bytes into our protocol handler, and essentially
letting it run its course. This data flows in and out of **five** layers of
code, as shown in our diagram, and eventually returns data to our unit test with
`s_resp_buffer`. We confirm the data is correct using CppUTest's `MEMCMP_EQUAL`
operation.

Feel free to check out the
[source code on Github](https://github.com/memfault/interrupt/blob/master/example/unit-testing/complex/tests/src/test_integration_protocol_kv_store.cpp)

> Do these integration tests give us the optimal 100% real-world test that QA or
> in-field testing provides? Of course not, but it gets us 90% of the way there
> which is infinitely better than nothing.

### Integration Tests in Practice

This type of integration test can give us embedded software developers a lot of
bang for our buck, but also cause frustration.

#### Benefits

- A large amount of code and logic can be tested using [continuous
  integration](https://interrupt.memfault.com/blog/continuous-integration-for-firmware)
- Ensuring correctness after a large refactor of a module that resides in the
  middle of an integration test becomes trivial.
- Enables short-staffed and budget-conscious teams to push out building a
  complex test automation system with real hardware using something like Robot
  Framework[^robot_framework].

#### Drawbacks

- Changing the API of a single commonly used module within integration tests
  will require updating all of those tests.
- They are susceptible to breaking in undefined ways since many source files are
  thrown into the same test.
- Integration tests are, in some ways, easier to write since they don't require
  new stub, fake, or mock files for each test that gets written. They might
  become the new normal, which would mean that each module would become less
  well tested and coverage of 100% might be more difficult to attain.

With the pros and cons taken into account, I can't argue with any amount of
testing, especially if it's fast, reliable, and tests the code in meaningful
ways. Even if I've battled a stale unit or integration test 2 years after it was
written, I reminded myself that I **would not** want to be testing it manually.
