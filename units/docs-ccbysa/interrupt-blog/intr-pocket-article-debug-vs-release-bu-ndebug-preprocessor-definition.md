---
id: "intr-pocket-article-debug-vs-release-bu-ndebug-preprocessor-definition"
type: "concept"
domain: "debug"
title: "Pocket article: Debug vs. Release Builds Considered Harmful: `NDEBUG` preprocessor definition"
summary: "Often these Debug/Release builds will have some preprocessor-defined symbols such as:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-04-25-debug-vs-release-builds.md"
doc_source: "https://interrupt.memfault.com/blog/debug-vs-release-builds#ndebug-preprocessor-definition"
license: "CC-BY-SA-4.0"
mode: "V"
---

Often these Debug/Release builds will have some preprocessor-defined symbols
such as:

- `DEBUG=1` (debug enabled)
- `NDEBUG=0` (indicating this is NOT a non-debug build)

Usually these flags will be used to adjust some of the following features for
production builds:

1. Changing **log verbosity** (disabling DEBUG or INFO levels in production, to
   prevent unnecessary flash wear)
   - I'd recommend instead, sticking with the **production** level, and in
     exceptional cases (problematic device), upgrade to a more verbose level
     temporarily
   - Depending on the particular system, it may be preferable to adjust
     verbosity at runtime and keep the build the same. For example, leave
     WARNING and ERROR enabled by default, but allow increasing verbosity via a
     persistent on-device setting, or a temporary runtime flag.
   - Be especially wary of builds with different log verbosity- it can impact
     timing and memory usage _dramatically_!
2. Disabling an **"engineering interface"** (eg ssh or local serial console
   backdoor)
   - This can be a security requirement. An alternative is to build
     authentication into the engineering console, but this can be error prone so
     proceed cautiously.
   - Having the interface available (in an authenticated way) on production
     units can be extremely useful when diagnosing faulty customer units that
     have been returned for analysis!
3. Enabling **signed/encrypted builds**
   - Also very tricky! Best practice is to verify the
     signing/encryption implementation works throughout the development and test
     cycle, instead of causing surprises at the end (execute-in-place encryption
     too slow, key management not actually production ready, etc).
   - It might make the most sense to have a separate "development" key for
     signing/encrypting development builds. A key that is separate and has different
     security concerns than the production key.
4. Disabling **runtime asserts**
    - If your system can tolerate a reset due
   to an `ASSERT` condition, these are _stupendously_ valuable in production
   builds- see [this
   post](https://interrupt.memfault.com/blog/asserts-in-embedded-systems) for more
   details

I've seen the `DEBUG` flag used pretty aggressively to cut out entire subsystems
that aren't strictly required for production. This can cause a lot of confusion,
for example the following scenario:

1. Production test build encounters a problem
2. Engineer goes to retrieve logs, realizes the logging subsystem was entirely
   disabled in the "release" build
3. 😩

**Summary: it can be quite hazardous to allow splitting features based on
preprocessor flags, and should only be done if there's a strict requirement.
Recommendation is to only do it when generating builds from a CI server, if
absolutely necessary.**

I prefer feature-specific flags when necessary. This is less confusing than a
global `DEBUG` flag, and less likely to leak to other places:

```c
#if !defined(LOG_LEVEL)
#define LOG_LEVEL kLogLevel_Debug
#endif
```

A crucial thing to be mindful of is turning off watchdogs in your debug version.
Instead, it's strongly advised to insert `__asm("bkpt");` into the watchdog
handler. This will enable you to promptly debug any instances where a watchdog
is triggered during debugging.

Depending on the particular device, it may be necessary to add some GDB hooks
for halt + continue to temporarily disable/reset a watchdog peripheral, so it
doesn't trigger when single-stepping. Some chips (like STM32's) even have a
feature that pauses a watchdog for you when the chip is debugger halted, which
is great!
