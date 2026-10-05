---
id: "intr-defensive-programming-friend-or-fo-offensive-programming-in-practice"
type: "concept"
domain: "debug"
title: "Defensive Programming - Friend or Foe?: Offensive Programming in Practice"
summary: "Let's dig into some concrete examples of bugs we can find using offensive programming practices."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-12-15-defensive-and-offensive-programming.md"
doc_source: "https://interrupt.memfault.com/blog/defensive-and-offensive-programming#offensive-programming-in-practice"
license: "CC-BY-SA-4.0"
mode: "V"
---

Let's dig into some concrete examples of bugs we can find using offensive
programming practices.

### Argument Validation

If a developer tries to use an API and passes invalid arguments into the
function, make sure the application yells at them to fix the issue. There is
nothing worse than receiving a `-1` return value and digging through 10 layers
of firmware code only to find out the real reason was that you passed in a
string of 20 characters when the maximum was 16 or because you accidentally
passed a null pointer due to an uninitialized variable.

```c
void device_set_name(char *name, size_t name_len) {
  ASSERT(name && name_len <= 16);
  ...
}
```

The only time I would choose, or at least heavily debate, to not use asserts to
validate arguments is when I am building a library that will be used by people
outside of my organization. In those cases, I would make the validation asserts
optional, just as FreeRTOS does with their RTOS functions by allowing developers
to define `configASSERT` themselves[^freertos_asserts].

### Resource Depletion

Although using dynamic memory in embedded systems is sometimes frowned upon, it
is often necessary for complex systems that don't have enough static memory to
go around. Even when dynamic memory is used, running out of memory should rarely
occur. When memory is low, systems should adapt and put back pressure on any
data flowing into the system and rate-limit memory-intensive operations.

However, if a firmware _does_ deplete the dynamic memory pool, we want to know
when and why it happened! It could be a memory leak or an accidental allocation
that consumed most of the heap. Running out of memory might not be a
show-stopping issue because the system _might_ recover, but if we are in the
development or internal testing phase, let's find out why we ran out!

To do this, we can add an assert inside of a `malloc()` function that verifies
that the call did not fail.

```c
void *malloc_assert(size_t n) {
  void *p = malloc(n)
  ASSERT(p);
  return p;
  ...
}
```

In code where the calls to `malloc()` should never fail, such as for the
allocation of RTOS primitives, request and response buffers, etc., we can use
this asserted version.

Another common issue with RTOS-based systems is a queue becoming full due to not
being processed quickly enough. As with memory depletion, this isn't a
show-stopping issue because the system might recover, but we could very well be
dropping events that are critical to the operation of the device! This is an
issue that should be investigated and ideally prevent from ever happening.

We can add an `ASSERT()` to confirm that each queue insertion succeeded, or
maybe even wrap that function if we want.

```c
void critical_event(void) {
  ...
  const bool success = xQueueSend(q, &item, 1000 /* wait 1s */)
  ASSERT(success);
  ...
}
```

