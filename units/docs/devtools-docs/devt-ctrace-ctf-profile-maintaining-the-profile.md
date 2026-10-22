---
id: "devt-ctrace-ctf-profile-maintaining-the-profile"
type: "concept"
domain: "trace"
title: "ctrace CTF profile: Maintaining the profile"
summary: "The primary implementation sources are OutputRequirements.cpp, CtfSchema.h, CtfMetadataModel.cpp, CtfMetadataWriter.cpp, CtfEncoder.cpp, CtfStreamWriter.cpp, CtfBundleOutput.cpp, TraceCompassXmlOutput.cpp, and TraceCompassXmlWriter.cpp."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@5f04db7:tools/ctrace/docs/ctf-format.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/ctf-format.md#maintaining-the-profile"
license: "Apache-2.0"
mode: "V"
---

The primary implementation sources are [`OutputRequirements.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../src/output/OutputRequirements.cpp),
[`CtfSchema.h`](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../src/output/ctf/CtfSchema.h),
[`CtfMetadataModel.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../src/output/ctf/CtfMetadataModel.cpp),
[`CtfMetadataWriter.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../src/output/ctf/CtfMetadataWriter.cpp),
[`CtfEncoder.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../src/output/ctf/CtfEncoder.cpp),
[`CtfStreamWriter.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../src/output/ctf/CtfStreamWriter.cpp),
[`CtfBundleOutput.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../src/output/ctf/CtfBundleOutput.cpp),
[`TraceCompassXmlOutput.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../src/output/ctf/TraceCompassXmlOutput.cpp), and
[`TraceCompassXmlWriter.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/5f04db7/tools/ctrace/docs/../src/output/ctf/TraceCompassXmlWriter.cpp).

The data-driven XML shape is an approved compatibility refinement of the former eager legacy XML: only graphical
topics observed in completed output create views. Target-level aggregation additionally scopes views by clock UUID
and Trace Bus ID. XML-shape changes must update focused XML tests, review and update the golden plus its
fixture-manifest hash, and
re-run the external Trace Compass acceptance.

Changes to an event ID, name, type, field, enum value, or interpretation must update this document and the relevant
metadata, encoder, Trace Compass, and CTF decoding tests together. Compatibility-impacting changes must also review
`cmsis_ctf_profile_version`.
