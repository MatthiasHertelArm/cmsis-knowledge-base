---
id: "spec-use-of-debug-descriptions-in-mu-vi-impact-of-debug-access-configuration"
type: "concept"
domain: "pack"
title: "Use of debug descriptions in &mu;Vision: Impact of debug access configuration"
summary: "When dbgdebugsettings are provided the &mu;Vision debugger automatically applies these settings to the new project for the MCU. This can be observed in  Options for Target... dialog - Debug tab - Settings button."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_dbg_setup_tutorial.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/dbg_sqns_uvision.html"
license: "Apache-2.0"
mode: "V"
---

### Debug connection


When dbg_debug_settings are provided the &mu;Vision debugger automatically applies these settings to the new project for the MCU. This can be observed in ** Options for Target...** dialog - **Debug** tab - **Settings** button.

Below is an example of the configuration code and how it is applied by &mu;Vision.

```
<devices>
  <family Dfamily="LPC54000 Series" Dvendor="NXP:11">
    <debugconfig default="swd" clock="5000000" swj="true"/>
    ...
  </family>
</devices>
```



SWD is selected as the default debug protocol with 5MHz clock and SWJ checkbox locked because this is a fixed characteristic of the device.


### Access port


With the specificaton of the debug connection &mu;Vision debugger will automatically use the access port specified via the **__ap** attribute when debugging the processor and there's no need for user to configure it in the IDE. Corresponding option is locked as shown on the figure below.



&mu;Vision debugger displays the JTAG ID Code and the IR Length values (actually read or overwritten ones) in debug settings:



You can test what the &mu;Vision debugger is able to detect automatically without the **debugport** configuration in the pdsc. For that the use of debug description shall be disabled in the **Pack** tab.


### Reset types and default selection


The default reset type can be specified in `<debug>` element via defaultResetSequence attribute.

It is also possible to disable particular reset type for selection by overwriting corresponding predefined reset sequence with **disable** attribute set to 'true'. For example reset configuration implemented for Microchip SAML11 device:

```
 <debug defaultResetSequence="ResetSystem"/>
...

 <!-- VECTRESET - Disabled -->
 <sequence name="ResetProcessor" disable="true" info="VECTRESET">
	<!-- ResetProcessor not available for CM23 -->
 </sequence>

```

&mu;Vision debugger applies it automatically and displays as default and selected in **Options for Target...** dialog - **Debug** tab - **Settings** button and then **Reset:**



You can see the VECTRESET type is absent and system reset is selected and marked as default. The user can still manually change the reset type for the project in this dialog.

Using the **Reset** dropdown menu mentioned above a user can specify the reset type to be performed by the debugger.

Figure below shows how the typically available reset options map to the corresponding reset types in the connect flow described in usage_of_sequences. Note that "Custom" reset type appears only when user-defined debug sequence is assigned to the defaultResetSequence attribute.



Detailed meanings for available options are explained in the documentation of corresponding debug adapter. For example for ULINKpro **Connect & Reset Options**
