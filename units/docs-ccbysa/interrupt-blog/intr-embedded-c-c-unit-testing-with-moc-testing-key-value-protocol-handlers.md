---
id: "intr-embedded-c-c-unit-testing-with-moc-testing-key-value-protocol-handlers"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: Real World Unit Test Example / Testing Key/Value Protocol Handlers"
summary: "We now need to test our above implementations using unit tests."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#testing-key-value-protocol-handlers"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

We now need to test our above implementations using unit tests.

In light of the amount of code in this post thus far, I'll keep it shorter here.
If you want to dive deeper, check out the source code to
[test_kv_store_protocol_handlers.cpp on Github](https://github.com/memfault/interrupt/blob/master/example/unit-testing/complex/tests/src/test_kv_store_protocol_handlers.cpp)

The only two external dependencies to `kv_store_protocol_handlers.c` are
`kv_store_read` and `kv_store_write`. We have a few options we could take.

If we included `kv_store.c` into our unit test build, we'd also have to provide
implementations for `kv_store.c` dependencies, which include LittleFS and
Mutexes. This is not what we want.

We could create a stub or fake for `kv_store_read` and `kv_store_write`. This
would allow us to compile our unit test, but we want to verify that these
functions were called with the correct arguments and values, so these aren't
ideal.

The last option, and the approach I took, was to write mock implementations for
`kv_store_read` and `kv_store_write` so that we could verify the argument and
return values.

Below is our mock implementation and unit test for `kv_store_read`:

```c++
bool kv_store_read(
    const char *key,
    void *buf,
    uint32_t buf_len,
    uint32_t *len_read) {
  return mock()
      .actualCall(__func__)
      .withStringParameter("key", key)
      .withOutputParameter("buf", buf)
      .withOutputParameter("len_read", len_read)
      .returnBoolValueOrDefault(true);
}

TEST(TestKvStoreProtocolHandlers, Read) {
  // Key: "hello"
  const uint8_t in_bytes[] = {
      'h', 'e', 'l', 'l', 'o', '\0' // Key
  };

  // Value: "world"
  const uint8_t out_bytes[] = {
      'w', 'o', 'r', 'l', 'd'
  };
  const uint32_t out_len = sizeof(out_bytes);

  mock()
      .expectOneCall("kv_store_read")
      .withStringParameter("key", "hello")
      .withOutputParameterReturning("buf", out_bytes, sizeof(out_bytes))
      .withOutputParameterReturning("len_read", &out_len, sizeof(out_len));

  kv_store_read_protocol_cmd(
      in_bytes, sizeof(in_bytes),
      s_resp_buffer, &s_resp_buffer_len);

  mock().checkExpectations();
  // Verify that our response buffer was correctly populated
  MEMCMP_EQUAL(out_bytes, s_resp_buffer, sizeof(out_bytes));
}
```

#### Adding and Testing Retry Logic

It's typical for code that deals with hardware to have a retry mechanism built
in. Testing this retry logic in code is usually cumbersome and generally
ignored, but I want to bring comfort and say that using mocks makes it easy!
Let's add a very simple retry loop around `kv_store_read` which retries the
operation 3 times.

```c++
// kv_store_protocol_handlers.c

void kv_store_read_protocol_cmd(
    const uint8_t *buffer, size_t len,
    uint8_t *resp_buffer, size_t *resp_len) {

  [...]

  bool success = false;
  int retries_left = 3;
  while (--retries_left >= 0) {
    success = kv_store_read(key, resp_buffer, (uint32_t)*resp_len, (uint32_t *)resp_len);
    if (success) {
      break;
    }
  }
}
```

Since we have mocked out `kv_store_read`, testing this retry logic is as simple
as adding a few more `expectCall` operations using CppUMock, where the first two
fail and the final one succeeds.

```c++
  // First, expect 2 failures
  mock()
      .expectNCalls(2, "kv_store_read")
      .withStringParameter("key", "hello")
      .withOutputParameterReturning("buf", out_bytes, sizeof(out_bytes))
      .withOutputParameterReturning("len_read", &out_len, sizeof(out_len))
      .andReturnValue(false);
  // On the third try, return a success
  mock()
      .expectOneCall("kv_store_read")
      .withStringParameter("key", "hello")
      .withOutputParameterReturning("buf", out_bytes, sizeof(out_bytes))
      .withOutputParameterReturning("len_read", &out_len, sizeof(out_len))
      .andReturnValue(true);

  // Should still pass!
  kv_store_read_protocol_cmd(
      in_bytes, sizeof(in_bytes),
      s_resp_buffer, &s_resp_buffer_len);
```

Retry logic and complimentary tests are critical for communication protocols and
stacks, and I highly recommend doing everything you can in the unit test phase
to verify correctness. Some of the most difficult bugs to investigate and fix
are those around BLE or Wi-Fi with devices half-way across the globe.
