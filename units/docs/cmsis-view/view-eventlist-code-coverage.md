---
id: "view-eventlist-code-coverage"
type: "concept"
domain: "trace"
title: "eventlist: Code coverage"
summary: "Users can get coverage and generate code coverage report in HTML format"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:tools/eventlist/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/tools/eventlist/README.md#code-coverage"
license: "Apache-2.0"
mode: "V"
---

Users can get coverage and generate code coverage report in HTML format

- Go to eventlist directory
    > cd \<**root**\>/tools/eventlist
- Run command
  - `./make.sh coverage`        : Run tests and show coverage info.\
  - `./make.sh coverage -html <FILE path>` : Run tests with coverage info and generate specified HTML coverage report.\

    for e.g.

    ```bash
    ./make.sh coverage -html cov/coverage.html
    ```

```txt
☑️ Note:
   for more usable commands, Use `./make.sh -h`.
```
