---
id: "spec-package-devices-family-element-package-devices-family-environment"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../environment"
summary: "Tool-specific elements for a device or a part."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Tool-specific elements for a device or a part.

Can occur on various levels. 

Contains information that is specific for a **development tool** identified by the **name** attribute.
The structure of the **element** is not specified in the schema file which gives the **development tool** 
full control of the **element** usage.

**Example**
```
<package>
  <devices>
    <family Dfamily="MySeries" Dvendor="Generic:5">
      ...    
      <environment name="MyConfigTool">
        <file>MyConfigFile.cfg</file>
        <control>MyControlString</control>
        ...
      </environment>
      ...
    </family>
  </devices>
</package>
```

```
<package>
  <devices>
    <family Dfamily="XMC1000 Series" Dvendor="Infineon:7">
      ...    
      <environment name="uv" Pname="M0">
        <CMisc>--C99</CMisc>
        ...
      </environment>
      ...
    </family>
  </devices>
</package>
```

```
<package>
  ...
  <parts>
    <part Hvendor="STMicroelectronics" Hname="STSAFE-A110" Hvariant="STSAFA110DFSPL02" Hclass="Secure" Hgroup="Authentication">
      ...
      <environment name="SomeConfigTool">
        <file>STSAFA110DFSPL02_ConfigFile.cfg</file>
      </environment>
      ...
    </part>
    ...
  <parts>
  ...
</package>
```

\n



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
    part | 
    element_part | 
  

  | 
    board | 
    element_board | 
  

  | 
    environments | 
    element_component_environments | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Name of the development tool (for example, "uv" for uVision) | 
    xs:string | 
    required | 
  

  | 
    Pname | 
    Identifies the processor the setting belongs to.
        Only alphabetical characters, decimal digits, '-' and '_' are allowed.
        


        Must not be used for:
        

          
- /package/parts/part
          
- /package/boards/board
          
- /package/components/.../component/environments
        
     | 
    RestrictedString | 
    optional | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    any | 
    Any element that is available for the specified development tool.

    For uVision, the following elements are available: \`<CMisc>`, `<AMisc>`, `<LMisc>`, `
`, `
`, `
`, `
`, `
`, `
`, `
`, `
`. | 
    xs:anyAttribute | 
    0..* | 
  



\delim
