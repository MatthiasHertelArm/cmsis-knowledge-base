---
id: "tfm-non-secure-client-extension-integr-nsce-integration-guide"
type: "concept"
domain: "security"
title: "Non-secure Client Extension Integration Guide: NSCE integration guide"
summary: "To enable NSCE in TF-M, set the build flag TFM_NS_MANAGE_NSID to ON (default OFF)."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/non-secure_client_extension_integration_guide.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/non-secure_client_extension_integration_guide.html#nsce-integration-guide"
license: "BSD-3-Clause"
mode: "V"
---

### Enable NSCE in TF-M


To enable NSCE in TF-M, set the build flag `TFM_NS_MANAGE_NSID` to `ON` (default
`OFF`).


### Support NSCE in an RTOS


For supporting NSCE in an RTOS, the integrator needs to do the following major
work:

- Integrate the NSCE API calls into the NS task lifecycle. For example,
  creating/scheduling/destroying a NS task.

- Manage the assignment for `gid`, `tid` and NSID.

The typical steps are listed below:

- Before programming, the integrator should plan the group assignment for
  the NS tasks that need to call secure services. If the number of tasks is less
  than or equal to TF-M non-secure context slots, then different gid can be
  assigned to each task for taking dedicated context in TF-M.
  Otherwise, the integrator need to think about grouping the tasks to share the
  context.

- In the kernel initialization stage, it calls `tfm_nsce_init()` with
  requested context number to initialize the non-secure context in TF-M. The
  actual allocated context number will be returned. `0` means initialization
  failed. The kernel could use different group assignment sets according to the
  context number allocated to it. TF-M only supports one context for now.

- The kernel calls `tfm_nsce_acquire_ctx()` when creating a new task. This
  should be done before the new task calls any secure service. A valid token
  returned should be saved as part of the task context in NSPE RTOS.

- When the kernel schedules in a task with a valid `token` associated,
  `tfm_nsce_load_ctx()` should be called before resuming the execution of that
  task. The NSID is specified by the kernel through the `nsid` parameter.
  The mapping between NSID and task is managed by the kernel.
  `tfm_nsce_load_ctx()` can be called multiple times without calling
  `tfm_nsce_save_ctx()` for switching the NSID for the same task (same tid and
  gid).

- `tfm_nsce_save_ctx()` should be called if the current task has a valid
  `token` before being switched to another task. Calling `tfm_nsce_load_ctx()`
  for another task before saving the current context may result in NS context
  lost in TF-M for the running task.

- When the task is terminated, destroyed or crashed, the kernel should call
  `tfm_nsce_release_ctx` to make sure the associated resource is back to the
  pool in TF-M.


### Integration example


This is the software module diagram of a typical RTOS/NSCE integration example.

- Built-in Secure Context Manager: An RTOS may have an existing built-in secure
  context manager with a group of secure context management APIs defined. Let's
  take RTX which uses [Armv8-M TrustZone APIs](http://arm-software.github.io/CMSIS_6/latest/Core/using_TrustZone_pg.html)
  as the example.

RTOS may define the NS task context in the secure side as "secure context". It
is the same thing as the "non-secure context" (context for a secure service
call from NS client) from TF-M's point of view.
- Shim Layer/Secure Context Manager: If the RTOS has a "Built-in Secure Context
  Manager", then a shim layer should be provided to translate the built-in API
  calls into the NSCE API calls. A reference shim layer for RTX TrustZone APIs
  is [here](https://review.trustedfirmware.org/c/TF-M/tf-m-tests/+/11291).

  If the RTOS has no existing one, then a "Secure Context Manager" should be
  implemented based on the NSCE APIs. You can refer to the shim layer example
  above for the implementation. The timing of calling NSCE APIs in the kernel is
  introduced in the Support NSCE in an RTOS section above.

- NSID Manager: If NSPE RTOS manages the NSID, then this module is used by the
  secure context manager or shim layer to manage the NSID assignment for the
  NS tasks. The assignment is implementation defined. A `task name based NSID
  manager <https://review.trustedfirmware.org/c/TF-M/tf-m-tests/+/11290>`_ is \
  provided as a reference.


### Integration notes


- `gid`: It is a `uint8_t` value (valid range is 0 - 255). So, maximum 256
  groups (NSCE context slots) are supported by the NSCE interface.
  TF-M only supports single context for now. So, it is recommended to use
  single group ID at this stage.

- `tid`: It is a `uint8_t` value (valid range is 0 - 255). Thread ID is used to
  identify a NS client within a given group. `tid` has no special meaning for
  TF-M. So, usually the kernel only needs to ensure a NS task has a unique `tid`
  within a group.

- `gid` and `tid` management: It is the responsibility of NSPE RTOS to manage
  the assignment of `gid` and `tid`. Based on the explanation above, the `gid`
  could be assigned as a constant value. And, the `tid` can be increased
  globally when calling `tfm_nsce_acquire_ctx()` for a new task. Just notice
  `tid` may overflow.

- NSID management: It is the responsibility of NSPE RTOS to manage the
  assignment of the NSID for each task. It is highly recommended that a NS
  client uses the same NSID following a reboot or update. The binding of a NS
  client to a specific NSID will ensure the correct access to the assets. For
  example, the data saved in the protected storage.

- Integrate with the existing secure context management APIs of NSPE RTOS: The
  NSCE APIs are designed to be compatible with most known existing secure
  context management APIs. A shim layer is needed to translate the API calls.
  See the integration example above.

- `tfm_nsce_acquire_ctx()` must be called before calling
  `tfm_nsce_load_ctx()`, `tfm_nsce_save_ctx()` or `tfm_nsce_release_ctx()`.

- `tfm_nsce_release_ctx()` can be called without calling `tfm_nsce_save_ctx()`
  ahead.

--------------

*Copyright (c) 2021, Arm Limited. All rights reserved.*
