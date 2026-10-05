---
id: "avh-hello-world-application"
type: "concept"
domain: "test"
title: "Hello World Application"
summary: "This example prints \"Hello World\" and a counter value via the standard output. It can be used as a starting point when developing new applications."
status: "draft"
collection: "avh"
source: "ARM-software/AVH@bb8431b:example/FVP_Hello/README.md"
doc_source: "https://github.com/ARM-software/AVH/blob/bb8431b/example/FVP_Hello/README.md"
license: "Apache-2.0"
mode: "V"
---

This example prints "Hello World" and a counter value via the standard output. It
can be used as a starting point when developing new applications.

### Functionality
The application initializes CMSIS-RTOS2, creates the main application thread and starts
the RTOS scheduler. The application thread increments a counter and outputs it together
with the counter value.

### Output
The "Hello World" string, along with the counter value, is output via printf and
retargeted to the debug console.
