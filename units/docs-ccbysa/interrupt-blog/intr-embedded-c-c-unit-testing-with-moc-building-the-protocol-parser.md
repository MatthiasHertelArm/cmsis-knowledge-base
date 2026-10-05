---
id: "intr-embedded-c-c-unit-testing-with-moc-building-the-protocol-parser"
type: "concept"
domain: "debug"
title: "Embedded C/C++ Unit Testing with Mocks: Real World Unit Test Example / Building the Protocol Parser"
summary: "We create a header, protocol.h, which contains a prototype for a function that will accept bytes structured in the way defined above, as well as error codes that the function may return."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-05-12-unit-test-mocking.md"
doc_source: "https://interrupt.memfault.com/blog/unit-test-mocking#building-the-protocol-parser"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Real World Unit Test Example_

We create a header, `protocol.h`, which contains a prototype for a function that
will accept bytes structured in the way defined above, as well as error codes
that the function may return. It also has two output arguments, `resp_buffer`
and `resp_len`, which is where we'll write the response bytes and response
length to.

```c
// protocol/protocol.h

#pragma once

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

typedef enum {
  kProtocolCode_Ok = 0,
  kProtocolCode_MalformedMsg = 1,
  kProtocolCode_CommandNotFound = 2,

  kProtocolCode_32bit = 0x7FFFFFFF,
} eProtocolCode;

eProtocolCode protocol_handle(
    const uint8_t *buffer, size_t len,
    uint8_t *resp_buffer, size_t *resp_len);
```

Although simple, it should work for our use-case. Let's build the
implementation.

```c
// protocol/protocol.c

#include "protocol/protocol.h"
#include "protocol/registry.h"

#include <stdbool.h>
#include <stddef.h>
#include <string.h>

eProtocolCode protocol_handle(
    const uint8_t *buffer, size_t len,
    uint8_t *resp_buffer, size_t *resp_len) {
  // Need at least a command and size
  if (len < 8) {
    return kProtocolCode_MalformedMsg;
  }
  uint8_t *iter = (void *)buffer;

  // Parse the desired command code
  uint32_t code = *(uint32_t *)(void *)iter;
  iter += sizeof(uint32_t);

  // Parse the payload size
  uint32_t payload_size = *(uint32_t *)(void *)iter;
  iter += sizeof(uint32_t);

  //
  // Here, we would pass our data to a protocol handler!
  //
}
```

Above, we take in a buffer and length, ensure we have 8 bytes for the command
and size pieces, and then parse them. Now, we need to build a way to register
commands in our system and then allow this function to call them based on the
**command** field.

We'll create another module to help register these commands, called the
`registry`.

```c
// registry.h

#pragma once

#include <stddef.h>

typedef void (*ProtocolHandler)(const uint8_t *buffer, size_t len,
    uint8_t *resp_buffer, size_t *resp_len);

typedef struct ProtocolCommand {
  uint32_t code;
  ProtocolHandler handler;
} sProtocolCommand;

extern const sProtocolCommand *const g_protocol_commands;
extern const size_t g_num_protocol_commands;
```

```c
// registry.c

#include "protocol/registry.h"
#include "protocol/handlers.h"

#include <stddef.h>

// Command that are registered, as:
//   <command_code>, <command_handler>
static const sProtocolCommand s_protocol_commands[] = {
  // This handler is defined in "protocol/handlers.h"
  {1, protocol_handler_hello},
};

// Define constants so the protocol module can read the command registry.
const sProtocolCommand *const g_protocol_commands = s_protocol_commands;
const size_t g_num_protocol_commands = 1;
```

Above, we defined a function pointer, `ProtocolHandler`, which accepts the
payload buffer and payload length, as well as a response buffer and length
output arguments. To register each command, we add an array element to the list
`s_protocol_commands`. When a command is received through our protocol, we'll
iterate over this list, look for a matching command code, and if we find one,
we'll call the handler.

The final piece we need is to write the code that iterates over these commands.
This will go into `protocol.c`.

```c
  ...
  //
  // Here, we would pass our data to a protocol handler!
  //

  // Find the right handler
  for (const sProtocolCommand *command = g_protocol_commands; \
    command < &g_protocol_commands[g_num_protocol_commands]; \
    ++command) {
    if (code == command->code) {
      command->handler(iter, len, resp_buffer, resp_len);
      return kProtocolCode_Ok;
    }
  }

  // Failed to find a command
  return kProtocolCode_CommandNotFound;
```

Whew, a lot of code, but we are done with the protocol parser and command
handling! Let's write some tests for it.
