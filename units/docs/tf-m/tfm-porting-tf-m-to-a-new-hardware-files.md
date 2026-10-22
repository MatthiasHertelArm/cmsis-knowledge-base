---
id: "tfm-porting-tf-m-to-a-new-hardware-files"
type: "concept"
domain: "security"
title: "Porting TF-M to a New Hardware: Platform Folder / Files"
summary: "This is the entry point for the build system to build your platform on the secure side and also export files to build Non-Secure side."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/platform/porting_tfm_to_a_new_hardware.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform/porting_tfm_to_a_new_hardware.html#files"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Platform Folder_

#### CMakeLists.txt :


    (MANDATORY)

    This is the entry point for the build system to build your platform on the secure side and
    also export files to build Non-Secure side.

    it must:

        - Add a folder to the target platform_region_defs. [PLATFORM_REGION_DEFS_]

            This folder will contain two files flash_layout.h_ and region_defs.h_

        - Add scatter files to the bl2 and tfm_s targets. [SCATTER_]

            Please note that TF-M provides a common scatter file for the bl2, tfm_s and
            tfm_ns targets, which can be used in most cases.

        - Add startup files to the bl2 and tfm_s targets. [STARTUP_]
        - Add required sources and includes for the bl2 and tfm_s targets [SOURCES_INCLUDES_]
        - Install all files required for building the platform in the Non-secure application [INSTALL_]

    The installation section expands the common installation script with the platform specific files.
    The following predefined variables are available to address the respective subfolders
    of the target `<Artifact folder>`.

    +-------------------------------------+------------------------------------------------------------+
    |    name                             |        description                                         |
    +=====================================+============================================================+
    |INSTALL_INTERFACE_INC_DIR            | interface/include - interface header files                 |
    +-------------------------------------+------------------------------------------------------------+
    |INSTALL_INTERFACE_SRC_DIR            | interface/src - interface source files                     |
    +-------------------------------------+------------------------------------------------------------+
    |INSTALL_INTERFACE_LIB_DIR            | interface/lib - interface libraries                        |
    +-------------------------------------+------------------------------------------------------------+
    |INSTALL_IMAGE_SIGNING_DIR            | image_signing tools and files                              |
    +-------------------------------------+------------------------------------------------------------+
    |INSTALL_CMAKE_DIR                    | CMake modules for Non-secure app build                     |
    +-------------------------------------+------------------------------------------------------------+
    |INSTALL_PLATFORM_NS_DIR              | NS platform source files                                   |
    +-------------------------------------+------------------------------------------------------------+


#### config.cmake:


    (MANDATORY)

    This file is used to setup default build configurations for TF-M and platform configurations
    which have fixed values depending on hardware and software supportness.
    These configurations should be set as normal CMake variables while others are cache variables.

    The platform configurations in the below table are required.

    +------------------------------+-------------------------------------------------------------------+
    |    name                      |        description                                                |
    +==============================+===================================================================+
    |CONFIG_TFM_USE_TRUSTZONE      | Use TrustZone to transition between NSPE and SPE on the same CPU  |
    +------------------------------+-------------------------------------------------------------------+
    |TFM_MULTI_CORE_TOPOLOGY       | NSPE runs on a separate CPU to SPE                                |
    +------------------------------+-------------------------------------------------------------------+

    The platform configurations in the below table control optional features which rely on platform
    specific implementation.
    These features are disabled by default.
    Platforms shall implement corresponding functionalities and explicitly set the configuration to
    enable the feature.

    +-------------------------------------+------------------------------------------------------------+
    |    name                             |        description                                         |
    +=====================================+============================================================+
    |PLATFORM_HAS_ISOLATION_L3_SUPPORT    | Whether the platform has isolation level 3 support         |
    +-------------------------------------+------------------------------------------------------------+
    |PLATFORM_HAS_FIRMWARE_UPDATE_SUPPORT | Whether the platform has firmware update support           |
    +-------------------------------------+------------------------------------------------------------+
    |PSA_API_TEST_TARGET                  | The target platform name of PSA API test                   |
    +-------------------------------------+------------------------------------------------------------+
    |PLATFORM_SVC_HANDLERS                | Whether the platform has specific SVC handling             |
    +-------------------------------------+------------------------------------------------------------+

    For build configurations, please refer to `config_base.cmake`.

    [config_cmake_]


