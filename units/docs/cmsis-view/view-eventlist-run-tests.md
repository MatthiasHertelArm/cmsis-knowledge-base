---
id: "view-eventlist-run-tests"
type: "concept"
domain: "trace"
title: "eventlist: Run Tests"
summary: "One can directly run the tests from the command line."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@fef5aca:tools/eventlist/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/fef5aca/tools/eventlist/README.md#run-tests"
license: "Apache-2.0"
mode: "V"
---

One can directly run the tests from the command line.

- Go to eventlist directory
  - cd \<**root**\>/tools/eventlist
- Clean existing cache test results
  - go clean -cache
- Run command
  - `./make.sh test` : Run all tests.
  - `./make.sh test <PACKAGE>` : Run test related to the specified package.\
    for e.g.

    ```bash
    ./make.sh test eventlist/pkg/event
    ```
