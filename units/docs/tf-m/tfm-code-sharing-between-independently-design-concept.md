---
id: "tfm-code-sharing-between-independently-design-concept"
type: "concept"
domain: "security"
title: "Code sharing between independently linked XIP binaries: Design concept"
summary: "The bootloader is sometimes implemented as ROM code (BL1) or stored in a region of the flash which is lockable, to prevent tampering."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/software/code_sharing.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/software/code_sharing.html#design-concept"
license: "BSD-3-Clause"
mode: "V"
---

The bootloader is sometimes implemented as ROM code (BL1) or stored in a region
of the flash which is lockable, to prevent tampering. In a secure system, the
bootloader is immutable code and thus implements a part of the Root of Trust
anchor in the device, which is trusted implicitly. The shared code is primarily
part of the bootloader, and is reused by the runtime SPE firmware at a later
stage. Not all of the bootloader code is reused by the runtime SPE, only some
cryptographic functions.

Simplified steps of building with code sharing enabled:

  - Complete the bootloader build process to have a final image that contains
    the absolute addresses of the shared functions, and the global variables
    used by these functions.
  - Extract the addresses of the functions and related global variables that are
    intended to be shared from the bootloader executable.
  - When building runtime firmware, provide the absolute addresses of the shared
    symbols to the linker, so that it can pick them up, instead of instantiating
    them again.

The execution flow looks like this:

```bash

SPE        MCUboot func1()    MCUboot func2()     MCUboot func3()
 |
 |     Hash()
 |------------->|
                |----------------->|
                                   |
                      Return       |
      Return    |<-----------------|
 |<-------------|
 |
 |
 |----------------------------------------------------->|
                                                        |
         Function pointer in shared global data()       |
 |<-----------------------------------------------------|
 |
 |                       Return
 |----------------------------------------------------->|
                                                        |
                         Return                         |
 |<-----------------------------------------------------|
 |
 |
```
The execution flow usually returns from a shared function back to the SPE with
an ordinary function return. So usually, once a shared function is called in the
call path, all further functions in the call chain will be shared as well.
However, this is not always the case, as it is possible for a shared function to
call a non-shared function in SPE code through a global function pointer.

For shared global variables, a dedicated data section must be allocated in the
linker configuration file. This area must have the same memory address in both
MCUboot's and the SPE's linker files, to ensure the integrity of the variables.
For simplicity's sake, this section is placed at the very beginning of the RAM
area. Also, the RAM wiping functionality at the end of the secure boot flow
(that is intended to remove any possible secrets from the RAM) must not clear
this area. Furthermore, it must be ensured that the linker places shared globals
into this data section. There are two way to achieve this:

 - Put a filter pattern in the section body that matches the shared global
   variables.
 - Mark the global variables in the source code with special attribute
   `__attribute__((section(<NAME_OF_SHARED_SYMBOL_SECTION>)))`

RAM memory layout in MCUboot with code sharing enabled:

```bash

+------------------+
|  Shared symbols  |
+------------------+
| Shared boot data |
+------------------+
|      Data        |
+------------------+
|    Stack (MSP)   |
+------------------+
|      Heap        |
+------------------+
```
RAM memory layout in SPE with code sharing enabled:

```bash

+-------------------+
|  Shared symbols   |
+-------------------+
| Shared boot data  |
+-------------------+
|    Stack (MSP)    |
+-------------------+
|    Stack (PSP)    |
+-------------------+
| Partition X Data  |
+-------------------+
| Partition X Stack |
+-------------------+
          .
          .
          .
+-------------------+
| Partition Z Data  |
+-------------------+
| Partition Z Stack |
+-------------------+
|     PRoT Data     |
+-------------------+
|       Heap        |
+-------------------+
```

### Patching Mbed TLS

In order to share some global function pointers from mbed-crypto that are
related to dynamic memory allocation, their scope must be extended from private
to global. This is needed because some compiler toolchain only extract the
addresses of public functions and global variables, and extraction of addresses
is a requirement to share them among binaries. Therefore, a short patch was
created for the mbed-crypto library, which "globalises" these function pointers:

`lib/ext/mbedcrypto/0002-Enable-crypto-code-sharing-between-independent-binar.patch`

The patch needs to be manually applied in the Mbed TLS repo, if code sharing is
enabled. The patch has no effect on the functional behaviour of the
cryptographic library, it only extends the scope of some variables.
