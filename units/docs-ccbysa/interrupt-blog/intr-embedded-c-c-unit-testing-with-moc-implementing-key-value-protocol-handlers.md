---
id: "intr-embedded-c-c-unit-testing-with-moc-implementing-key-value-protocol-handlers"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: Real World Unit Test Example / Implementing Key/Value Protocol Handlers"
summary: "Thus far, we've only implemented a mock protocol handler. Our goal is to build a key/value protocol handler that will read and write values. Let's build the read and write handlers now in a file called kv_store_protocol_handlers.c"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#implementing-key-value-protocol-handlers"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

Thus far, we've only implemented a mock protocol handler. Our goal is to build a
key/value protocol handler that will read and write values. Let's build the read
and write handlers now in a file called `kv_store_protocol_handlers.c`

```c++
// kv_store_protocol_handlers.c

void kv_store_read_protocol_cmd(
    const uint8_t *buffer, size_t len,
    uint8_t *resp_buffer, size_t *resp_len) {

  // Forgo error checking for simplicity
  const char *key = (char *)buffer;
  // Simply read the value into the resp_buffer
  kv_store_read(key, resp_buffer, (uint32_t)*resp_len, (uint32_t *)resp_len);
}

void kv_store_write_protocol_cmd(
    const uint8_t *buffer, size_t len,
    uint8_t *resp_buffer, size_t *resp_len) {

  // Buffer should be in format:
  // <key_bytes>\0<value_bytes>

  // Forgo error checking for simplicity
  const char *key = (char *)buffer;
  size_t key_len = strlen(key);

  // Compute val_ptr and val_len. 1 is the \0 char
  const uint8_t *val_ptr = buffer + key_len + 1;
  const size_t val_len = len - key_len - 1;

  kv_store_write(key, val_ptr, val_len);
  // Write an ACK of sorts
  *resp_buffer = 1;
  *resp_len = 1;
}
```

The read handler is simple. We can just cast the buffer to the key, and read the
data back into the response buffer and we're all set.

The write handler is a bit more complicated, but still relatively simple. The
only tricky part is splitting the key and value parts of the data buffer.
