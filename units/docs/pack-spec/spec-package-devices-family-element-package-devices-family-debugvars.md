---
id: "spec-package-devices-family-element-package-devices-family-debugvars"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../debugvars"
summary: "Specify global debug access variables. Use these in addition to the pre-defined variables to pass user settings to debug access sequences."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Specify global debug access variables. Use these in addition 
to the pre-defined variables to pass user settings
to debug access sequences.



Define debug access variables with statements of the following form.
```
__var uservar = value;  // Comment: Define "uservar" and initialize to "value"
```

**Note:** 
- Initialization values must be constant unsigned numbers. No expressions are allowed.
- User-defined debug access variables are **read-only** in a debug access sequence.
- Pre-defined debug access variables cannot be set in this element.
- The `__` prefix is used for pre-defined debug access variables and for local
  variables in debugger-provided default sequence implementations. It should not be used
  for user-defined debug access variables or for local variables in DFP-provided sequences.
  If a debugger implementation copies a default sequence shown in this specification, it
  should add the `__` prefix to the local variable names.

**Example**
```

<family Dfamily="EFM32WG Series" Dvendor="Energy Micro:97">
  ...
  <debugvars configfile="Debug/EFM32WGxxx.dbgconf" version="1.0">
  
    __var TPIU_pinlocation = 0;  // Select one of four possible TPIU pin locations
    
    __var SWO_pinlocation  = 0;  // Select one of four possible SWO pin locations
    
  </debugvars>
  ...
  <sequences>
    <sequence name="TraceStart">
      ...
      <block if="TPIU_pinlocation == 2">
        ...
        <!-- Configure device to use pins as defined for TPIU pin location 2 -->
        ...
      </block>
      ...
    </sequence>
  </sequences>
  ...
  <debug __dp="0" __ap="0"/>
  ...
</family>
```


 



| Parents | Element Chain |  |  |
|---|---|---|---|
| family | element_family |  |  |
| subFamily | element_subFamily |  |  |
| device | element_device |  |  |
| Attributes | Description | Type | Use |
| configfile | Configuration file with path relative to the package base folder (extension *.DBGCONF). This file contains assignments of a default value to global debug access variables. This file gets copied to the project folder and is editable by the end-user. This file is read by the debugger after processing the global debug access variables. By editing the values of the debug access variables, the end-user effectively controls the behavior of sequences. The file can only assign new values but must not specify any new debug access variables. Configuration Wizard Annotations shall be used within the file to provide a graphical user interface for editing configuration options. | xs:string | optional |
| version | Version refers to the file version of the configfile attribute. If a configfile is specified the version attribute becomes mandatory. The version shall be incremented if any changes have been made to the global debug access variable names or default values. Based on the version information the tool environment will load a configfile with the version required by the debug description. The end-user may be required to update the settings after updating to a new version. | VersionType | optional |




 

**Example:** Configuration File 
```
// File: EFM32WGxxx.dbgconf 
// Version: 1.0
// <<< Use Configuration Wizard in Context Menu >>>
// <h>Trace Pin Setup
 // <o> TPIU Pin Location
//   <0=> Pin Location 0
//   <1=> Pin Location 1
//   <2=> Pin Location 2
//   <3=> Pin Location 3
// <i> Select TPIU pin location for your board configuration:
// <i> - Pin Location 0 (TRACECLK: PD7, TRACEDATA0: PD6, TRACEDATA1: PD3,  TRACEDATA2: PD4,  TRACEDATA3: PD5)
// <i> - Pin Location 1 (TRACECLK: PF8, TRACEDATA0: PF9, TRACEDATA1: PD13, TRACEDATA2: PB15, TRACEDATA3: PF3)
// <i> - Pin Location 2 (TRACECLK: PC6, TRACEDATA0: PC7, TRACEDATA1: PD3,  TRACEDATA2: PD4,  TRACEDATA3: PD5)
// <i> - Pin Location 3 (TRACECLK: PA6, TRACEDATA0: PA2, TRACEDATA1: PA3,  TRACEDATA2: PA4,  TRACEDATA3: PA5)
// <i> Default: Pin Location 0
TPIU_pinlocation = 0;
  
// <o> SWO Pin Location
//   <0=> Pin Location 0
//   <1=> Pin Location 1
//   <2=> Pin Location 2
//   <3=> Pin Location 3
// <i> Select SWO pin location for your board configuration:
// <i> - Pin Location 0 (SWO: PF2)
// <i> - Pin Location 1 (SWO: PC15)
// <i> - Pin Location 2 (SWO: PD1)
// <i> - Pin Location 3 (SWO: PD2)
// <i> Default: Pin Location 0
SWO_pinlocation = 0;
  
// </h>
// <<< end of configuration section >>>
```
