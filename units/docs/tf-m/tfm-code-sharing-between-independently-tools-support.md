---
id: "tfm-code-sharing-between-independently-tools-support"
type: "concept"
domain: "security"
title: "Code sharing between independently linked XIP binaries: Tools support"
summary: "All the currently supported compilers provide a way to achieve the above objectives. However, there is no standard way, which means that the code sharing functionality must be implemented on a per compiler basis. The following steps are needed:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/code_sharing.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/code_sharing.html#tools-support"
license: "BSD-3-Clause"
mode: "V"
---

All the currently supported compilers provide a way to achieve the above
objectives. However, there is no standard way, which means that the code sharing
functionality must be implemented on a per compiler basis. The following steps
are needed:

 - Extraction of the addresses of all global symbols.
 - The filtering out of the addresses of symbols that aren't shared. The goal is
   to not need to list all the shared symbols by name. Only a simple pattern
   has to be provided, which matches the beginning of the symbol's name.
   Matching symbols will be shared. Examples are in :
   `bl2/shared_symbol_template.txt`
 - Provision of the addresses of shared symbols to the linker during the SPE
   build process.
 - The resolution of symbol collisions during SPE linking. Because mbed-crypto
   is linked to both firmware components as a static library, the external
   shared symbols will conflict with the same symbols found within it. In order
   to prioritize the external symbol, the symbol with the same name in
   mbed-crypto must be marked as weak in the symbol table.

The above functionalities are implemented in the toolchain specific CMake files:

 - `toolchain_ARMCLANG.cmake`
 - `toolchain_GNUARM.cmake`

By the following two functions:

 - `target_share_symbols()`: Extract and filter shared symbol addresses
   from MCUboot.
 - `target_link_shared_code()`: Link shared code to the SPE and resolve symbol
   conflict issues.


### ARMCLANG

The toolchain specific steps are:

 - Extract all symbols from MCUboot: add `-symdefs` to the compiler command line
 - Filter shared symbols: call CMake script `FilterSharedSymbols.cmake`
 - Weaken duplicated (shared) symbols in the mbed-crypto static library that are
   linked to the SPE: `arm-none-eabi-objcopy`
 - Link shared code to SPE: Add the filtered output of `-symdefs` to the SPE
   source file list.


### GNUARM

The toolchain specific steps are:

 - Extract all symbols from MCUboot: `arm-none-eabi-nm`
 - Filter shared symbols: call CMake script: `FilterSharedSymbols.cmake`
 - Strip unshared code from MCUboot:  `arm-none-eabi-strip`
 - Weaken duplicated (shared) symbols in the mbed-crypto static library that are
   linked to the SPE: `arm-none-eabi-objcopy`
 - Link shared code to SPE: Add `-Wl -R <SHARED_STRIPPED_CODE.axf>` to the
   compiler command line


### IAR

Functionality currently not implemented, but the toolchain supports doing it.
