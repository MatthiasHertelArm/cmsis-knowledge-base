---
id: "intr-how-to-transition-from-nrf5-sdk-to-1-bootloader-update-for-migration-suppor"
type: "concept"
domain: "debug"
title: "How to Transition from nRF5 SDK to Zephyr NCS － Lessons from Ultrahuman’s Journey: Behind the Solution / 1\\. Bootloader Update for Migration Support"
summary: "The following code changes, noted as commented out lines, needed to be made to the relevant bootloader files:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-12-11-upgrading-from-nrf5-sdk-to-ncs.md"
doc_source: "https://interrupt.memfault.com/blog/upgrading-from-nrf5-sdk-to-ncs#1-bootloader-update-for-migration-support"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Behind the Solution_

The following code changes, noted as commented out lines, needed to be made to the relevant bootloader files:

`nrf_dfu_validation.c`

```c
/*
 * @param[in]  sd_start_addr  Start address of received SoftDevice.
 * @param[in]  sd_size        Size of received SoftDevice in bytes.
 */
static bool softdevice_info_ok(uint32_t sd_start_addr, uint32_t sd_size)
{
    bool result = true;

    if (SD_MAGIC_NUMBER_GET(sd_start_addr) != SD_MAGIC_NUMBER)
    {
        NRF_LOG_ERROR("The SoftDevice does not contain the magic number identifying it as a SoftDevice.");

        // Protection removed for bootloader migration
        // result = false;
    }
    else if (SD_SIZE_GET(sd_start_addr) < ALIGN_TO_PAGE(sd_size + MBR_SIZE))
    {
        // The size in the info struct should be rounded up to a page boundary
        // and be larger than the actual size + the size of the MBR.
        NRF_LOG_ERROR("The SoftDevice size in the info struct is too small compared with the size reported in the init command.");
        result = false;
    }
    else if (SD_PRESENT && (SD_ID_GET(MBR_SIZE) != SD_ID_GET(sd_start_addr)))
    {
        NRF_LOG_ERROR("The new SoftDevice is of a different family than the present SoftDevice. Compatibility cannot be guaranteed.");
        result = false;
    }

    return result;
}
```

And of course, we needed to let go of SD magic number:

`nrf_bootloader_fw_activation.c`

```c
static uint32_t sd_activate(void)
{
    uint32_t   ret_val      = NRF_SUCCESS;
    uint32_t   target_addr  = nrf_dfu_softdevice_start_address() + s_dfu_settings.write_offset;
    uint32_t   src_addr     = s_dfu_settings.progress.update_start_address;
    uint32_t   sd_size      = s_dfu_settings.sd_size;
    uint32_t   length_left  = ALIGN_TO_PAGE(sd_size - s_dfu_settings.write_offset);

    NRF_LOG_DEBUG("Enter nrf_bootloader_dfu_sd_continue");

    if (SD_MAGIC_NUMBER_GET(src_addr) != SD_MAGIC_NUMBER)
    {
        NRF_LOG_ERROR("Source address does not contain a valid SoftDevice.")
        
        // Protection removed for bootloader migration
        // return NRF_ERROR_INTERNAL;
    }

    // This can be a continuation due to a power failure
    src_addr += s_dfu_settings.write_offset;

    if (s_dfu_settings.write_offset == sd_size)
    {
        NRF_LOG_DEBUG("SD already copied");
        return NRF_SUCCESS;
    }

    if (s_dfu_settings.write_offset == 0)
    {
        NRF_LOG_DEBUG("Updating SD. Old SD ver: %d, New ver: %d",
            SD_VERSION_GET(MBR_SIZE) / 1000000, SD_VERSION_GET(src_addr) / 1000000);
    }

    ret_val = image_copy(target_addr, src_addr, length_left, NRF_BL_FW_COPY_PROGRESS_STORE_STEP);
    if (ret_val != NRF_SUCCESS)
    {
        NRF_LOG_ERROR("Failed to copy firmware.");
        return ret_val;
    }

    ret_val = nrf_dfu_settings_write_and_backup(NULL);

    return ret_val;
}
```
