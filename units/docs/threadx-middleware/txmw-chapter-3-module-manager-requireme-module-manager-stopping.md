---
id: "txmw-chapter-3-module-manager-requireme-module-manager-stopping"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Module Manager requirements: Module Manager stopping"
summary: "The Module Manager terminates execution of a previously-loaded and executing module via the txm_module_manager_stop function. This API function first terminates and deletes the initial starting thread. If the module preamble specifies a stop thread, this thread is created and executed."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter3.md#module-manager-stopping"
license: "MIT"
mode: "V"
---

The Module Manager terminates execution of a previously-loaded and executing module via the ***txm_module_manager_stop*** function. This API function first terminates and deletes the initial starting thread. If the module preamble specifies a stop thread, this thread is created and executed. The Module Manager waits for a fixed period of time for the stop thread to complete. Once complete, all system resources created by the module are deleted and the module is placed in a dormant state, from which it can be either restarted or unloaded.
