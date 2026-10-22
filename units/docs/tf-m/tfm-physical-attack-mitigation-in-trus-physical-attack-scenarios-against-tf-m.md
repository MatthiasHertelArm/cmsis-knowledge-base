---
id: "tfm-physical-attack-mitigation-in-trus-physical-attack-scenarios-against-tf-m"
type: "concept"
domain: "security"
title: "Physical attack mitigation in Trusted Firmware-M: TF-M Threat Model against physical attacks / Physical attack scenarios against TF-M"
summary: "Part of: TF-M Threat Model against physical attacks"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/tfm_physical_attack_mitigation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_physical_attack_mitigation.html#physical-attack-scenarios-against-tf-m"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: TF-M Threat Model against physical attacks_

Based on the analysis above, a malicious actor may perform physical attacks
against critical operations in `SPE` workflow and critical modules in
TF-M, to indirectly gain unauthenticated accesses to assets.

Those critical operations and modules either directly access the assets or
protect the assets from disclosure. Those operations and modules can include:

  - Image validation in bootloader
  - Isolation management in TF-M, including platform specific configuration
  - Cryptographic operations
  - TF-M Secure Storage operations
  - PSA client permission check in TF-M

The detailed scenarios are discussed in following sections.


#### Physical attacks against bootloader

Physical attacks may bypass secure image validation in bootloader and a
malicious image can be installed.

The countermeasures is bootloader specific implementation and out of the scope
of this document. TF-M relies on MCUboot by default. MCUboot has already
implemented countermeasures against fault injection attacks [3]_.


#### Physical attacks against TF-M SPM

TF-M SPM initializes and manages the isolation configuration. It also performs
permission check against secure service requests from PSA clients.


##### Static isolation configuration

It is TF-M SPM's responsibility to build up isolation during the initialization
phase. If this is missed or not done correctly then it might be possible for
non-secure code to access some secure memory area or an external device can
access assets in the device through a debug port.

Therefore, hindering the setup of memory or peripheral isolation hardware is an
obvious candidate for physical attacks. The initialization phase has a constant
time execution (like the previous boot-up state), therefore the timing of the
attack is simpler, compared to cases when secure and non-secure runtime firmware
is up-and-running for a while and IRQs make timing unpredictable.

Some examples of attacking isolation configuration are shown in the list below.

  - Hinder the setting of security regions. Try to execute non-secure code as
    secure.
  - Manipulate the setting of secure regions, try to extend the non-secure
    regions to cover a memory area which otherwise is intended to be secure
    area.
  - Hinder the setting of isolation boundary. In this case vulnerable ARoT code
    has access to all memory.
  - Manipulate peripheral configuration to give access to non-secure code to a
    peripheral which is intended to be secure.


##### PSA client permission checks

TF-M SPM performs several permission checks against secure service requests from
a PSA client, such as:

- Check whether the PSA client is a non-secure client or a secure client

  NS client's PSA client ID is negative. NS client is not allowed to directly
  access secure areas. A malicious actor can inject faults when TF-M SPM
  authenticates a NS client. It may manipulate TF-M to accept it as a secure
  client and allow the NS client to access assets.

- Memory access checks

  TF-M SPM checks whether the request has correct permission to access a secure
  memory area. A malicious actor can inject faults when TF-M SPM checks memory
  access permission. It may skip critical check steps or corrupt the check
  result. Thereby a malicious service request may pass TF-M memory access check
  and accesses assets which it is not allowed to.

The physical attacks mentioned above relies on the a malicious NS application or
a vulnerable RoT service to start a malicious secure service request to access
the assets. The malicious actor has to be aware of the accurate timing of
dealing with the malicious request in TF-M SPM. The timing can be affected by
other clients and interrupts.
It should be more difficult than pure fault injection.


##### Dynamic isolation boundary configuration

