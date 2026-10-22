---
id: "view-eventlist-build-components"
type: "concept"
domain: "trace"
title: "eventlist: Build components"
summary: "The steps below demonstrate how to build and create an executable:"
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:tools/eventlist/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/tools/eventlist/README.md#build-components"
license: "Apache-2.0"
mode: "V"
---

The steps below demonstrate how to build and create an executable:

- Go to eventlist directory
  - cd \<**root**\>/tools/eventlist
- Run the command to build an executable under `build` directory
  - `./make.sh build` : Build and generate executable for host OS & architecture in current directory.
  - `./make.sh build -arch <ARCH> -os <OS> -outdir <OUT directory>` : Build and generate executable for provided configs.\
    for e.g.

    ```bash
    ./make.sh build -arch arm64 -os darwin -outdir "Path/to/output/dir"
    ```
