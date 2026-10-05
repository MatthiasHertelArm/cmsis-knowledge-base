---
id: "devt-ctrace-multi-source-design-ownership-before-and-after"
type: "concept"
domain: "trace"
title: "ctrace multi-source design: Ownership before and after"
summary: "The common TraceEvent boundary already separated protocol decoding from output formats. Some semantic state was already partitioned by source. The migration made route identity explicit throughout that pipeline and removed the remaining single-input assumptions:"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/multi-source-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/multi-source-design.md#ownership-before-and-after"
license: "Apache-2.0"
mode: "V"
---

The common `TraceEvent` boundary already separated protocol decoding from output formats. Some semantic state was
already partitioned by source. The migration made route identity explicit throughout that pipeline and removed the
remaining single-input assumptions:

| Area | Before | After |
| --- | --- | --- |
| Raw frontend | Direct ITM session | One `DecodeTree`, with a single or formatted root |
| Protocol state | One ITM decoder | One ITM decoder per configured route |
| Transactions and recovery | Input-wide buffering and loss interval | Rollback, reset, and loss interval per route |
| Semantic state | Existing per-source post-decoders | Explicit normalized routes for timestamps and DWT pairing |
| CTF output | One writer and shared clock configuration | Bundle metadata plus writers and clocks per route |
| CSV output | One ordered writer | Same writer, retaining formatted source IDs |

Both input formats use the same tree ownership boundary. `SINGLE` connects one ITM decoder to a synthetic route;
`FRAME_FORMATTED` owns the deformatter and dispatches payload to configured ITM decoders. Moving SWO onto the tree
first made the established input path exercise the new session lifecycle before formatted decoding was enabled.
It also avoided maintaining two raw-input architectures with different error and lifetime behavior.

The tree session owns the OpenCSD components. Callback adapters, packet collectors, and error state outlive the tree
that refers to them. OpenCSD's alternate logger and live-tree registry use process-global state, so ctrace permits
only one live tree at a time and restores the previous logger after destroying it. Multi-source decoding remains
synchronous; it does not imply parallel tree execution or concurrent writes to CSV.

The resulting pipeline is:

```text
one raw file + normalized trace-run metadata
                  |
       DecodeTree SINGLE / FRAME_FORMATTED
                  |
        route-bound ITM protocol decoders
                  |
       independent Cortex-M semantic state
                  |
            TraceEvent flow
           /              \
   one combined CSV    one CTF bundle
                      metadata + stream_<id> files
```
