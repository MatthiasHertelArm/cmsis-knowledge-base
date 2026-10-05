---
id: "spec-package-devices-family-element-package-devices-family-compile"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../compile"
summary: "Specify the CMSIS-Core compliant device header file and a device specific preprocessor define automatically included and set by the build tools. In case of devices embedding multiple processor cores, an additional core specific define can be specified."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Specify the CMSIS-Core compliant device header file and a device specific preprocessor define automatically included and set by the build tools.
In case of devices embedding multiple processor cores, an additional core specific define can be specified. In this case the Pname attribute becomes mandatory.
This element can occur on various levels. Multiple elements are allowed. The last occurrence in the hierarchy determines the effective
include path and define. It is required that each device has an effective header and define.

**Note:**
- In the example below, the device **STM32F407IG** will have a define `STM32F407IG.` Previous defines
  are overridden.
- It is good practice to add both attributes (`header` and `define)` in the attributes list of the 
  `compile` element together. This clarifies the relationship between header file and define.
- The name of the header file should be exported by the IDE to the RTE_Components_h file using the \#define CMSIS_device_header.
  
**Example**
```
<family Dfamily="STM32F4" Dvendor="STMicroelectronics:13">
  ...
  <compile   header="Device/Include/stm32f4xx.h"/>

  <subFamily DsubFamily="STM32F407">
    ...
    <compile  header="Device/Include/stm32f4xx.h" define="STM32F40XX"/>

    <device Dname="STM32F407IG">
      <compile  header="Device/Include/stm32f4xx.h" define="STM32F407IG"/>
    </device>
  </subFamily>
</family>
```



  | 
    Parents | 
    Element Chain | 
  

  | 
    family | 
    element_family | 
  

  | 
    subFamily | 
    element_subFamily | 
  

  | 
    device | 
    element_device | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Pname | 
    Processor identifier. This attribute **is mandatory for devices that embed multiple processors if the header and define is different for each processor**.
        Only alphabetical characters, decimal digits, '-' and '_' are allowed.  | 
   RestrictedString | 
    optional | 
  

  | 
    header | 
    CMSIS-Core compliant device header file with path relative to the pack's base folder. | 
    xs:string | 
    required | 
  

  | 
    define | 
    Device specific preprocessor define (macro). This macro is set in the pre-processor command line (-D\`<macro>`) and allows to
	    select device specific code during preprocessing of the application code, e.g. enabling/disabling device specific definitions in the device header file. | 
    xs:string | 
    required | 
  

    | 
    Pdefine | 
    This attribute can only be used for devices with multiple processor cores. It specifies a core specific preprocessor define (macro).
        This macro is set in the pre-processor command line (-D\`<macro>`) and allows to select processor specific code during preprocessing
		of the application code, e.g. enabling/disabling core specific definitions in the device header file. | 
    xs:string | 
    optional | 
  



\delim
