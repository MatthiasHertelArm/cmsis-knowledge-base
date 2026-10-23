---
id: "tfm-firmware-update-service-shim-layer-between-fwu-and-bootloader"
type: "concept"
domain: "security"
title: "Firmware Update Service: Shim Layer between FWU and bootloader"
summary: "The firmware update operations are achieved by calling the shim layer APIs between bootloader and FWU."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_fwu_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_fwu_service.html#shim-layer-between-fwu-and-bootloader"
license: "BSD-3-Clause"
mode: "V"
---

The firmware update operations are achieved by calling the shim layer APIs
between bootloader and FWU.


### Shim layer introduction

This shim layer provides the APIs with the functionality of operating the
bootloader to cooperate with the Firmware Update service. This shim layer
is decoupled from bootloader implementation. Users can specify a specific
bootloader by setting `TFM_FWU_BOOTLOADER_LIB` build configuration and
adding the specific build scripts into that file. By default, the MCUboot
is chosen as the bootloader.


### Interfaces of the shim Layer



#### fwu_bootloader_init(function)


##### Prototype

```c

psa_status_t fwu_bootloader_init(void);
```

###### Description

Bootloader related initialization for the firmware update. It reads
some necessary shared data from the memory if needed. It initializes
the flash drivers defined in FLASH_DRIVER_LIST. Platform can define
FLASH_DRIVER_LIST in flash_layout.h to overload the default driver list.


###### Parameters

    N/A


#### fwu_bootloader_staging_area_init(function)

**Prototype**

```c

psa_status_t fwu_bootloader_staging_area_init(psa_fwu_component_t component,
                                              const void *manifest,
                                              size_t manifest_size);
```
**Description**

The component is in READY state. Prepare the staging area of the component for image download.
For example, initialize the staging area, open the flash area, and so on.

**Parameters**

- `component`: The identifier of the target component in bootloader.
- `manifest`: A pointer to a buffer containing a detached manifest for the update.
  If the manifest is bundled with the firmware image, manifest must be NULL.
- `manifest_size`: Size of the manifest buffer in bytes.


#### fwu_bootloader_load_image(function)

**Prototype**

```c

psa_status_t fwu_bootloader_load_image(psa_fwu_component_t component,
                                       size_t        image_offset,
                                       const void    *block,
                                       size_t        block_size);
```
**Description**

Load the image into the target component.

**Parameters**

- `component`: The identifier of the target component in bootloader.
- `image_offset`: The offset of the image being passed into block, in bytes.
- `block`: A buffer containing a block of image data. This might be a complete image or a subset.
- `block_size`: Size of block.


#### fwu_bootloader_install_image(function)

**Prototype**

```c

psa_status_t fwu_bootloader_install_image(psa_fwu_component_t *candidates,
                                          uint8_t number);
```
**Description**

Check the authenticity and integrity of the image. If a reboot is required to
complete the check, then mark this image as a candidate so that the next time
bootloader runs it will take this image as a candidate one to boot-up. Return
the error code PSA_SUCCESS_REBOOT.

**Parameters**

- `candidates`: A list of components in CANDIDATE state.
- `number`: Number of components in CANDIDATE state.


#### fwu_bootloader_mark_image_accepted(function)

**Prototype**

```c

psa_status_t fwu_bootloader_mark_image_accepted(const psa_fwu_component_t *trials,
                                                uint8_t number);
```
**Description**

Call this API to mark the TRIAL(running) image in component as confirmed to avoid
revert when next time boot-up. Usually, this API is called after the running
images have been verified as valid.

**Parameters**

- `trials`: A list of components in TRIAL state.
- `number`: Number of components in TRIAL state.


#### fwu_bootloader_reject_staged_image(function)

**Prototype**

```c

psa_status_t fwu_bootloader_reject_staged_image(psa_fwu_component_t component);
```
**Description**

The component is in STAGED state. Call this API to Uninstall the staged image in the
component so that this image will not be treated as a candidate next time boot-up.

**Parameters**

- `component`: The identifier of the target component in bootloader.


#### fwu_bootloader_reject_trial_image(function)

**Prototype**

```c

psa_status_t fwu_bootloader_reject_trial_image(psa_fwu_component_t component);
```
**Description**

The component is in TRIAL state. Mark the running image in the component as rejected.

**Parameters**

- `component`: The identifier of the target component in bootloader.


#### fwu_bootloader_clean_component(function)

**Prototype**

```c

psa_status_t fwu_bootloader_clean_component(psa_fwu_component_t component);
```
**Description**

The component is in FAILED or UPDATED state. Clean the staging area of the component.

**Parameters**

- `component`: The identifier of the target component in bootloader.


#### fwu_bootloader_get_image_info(function)

**Prototype**

```c

psa_status_t fwu_bootloader_get_image_info(psa_fwu_component_t component,
                                           bool query_state,
                                           bool query_impl_info,
                                           psa_fwu_component_info_t *info);
```
**Description**

Get the image information of the given bootloader_image_id in the staging area
or the running area.

**Parameters**

    - `component`: The identifier of the target component in bootloader.
    - `query_state`: Whether query the 'state' field of psa_fwu_component_info_t.
    - `query_impl_info`: Whether Query 'impl' field of psa_fwu_component_info_t.
    - `info`: Buffer containing return the component information.
