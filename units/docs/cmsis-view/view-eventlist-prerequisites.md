---
id: "view-eventlist-prerequisites"
type: "concept"
domain: "trace"
title: "eventlist: Prerequisites"
summary: "The following applications are required to be installed on your machine to allow eventlist utility to be built and run."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:tools/eventlist/README.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/tools/eventlist/README.md#prerequisites"
license: "Apache-2.0"
mode: "V"
---

The following applications are required to be installed on your
machine to allow **eventlist** utility to be built and run.

Note that some of the required tools are platform dependent:

- [Git](https://git-scm.com/)
- [golang](https://go.dev/doc/install) (minimum recommended version **1.17**)
- Platform specific command line terminal
  - **Windows:**
    - [GIT Bash](https://gitforwindows.org/)

    ```txt
    ☑️ Note:
        Make sure 'git' and 'bash' paths are listed under the PATH environment
        variable and set the git bash priority higher in the path.
    ```

  - **Linux/MacOS:**
    - GNU Bash (minimum recommended version **5.0.17**)
