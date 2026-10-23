---
id: "devt-ctrace-architecture-suggested-code-reading-path"
type: "concept"
domain: "trace"
title: "ctrace Architecture: Suggested code-reading path"
summary: "This path follows one trace file through the system without requiring the build-target graph or every backend detail up front."
status: "draft"
collection: "devtools-docs"
source: "Open-CMSIS-Pack/devtools@6cb5a3c:tools/ctrace/docs/architecture.md"
doc_source: "https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/architecture.md#suggested-code-reading-path"
license: "Apache-2.0"
mode: "V"
---

1. Start at [`CtraceMain.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/../src/CtraceMain.cpp) for command-line handling and top-level error policy.
2. Follow [`TraceDirectoryJob.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/../src/control/TraceDirectoryJob.cpp) and
   [`TraceRunDiscovery.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/../src/tracerun/TraceRunDiscovery.cpp) to see how a solution set and YAML select all
   matching SWO/TB inputs, each with its own preflighted descriptor and file job.
3. Read [`FileDecodeJob.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/../src/control/FileDecodeJob.cpp) for output preflight, chunked input, pipeline
   construction, and finalization.
4. Continue through [`DecodePipeline.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/../src/decode/DecodePipeline.cpp),
   [`OpenCsdItmDecoder.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/../src/decode/OpenCsdItmDecoder.cpp),
   [`OpenCsdTreeSession.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/../src/decode/OpenCsdTreeSession.cpp), and
   [`CortexMStreamDecoder.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/../src/decode/CortexMStreamDecoder.cpp) for the tree, protocol, and semantic decode
   representations.
5. Use [`TraceEvent.h`](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/../src/model/TraceEvent.h) as the semantic contract between decoding and all consumers.
6. Finish with [`DecodeConsumers.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/../src/control/DecodeConsumers.cpp) and
   [`TraceOutputLifecycle.cpp`](https://github.com/Open-CMSIS-Pack/devtools/blob/6cb5a3c/tools/ctrace/docs/../src/output/TraceOutputLifecycle.cpp), then inspect either the CSV or CTF backend.

This path follows one trace file through the system without requiring the build-target graph or every backend detail
up front.
