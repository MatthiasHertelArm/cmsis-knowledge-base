---
id: "intr-embedded-c-c-unit-testing-with-moc-mocking-for-protocol-test"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: Real World Unit Test Example / Mocking for Protocol Test"
summary: "Since we only want to test the protocol parsing logic in protocol.c, this is a great time to use a mock. We can convert prv_command_hello into a CppUMock by modifying the body of the function."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#mocking-for-protocol-test"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

Since we only want to test the protocol parsing logic in `protocol.c`, this is a
great time to use a mock. We can convert `prv_command_hello` into a CppUMock by
modifying the body of the function.

```c++
static void prv_command_hello(const uint8_t *in_buffer, size_t in_len,
    uint8_t *resp_buffer, size_t *resp_len) {

  mock()
      .actualCall(__func__)
      .withParameter("len", in_len)
      .withMemoryBufferParameter("buffer", in_buffer, in_len);
  // Ignore resp buffer, nothing to check
}
```

By adding the `mock()...` call, we tell CppUMock that a particular function was
called with a parameter `len` of value `in_len` and memory buffer `buffer` with
a value and length of `in_buffer` and `in_len`. CppUMock records this call in
its internal book-keeping system, and then we can assert expectations on it!
Let's add this handling now.

```c++
TEST(TestProtocolParser, Hello) {
  const uint8_t in_bytes[] = {
      0xD2, 0x04, 0x00, 0x00, // Code (1234)
      0x04, 0x00, 0x00, 0x00, // Payload Size (4)
      0xFF, 0xFF, 0xFF, 0xFF, // Payload (junk)
  };

  const uint8_t payload_bytes[] = {
      0xFF, 0xFF, 0xFF, 0xFF, // Payload
  };

  mock()
      .expectOneCall("prv_command_hello")
      .withMemoryBufferParameter("buffer",
                                 payload_bytes,
                                 sizeof(payload_bytes))
      .withParameter("len", sizeof(payload_bytes))
      .ignoreOtherParameters();

  size_t len = s_resp_buffer_len;
  eProtocolCode rv = protocol_handle(
      in_bytes, sizeof(in_bytes),
      s_resp_buffer, &len);

  CHECK_EQUAL(kProtocolCode_Ok, rv);
  mock().checkExpectations();
}
```

We've added a `payload_bytes` buffer to confirm that `prv_command_hello`
receives this exact memory buffer, a `mock()...` call to set an expectation that
the handler is called in a particular way, and finally call
`mock().checkExpectations` to confirm that what we expect happened actually
happened.

If the call to `prv_command_hello` had not been called, or the call differed
from what we expected, then `mock().checkExpectations` would have produced an
error, such as the following:

```
interrupt/example/unit-testing/complex/tests/src/test_protocol.cpp:45:
    error: Failure in TEST(TestProtocolParser, Hello)

  Mock Failure: Unexpected call to function: prv_command_hello
  EXPECTED calls that did NOT happen:
    prv_command_hello -> const unsigned char* buffer: <Size = 4 | HexContents = FF FF FF FF>,
        unsigned long int len: <4 (0x4)>,
        other parameters are ignored
  ACTUAL calls that did happen (in call order):
    <none>
```

The above error is saying that our unit test expected a call to
`prv_command_hello` that did not happen.
