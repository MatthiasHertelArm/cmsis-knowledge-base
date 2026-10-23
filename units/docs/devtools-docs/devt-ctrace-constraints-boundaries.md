---
id: "devt-ctrace-constraints-boundaries"
type: "concept"
domain: "trace"
title: "ctrace Constraints: Boundaries"
summary: "ctrace Constraints: Boundaries"
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/constraints.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/constraints.md#boundaries"
license: "Apache-2.0"
mode: "V"
---

- OpenCSD types remain inside the decode layer. Other modules and output backends consume semantic `TraceEvent`
  values, `TraceByteSkip` input annotations without a decoded route or clock, and input-wide `TraceDecodeAbort`
  finalization context.
- An OpenCSD API migration must retain access to typed ITM configuration and packet data and must preserve every
  structured decoder error from each data-path operation; falling back to only the last error or formatted log text
  would change recovery behavior.
- YAML types remain inside the trace-run reader. The rest of ctrace consumes normalized configuration and metadata.
- The YAML reader ignores unrelated fields. Structural and routing fields required to construct the normalized
  configuration are validated while reading or normalizing; malformed consumed values remain errors. Optional null
  scalars and null collection entries are read as absent wherever their schema permits it, while presence-only nodes
  retain their defined flag semantics. Backend-dependent values such as `timestamps.clock` and DWT `address`,
  `data-type`, and `size` retain parse failures for later validation. CTF preflight reports them only when the
  corresponding route or DWT source is selected; absence remains valid where the field is optional. Defaults and
  other operation-specific requirements are likewise evaluated after reading. Missing or null
  `ctrace-setup.itm.enable` is absent; a malformed enable value bound to an active route is an Error. Conflicting valid
  masks on one route produce one Warning and disable that route's optional received-on-disabled-channel check. An ITM
  reference without `index` values is valid and contributes no source events. The `index` field accepts a scalar or
  array of ITM channel or DWT comparator numbers. Unconsumed fields are ignored without validation or diagnostics.
- DWT data metadata comes from reference-level `address`, `size`, and `data-type`. When reference `size` is absent,
  the referenced `ctrace-setup.data.size` supplies it. DWT instruction-control references may bind a processor stream
  but do not create decoded data-source routes.
- Backend-specific requirements and failures remain independent; requesting CTF must not disable otherwise valid CSV
  output, or vice versa.