#### cpuarch.cmake:


    (MANDATORY)

    This file contains hardware information such as the main processor and architecture of the SPE
    CPU.
    On single-core platforms, it should be installed to `<Artifact folder>` for NSPE build.
    On multi-core platforms, two cpuarch.cmake files should be added.

    - a SPE specific `cpuarch.cmake` used in SPE build
    - an NSPE one which should be installed to `<Artifact folder>` with filename `cpuarch.cmake`
      for NSPE build. See ns/cpuarch_ns.cmake.

    +-------------------------+------------------------------------------------------------+
    |    name                 |        description                                         |
    +=========================+============================================================+
    |TFM_SYSTEM_PROCESSOR     | The SPE Processor the platform is using                    |
    +-------------------------+------------------------------------------------------------+
    |TFM_SYSTEM_ARCHITECTURE  | The architecture of the processor                          |
    +-------------------------+------------------------------------------------------------+
    |CONFIG_TFM_FP_ARCH       | The Float Point architecture flag for toolchain            |
    +-------------------------+------------------------------------------------------------+
    |CONFIG_TFM_FP_ARCH_ASM   | The Float Point architecture flag for assembly code        |
    +-------------------------+------------------------------------------------------------+


#### tests/tfm_tests_config.cmake:


    (OPTIONAL)

    This file contains platform-specific config options for TF-M regression tests.
    The `tests` folder should installed to <Artifact folder>/platform for NSPE build.
    Here are some examples.

    +--------------------------------+------------------------------------------------------------+
    |    name                        |        description                                         |
    +================================+============================================================+
    |PLATFORM_SLIH_IRQ_TEST_SUPPORT  | Whether the platform has SLIH test support                 |
    +-------------------------+-------------------------------------------------------------------+
    |PLATFORM_FLIH_IRQ_TEST_SUPPORT  | Whether the platform has FLIH test support                 |
    +--------------------------------+------------------------------------------------------------+


#### tests/psa_arch_tests_config.cmake:


    (OPTIONAL)

    This file contains platform-specific config options for PSA API tests.
    Here are some examples.

    +--------------------------------+------------------------------------------------------------+
    |    name                        |        description                                         |
    +================================+============================================================+
    |PSA_API_TEST_TARGET             | The target platform name of PSA API test                   |
    +--------------------------------+------------------------------------------------------------+


#### startup files:


    (MANDATORY)

    These files (one for BL2, one for S, one for NS) are the expected startup
    files. The reset handler should call SystemInit and then should end up
    calling __START which should be defined as _start if not defined elsewhere.

.. _flash_layout.h:


#### flash_layout.h:


    (MANDATORY)

    This file can be anywhere in the platform folder, usually in a sub folder
    named `partition`.
    TF-M doesn't provide a template for this file, common practice is to copy it
    from another platform (e.g. arm/mps2/an521) and update the following entries.

    Note: all size are in bytes

    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |    name                      |        description                                                |    Requisiteness                          |
    +==============================+===================================================================+===========================================+
    |FLASH_S_PARTITION_SIZE        | Size of the Secure partition in flash                             | Yes                                       |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |FLASH_NS_PARTITION_SIZE       | Size of the Non-Secure partition in flash                         | if tfm_ns is built                        |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |FLASH_AREA_IMAGE_SECTOR_SIZE  | Size of the flash sector                                          | if bl2 is built                           |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |FLASH_TOTAL_SIZE              | Flash total size                                                  | Yes                                       |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |FLASH_BASE_ADDRESS            | Flash base memory address                                         | if bl2 is built                           |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |FLASH_AREA_BL2_OFFSET         | BL2 offset in flash                                               | if bl2 is built                           |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |FLASH_AREA_BL2_SIZE           | BL2 flash size                                                    | if bl2 is built                           |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |FLASH_PS_AREA_SIZE            | Allocated size for the protected storage data in flash            | Yes                                       |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |FLASH_ITS_AREA_SIZE           | Allocated size for the internal trusted storage data in flash     | Yes                                       |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |SECURE_IMAGE_OFFSET           | Offset of the secure image data in flash                          | if bl2 is built                           |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |FLASH_DEV_NAME                | Name as defined in the CMSIS flash drivers                        | Yes                                       |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |TFM_HAL_PS_FLASH_DRIVER       | Name as defined in the CMSIS flash drivers                        | used by protected storage partition       |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |TFM_HAL_PS_SECTORS_PER_BLOCK  | Number of physical erase sectors per logical FS block             | used by protected storage partition       |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |TFM_HAL_PS_PROGRAM_UNIT       | Smallest flash programmable unit in bytes                         | used by protected storage partition       |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |TFM_HAL_ITS_FLASH_DRIVER      | Name as defined in the CMSIS flash drivers                        | used by internal trusted storage partition|
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |TFM_HAL_ITS_SECTORS_PER_BLOCK | Number of physical erase sectors per logical ITS block            | used by internal trusted storage partition|
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |TFM_HAL_ITS_PROGRAM_UNIT      | Smallest flash programmable unit in bytes                         | used by internal trusted storage partition|
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+
    |TFM_NV_COUNTERS_AREA_SIZE     | Allocated size for the NV counters data in flash                  | if using TF-M templates                   |
    +------------------------------+-------------------------------------------------------------------+-------------------------------------------+

