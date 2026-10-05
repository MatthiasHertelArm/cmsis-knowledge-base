---
id: "ocp-cmsis-trace-decoder-command"
type: "concept"
domain: "trace"
title: "CMSIS Trace: Decoder command"
summary: "During debug pause, the live decoder keeps writing the same raw trace file while the one-shot decoder reads the current snapshot."
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/cmsis-trace-extension@1aebf86:README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/cmsis-trace-extension/blob/1aebf86/README.md#decoder-command"
license: "Apache-2.0"
mode: "V"
---

```sh
cmsis-trace-decoder --pyocd-swo 127.0.0.1:3443 \
  --output-raw .trace/<active-target-set>/SWO.raw \
  --output-tcp 127.0.0.1:4554
```

During debug pause, the live decoder keeps writing the same raw trace file while
the one-shot decoder reads the current snapshot.

The decoder is located in this order: the `cmsisTrace.executablePath` setting;
in an Extension Development Host, a sibling `cmsis-trace-decoder` checkout; when
installed, the bundled decoder under `dist/tools`; then `cmsis-trace-decoder` on
`PATH`.
