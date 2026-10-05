---
id: "spec-configure-debug-access-specify-debug-port"
type: "concept"
domain: "pack"
title: "Configure debug access: Specify debug port"
summary: "A microcontroller system can have one or more CoreSight debug ports with one or more supported debug protocols (for example JTAG and SWD). <debugport> element can be used to describe the debug ports capabilities."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_setup_access.html"
license: "Apache-2.0"
mode: "V"
---

A microcontroller system can have one or more CoreSight debug ports with one or more supported debug protocols (for example JTAG and SWD). `<debugport>` element can be used to describe the debug ports capabilities.

For example if only Arm Serial Wire Debug (SWD) interface is supported, then **debugport** shall be defined only with swd child element and no jtag elements. The **swd** element is really simple and can only take an **idcode** attribute that needs to be explicitly provided when you want to override the value of the SWD debug port's DPIDR register that will be read from the device.

```
...
  <debugport __dp="0"/>
    <swd/>
  </debugport>
...
```

Vice versa is true as well, if only JTAG is supported then SWD shall not be listed in the **debugport** element.

The numeric value assinged to the **__dp** identifies the debug port and is for the user to choose. When describing JTAG chains it is recommended to use the **tapindex** as the **__dp** value to avoid confusion.

Debuggers can normally autodetect JTAG chains. But with some devices there is still a need to fully specify the JTAG chain to avoid potential detection issues by the debugger. Below is an example for the NXP IMX6 Solo X:

```
<debugport __dp="0">
  <jtag tapindex="0" idcode="0x4BA00477" irlen="4"/>
</debugport>

<debugport __dp="1">
  <jtag tapindex="1" idcode="0x4BA00477" irlen="4"/>
</debugport>

<debugport __dp="2">
  <jtag tapindex="2" idcode="0x00000000" irlen="4"/>
</debugport>

<debugport __dp="3">
  <jtag tapindex="3" idcode="0x0891C01D" irlen="5"/>
</debugport>

<debug Pname="Cortex-A9" __dp="1" __ap="0"/>
<debug Pname="Cortex-M4" __dp="0" __ap="0"/>

```

Even though only two debug ports are used to access the processor cores, the other debug ports available in the system are specified as well. In this case it is needed to provide debugger with correct **irlen** values thus allowing it to correctly scan the JTAG chain and access the processors.

The **tapindex** uniquely identifies the JTAG interface and typically its value is also used as the identifier for the debug port (**__dp)** index.  Same as with the SWD the explicit specification of the **idcode** attribute is really necessary only when it needs to overwrite the IDCODe value read from the device. And **irlen** attribute may require explicit specification here if there're problems correctly obtaining its value from the device.
