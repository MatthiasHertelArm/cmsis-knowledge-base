---
id: "devt-ctrace-constraints-routing-invariants"
type: "concept"
domain: "trace"
title: "ctrace Constraints: Routing invariants"
summary: "ctrace Constraints: Routing invariants"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/constraints.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/constraints.md#routing-invariants"
license: "Apache-2.0"
mode: "V"
---

- Generated `ctrace-refs.stream` values are the routing authority. Processor `itm` references using a `[pname/]itm`
  path are the preferred route anchors. For compatibility with current pyTS output, only these reference-type and
  `[pname/]feature` pairs may establish a route without that anchor, and only when the reference supplies `stream`:
  `dwt` with a resolved `data#<index>`, `timestamps`, or `synchronization`; `itm` with `timestamps`; `exception` with
  `exceptions`; `event` or `pmu` with `events#<index>`; and `pcsample` with `pcsampling`. The optional `pname/` prefix
  is one path segment; nested feature paths are not fallbacks. `overflow`/`overflow` and `global_ts`/`timesync` may
  describe an established route but cannot establish one. A copied or enriched `ctrace-setup.itm.atbid` is tolerated
  but never creates, changes, or invalidates a route.
- Configured architectural Trace Bus IDs are restricted to `1` through `111` and bind one supported ITM protocol
  route each. DWT and PMU data travel on that processor's ITM route rather than creating separate decoders.
- Unformatted input has one synthetic route with no architectural Trace Bus ID. OpenCSD channel `0`, public stream
  selector `0`, and CTF stream-class ID `0` are compatibility representations of that route, not configured ATB ID 0.
- Formatted ID `0` is NULL/padding and creates no route, semantic event, CTF stream, or Trace Compass lane. A normal
  observed ID without a configured ITM route is diagnosed once and skipped without guessing its protocol.
  Skipped-byte Info may still expose the observed ID, including NULL/reserved IDs, without creating a decoded route.
- Normalized route identity, processor binding, timestamp prescaler, source metadata, errors, synchronization,
  overflow, and data-loss state remain route-local. ITM stimulus ports are restricted to `0` through `31`; port `0`
  is decoded for stream integrity but excluded from payload output.
