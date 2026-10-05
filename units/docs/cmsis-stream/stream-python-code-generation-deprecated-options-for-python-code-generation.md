---
id: "stream-python-code-generation-deprecated-options-for-python-code-generation"
type: "concept"
domain: "cmsis-stream"
title: "Python code generation (deprecated): Options for Python code generation"
summary: "Optional arguments to pass to the Python version of the scheduler function"
status: "draft"
collection: "cmsis-stream"
source: "ARM-software/CMSIS-Stream@efdc521:Documentation/PythonGen.md"
doc_source: "https://github.com/ARM-software/CMSIS-Stream/blob/efdc521/Documentation/PythonGen.md#options-for-python-code-generation"
license: "Apache-2.0"
mode: "V"
---

### pyOptionalArgs (default = "")

Optional arguments to pass to the Python version of the scheduler function

### customPythonName (default = "custom")

Name of custom header in generated Python code. If you use several scheduler, you may want to use different headers for each one.

### appNodesPythonName (default = "appnodes")

Name of AppNodes header in generated Python code. If you use several scheduler, you may want to use different headers for each one.

### schedulerPythonFileName (default = "sched")

Name of scheduler file in generated Python code. If you use several scheduler, you may want to use different headers for each one.

If the option is set to `xxx`, the name generated will be `xxx.py`
