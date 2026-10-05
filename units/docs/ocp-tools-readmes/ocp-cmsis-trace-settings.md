---
id: "ocp-cmsis-trace-settings"
type: "concept"
domain: "trace"
title: "CMSIS Trace: Settings"
summary: "CMSIS Trace: Settings"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/cmsis-trace-extension@1aebf86:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-trace-extension/blob/1aebf86/README.md#settings"
license: "Apache-2.0"
mode: "V"
---

| Setting | Default | Description |
| --- | --- | --- |
| `cmsisTrace.executablePath` | `""` | Path to `cmsis-trace-decoder` or its `dist/cli.js`. Empty auto-detects. |
| `cmsisTrace.pyocdHost` | `127.0.0.1` | Host of the pyOCD raw SWO TCP server. |
| `cmsisTrace.pyocdPort` | `3443` | Port of the pyOCD raw SWO TCP server. |
| `cmsisTrace.decodedHost` | `127.0.0.1` | Host for decoded event listener clients. |
| `cmsisTrace.decodedPort` | `4554` | Port for decoded event listener clients. |
| `cmsisTrace.outputRawFile` | `""` | Raw trace file override. Empty uses `.trace/<active CMSIS target-set>/SWO.raw` or `.trace/default/SWO.raw`. |
| `cmsisTrace.workingDirectory` | `""` | Decoder working directory. Empty uses the first workspace folder. |
| `cmsisTrace.tspServerUrl` | `http://localhost:8080/tsp/api` | Base URL of the Trace Server TSP API. |