.. _region_defs.h:


#### region_defs.h:


    (MANDATORY)

    This file can be anywhere in the platform folder, usually in a sub folder
    named `partition`.
    TF-M doesn't provide a template for this file, common practice is to copy it
    from another platform (e.g. arm/mps2/an521) and update the following entries.

    General advice: if you don't know beforehand the size you will want for
    these elements you will have to make it iterative from an arbitrary value
    taken from another platform (e.g. arm/mps2/an521)

    Note: all size are in bytes

    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |    name                          |        description                                                | Requisiteness                                 |
    +==================================+===================================================================+===============================================+
    |BL2_HEAP_SIZE                     | Size of the Bootloader (MCUboot) heap                             | if bl2 is built                               |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |BL2_MSP_STACK_SIZE                | (if bl2 is built) Size of the Bootloader (MCUboot) Main stack     | if bl2 is built                               |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |S_HEAP_SIZE                       | Size of the Secure (S) world Heap                                 | yes                                           |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |S_MSP_STACK_SIZE                  | Size of the Secure (S) world Main stack                           | yes                                           |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |S_PSP_STACK_SIZE                  | Size of the Secure (S) world Process stack                        | no for IPC model                              |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |NS_HEAP_SIZE                      | Size of the Non-Secure (NS) world Heap                            | if tfm_ns is built                            |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |NS_STACK_SIZE                     | Size of the Non-Secure (NS) world stack                           | if tfm_ns is built                            |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |PSA_INITIAL_ATTEST_MAX_TOKEN_SIZE | Size of the buffer that will store the initial attestation        | used by initial attestation partition         |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |TFM_ATTEST_BOOT_RECORDS_MAX_SIZE  | Size of buffer that can store the encoded list of boot records    | used by delegated attestation partition       |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |BL2_HEADER_SIZE                   | Size of the Header for the Bootloader (MCUboot)                   | if bl2 is built                               |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |BL2_TRAILER_SIZE                  | Size of the Trailer for the Bootloader (MCUboot)                  | if bl2 is built                               |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+
    |SHARED_SYMBOL_AREA_SIZE           | Size of shared common code between bl2 and tfm_s                  | if bl2 is built and want to reduce image size |
    +----------------------------------+-------------------------------------------------------------------+-----------------------------------------------+

    (OPTIONAL)

    If the TF-M common linker script is used then:

    +----------------------------------+-----------------------------------------------------------------------+-----------------------------------+
    |    name                          |        description                                                    | Requisiteness                     |
    +==================================+=======================================================================+===================================+
    |S_CODE_START                      | Start address for the S code                                          | Yes                               |
    +----------------------------------+-----------------------------------------------------------------------+-----------------------------------+
    |S_CODE_SIZE                       | Size of the S code                                                    | Yes                               |
    +----------------------------------+-----------------------------------------------------------------------+-----------------------------------+
    |S_DATA_START                      | Start address for the S data                                          | Yes                               |
    +----------------------------------+-----------------------------------------------------------------------+-----------------------------------+
    |S_DATA_SIZE                       | Size of the S data                                                    | Yes                               |
    +----------------------------------+-----------------------------------------------------------------------+-----------------------------------+
    |S_RAM_CODE_START                  | Start address for the S code                                          | if no XIP on flash                |
    +----------------------------------+-----------------------------------------------------------------------+-----------------------------------+
    |S_RAM_CODE_SIZE                   | Size of the S code                                                    | if no XIP on flash                |
    +----------------------------------+-----------------------------------------------------------------------+-----------------------------------+


#### CMSIS_Driver/Config/cmsis_driver_config.h:


    (location as defined in CMakeLists.txt)

    This file should include the CMSIS drivers implementation headers.


#### CMSIS_Driver/Config/RTE_Device.h:


    (location as defined in CMakeLists.txt)

    This is the Run-Time Environment file from CMSIS, which is there to allow
    enabling or disabling drivers prior to building. If your platform is
    designed as a general use platform, this file should contain all the
    available CMSIS drivers, and you should provide a recommended configuration.
    If your platform is designed for a specific use-case then you should
    reference and enable only the mandatory drivers.


