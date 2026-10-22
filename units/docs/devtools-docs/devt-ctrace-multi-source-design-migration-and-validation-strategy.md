---
id: "devt-ctrace-multi-source-design-migration-and-validation-strategy"
type: "concept"
domain: "trace"
title: "ctrace multi-source design: Migration and validation strategy"
summary: "The implementation was staged so that clean multi-source decoding did not depend on unproven changes in every layer at once. Each stage retained a buildable implementation and the established single-source output checks."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/multi-source-design.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/multi-source-design.md#migration-and-validation-strategy"
license: "Apache-2.0"
mode: "V"
---

The implementation was staged so that clean multi-source decoding did not depend on unproven changes in every layer
at once. Each stage retained a buildable implementation and the established single-source output checks.

| Stage | Purpose |
| --- | --- |
| Baseline and input model | Freeze fixtures and goldens; normalize routes; preflight exactly one raw input |
| Semantic and output model | Make route identity explicit; isolate state; add CTF stream and clock descriptors |
| Multi-stream output | Validate independent CTF writers and metadata using direct semantic input |
| Common frontend | Migrate existing unformatted input to `DecodeTree(SINGLE)` |
| Formatted decoding | Enable clean memory-aligned input after consumers support multiple routes |
| Recovery and acceptance | Add route-local faults, then validate the complete CLI and external consumers |

Formatted input was rejected before decoder/output construction until its frontend was ready. Initial formatted
support treated protocol errors as input-fatal; local recovery followed only after transaction isolation and
deformatter-state preservation had dedicated tests.

The validation combined complementary evidence:

- Legacy SWO goldens protected CSV bytes and CTF/XML compatibility during the structural migration.
- The reconstructed [TB fixture](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../test/data/TB-Trace/README.md) preserved real interleaved hardware payload but
  documented ID changes and added synchronization. Its independent deformatter checked routing; it was not evidence
  for a producer's capture-export behavior.
- [Synthetic formatted fixtures](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../test/data/formatted-synthetic/README.md) covered event families absent from the
  hardware payload, boundary IDs, filtering, malformed packets, and per-route isolation.
- Fault tests exercised multiple callbacks, partial-frame delivery, continuous IDs, failed resets, missing clocks,
  and backend cleanup. Chunk boundaries were varied independently of protocol packets.
- Portable tests, 100% source-line coverage, branch review, and external consumer checks covered different failure modes.
  Babeltrace validated each clock's scaling; Trace Compass acceptance checked timestamps and graphical semantics.

Reproducible commands and supported consumer versions belong to the current
[integration-test documentation](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../test/integration/README.md), rather than frozen test counts or execution logs.