Physical attack may affect the isolation boundary setting during TF-M context
switch, especially in Isolation Level 3. For example:

  - A fault injection may cause TF-M SPM to skip clear privileged state before
    switching in an ARoT service.
  - A fault injection may cause TF-M SPM to skip updating MPU regions and
    therefore the next RoT service may access assets belonging to a previous
    one.

However, it is much more difficult to find out the accurate timing of TF-M
context switch, compared to other scenarios in TF-M SPM. It also requires a
vulnerable RoT service to access assets after fault injection.


#### Physical attacks against TF-M Crypto service

Since crypto operations are done by TF-PSA-Crypto library or by a custom crypto
accelerator engine and its related software driver stack, the analysis of
physical attacks against crypto operations is out-of-scope for this document.
However, in general the same requirements are applicable for the crypto, to be
compliant with PSA Level 3 certification. That is, it must be resistant against
physical attacks. So crypto software and hardware must be hardened against
side-channel and physical attacks.


#### Physical attacks against Secure Storage


###### Physical attacks against Internal Trusted Storage

Based on the assumption in attacker-capability, a malicious actor is
unable to directly retrieve assets via physical attacks against
`Internal Trusted Storage` (ITS).

Instead, a malicious actor can inject faults into isolation configuration of ITS
area in TF-M SPM to gain the access to assets stored in ITS. Refer to
physical-attacks-spm for details.


##### Physical attacks against Protected Storage

Based on the assumption in attacker-capability, a malicious actor can be
able to directly access external storage device.
Therefore `Protected Storage` (PS) shall enable encryption and
authentication by default to detect tampering with the content in external
storage device.

A malicious actor can also inject faults into isolation configuration of PS and
external storage device peripherals in TF-M SPM to gain the access to assets
stored in PS. Refer to physical-attacks-spm for details.

It is out of the scope of TF-M to fully prevent malicious actors from directly
tampering with or retrieving content stored in external storage devices.


#### Physical attacks against platform specific implementation

Platform specific implementation includes critical TF-M HAL implementations.
A malicious actor can perform physical attack against those platform specific
implementations to bypass the countermeasures in TF-M common code.


##### Platform early initialization

TFM provides a HAL API for platforms to perform HW initialization before SPM
initialization starts.
The system integrator is responsible to implement this API on a particular SoC
and harden it against physical attacks:

```c

enum tfm_hal_status_t tfm_hal_platform_init(void);
```
The API can have several initializations on different modules. The system
integrator can choose to even harden some of these initializations functions
within this platform init API. One of the examples is the debug access setting.


###### Debug access setting

TF-M configures debug access according to device lifecycle and accessible debug
certificates. In general, TF-M locks down the debug port if the device is in
secure production state.
The system integrator can put the settings into an API and harden it against
physical attacks.


##### Platform specific isolation configuration

TFM SPM exposes a HAL API for static and dynamic isolation configuration. The
system integrator is responsible to implement these API on a particular SoC and
harden it against physical attacks.

```c

enum tfm_hal_status_t tfm_hal_set_up_static_boundaries(void);
enum tfm_hal_status_t tfm_hal_bind_boundary(const struct partition_load_info_t *p_ldinf,
                                            uintptr_t *p_boundary);
```

##### Memory access check

TFM SPM exposes a HAL API for platform specific memory access check. The
system integrator is responsible to implement this API on a particular SoC and
harden it against physical attacks.

