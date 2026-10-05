---
id: "txmw-chapter-4-module-apis-txm-module-application-request"
type: "concept"
domain: "rtos"
title: "Chapter 4 - Module APIs: txm_module_application_request"
summary: "Application-specific request to resident code."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx-modules/chapter4.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx-modules/chapter4.md#txm-module-application-request"
license: "MIT"
mode: "V"
---

Application-specific request to resident code.

### Prototype

```c
UINT txm_module_application_request(
    ULONG request, 
    ULONG param_1,
    ULONG param_2,
    ULONG param_3);
```

### Description

This service makes the specified request to the resident portion of the application. It is assumed that the request structure is prepared prior to the call. The actual processing of the request takes place in the resident code in the function ***_txm_module_manager_application_request***. By default, this function is left empty and is designed for the resident application developer to modify.

### Input parameters

- **request** Request ID (application defined)
- **param_1** First parameter
- **param_2** Second parameter
- **param_3** Third parameter

### Return values

- **TX_SUCCESS** (0x00) Successful request.
- **TX_NOT_AVAILABLE** (0x1D) Request not supported by resident code.

### Allowed from

Module threads

### Example

```c
/* Call application resident code with ID=77 and the
   parameters set to 1, 2, 3. */
status = txm_module_application_request(77, 1, 2, 3);

/* If status is TX_SUCCESS the request was successful. */
```
### See also

- [Threadx Module APIs](#Threadx_Module_APIs)
