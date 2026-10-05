---
id: "devt-ctrace-multi-source-design-input-and-route-identity"
type: "concept"
domain: "trace"
title: "ctrace multi-source design: Input and route identity"
summary: "Input format describes the effective capture bytes. A single source can be formatted, and a sink's name does not prove how its formatter was configured. The migration introduced the provisional, ctrace-private ctrace-run.trace-format field and an internal 16-byte memory-aligned framing contract."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@30f5e817:tools/ctrace/docs/multi-source-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/multi-source-design.md#input-and-route-identity"
license: "Apache-2.0"
mode: "V"
---

Input format describes the effective capture bytes. A single source can be formatted, and a sink's name does not
prove how its formatter was configured. The migration introduced the provisional, ctrace-private
`ctrace-run.trace-format` field and an internal 16-byte memory-aligned framing contract. It did not introduce
byte-pattern detection or a public `trace-framing` field. The discovery defaults were subsequently revised, as recorded
below. The format field remains a temporary override, not a field awaiting standardization. The current
[trace proposal](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/pull/699) keeps formatter configuration with trace
communication rather than trace-source setup.

Generated `ctrace-refs.stream` assignments are the routing authority. Copied target setup, including an optional
`itm.atbid`, cannot replace effective generated routing information. Processor-ITM references are the preferred route
anchors; a constrained feature-reference fallback accommodates existing producer output. The full normalization rules
remain in the [routing constraints](https://github.com/Open-CMSIS-Pack/devtools/blob/30f5e817/tools/ctrace/docs/constraints.md#routing-invariants).

Four identities have separate purposes:

| Identity | Purpose |
| --- | --- |
| Normalized route | Associates decoder state, semantic events, and configuration |
| Trace Bus ID | Routes payload in formatted CoreSight input |
| Processor binding | Supplies processor-specific metadata and display labels |
| CTF stream-class ID | Identifies records and declarations within an output bundle |

Configured formatted ITM IDs are `1..111`. Formatter ID `0` is NULL/padding, not another decoder route. Unformatted
input carries no architectural ID: its synthetic route uses OpenCSD channel `0`, an empty CSV `stream`, and the
legacy CTF stream-class ID `0`. These representations do not turn it into CoreSight source ID `0`.

An observed formatter ID without a configured ITM route is diagnosed and skipped. Its presence cannot establish
whether its bytes contain ITM or an instruction-trace protocol. This keeps unsupported sources from corrupting
supported routes. The original plan deferred simultaneous raw inputs and anticipated extending route identity with
input identity because different formatter domains can reuse the same Trace Bus ID. The later independent-file
processing described below keeps these domains separate through per-input jobs and outputs.
