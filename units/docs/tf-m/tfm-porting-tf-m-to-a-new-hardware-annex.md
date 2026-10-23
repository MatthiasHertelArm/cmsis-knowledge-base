---
id: "tfm-porting-tf-m-to-a-new-hardware-annex"
type: "concept"
domain: "security"
title: "Porting TF-M to a New Hardware: Platform Folder / Annex"
summary: "CMakeLists.txt: Defining regions for Secure world platform and all linked to it."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/platform/porting_tfm_to_a_new_hardware.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform/porting_tfm_to_a_new_hardware.html#annex"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Platform Folder_

CMake build system snippets examples

CMakeLists.txt: Defining regions for Secure world platform and all linked to it.

```CMake

target_include_directories(platform_region_defs
    INTERFACE
    <folder name under the platform folder - usually named platform>
)
```
CMakeLists.txt: Scatter files for SPE platform and bootloader

```CMake

target_add_scatter_file(bl2
    $<$<C_COMPILER_ID:ARMClang>:${PLATFORM_DIR}/ext/common/armclang/tfm_common_bl2.sct>
    $<$<C_COMPILER_ID:GNU>:${PLATFORM_DIR}/ext/common/gcc/tfm_common_bl2.ld>
    $<$<C_COMPILER_ID:IAR>:${PLATFORM_DIR}/ext/common/iar/tfm_common_bl2.icf>
)
target_add_scatter_file(tfm_s
    $<$<C_COMPILER_ID:ARMClang>:${PLATFORM_DIR}/ext/common/armclang/tfm_isolation_s.sct>
    $<$<C_COMPILER_ID:GNU>:${PLATFORM_DIR}/ext/common/gcc/tfm_isolation_s.ld>
    $<$<C_COMPILER_ID:IAR>:${PLATFORM_DIR}/ext/common/iar/tfm_isolation_s.icf>
)
```
CMakeLists.txt: Startup files for SPE platform and bootloader

```CMake

target_sources(bl2
    PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/platform/ext/target/<folder to platform>/device/source/startup_<platform name>.c
)
target_sources(tfm_s
    PRIVATE
    ${CMAKE_CURRENT_SOURCE_DIR}/platform/ext/target/<folder to platform>/device/source/startup_<platform name>.c
)
```
CMakeLists.txt: The Secure world platform sources

```CMake

target_include_directories(platform_bl2
    PUBLIC
)
target_include_directories(platform_s
    PUBLIC
)

target_sources(platform_bl2
    PRIVATE
)
target_sources(platform_s
    PRIVATE
)
target_sources(tfm_spm
    PRIVATE
        target_cfg.c
        tfm_hal_isolation.c
        tfm_hal_platform.c
)
```
CMakeLists.txt: installation for the Non-Secure world platform build

```CMake

install(FILES ${PLATFORM_DIR}/ext/common/uart_stdout.c
              native_drivers/arm_uart_drv.c
              native_drivers/timer_cmsdk/timer_cmsdk.c
              cmsis_drivers/Driver_USART.c
              retarget/platform_retarget_dev.c
              cmsis_core/an521_ns_init.c
        DESTINATION ${INSTALL_PLATFORM_NS_DIR})

install(DIRECTORY ${PLATFORM_DIR}/ext/common
        DESTINATION ${INSTALL_PLATFORM_NS_DIR}/ext)
```
config.cmake

```CMake

set(CONFIG_TFM_USE_TRUSTZONE            ON)
set(TFM_MULTI_CORE_TOPOLOGY             OFF)
set(BL2                                 OFF         CACHE BOOL      "Whether to build BL2")
set(NS                                  FALSE       CACHE BOOL      "Whether to build NS app" FORCE)
```
.. _check_config.cmake:

check_config.cmake

```CMake

function(tfm_invalid_config)
    if (${ARGV})
        string (REPLACE ";" " " ARGV_STRING "${ARGV}")
        string (REPLACE "STREQUAL"     "=" ARGV_STRING "${ARGV_STRING}")
        string (REPLACE "GREATER"      ">" ARGV_STRING "${ARGV_STRING}")
        string (REPLACE "LESS"         "<" ARGV_STRING "${ARGV_STRING}")
        string (REPLACE "VERSION_LESS" "<" ARGV_STRING "${ARGV_STRING}")
        string (REPLACE "EQUAL"        "=" ARGV_STRING "${ARGV_STRING}")
        string (REPLACE "IN_LIST"      "in" ARGV_STRING "${ARGV_STRING}")

        message(FATAL_ERROR "INVALID CONFIG: ${ARGV_STRING}")
    endif()
endfunction()

# Requires armclang >= 6.10.1
tfm_invalid_config((CMAKE_C_COMPILER_ID STREQUAL "ARMClang") AND (CMAKE_C_COMPILER_VERSION VERSION_LESS "6.10.1"))
```
.. _NSCMakeLists.txt:

/ns/CMakeLists.txt:

```CMake

add_library(platform_ns)

target_sources(platform_ns
    PRIVATE
        arm_uart_drv.c
        timer_cmsdk.c
        uart_stdout.c
        Driver_USART.c
    PUBLIC
        cmsis_core/startup_an521.c
)

target_include_directories(platform_ns
    PUBLIC
        include
        cmsis
        cmsis_core
)

target_compile_definitions(platform_ns
    PUBLIC
        $<$<BOOL:${PLATFORM_DEFAULT_CRYPTO_KEYS}>:PLATFORM_DEFAULT_CRYPTO_KEYS>
)
```
*Copyright (c) 2021-2024, Arm Limited. All rights reserved.*

*Copyright (c) 2022 Cypress Semiconductor Corporation (an Infineon company)
or an affiliate of Cypress Semiconductor Corporation. All rights reserved.*
