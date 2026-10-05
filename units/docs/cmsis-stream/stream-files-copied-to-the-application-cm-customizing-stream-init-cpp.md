---
id: "stream-files-copied-to-the-application-cm-customizing-stream-init-cpp"
type: "concept"
domain: "cmsis-stream"
title: "Files copied to the application {#cmsis_stream_files_copied}: Customizing `stream_init.cpp`"
summary: "Include the generated scheduler header for each graph. The template contains a single example include such as scheduler_hello.h; replace it with the header generated from the Python graph description. For several graphs, include one generated scheduler header per graph."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/Doxygen/src/01_files_copied.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/Doxygen/src/01_files_copied.md#customizing-stream-init-cpp"
license: "Apache-2.0"
mode: "V"
---

Include the generated scheduler header for each graph. The template contains a
single example include such as `scheduler_hello.h`; replace it with the header
generated from the Python graph description. For several graphs, include one
generated scheduler header per graph.

Create one event queue per graph. The template stores them in `queue_app`, and
`stream_configure_and_start()` calls `stream_new_event_queue()` for each entry.
This model allows paused graphs to keep their own event queue while sharing the
runtime memory pools.

Add application hardware initialization before scheduler initialization. This
is where timers, sensors, displays, accelerators, audio interfaces, or other
drivers should be created and configured. Any handles or hardware parameters
needed by generated nodes should be stored in the application parameter
structures before the scheduler `init_scheduler_*` function is called.

Initialize every generated scheduler with the arguments expected by that graph.
The exact `init_scheduler_*` function name and argument list come from the
Python graph description. Some graphs use one parameter block, some use several
node-specific parameter blocks, and some use no parameter block.

For each graph, fill one `stream_execution_context_t` entry. The function
pointers must match the generated scheduler names:

- `scheduler_*`: dataflow scheduler function
- `reset_fifos_scheduler_*`: FIFO reset function
- `get_*_node`: local wrapper around the generated node lookup function
- `pause_scheduler_app` and `resume_scheduler_app`: helpers that visit
  identified nodes implementing `ContextSwitchInterface`

The `get_*_node` wrapper hides the application-specific `CStreamNode` type from
the shared runtime by returning `void *`. Add one wrapper per generated graph
when several graphs are present.

Adapt `pause_scheduler_app()` and `resume_scheduler_app()` when the application
extends `CStreamNode` with additional C-callable interfaces. The default
implementation only checks `ContextSwitchInterface` and calls `pause()` or
`resume()` on identified nodes that implement it.

Select the first graph to run with `currentNetwork`, call
`resume_scheduler_app(&contexts[currentNetwork])`, then start the runtime
threads with `stream_start_threads(&contexts[currentNetwork])`. This ordering
lets nodes publish initial events after their event queue exists.

Update `stream_free_all()` to free every resource allocated during startup.
The usual order is:

1. Wait for the runtime threads with `stream_wait_for_threads_end()`.
2. Call every generated `free_scheduler_*` function.
3. Delete the event queues.
4. Release shared runtime memory with `stream_free_memory()`.

If startup can fail midway, keep the error path consistent with the resources
already allocated by the application. Projects with more hardware resources may
need additional cleanup in the error path.
