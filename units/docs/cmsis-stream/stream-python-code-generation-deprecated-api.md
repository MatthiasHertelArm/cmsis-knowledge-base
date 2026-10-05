---
id: "stream-python-code-generation-deprecated-api"
type: "concept"
domain: "cmsis-stream"
title: "Python code generation (deprecated): API"
summary: "It is a method of the Schedule object returned by computeSchedule."
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/PythonGen.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/PythonGen.md#api"
license: "Apache-2.0"
mode: "V"
---

```python
def pythoncode(self,directory,config=Configuration())
```

It is a method of the `Schedule` object returned by `computeSchedule`.

It generate Python code to implement the static schedule.

* `directory` : The directory where to generate the C++ files
* `config` : An optional configuration object