To help with the debugging process of a queue full, I highly suggest writing a
[Python GDB
script](https://interrupt.memfault.com/blog/automate-debugging-with-gdb-python-api) to
dump the contents of the queue. Then, when the system is halted or you have a
core dump allowing you to find out what events were consuming the majority of
the space in the queue!

```
(gdb) queue_print s_event_queue
Queue Status: 10/10 events in queue (FULL!)
0: Addr: 0x200070c0, event: BLE_PACKET
1: Addr: 0x200070a8, event: TICK_EVENT
2: Addr: 0x20007088, event: BLE_PACKET
3: Addr: 0x20007070, event: BLE_PACKET
4: Addr: 0x20007050, event: BLE_PACKET
5: Addr: 0x20007038, event: BLE_PACKET
6: Addr: 0x20007018, event: BLE_PACKET
7: Addr: 0x20007000, event: BLE_PACKET
8: Addr: 0x20006fe0, event: BLE_PACKET
9: Addr: 0x20006fc8, event: BLE_PACKET
```

Looks like our queue was full of packets from our comms stack and we weren't
processing them quickly enough. We now know where the issue is and we can find a
solution.

### Software Stalls & Deadlocks

Embedded devices need to respond in a reasonable amount of time to user input
and communication packets all while being performant and not showing any signs
of lag or stalls.

I can't count the number of times while working on previous projects that slow
flash operations caused the system to freeze for 2-3 seconds at a time, wreaking
havoc on the user experience or causing other operations in the system to time
out. The worst part about these issues is that they often aren't brought to
developers' attention until it's too late.

To help catch these issues before pushing firmware to external users, you can
create and configure your [task
watchdogs](https://interrupt.memfault.com/blog/firmware-watchdog-best-practices#adding-a-task-watchdog)
to be more aggressive, set up timers to assert after a few seconds during
potentially long operations, and make sure to set timeouts on your threading
system calls.

To assert that a mutex was successfully locked, we can pass a timeout into most
RTOS calls and assert that it succeeded.

```c
void timing_sensitive_task(void) {
  // Task watchdog will assert a stall
  const bool success = mutex_lock(&s_mutex, 1000 /* 1 second */);
  ASSERT(success);
  {
    ...
  }
}
```

Or, if a [task
watchdog](https://interrupt.memfault.com/blog/firmware-watchdog-best-practices#adding-a-task-watchdog)
is configured to detect stalls, you can just wait indefinitely!

```c
void timing_sensitive_task(void) {
  // Task watchdog will assert a stall
  mutex_lock(&s_mutex, INFINITY);
  {
    ...
  }
}
```

Since a hiccup and stall here and there isn't the end of the world, when you
build the final image that you'll push to customers, you can either tune down or
(gasp!) remove these checks altogether.

### Use After Free Bugs

After a buffer allocated with `malloc()` is `free()`'ed, it should never be used
again by software. However, it happens all the time. This bug is aptly named a
"Use After Free" bug[^use-after-free]. If the system re-uses a buffer that was
freed, there's a good chance nothing bad will happen. The system will happily
use the buffer and write and read data from it.

However, sometimes, it will result in memory corruption and present itself in
the strangest of ways. Memory corruption bugs are notoriously difficult to
debug.


> If you are struggling with memory corruption issues, you might want to read
> [this section on catching memory corruption
> bugs](https://interrupt.memfault.com/blog/cortex-m-watchpoints#memory-corruption) from a
> previous post.


One way to help prevent use-after-free bugs is to scrub the entire contents of
the memory with an invalid address that, when accessed, would cause a
[HardFault](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug) on our Cortex-M4 and
ultimately halt the system or capture a core dump.

```c
void my_free(void *p) {
  const size_t num_bytes = prv_get_size(p);
  // Set each word to 0xbdbdbdbd
  memset(p, 0xbd, num_bytes);
  free(p);
}
```

When inspecting the core dump, the backtraces and buffer contents would show our
bad address `0xbdbdbdbd` and we'd immediately know that it was a "use after
free" bug.

### State Transition Errors

I'm assuming most state machine generators or best practices prevent state
transition errors from happening to begin with, but if that isn't the case, this
one is important and worth putting in your state machines.

Let's pretend we have two states, `kState_Flushing`, and `kState_Committing`,
where the commit happens after and only after a flush state. We can assert this
state change in our function as a sanity check.

```c
void on_commit(eState prev_state) {
  ASSERT(prev_state == kState_Flushing);
}
```

### Compile-Time Programmer Errors

Developers make mistakes all the time. One defense we can put in place against
ourselves is by using `static_assert`[^static_assert]. I commonly use this is to
make sure that my structs don't exceed a required size limit.

```c
typedef struct {
  uint32_t count;
  uint8_t buf[12];
  uint8_t new_value; // New field
} MyStruct;

_Static_assert(sizeof(MyStruct) <= 16, "Oops, too large!");
```

When I try to compile this, I get a compile time error assert:

```
$ gcc test.c
test.c:14:1: error: static_assert failed due to requirement
    'sizeof(MyStruct) <= 16' "Oops, too large!"

_Static_assert(sizeof(MyStruct) <= 16, "Oops, too large!");
^              ~~~~~~~~~~~~~~~~~~~~~~
1 error generated.
```

You can use this on anything that can be statically defined, including alignment
of struct fields, struct and enum sizes, and string lengths. Funny enough, I
also use this when I want to force myself and others to think twice about
certain changes. If I wanted to make sure that I or anyone else

```
_Static_assert(sizeof(MyStruct) == 16,
    "You are changing the size! "
    "Please refer to https://wiki.mycompany.com/... "
    "to learn how to update the protocol version ...");
```

Thankfully, those strings don't get included in the final firmware binary so you
are free to make them as long as you like!
