---
id: "intr-using-asserts-in-embedded-systems-common-usages-of-asserts"
type: "concept"
domain: "debug"
title: "Using Asserts in Embedded Systems: Common Usages of Asserts"
summary: "Many assertions are application-specific, but we've got a few rules of thumbs on when you should use assertions. Below are some examples of when using assertions is a good idea."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-11-05-asserts-in-embedded-systems.md"
doc_source: "https://interrupt.memfault.com/blog/asserts-in-embedded-systems#common-usages-of-asserts"
license: "CC-BY-SA-4.0"
mode: "V"
---

Many assertions are application-specific, but we've got a few rules of thumbs on
when you should use assertions. Below are some examples of when using assertions
is a good idea.

### When malloc shouldn't fail

Dynamic memory allocation is common in embedded systems, especially in today's
Internet connected consumer electronics. These devices need to be able to
receive an influx of packets, use large HTTP buffers, and possibly load assets
or fonts into RAM for a user interface. Keeping around statically allocated
buffers for all of these functions would be wasteful, especially for the devices
that measure RAM in kilobytes. In these devices, dynamic memory allocation is a
must.

There are also places where malloc could fail, and where **it shouldn't**.

For example, let's give an example of dynamically allocated mutexes where malloc
should not fail.

```c
Mutex *mutex_create(void) {
  Mutex *mutex = malloc(sizeof(Mutex));
  ASSERT(mutex);
  mutex_init(mutex);

  return mutex;
}
```

This malloc **should never fail**. If it did, then it would mean the system is
out of heap space. If we didn't assert here, then the system would risk using an
unprotected resource.

On the contrary, there are cases where it is perfectly fine for malloc to fail,
such as when a surge of packets are received and the heap becomes exhausted. The
system should process the packets, free the memory, and then ask for more data.

### Invalid arguments passed into function

Argument checking is one of the best (and easiest) places to assert.

We can check for NULL pointers

```c
void handle_event(Event *evt) {
  ASSERT(evt);
  ...
}
```

or check sizes of buffers

```c
void read_packet(void *buf, size_t buf_len) {
  ASSERT(buf_len >= sizeof(Packet));
  memcpy(...)
}

```

or prevent silly operations.

```c
void *my_malloc(uint32_t n) {
  ASSERT(n < 131072);
  ...
}
```

All of the above examples above are **bugs** introduced by a developer and they
likely shouldn't be handled gracefully. The alternative is to return an error
code, and burden the developer with finding out _exactly_ where in the call
stack a particular argument check filed.

> It's not common to see asserts on arguments in vendor and library code, since
> they aren't in the business of crashing devices, but it is sometimes
> configurable on mature software. An example of configurable asserting in a
> library can be found in FreeRTOS, e.g. `xTaskCreateStatic`[^4]. In this
> function, `configASSERT` is used to check for non-null pointers, and if
> `configASSERT` is configured to a no-op, the code will still check those
> values later in the function and return an error if they are invalid.

### When undefined behavior is imminent

```c
typedef enum {
  EventType_A,
  EventType_B,
} EventType;

void handle_event(Event *evt) {
  ...
  switch (evt->type) {
    case EventType_A:
      // something
      break;
    case EventType_B:
      // something
      break;
    default:
      // shouldn't ever get here.
      // something is corrupted
      ASSERT(0);
  }
}
```

If we want to make this even more understandable for future developers who come
across this, something like the following can also be done.

```c
#define WTF ASSERT(0)


void handle_event(Event *evt) {
  ...
  switch (evt->type) {
    ...
    default:
      WTF;
  }
}
```

This makes it pretty obvious that anything that falls through to the `default:`
case is undefined behavior.

### RTOS API functions fail

Another great place to assert is when you expect certain system functions to
succeed, and if they don't, the system is in a bad state. Below is a snippet
where we assert if a mutex wasn't locked after a few seconds, which likely means
there is a deadlock somewhere else.

```c
int rv = xSemaphoreTake(s_mutex, sec_to_ticks(5));
ASSERT(rv == pdTRUE);
```

> WARNING: Do not place code which performs operations within an `ASSERT`, such
> as `ASSERT(pdTRUE == xSemaphoreTake(s_mutex, 0))`. Aside from it being bad
> practice, if a developer _were_ to disable asserts, this would cause undefined
> behavior.
