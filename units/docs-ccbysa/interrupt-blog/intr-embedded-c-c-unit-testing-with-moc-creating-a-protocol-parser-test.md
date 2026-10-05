---
id: "intr-embedded-c-c-unit-testing-with-moc-creating-a-protocol-parser-test"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: Real World Unit Test Example / Creating a Protocol Parser Test"
summary: "Even though we don't have any handlers defined in our source code, nor a way to actually plumb data in or out of the protocol in real life, we can do so in a unit test using mocks!"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#creating-a-protocol-parser-test"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

Even though we don't have any handlers defined in our source code, nor a way to
actually plumb data in or out of the protocol in real life, we can do so in a
unit test using mocks!

I won't be copying the full code into the blog post since most of it is
boilerplate, but please
[reference the source code on Github](https://github.com/memfault/interrupt/blob/master/example/unit-testing/complex/tests/src/test_protocol.cpp)
for more context.

First, let's write our test with no knowledge of mocking and see what happens.

```c++
static uint8_t s_resp_buffer[1024];
static const size_t s_resp_buffer_len = sizeof(s_resp_buffer);

TEST(TestProtocolParser, Hello) {
  const uint8_t in_bytes[] = {
      0xD2, 0x04, 0x00, 0x00, // Code (1234)
      0x04, 0x00, 0x00, 0x00, // Payload Size (4)
      0xFF, 0xFF, 0xFF, 0xFF, // Payload (junk)
  };

  size_t len = s_resp_buffer_len;
  eProtocolCode rv = protocol_handle(
      in_bytes, sizeof(in_bytes),
      s_resp_buffer, &len);

  CHECK_EQUAL(kProtocolCode_Ok, rv);
}
```

The memory buffer `in_buffer` matches our spec of code, size, and payload, and
we assert that the function returns a successful code.

However, if we try to compile this now, we get something like the following:

```
$ UNITTEST_MAKEFILE_FILTER="*protocol.mk" make
make -f interrupt/example/unit-testing/complex/tests/makefiles/Makefile_protocol.mk
compiling test_protocol.cpp
Linking build/protocol/protocol_tests
Undefined symbols for architecture x86_64:
  "_g_num_protocol_commands", referenced from:
      _protocol_handle in libprotocol.a(protocol.o)
  "_g_protocol_commands", referenced from:
      _protocol_handle in libprotocol.a(protocol.o)
ld: symbol(s) not found for architecture x86_64
```

Oops, we forgot to register a protocol handler function and implement it. Let's
define those above the test.

```c++

static void prv_command_hello(const uint8_t *buffer, size_t len,
    uint8_t *resp_buffer, size_t *resp_len) {
  // Ignore resp buffer, nothing to check
}

static const sProtocolCommand s_protocol_commands[] = {
  {1234, prv_command_hello},
};

const sProtocolCommand *const g_protocol_commands = s_protocol_commands;
const size_t g_num_protocol_commands = 1;
```

Now if we compile the test:

```
$ UNITTEST_MAKEFILE_FILTER="*protocol.mk" make
make -f interrupt/example/unit-testing/complex/tests/makefiles/Makefile_protocol.mk
compiling test_protocol.cpp
Linking build/protocol/protocol_tests
Running build/protocol/protocol_tests
.
OK (1 tests, 1 ran, 1 checks, 0 ignored, 0 filtered out, 0 ms)
```

The test compiles and runs successfully. Awesome! But we aren't done. Notice our
`prv_command_hello` function does nothing, and we aren't asserting that anything
happens other than the return value is `kProtocolCode_Ok`.