```c

tfm_hal_status_t tfm_hal_memory_check(uintptr_t boundary,
                                      uintptr_t base,
                                      size_t size,
                                      uint32_t access_type);

## TF-M countermeasures against physical attacks

This section propose a design of software countermeasures against physical
attacks.


### Fault injection hardening library

There is no open-source library which implements generic mitigation techniques
listed in phy-att-countermeasures.
TF-M project implements a portion of these techniques. TF-M software
countermeasures are implemented as a small library Fault Injection Hardening
(FIH) in TF-M code base. A similar library was first introduced and tested in
the MCUboot project (version 1.7.0) [2]_ which TF-M relies on.

The FIH library is put under TF-M `lib/fih/`.

The implementation of the different techniques was assigned to fault injection
protection profiles. Four profiles (OFF, LOW, MEDIUM, HIGH) were introduced to fit
better to the device capability (memory size, TRNG availability) and to
protection requirements mandated by the device threat model. Fault injection
protection profile is configurable at compile-time, default value: OFF.

Countermeasure profiles and corresponding techniques are listed in the table
below.

+--------------------------------+-------------+----------------+--------------+------------------+
|        Countermeasure          | Profile LOW | Profile MEDIUM | Profile HIGH | Comments         |
+================================+=============+================+==============+==================+
| Control flow monitor           | Y           | Y              | Y            |                  |
+--------------------------------+-------------+----------------+--------------+------------------+
| Failure loop hardening         | Y           | Y              | Y            |                  |
+--------------------------------+-------------+----------------+--------------+------------------+
| Complex constant               |             | Y              | Y            |                  |
+--------------------------------+-------------+----------------+--------------+------------------+
| Redundant variables and checks |             | Y              | Y            |                  |
+--------------------------------+-------------+----------------+--------------+------------------+
| Random delay                   |             |                | Y            | Implemented, but |
|                                |             |                |              | depends on HW    |
|                                |             |                |              | capability       |
+--------------------------------+-------------+----------------+--------------+------------------+

Similar to MCUboot, four profiles are supported. It can be configured at build
time by setting (default is OFF):

  `-DTFM_FIH_PROFILE=<OFF, LOW, MEDIUM, HIGH>`


### How to use FIH library

As analyzed in phy-att-threat-model, this section focuses on integrating
FIH library in TF-M SPM to mitigate physical attacks.

  - Identify critical function call path which is mandatory for configuring
    isolation or debug access. Change their return types to `FIH_RET_TYPE` and
    make them return with `FIH_RET`. Then call them with `FIH_CALL`. These macros
    are providing the extra checking functionality (control flow monitor, redundant
    checks and variables, random delay, complex constant) according to the profile
    settings. More details about usage can be found here:
    `trusted-firmware-m/lib/fih/inc/fih.h`

    Take simplified TF-M SPM initialization flow as an example:

```c

main()
  |
  |--> tfm_core_init()
  |           |
  |           |--> tfm_hal_set_up_static_boundaries()
  |           |                  |
  |           |                  |--> platform specific isolation impl.
  |           |
  |           |--> tfm_hal_platform_init()
  |                              |
  |                              |--> platform specific init
  |
  |--> During each partition initialization
              |
              |--> tfm_hal_bind_boundary()
                                 |
                                 |--> platform specific peripheral isolation impl.
```
  - Might make the important setting of peripheral config register redundant
    and verify them to match expectations before continue.

  - Implements an extra verification function which checks the critical hardware
    config before secure code switches to non-secure. Proposed API for this
    purpose:

```c

fih_int tfm_hal_verify_static_boundaries(void);
```
    This function is intended to be called just after the static boundaries are
    set up and is responsible for checking all critical hardware configurations.
    The goal is to catch if something is missed and act according
    to system policy. The introduction of one more checking point requires one
    more intervention with precise timing. The system integrator is responsible
    to implement this API on a particular SoC and harden it against physical
    attacks. Make sure that all platform dependent security feature is properly
    configured.

  - The most powerful mitigation technique is to add random delay to the code
    execution. This makes the timing of the attack much harder. However it
    requires an entropy source. It is recommended to use the `HIGH` profile
    when hardware support is available. There is a porting API layer to fetch
    random numbers in FIH library:

```c

