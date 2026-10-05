---
id: "spec-package-components-element"
type: "concept"
domain: "pack"
title: "/package/components element"
summary: "The element elementcomponents describes software components contained in the Pack. A component lists the files that belong to a component and that are relevant for a project."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

The element element_components describes software components contained in the Pack.
A component lists the files that belong to a component and that are relevant for a project. 
The component itself or each individual file may refer to a condition that
must resolve to true; if it is false the component or file is not applicable in the given context.

Each component must have a class (Cclass=), a group (Cgroup=), and a version (Cversion=) which is
used to identify the component. Optionally, a component may have a bundle (Cbundle=), sub-group (Csub=)
and variant (Cvariant=) to add further categories. A component is identified by the class/bundle,
group, sub-group, variant and version information together with the vendor specified by the pack or
explicitly specifying the (Cvendor=) for a component. The component vendor must ensure that the
combination of class/bundle, group, sub-group, version, and variant is unique and not used by multiple
components (after evaluating filter conditions).

Note: The selection of multiple variants of the same component is mutually exclusive and must not be
supported by tools. Graphical user interfaces may use drop down boxes for selecting a component variant.

**Example**
```
<package>
  ...
  <components>
    <!-- component has dependency described by "CMSIS Core" condition -->
    <component Cclass="CMSIS" Cgroup="Core" Cversion="3.1.0" condition="CMSIS Core">
      <description>CMSIS-Core (Cortex-M) for Cortex-M, SC000, and SC300 processor.</description>
      <files>
        <!-- CPU independent -->
        <file category="doc"    name="CMSIS/Documentation/Core/html/index.html"/>
        <file category="header" name="CMSIS/Include/core_cmFunc.h"/>
        <file category="header" name="CMSIS/Include/core_cmInstr.h"/>
        <!-- CPU dependent -->
        <file category="header" condition="CM0"   name="CMSIS/Include/core_cm0.h"/>
        <file category="header" condition="CM0+"  name="CMSIS/Include/core_cm0plus.h"/>
        <file category="header" condition="CM3"   name="CMSIS/Include/core_cm3.h"/>
        <file category="header" condition="CM4"   name="CMSIS/Include/core_cm4.h"/>
        <file category="header" condition="CM4"   name="CMSIS/Include/core_cm4_simd.h"/>
        <file category="header" condition="SC000" name="CMSIS/Include/core_sc000.h"/>
        <file category="header" condition="SC300" name="CMSIS/Include/core_sc300.h"/>
      </files>
    </component>

    <component Cclass="CMSIS" Cgroup="DSP" Cversion="1.1.0" condition="CMSIS DSP">
      <description>CMSIS-DSP Library for Cortex-M0, Cortex-M3 and Cortex-M4 as well as SC000 and SC300 processor based devices</description>
      <files>
        <!-- CPU independent -->
        <file category="doc" name="CMSIS/Documentation/DSP/html/index.html"/>
        <file category="header" name="CMSIS/Include/arm_math.h"/>
        <!-- CPU and Compiler dependent -->
        <!-- ARMCC -->
        <file category="library" condition="CM0_LE_ARMCC"  name="CMSIS/Lib/ARM/arm_cortexM0l_math.lib"/>
        <file category="library" condition="CM0_BE_ARMCC"  name="CMSIS/Lib/ARM/arm_cortexM0b_math.lib"/>
        <file category="library" condition="CM3_LE_ARMCC"  name="CMSIS/Lib/ARM/arm_cortexM3l_math.lib"/>
        <file category="library" condition="CM3_BE_ARMCC"  name="CMSIS/Lib/ARM/arm_cortexM3b_math.lib"/>
        <file category="library" condition="CM4_LE_ARMCC"  name="CMSIS/Lib/ARM/arm_cortexM4l_math.lib"/>
        <file category="library" condition="CM4_BE_ARMCC"  name="CMSIS/Lib/ARM/arm_cortexM4b_math.lib"/>
        <file category="library" condition="CM4F_LE_ARMCC" name="CMSIS/Lib/ARM/arm_cortexM4lf_math.lib"/>
        <file category="library" condition="CM4F_BE_ARMCC" name="CMSIS/Lib/ARM/arm_cortexM4bf_math.lib"/>
        <!-- GCC -->
        <file category="library" condition="CM0_LE_GCC"    name="CMSIS/Lib/GCC/libarm_cortexM0l_math.a"/>
        <file category="library" condition="CM3_LE_GCC"    name="CMSIS/Lib/GCC/libarm_cortexM3l_math.a"/>
        <file category="library" condition="CM4_LE_GCC"    name="CMSIS/Lib/GCC/libarm_cortexM4l_math.a"/>
        <file category="library" condition="CM4F_LE_GCC"   name="CMSIS/Lib/GCC/libarm_cortexM4lf_math.a"/>
        <!-- G++ -->
        <file category="library" condition="CM0_LE_G++"    name="CMSIS/Lib/G++/libarm_cortexM0l_math.a"/>
        <file category="library" condition="CM3_LE_G++"    name="CMSIS/Lib/G++/libarm_cortexM3l_math.a"/>
        <file category="library" condition="CM4_LE_G++"    name="CMSIS/Lib/G++/libarm_cortexM4l_math.a"/>
        <file category="library" condition="CM4F_LE_G++"   name="CMSIS/Lib/G++/libarm_cortexM4lf_math.a"/>
      </files>
    </component>

    <!-- Cortex-M0 -->
    <component Cclass="Device" Cgroup="Startup" Cvariant="C Startup" Cversion="2.0.0" condition="ARMCM0 CMSIS">
      <description>System and Startup for Generic Arm Cortex-M0 device</description>
      <files>
        <!-- include folder / device header file -->
        <file category="header"  name="Device/ARM/ARMCM0/Include/ARMCM0.h"/>
        <!-- startup / system file -->
        <file category="sourceC"      name="Device/ARM/ARMCM0/Source/startup_ARMCM0.c"     version="2.0.0" attr="config"/>
        <file category="linkerScript" name="Device/ARM/ARMCM0/Source/ARM/ARMCM0_ac5.sct"   version="1.0.0" attr="config" condition="ARMCC5"/>
        <file category="linkerScript" name="Device/ARM/ARMCM0/Source/ARM/ARMCM0_ac6.sct"   version="1.0.0" attr="config" condition="ARMCC6"/>
        <file category="linkerScript" name="Device/ARM/ARMCM0/Source/GCC/gcc_arm.ld"       version="2.0.0" attr="config" condition="GCC"/>
        <file category="sourceC"      name="Device/ARM/ARMCM0/Source/system_ARMCM0.c"      version="1.0.0" attr="config"/>
      </files>
    </component>

    <!-- Cortex-M0+ - the same component as above, but with different filter conditions, so each one is unique -->
    <component Cclass="Device" Cgroup="Startup" Cvariant="C Startup" Cversion="2.0.0" condition="ARMCM0+ CMSIS">
      <description>System and Startup for Generic Arm Cortex-M0+ device</description>
      <files>
        <!-- include folder / device header file -->
        <file category="header"  name="Device/ARM/ARMCM0plus/Include/ARMCM0plus.h"/>
        <!-- startup / system file -->
        <file category="sourceC"      name="Device/ARM/ARMCM0plus/Source/startup_ARMCM0plus.c"     version="2.0.0" attr="config"/>
        <file category="linkerScript" name="Device/ARM/ARMCM0plus/Source/ARM/ARMCM0plus_ac5.sct"   version="1.0.0" attr="config" condition="ARMCC5"/>
        <file category="linkerScript" name="Device/ARM/ARMCM0plus/Source/ARM/ARMCM0plus_ac6.sct"   version="1.0.0" attr="config" condition="ARMCC6"/>
        <file category="linkerScript" name="Device/ARM/ARMCM0plus/Source/GCC/gcc_arm.ld"           version="2.0.0" attr="config" condition="GCC"/>
        <file category="sourceC"      name="Device/ARM/ARMCM0plus/Source/system_ARMCM0plus.c"      version="1.0.0" attr="config"/>
      </files>
    </component>
  </components>
  ...
</package>
```
