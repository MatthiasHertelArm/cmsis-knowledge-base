---
id: "intr-embedded-c-c-unit-testing-with-moc-c-c-mocking-libraries"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: C/C++ Mocking Libraries"
summary: "Here are the mocking libraries that I most commonly see used within embedded projects."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#c-c-mocking-libraries"
license: "CC-BY-SA-4.0"
mode: "V"
---

Here are the mocking libraries that I most commonly see used within embedded
projects.

- [CppUMock](https://cpputest.github.io/mocking_manual.html)
- [Fake Function Framework (fff)](https://github.com/meekrosoft/fff) - _Although
  the name suggests it generates fakes implementations, they are actually
  mocks_.
- [CMock](http://www.throwtheswitch.org/cmock)

There is one other frequently mentioned mocking library,
[cmocka](https://cmocka.org/), but I don't often see it in the embedded space.

As with the unit testing framework itself, it **does not** matter what mocking
library you choose. As long as it plugs into your build system and it makes
sense to you, use it.

If I had to recommend which one you should use, I would say use CppUMock (and
CppUTest) if you are starting from scratch, and if you just want a mocking
library to hook into your already existing setup, go with fff.

### CppUMock

CppUMock is the mocking library that is included with
[CppUTest](https://cpputest.github.io/), the popular C/C++ unit testing
framework that was used within the book Test Driven Development for Embedded C
by James W. Grenning[^tdd_book]. This is also the framework I find myself
reaching for most often, as it is full-featured, works with both C and C++, and
is the most configurable.

In the following example, we create a mock for `my_malloc` which should be
called by `allocate_buffer` so that we can validate that `allocate_buffer`
behaves correctly if `malloc` fails and succeeds.

```c
// The mock is written explicitly
void *my_malloc(size_t size) {
  mock()
      .actualCall(__func__)
      .withParameter("size", size);

  if (mock().hasReturnValue()) {
    return mock().returnPointerValue();
  }

  // Actually return a real buffer if a return
  // value isn't set
  return malloc(size);
}

TEST(TestAllocateBuffer, Test_AllocateBufferBasic) {
  // Set return value
  mock()
      .expectOneCall("my_malloc")
      .withParameter("size", 32)
      .andReturnValue(NULL);

  uint8_t *buf = allocate_buffer(32);

  // Validate expectations
  mock().checkExpectations();
  POINTERS_EQUAL(NULL, buf);

  // Get a real buffer we can write into
  // No expected return value will pass us a real buffer
  mock()
      .expectOneCall("my_malloc")
      .withParameter("size", 32)
  uint8_t *buf = allocate_buffer(32);
  CHECK(buf != NULL);
}
```

Notice above that since we define the mock `my_malloc` ourselves, we can add
extra functionality to it, such as returning a real malloc buffer when the
programmer doesn't explicitly set it to return `NULL`. With other mocking
libraries, this isn't easily achieved and will require allocating a buffer
before and setting that as a return value.

At first, I thought the verbosity of CppUMock was its primary weakness, but as I
explored the other alternatives, I realized it was actually its greatest
strength. Where fff heavily relies on macros and CMock relies on generating
mocks using Ruby, CppUMock mocks are just normal functions with some extra
book-keeping done using `expectCall` and `actualCall`.

When using CppUMock, if you have a few functions you are trying to mock out,
it's probably best to keep them defined in the test file, especially if you think
it's an isolated case. If you are mocking out a large number of functions, or
think it might be used by other teammates or in future tests, go ahead and move
it to its own file. Mocks can be easily generated for CppUMock using any of the
following tools: [CppUMockGen](https://github.com/jgonzalezdr/CppUMockGen),
[mockify](https://github.com/marco-m/mockify), or
[cpputest_mockify](https://github.com/kesyog/cpputest_mockify).

The [Memfault Firmware SDK](https://github.com/memfault/memfault-firmware-sdk)
has a good example of a dedicated mock file,
[mock_memfault_platform_debug_log.cpp](https://github.com/memfault/memfault-firmware-sdk/blob/master/tests/mocks/mock_memfault_platform_debug_log.cpp#L22-L34).
This is a mock for the logging system, which I feel is a neat example because it
allows the developer to assert on how `memfault_platform_log` was called but it
also prints the logs to standard out as one would expect.

### Fake Function Framework (fff)

[Fake Function Framework (fff)](https://github.com/meekrosoft/fff) is the
simplest way to get started with mocking. It is a header-only library which
makes it trivial to include in your project.

Below, we implement the same functionality as the example from the CppUMock
section.

```c
TEST(TestAllocateBuffer, Test_AllocateBufferBasic) {
  // Set return value
  MOCK_my_malloc.return_value = NULL;

  uint8_t *buf = allocate_buffer(32);

  // Validate expectations
  LONGS_EQUAL(1, MOCK_my_malloc.call_count);
  LONGS_EQUAL(MOCK_my_malloc.arg0_val, 32);
  POINTERS_EQUAL(NULL, buf);

  // Get a real buffer we can write into
  void *real_buf = malloc(32);
  MOCK_my_malloc.return_value = real_buf;
  uint8_t *buf = allocate_buffer(32);
  CHECK(buf != NULL);
}
```

The primary reason I choose not to use fff is because I find the use of the
macros difficult to understand at a glance. The CppUMock function chain calls
might be verbose, but they read like spoken word and are easy for anyone to
parachute into the codebase and easily grasp what is happening.

Here is
[an example](https://github.com/marel-keytech/openCANopen/blob/master/test/unit_sdo_req.c)
unit test file from the
[marel-keytech/openCANopen](https://github.com/marel-keytech/openCANopen)
project that uses fff as it's mocking library.

### CMock

CMock is a mocking library from the group behind
[ThrowTheSwitch.org](http://www.throwtheswitch.org/), which also makes the Unity
unit testing framework[^unity]. It is compatible with C and includes some
tooling around running and generating boilerplate for you given a set of header
files. The flow is similar to CppUMock in that you define your expectations
first and then call the implementation under test.

```c
TEST(TestAllocateBuffer, Test_AllocateBufferBasic) {
  // Set return value and expectation
  my_malloc_ExpectAndReturn(32, NULL);

  uint8_t *buf = allocate_buffer(32);

  // Validate expectations
  POINTERS_EQUAL(NULL, buf);

  // Get a real buffer we can write into
  void *real_buf = malloc(32);
  my_malloc_ExpectAndReturn(32, real_buf);
  uint8_t *buf = allocate_buffer(32);
  CHECK(buf != NULL);
}
```

The main reason I do not use the tools from ThrowTheSwitch is that they require
Ruby, and I haven't seen any significant number of embedded engineers or
projects in the wild using Ruby. With this in mind, I prefer to use other
frameworks and tools so that my team and I do not need to manage a Ruby
environment (alongside the usual GCC and Python environments).
