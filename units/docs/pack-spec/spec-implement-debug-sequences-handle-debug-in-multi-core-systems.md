---
id: "spec-implement-debug-sequences-handle-debug-in-multi-core-systems"
type: "concept"
domain: "pack"
title: "Implement debug sequences: Handle debug in multi-core systems"
summary: "To correctly debug multicore systems, first of all the debug connection shall be correctly specified using <debug>. See dbg_debug for description and examples."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_debug_sqns.html"
license: "Apache-2.0"
mode: "V"
---

To correctly debug multicore systems, first of all the debug connection shall be correctly specified using `<debug>`. See dbg_debug for description and examples.

To achieve correct debug operation on a multi-core system often modification of the predefined debug sequences are required. The actual implementation very much depends on the particular system architecture.

The usage_of_sequences provides example flows for debugger operation. These flows shall be analyzed for particular system and different implementations may be required for each available core.

Recommendations described in previous sections such as error-handling, trace configuration, bootloader support can be applied for individual cores in the multi-core system as well. Using the **Pname** identifier in the `<sequence>`  element it is possible to specify the debug access sequence for a particular core.

The most multi-core Cortex-M systems have their CPUs intended for running different applications and not for load balancing. For simplicity we consider further such an assymmetric (AMP) dual-core system. In this system the CPUs can have either equal roles or master-slave dependancy. The roles can also be either predefined or configurable.

Sections below explain additional use-cases specific for multi-core systems:

 - dbg_sqns_multicore_reset
 - dbg_sqns_multicore_debug


### Reset sequences


Multi-core devices often have quite unique reset systems that a debugger shall use correctly when connecting to a target and during debug operation. For that the default reset debug sequences (see dbg_sqns_reset) need to be overwritten or require processor-specific implementations. Below is an overview for different reset types:

 - resetHardware is a hardware-triggered system-wide reset and should not be differentiated per individual core. However its default implementation may need to be overwritten in order to take the system configuration into account (master-slave, etc.).
 - resetSystem is a software-triggered system-wide reset. It is assumed to be applied to the whole system and shouldn't be core-specific. But same as with **ResetHardware** it may require different implementation, for example to ensure correct reset in master-slave systems.
 - resetProcessor is a software-triggered local reset for the specified CPU (or if required CPU subsystem). It needs to be differentiated for each core and is done by overwriting predefined **ResetProcessor** sequence for each CPU. Custom debug access sequences can be used to simplify code structure as shown in the example below:

```
    <sequences>
    //-- Begin: ResetProcessor Sequence for Cortex-M4
      <sequence name="ResetProcessor" Pname="CM4">
        <block>
          Sequence("ResetProcessor_CM4");
        </block>
      </sequence>

    //-- Begin: ResetProcessor Sequence for Cortex-M0
      <sequence name="ResetProcessor" Pname="CM0plus">
        <block>
          Sequence("ResetProcessor_CM0plus");
        </block>
      </sequence>
      ...
    </sequences>
```

In the example above the reset functionality itself is implemented in the user-defined (custom) debug sequences `ResetProcessor_CM0plus` and `ResetProcessor_CM4.`

The same **Pname** identifier shall be used in `<sequence>` element as defined in the corresponding `<processor>` element ('CM0plus' or 'CM4' in this example).

Following the same concept the resetCatchSet and resetCatchClear sequences may need to be overwritten for individual cores, as reset vectors for different cores are located in different areas and hence the breakpoint for halt after reset shall be set differently. The approach is very similar to the one described in dbg_sqns_boot.


### Debug sequences for different use cases


When debugging an application running on a processor in a multi-core system, it is often required to have special control over the processors in the system. For example in a master-slave system it may be desired to debug only the application on the slave. For that debugger needs to ensure that the slave is running independent from the master.  Debug-related sequence debugCoreStart can be used for that. Below is an example for NXP LPC4300 family, with **ReleaseM0OnConnect** is a configuration parameter specified via *.dbgconf as explained in dbg_sqns_dbgconf.
```
    <sequence name="DebugCoreStart" Pname="Cortex-M0">
      <block>
        // Default implementation
        // Enable Core Debug via DHCSR
        Write32(0xE000EDF0, 0xA05F0001);
      </block>

      <control if="ReleaseM0OnConnect">
        <block>
          // Release M0 from reset
          Write32(0x40053104, 0x00000000);  // RESET_CTRL1: Clear M0APP_RST (Bit 24)
        </block>
      </control>
    </sequence>
```
