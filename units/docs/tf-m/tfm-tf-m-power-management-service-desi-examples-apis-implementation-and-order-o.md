---
id: "tfm-tf-m-power-management-service-desi-examples-apis-implementation-and-order-o"
type: "concept"
domain: "security"
title: "TF-M Power Management Service design (RFC): Examples: APIs implementation and order of execution"
summary: "In the example above, entering the power state transition pre_state_custom_1b follows pre_state_custom_1a, while exiting the state post_state_custom_1b preceeds post_state_custom_1b."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_power_mgmt.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_power_mgmt.html#examples-apis-implementation-and-order-of-execution"
license: "BSD-3-Clause"
mode: "V"
---

```c

/* callbacks need to be sorted per-state */
static const struct plat_power_mgmt_set_state_callback_settings_t
    plat_callbacks[] = {
    {
        .state = TFM_POWER_MGMT_PWR_STATE_CUSTOM_1,
        .pre_cb = &pre_state_custom_1a,
        .post_cb = &post_state_custom_1b,
        .policy = TFM_POWER_MGMT_PWR_POLICY_GRACEFUL,
    },
    {
        .state = TFM_POWER_MGMT_PWR_STATE_CUSTOM_1,
        .pre_cb = &pre_state_custom_1b,
        .post_cb = &post_state_custom_1b,
        .policy = TFM_POWER_MGMT_PWR_POLICY_FORCEFUL,
    },
};
```
In the example above, entering the power state transition pre_state_custom_1b
follows pre_state_custom_1a, while exiting the state post_state_custom_1b
preceeds post_state_custom_1b.
