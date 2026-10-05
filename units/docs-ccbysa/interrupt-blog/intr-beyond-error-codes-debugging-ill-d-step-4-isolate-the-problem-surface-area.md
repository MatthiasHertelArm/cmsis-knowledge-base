---
id: "intr-beyond-error-codes-debugging-ill-d-step-4-isolate-the-problem-surface-area"
type: "concept"
domain: "debug"
title: "Beyond Error Codes - Debugging Ill-Defined Problems: Steps / Step 4 - Isolate the Problem Surface Area with Logging and/or Debugging"
summary: "This step aims to isolate where the problem occurs to the smallest possible piece of code. I don't say \"line of code\" here because sometimes problems (especially related to stack/heap corruption) don't happen in the same place each time."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2025-04-18-debugging-steps.md"
doc_source: "https://interrupt.memfault.com/blog/debugging-steps#step-4-isolate-the-problem-surface-area-with-logging-and-or-debugging"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Steps_

This step aims to isolate where the problem occurs to the smallest possible
piece of code. I don't say "line of code" here because sometimes problems
(especially related to stack/heap corruption) don't happen in the same place
each time. Firmware is often quite dynamic, responding to stimuli from the
outside world. Here, we are trying to remove as many changing variables as
possible. Ideally, we want to be able to reproduce the fault in the same place
and the same way each time.

Methods to accomplish this can include:

- Adding log statements before/after the suspected fault area, moving them
  closer and closer together until the offending code is isolated
- Attaching a debugger and seeing if you can generate the fault while "stepping
  through" code
- Simplifying/mocking certain aspects of your firmware to make runs more
  repeatable (for instance, fixing a sensor to a specific value or set of
  values)
- For problems that only happen sporadically, setting up as much logging as you
  can surrounding the suspect code (state of the system, state of variables,
  etc.) and letting your firmware run overnight can help catch the issue. It
  must be noted that Memfault's entire platform is dedicated to catching errors
  like these in shipped products! With cloud connected devices, you wouldn't
  even need a debugger connected as core dumps are automatically uploaded for
  later analysis.

Don't feel discouraged if you've completed this step and you _still_ don't quite
understand what's happening. For example, you may know that a bad memory access
occurs at a specific function call in your program. But you still have no idea
_why_ it's occurring. You might even call this function elsewhere, and it
_doesn't_ generate a fault!

Now that you've hopefully isolated more or less where the error is occurring, we
can start to dig into more subtle and nuanced potential root causes.
