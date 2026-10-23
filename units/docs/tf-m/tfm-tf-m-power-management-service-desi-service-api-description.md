---
id: "tfm-tf-m-power-management-service-desi-service-api-description"
type: "concept"
domain: "security"
title: "TF-M Power Management Service design (RFC): Service API description"
summary: "The service exposes an interface that secure and non-secure callers can use."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_power_mgmt.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_power_mgmt.html#service-api-description"
license: "BSD-3-Clause"
mode: "V"
---

The service exposes an interface that secure and non-secure callers can use.

The API interface defines a number of generic power states for the core itself
but also allows custom states to be added for system-wide or platform
peripherals.
Platform code is expected to implement the supported callbacks for the listed
power states.

To request a state transition:

```c

enum tfm_power_mgmt_err_t tfm_power_mgmt_set_state(
    enum tfm_power_mgmt_power_state_t pwr_state,
    uint32_t wait_for);
```
The API `tfm_power_mgmt_set_state()` validates pwr_state and call_type,
packages struct tfm_power_mgmt_set_params, and calls
`TFM_POWER_MGMT_SERVICE_HANDLE`.

To probe a (custom) power state:

```c

enum tfm_power_mgmt_err_t tfm_power_mgmt_get_state(
    uint32_t device_id,
    int32_t *state);
```
The API `tfm_power_mgmt_get_state()` validates the device_id against the
platform-defined `PLAT_POWER_MGMT_DEVICE_ID_MAX`, and calls
`TFM_POWER_MGMT_SERVICE_HANDLE`.