void fih_delay_init(void);
uint8_t fih_delay_random(void);
```
  - Similar countermeasures can be implemented in critical steps in platform
    specific implementation.

    Take memory isolation settings on AN521 platform as an example.
    The following hardware components are responsible for memory isolation in a
    SoC, which is based on SSE-200 subsystem.
    System integrators must examine the chip specific memory isolation solution,
    identify the key components and harden the configuration of those.
    This list just serves as an example here for easier understanding:

      - Implementation Defined Attribution Unit (IDAU): Implementation defined,
        it can be a static config or dynamic.
        Contains the default security access permissions of the memory map.
      - SAU: The main module in the CPU to determine the security settings of
        the memory.
      - `MPC`: External module from the CPU point of view. It protects the
        non security aware memories from unauthenticated access. Having a
        properly configured MPC significantly increases the security of the
        system.
      - `PPC`: External module from the CPU
        point of view. Protects the non security aware peripherals from
        unauthenticated access.
      - MPU: Protects memory from unprivileged access. ARoT code has only a
        restricted access in secure domain. It mitigates that a vulnerable or
        malicious ARoT partition can access to device assets.

    The following AN521 specific isolation configuration functions
    shall be hardened against physical attacks.

```c

sau_and_idau_cfg()
mpc_init_cfg()
ppc_init_cfg()
```
    Some platform specific implementation rely on platform standard device
    driver libraries. It can become much more difficult to maintain drivers if
    the standard libraries are modified with FIH library. Platform specific
    implementation can implement duplicated execution and redundant variables/
    condition check when calling platform standard device driver libraries
    according to usage scenarios.


### Impact on memory footprint

The addition of protection code against physical attacks increases the memory
footprint. The actual increase depends on the selected profile and where the
mitigation code is added.


### Attack experiment with SPM

The goal is to bypass the setting of memory isolation hardware with simulated
instruction skips in fast model execution (FVP_MPS2_AEMv8M) in order to execute
the regular non-secure test code in secure state. This is done by identifying
the configuration steps which must be bypassed to make this happen. The
instruction skip simulation is achieved by breakpoints and manual manipulation
of the program counter. The following steps are done on AN521 target, but this
can be different on another target:

  - Bypass the configuration of isolation HW: SAU, MPC.
  - Bypass the setting of the PSP limit register. Otherwise, a stack overflow
    exception will happen. Because the secure PSP will be overwritten by the
    address of the non-secure stack and on this particular target the non-secure
    stack is on lower address than the value in the secure PSP_LIMIT register.
  - Avoid the clearing of the least significant bit in the non-secure entry
    point, where BLXNS/BXNS is jumping to non-secure code. Having the least
    significant bit cleared indicates to the hardware to switch security state.

The previous steps are enough to execute the non-secure Reset_Handler() in
secure state. Usually, RTOS is executing on the non-secure side. In order to
properly boot it up further steps are needed:

  - Set the S_VTOR system register to point the address of the NS Vector table.
    Code is executed in secure state therefore when an IRQ hit then the handler
    address is fetched from the table pointed by S_VTOR register. RTOS usually
    do an SVC call at start-up. If S_VTOR is not modified then SPM's SVC handler
    will be executed.
  - TBC: RTX osKernelStart still failing.

The bottom line is that in order to execute the regular non-secure code in
secure state the attacker need to interfere with the execution flow at many
places. Successful attack can be made even harder by adding the described
mitigation techniques and some random delays.



## Reference


.. [1] [PSA Certified Level 3 Lightweight Protection Profile](https://www.psacertified.org/app/uploads/2020/11/JSADEN009-PSA_Certified_Level_3_LW_PP-1.0-ALP02.pdf)

.. [2] [MCUboot project - fault injection hardening](https://github.com/mcu-tools/mcuboot/blob/master/boot/bootutil/include/bootutil/fault_injection_hardening.h)

.. [3] [MCUboot fault injection mitigation](https://www.trustedfirmware.org/docs/TF-M_fault_injection_mitigation.pdf)

--------------------------------

*SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors*

*SPDX-License-Identifier: BSD-3-Clause*
