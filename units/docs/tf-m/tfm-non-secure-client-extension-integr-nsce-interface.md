---
id: "tfm-non-secure-client-extension-integr-nsce-interface"
type: "concept"
domain: "security"
title: "Non-secure Client Extension Integration Guide: NSCE interface"
summary: "NSCE defines a set of APIs as the interface for NSPE RTOS to manage the context in TF-M. NSID is provided as an input parameter of tfm_nsce_load_ctx()."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/non-secure_client_extension_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/non-secure_client_extension_integration_guide.html#nsce-interface"
license: "BSD-3-Clause"
mode: "V"
---

NSCE defines a set of APIs as the interface for NSPE RTOS to manage the context
in TF-M. NSID is provided as an input parameter of `tfm_nsce_load_ctx()`.

NSCE APIs are typically called by the kernel and must be called from the
non-secure handler mode.

```c

uint32_t tfm_nsce_init(uint32_t ctx_requested)
```
This function should be called before any other NSCE APIs below to do non-secure
context initialization in NSCE for the calling NS entity. `ctx_requested` is the
number of the contexts requested by the NS entity. The number of assigned
context will be returned. It may be equal to or smaller than the requested
context number based on the current available resource in TF-M. If
`ctx_requested` is `0`, then the maximum available context number will be
assigned and returned. If the initialization is failed, `0` should be returned.

As TF-M only supports one context for now, so the return value is always `1`
if no error. Currently, it is safe to skip calling `tfm_nsce_init()`.
But, for future compatibility, it is recommended to do so.
```c

uint32_t tfm_nsce_acquire_ctx(uint8_t group_id, uint8_t thread_id)
```
This function allocates a context for the NS client connection. The `gid` and
`tid` are the input parameters. A token will be returned to the NSPE if TF-M
has an available context slot. Otherwise, `TFM_NS_CLIENT_INVALID_TOKEN` is
returned.
It is the responsibility of NSPE RTOS to assign gid and tid for each NS client.

```c

uint32_t tfm_nsce_release_ctx(uint32_t token)
```
This function tries to release the context which was retrieved by
`tfm_nsce_acquire_ctx()`. As the context may be shared with other threads
within the same group, the context is only freed and back to the available
context pool after all threads in the same group release the context.

```c

uint32_t tfm_nsce_load_ctx(uint32_t token, int32_t nsid)
```
This function should be called when NSPE RTOS schedules in a NS client. `token`
is returned by `tfm_nsce_acquire_ctx()`. `nsid` is the non-secure client ID
used for the following PSA service calls.

The assignment of NSID is managed by the NSPE RTOS. It is not required to use
the same NSID for a NS client when calling this function each time. This allows
the NS client changing its NSID in the lifecycle. For example, the provisioning
task may need to switch NSID to provision the keys for different NS clients
created afterwards.

```c

uint32_t tfm_nsce_save_ctx(uint32_t token)
```
This function should be called when NSPE RTOS schedules out a NS client. The
input parameter `token` is returned by `tfm_nsce_acquire_ctx()`.
After the context is saved, no secure service call can be made from NSPE until a
context is loaded via `tfm_nsce_load_ctx()`.
