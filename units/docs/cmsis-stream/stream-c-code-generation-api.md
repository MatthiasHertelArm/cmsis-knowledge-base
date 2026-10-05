---
id: "stream-c-code-generation-api"
type: "concept"
domain: "cmsis-stream"
title: "C++ Code generation: API"
summary: "It is a method of the Schedule object returned by computeSchedule."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/CCodeGen.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/CCodeGen.md#api"
license: "Apache-2.0"
mode: "V"
---

```python
def ccode(self,directory,config=Configuration())
```

It is a method of the `Schedule` object returned by `computeSchedule`.

It generate C++ code implementing the static schedule.

* `directory` : The directory where to generate the C++ files
* `config` : An optional configuration object
