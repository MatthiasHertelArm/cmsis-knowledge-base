---
id: "cda-troubleshooting-python-debug-sessi-one-test-at-a-time-with-testname"
type: "concept"
domain: "debug"
title: "Troubleshooting Python debug sessions: One test at a time with testName"
summary: "testName only shapes the configuration start_debugging builds itself (configurationName: \"Default Configuration\"); a named entry runs as written and ignores it. The built configuration runs python -m unittest <module>.<Class>.<test> -v in the test file's folder, with justMyCode off:"
status: "draft"
collection: "cda-guides"
source: "Open-CMSIS-Pack/CMSIS-Developer-Assistant@7db44ba:docs/agent-resources/troubleshooting/python.md"
doc_source: "https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant/blob/7db44ba/docs/agent-resources/troubleshooting/python.md#one-test-at-a-time-with-testname"
license: "Apache-2.0"
mode: "V"
---

`testName` only shapes the configuration `start_debugging` builds itself (`configurationName: "Default Configuration"`); a named entry runs as written and ignores it. The built configuration runs `python -m unittest <module>.<Class>.<test> -v` in the test file's folder, with `justMyCode` off:

- `<module>` is the file name without `.py`. A `testName` containing a dot is appended as given (`TestParser.test_empty`). Without a dot, `<Class>` is the first capitalised name after the word `class` anywhere in the file, comments and strings included, so pass `Class.test_name` whenever the file holds more than one class.
- It is unittest only. For pytest, add an entry with `"module": "pytest"` and `"args": ["tests/test_parser.py::test_empty"]` and pass its name.
- The project root is not on `sys.path` when the test file sits in a subfolder, so a package there that is not installed fails to import. Use an entry whose `cwd` is the project root.
- A failing assertion is caught by the test runner and never counts as uncaught, so the run does not stop at it. Break on the assertion line, with a `condition` when it sits in a loop.
