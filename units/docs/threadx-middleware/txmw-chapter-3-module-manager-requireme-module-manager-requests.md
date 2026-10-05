---
id: "txmw-chapter-3-module-manager-requireme-module-manager-requests"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Module Manager requirements: Module Manager requests"
summary: "Requests made by modules to the Module Manager are done via macros in txm_module.h that map all ThreadX calls to call the Module Manager dispatch function via a function pointer supplied to the module by the Module Manager."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter3.md#module-manager-requests"
license: "MIT"
mode: "V"
---

Requests made by modules to the Module Manager are done via macros in ***txm_module.h*** that map all ThreadX calls to call the Module Manager dispatch function via a function pointer supplied to the module by the Module Manager.

Additional application-specific services made via the module calling ***txm_module_application_request*** are handled by the same macro mechanism used for the ThreadX API. By default, this handling function in the Module Manager is empty and designed such that the application adds the necessary code to process the application-specific requests.

If the request is not implemented by the Module Manager, a value of **TX_NOT_AVAILABLE** error status is returned by the Module Manager. This error code is also returned if the module requests an operation that is outside the scope of the module's access. For example, a module is not allowed to create a timer with the timer control block or callback address outside of the module's code area.
