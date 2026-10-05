---
id: "cda-troubleshooting-python-debug-sessi-generators-async-code-and-threads"
type: "concept"
domain: "debug"
title: "Troubleshooting Python debug sessions: Generators, async code and threads"
summary: "Troubleshooting Python debug sessions: Generators, async code and threads"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@7db44ba:docs/agent-resources/troubleshooting/python.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/python.md#generators-async-code-and-threads"
license: "Apache-2.0"
mode: "V"
---

- Calling a generator function, or an `async def` function without awaiting it, only creates an object; the body runs later, when something iterates or awaits it. `step_into` on such a line does not enter the body: break inside the body and `continue_execution`.
- `step_over` on an `await` or a `yield` ends on the next line of the same coroutine or generator once it resumes. Other code runs in between, and a breakpoint it reaches stops the program first.
- `step_out` inside a generator or coroutine waits until its body has finished; a `yield` or an `await` does not count as leaving it. To get back to the consumer sooner, break there and continue.
- The tasks of one event loop share a thread, so `get_threads` cannot tell them apart. Stopped inside a coroutine, evaluate `__import__('asyncio').current_task()` to see which task it is.
- At a stop the other threads are held as well. `get_threads` lists them, and `get_call_stack` with a `threadId` shows where one of them is; for a hang, `pause_execution` first.
