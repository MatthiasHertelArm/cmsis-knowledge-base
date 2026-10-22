---
id: "mlek-implementing-custom-ml-application-adding-custom-platform-support"
type: "concept"
domain: "edge-ai"
title: "Implementing custom ML application: Adding custom platform support"
summary: "Platform build configuration script build_configuration.cmake is the main build entry point for platform sources. It is used by top level CMakeLists.txt script to add a platform into the public build stream. Platform build configuration script must have 2 functions:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@138a9c0:docs/sections/customizing.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/138a9c0/docs/sections/customizing.md#adding-custom-platform-support"
license: "Apache-2.0"
mode: "V"
---

Platform build configuration script `build_configuration.cmake` is the main build entry point for platform sources.
It is used by top level CMakeLists.txt script to add a platform into the public build stream.
Platform build configuration script must have 2 functions:

- `set_platform_global_defaults` - to set platform source locations and other build options.
- `platform_custom_post_build` - to execute specific post build steps.

The function `set_platform_global_defaults` must set `PLATFORM_DRIVERS_DIR` variable

```cmake
    set(PLATFORM_DRIVERS_DIR "${MLEK_HAL_PLATFORM_DIR}/mps3" PARENT_SCOPE)
```

location of the platform library sources.

> **Convention:**  The default search path for platform build configuration scripts is in `scripts/cmake/platforms`.
> The directory name for a platform configuration script is also used as a value for `TARGET_PLATFORM`
> build option. For example:
> `scripts/cmake/platforms/my_platform` results in having `my_platform` as a `TARGET_PLATFORM` option for the build.

The function `platform_custom_post_build` could be used to add platform specific post use-case application build steps.

Repository's root level CMakeLists.txt calls common utility function

```cmake
add_platform_build_configuration(TARGET_PLATFORM ${TARGET_PLATFORM})
```
to add given target platform to the build stream. The function finds the script and includes `build_configuration.cmake`
file. After that public build can invoke:

- `set_platform_global_defaults`
- `platform_custom_post_build`

for a specified platform.

New platform sources, that are pointed to by `PLATFORM_DRIVERS_DIR` variable, could be placed anywhere, conventional location
is `source/hal/platform`. Platform must be a separate CMake project with CMakeLists.txt script and build into a static
library `libplatform-drivers.a`.
HAL expects platform to have `platfrom_drivers.h`  header file with required interfaces for included peripherals.

If the new platform uses existing cmsis device project then it should be linked with it like this:

```cmake
    target_link_libraries(${PLATFORM_DRIVERS_TARGET} PUBLIC cmsis_device)
```

Cmsis device exposes an entry point `--entry Reset_Handler` as a link interface.

If the new platform defines custom cmsis device and has custom application entry point,
it must tell linker about it like this:

```cmake
    target_link_options(${PLATFORM_DRIVERS_TARGET} INTERFACE --entry `<custom handler name>`)
```

Most of the ML use-case applications use UART driven standard output (stdout), and LCD. It is therefore a hard
requirement to implement at least stubs for those. LCD driver must provide implementation for functions declared in
`lcd_img.h` header. The LCD component under HAL sources provides an implementation for MPS3's LCD peripheral as well
as a stub. The application linking to the library produced by LCD has a choice of picking either target. For example,
the MPS3 platform implementation has:

```cmake
target_link_libraries(${PLATFORM_DRIVERS_TARGET} PUBLIC
    `<other libs>`
    hal_display_mps3)
```

The standard output (stdout) component follows the same convention. It can expose three targets:

- `stdout_retarget_cmsdk`
- `stdout_retarget_pl011`

The two targets use the UART, pulling in `CMSDK UART` and `PL011 UART` drivers respectively. It is also possible to run
applications with semihosting enabled where stardard output and error streams should use the host machine console,
typically via a debugger. To enable this, the CMake toolchain files implement a function called `configure_semihosting`.
For supported targets semihosting is disabled by default, but can be enabled using CMake configuration option
`SEMIHOSTING_ENABLED`.

Other re-usable component is the NPU. It wraps the Arm Ethos-U NPU driver sources with functions that can be called
from the platform initialisation routine. In addition to general utility functions, this component also provides
**cache invalidation overrides** for the `weak` implementations available in the driver. This is useful for custom
targets that use the data cache for the target CPU (typically enabled somewhere in the start-up code for the system).
The driver will call these functions for invalidating data cache (memory regions the NPU has written to).

> **Note**: To do the Arm Ethos-U interrupt set up, the NPU component should be provided with the base address of the
> NPU as well as the IRQ number wired to the CPU. To set this up, the NPU component relies on the system specific
> header files made available by the CMake interface target provided by the `cmsis_device` CMake project. If this
> target is not used by the new custom platform implementation, the NPU component target must be given access to an
> "RTE_Components.h" header in some way. This header should pull in the required definitions for functions like
> `SCB_InvalidateDCache` and `NVIC_SetVector`. The pre-processor definitions like `__DCACHE_PRESENT` are also expected
> to be exposed via the same header.

Examples of the standard output, LCD and NPU components can be found here: `source/hal/source/components`.

Linker scripts for all supported toolchains should be added. The location of the files is on your discretion.
The new platform build configuration script must add it in the `platform_custom_post_build` function like this:

```cmake
    get_target_property(target_linker_script_override
            ${PARSED_TARGET_NAME}
            MLEK_LINKER_SCRIPT_OVERRIDE_PATH)
    set(default_linker_script_path
            "${CMAKE_CURRENT_FUNCTION_LIST_DIR}/${TARGET_SUBSYSTEM}/${LINKER_SCRIPT_NAME}${LINKER_SCRIPT_SUFFIX}")
    resolve_linker_script_path(
            linker_script_path
            "${default_linker_script_path}"
            "${target_linker_script_override}")

    add_linker_script(
            ${PARSED_TARGET_NAME}  # Target
            ${linker_script_path}) # Full linker control file path
```

Please see existing platforms sources and build scripts for more details.