#### CMSIS_Driver/Driver_Flash.c:


    (location as defined in CMakeLists.txt)

    TF-M relies on CMSIS Drivers, as such it requires the CMSIS functions to
    be implemented. As a platform owner you can decide to either implement the
    drivers in the CMSIS functions or to use the CMSIS functions as a shim to
    your native drivers.

    Refer to the CMSIS [FLASH](https://arm-software.github.io/CMSIS_6/latest/Driver/group__flash__interface__gr.html)
    documentation.


#### CMSIS_Driver/Driver_USART.c:


    (location as defined in CMakeLists.txt)

    TF-M relies on CMSIS Drivers, as such it requires the CMSIS functions to
    be implemented. As a platform owner you can decide to either implement the
    drivers in the CMSIS functions or to use the CMSIS functions as a shim to
    your native drivers.

    Refer to the CMSIS [USART](https://arm-software.github.io/CMSIS_6/latest/Driver/group__usart__interface__gr.html)
    documentation.


#### target_cfg.[ch]:


    (location as defined in CMakeLists.txt)

    It is expected that these files contain all platform specific code related
    to memory protection (e.g. SAU/PPC/MPC). These functions will not be called
    by TF-M directly, but are expected to be called from the function
    tfm_hal_set_up_static_boundaries() in tfm_hal_isolation.c.


#### tfm_hal_platform.c:


    (location as defined in CMakeLists.txt)

    Each platform is expected to implement the following API declared in
    platform/include/tfm_hal_platform.h

```c

enum tfm_hal_status_t tfm_hal_platform_init(void);

The function will be called before SPM initialization.
```

#### tfm_hal_isolation.c:


    (location as defined in CMakeLists.txt)

    Each platform is expected to implement all the functions declared in
    platform/include/tfm_hal_isolation.h.

    A reference implementation for Armv8-M platforms is provided in
    platform/ext/common/tfm_hal_isolation_v8m.c. Platforms using the common TF-M
    linker scripts and scatter files can use it to implement standard TF-M
    isolation with Armv8-M MPU regions. Platform-specific MPU regions can be
    appended by defining PLATFORM_STATIC_MPU_REGIONS in the platform's
    tfm_peripherals_def.h header.

    These functions will be called from TF-M.


#### tfm_platform_system.c:


    (location as defined in CMakeLists.txt)

    Each platform is expected to implement all the functions declared in
    platform/include/tfm_platform_system.h.


#### check_config.cmake:


    As a platform owner you may want to enforce some configuration or to prevent
    the use of unsupported configurations.

    This file (CMake format) allows you to do so by allowing you to check for
    invalid configuration values.

    This file is optional.

    TF-M build system already provides a generic configuration checker that will
    be called on top of one provided by the platform owner. The generic checker
    is located in <TF-M ROOT>/config/.

    [check_config.cmake_]


#### platform_svc_numbers.h


    (OPTIONAL)

    If your platform has its own SVC handling, then you need to

    - create the `platform_svc_numbers.h` which defines the platform SVC numbers.

      The bit [7] of the number must be set to 1 to reflect that it is a platform SVC number.
      The bit [6] indicates whether this SVC should be called from Handler mode or Thread mode.
      For more details of the bit assignments, please check the `svc_num.h`.
      TF-M provides two Macros `TFM_SVC_NUM_PLATFORM_THREAD(index)` and
      `TFM_SVC_NUM_PLATFORM_HANDLER(index)` to easily construct a valid number.

    - implement the platform_svc_handlers function which handles SVC.
    - enable `PLATFORM_SVC_HANDLERS` config option.


#### ns/CMakeLists.txt


    (MANDATORY)

    This is CMake script for building the platform support on NSPE side. It's
    copied to `<Artifact folder>` in the installation phase and instructs on
    how to build **platform_ns** target. The default NSPE build script expects
    this target definition and extends it with files, common for all TF-M platforms.

    Note::
```
This file shall define and use paths of installed directories in ``<Artifact folder>``,
instead of paths in TF-M platform folder.
```
    [NSCMakeLists.txt_]


#### ns/cpuarch_ns.cmake


    (MANDATORY for multi-core platforms)

    This file contains the hardware information for the NSPE CPU.
    It should be installed to `<Artifact folder>/platform` for NSPE build,
    ranamed to `ns/cpuarch_ns.cmake`.

    [ns/cpuarch_ns.cmake]
