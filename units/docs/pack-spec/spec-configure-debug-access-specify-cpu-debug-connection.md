---
id: "spec-configure-debug-access-specify-cpu-debug-connection"
type: "concept"
domain: "pack"
title: "Configure debug access: Specify CPU debug connection"
summary: "An important item that needs to be specified for an MCU is the debug connection to the CPU. For that <debug> element shall be used."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_setup_access.html"
license: "Apache-2.0"
mode: "V"
---

An important item that needs to be specified for an MCU is the debug connection to the CPU. For that `<debug>` element shall be used. This element is most commonly used in DFPs to specify the **system view description file (.svd)**. But it also contains useful attributes to define the debug connection to the processor: **__dp** , **__ap** and **Pname.**

An example code below defines debug connection for a dual-core device with one debug port and 2 access ports: indexed as `0` for Cortex-M4 and `1` for Cortex-M0+.

```
<devices>
  <family Dfamily="LPC54114" Dvendor="NXP:11">
    ...
    <device Dname="LPC54114J256">
      <processor Pname="CM0plus" Dcore="Cortex-M0+" Dfpu="NO_FPU" Dmpu="NO_MPU" Dendian="Little-endian" Dclock="100000000"/>
      <processor Pname="CM4" Dcore="Cortex-M4" Dfpu="SP_FPU" Dmpu="MPU" Dendian="Little-endian" Dclock="100000000"/>
      ...
      <debug svd="SVD/LPC54114_cm0plus.xml" Pname="CM0plus" __dp="0" __ap="1"/>
      <debug svd="SVD/LPC54114_cm4.xml" Pname="CM4" __dp="0" __ap="0"/>
	  ...
    </device>
    ...
  </family>
</devices>
```

The same **Pname** identifier shall be used in `<debug>` element as defined in the corresponding `<processor>` element ('CM0plus' or 'CM4' in this example).

The numeric index values shall be typically specified for **__dp** attribute when multiple debug ports are available in the system and defined via `<debugport>` element. See dbg_debug_port for details about configuring debug ports.

For the **__ap** attribute the numeric index values shall be assigned based on the debug system implementation.

There's no need to specify all attributes in a single line at once, it can also be split over multiple assignments if it helps to better structure the sequences code. However the same **Pname** identifier shall be used. So the code below specifies the same debug connection for M4 processor as in the example above:

```
<debug Pname="CM4" svd="SVD/LPC54114_cm4.xml"/>
...
<debug Pname="CM4" __dp="0" __ap="0"/>
...
```

The attribute defaultResetSequence specifies the debug sequence that will be used by default to reset the device.

The debug IDE may also allow users to specify the reset type in the project options thus overwriting this default configuration. In multi-core systems **Pname** shall be used to ensure that the default reset sequence is set for a correct core.

```
<debug Pname="M4" defaultResetSequence="ResetProcessor"/>
```
