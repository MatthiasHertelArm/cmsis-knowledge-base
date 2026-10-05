---
id: "intr-embedded-c-c-unit-testing-with-moc-real-world-unit-test-example"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: Real World Unit Test Example"
summary: "Throughout this post, we are going to build a way for a remote system (such as an iOS app) connected to the device over some transport (e.g."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#real-world-unit-test-example"
license: "CC-BY-SA-4.0"
mode: "V"
---

Throughout this post, we are going to build a way for a remote system (such as
an iOS app) connected to the device over some transport (e.g. BLE or serial) to
be able to read and write key/value pairs to and from the device's internal file
system.

This is likely a system that most embedded engineers have either built or worked
with.

Below is a diagram of our unit test stack, which looks similar to a real
device's end-to-end stack except for the fake NOR flash at the bottom.



Even though each module is linked to one another, they can be tested
individually and that's what we'll be doing today.

What this means in the context of a C/C++ project is that only the source files
of a **single module** will be included in a unit test. If we are testing a
module called `kv_store`, then a Makefile which compiles the unit test could
look something like this:

```
SRC_FILES = \
  $(PROJECT_SRC_DIR)/kv_store/kv_store.c \
  $(UNITTEST_ROOT)/mocks/mock_littlefs.cpp \
  $(UNITTEST_ROOT)/fakes/fake_mutex.c

TEST_SRC_FILES = \
  $(UNITTEST_SRC_DIR)/test_kv_store.cpp
```

Notice we aren't including a bunch of RTOS source files or LittleFS modules, but
rather fakes and mocks of each of those. This way, we ensure that we are only
testing a single module and the test is as simple as possible.

With this in mind, we can start building some new modules and unit tests using
mocks.

We'll be building upon the [Unit Testing
Basics](https://interrupt.memfault.com/blog/unit-testing-basics#real-world-unit-test-example)
example code. The green boxes shown above are modules we've already implemented
in the previous post, and the blue ones are the ones we'll be implementing
today.

Let's get started!
