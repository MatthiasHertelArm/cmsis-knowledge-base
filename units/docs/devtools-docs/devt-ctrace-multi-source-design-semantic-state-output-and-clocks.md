---
id: "devt-ctrace-multi-source-design-semantic-state-output-and-clocks"
type: "concept"
domain: "trace"
title: "ctrace multi-source design: Semantic state, output, and clocks"
summary: "Each route owns its local timestamp, pending events, DWT correlation, overflow state, and timestamp quality. Processor names, source descriptions, and clock settings stay in normalized route metadata rather than being copied into every event."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/multi-source-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/multi-source-design.md#semantic-state-output-and-clocks"
license: "Apache-2.0"
mode: "V"
---

Each route owns its local timestamp, pending events, DWT correlation, overflow state, and timestamp quality.
Processor names, source descriptions, and clock settings stay in normalized route metadata rather than being copied
into every event. The route's ITM prescaler is applied once when raw ticks enter the semantic decoder; outputs consume
the resulting cycle values.

All routes are decoded even when output filters select only some of them. Synchronization, recovery, and CLI
diagnostics therefore remain complete. CSV retains one combined file in synchronous semantic callback order. Pending
events may be released by a later timestamp, so that order does not promise raw-byte order or a common chronology
across independent processors.

CTF uses one bundle-local metadata model, one shared trace UUID, and one writer per emitted formatted route. Each
writer owns its packet sequence and timestamp state. Source labels and DWT metadata are scoped by route, preventing
identical channel or comparator numbers on different processors from overwriting each other. Formatted writers are
created lazily after output selection; the eager legacy `stream_0` remains a compatibility exception.

Using a formatted Trace Bus ID as the CTF stream-class ID is a deliberate ctrace mapping. Neither that mapping nor
the filename `stream_<id>` defines a clock domain. Every stream references an explicit clock descriptor, and
independent domains receive distinct clock UUIDs even at equal frequencies. Frequency scales local cycles; it does
not establish a shared origin. Global Timestamp records alone do not establish cross-route synchronization.

CTF requires a valid configured frequency for each selected route. A missing or invalid clock disables CTF with an
Error while CSV or validation-only decoding can continue. Backend-specific requirements and failures remain
independent. The original implementation treated CTF metadata, stream files, and companion XML as one completion
and cleanup unit. Target-level XML now has an independent lifecycle, as recorded under
[revised decisions](#decisions-revised-after-the-migration).

The supported Trace Compass reader cannot safely combine independent clock declarations. Ctrace therefore emits
views for a bundle only when retained streams use one clock domain. Multi-clock CTF remains valid, but produces a
warning and contributes no XML views. Separate single-clock captures can now share a target XML while retaining
UUID-scoped identities; their clocks are not correlated or rebased.
