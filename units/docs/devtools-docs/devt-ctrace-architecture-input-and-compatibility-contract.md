---
id: "devt-ctrace-architecture-input-and-compatibility-contract"
type: "concept"
domain: "trace"
title: "ctrace Architecture: Input and compatibility contract"
summary: "Input selection and route binding belong to tracerun and complete before each input's decoder and output backends are constructed. Target-level XML preparation precedes these per-input jobs."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/architecture.md#input-and-compatibility-contract"
license: "Apache-2.0"
mode: "V"
---

Input selection and route binding belong to `tracerun` and complete before each input's decoder and output backends
are constructed. Target-level XML preparation precedes these per-input jobs.
The provisional, ctrace-private `trace-format` declaration describes effective capture bytes rather than target
capability or file identity. Discovery collects every matching SWO, TB, and named-TB input, independently of whether
the format is declared. Each input is preflighted and normalized separately. An explicit format applies to every input;
otherwise SWO defaults to `unformatted` and TB or named-TB to `formatted`. The format is resolved before
`CtraceRunMeta` normalizes that input's routes, so the decoder and route model use the same effective format. This
channel-based heuristic does not inspect capture bytes. Framing remains an internal decoder contract.

The [input constraints](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/constraints.md#input-format-framing-and-discovery) define the accepted declarations, defaults,
file candidates, and framing limits. The [routing invariants](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/constraints.md#routing-invariants) define reference
binding, valid IDs, and the synthetic unformatted route; backends preserve its legacy output representation.
