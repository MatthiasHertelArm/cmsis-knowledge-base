---
id: "spec-package-devices-family-element-package-devices-family-book"
type: "concept"
domain: "pack"
title: "/package/devices/family element: /package/devices/family/.../book"
summary: "Specifies documents related to a device or a part. Books can be entered on various levels. The book element contains the location, the name and the extension of the file."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/devices_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_family_pg.html"
license: "Apache-2.0"
mode: "V"
---

Specifies documents related to a device or a part. Books can be entered on various levels.
The book element contains the location, the name and the extension of the file. The link to a document on an external web site is also allowed. The title is used for display purposes.

**Example**
```
<family Dfamily="STM32F4" Dvendor="STMicroelectronics:13">
  ...
  <book name="Documents/STM32F40x_DS.PDF" title="STM32F40x Data Sheet"/>                 <!-- valid for all devices of the family  -->

  <subFamily DsubFamily="STM32F405">
    <book name="Documents/STM32F4xx_RM.pdf" title="STM32F4 Series Reference Manual"/>    <!-- valid for all devices of a subFamily -->

    <device Dname="STM32F405OE">
      <book name="Documents/STM32F405OE_DS.PDF" title="STM32F405OE - Data Sheet"/>       <!-- valid for this device; Inherits all above -->
    </device>
    ...
</family>
```

```
<package>
  ...
  <parts>
    <part Hvendor="STMicroelectronics" Hname="STSAFE-A110" Hvariant="STSAFA110DFSPL02" Hclass="Secure" Hgroup="Authentication">
      ...
      <book name="Images/STSAFA110DFSPL02_image.jpg" title="image" public="true"/>
    </part>
    ...
  <\parts>
  ...
<\package>
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
    part | 
    element_part | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Pname | 
    Processor identifier. This attribute **is mandatory for devices that embed multiple processors and where the book refers to a single processor only**.
        Only alphabetical characters, decimal digits, '-' and '_' are allowed.
        


        Must not be used for package/parts/part. | 
    RestrictedString | 
    optional | 
  

  | 
    name | 
    File name of the document including the extension. The document path is relative to the package base folder. 
        Directory/file names are case-sensitive. The link to a document on an external web site is also allowed. | 
    xs:string | 
    required | 
  

  | 
    title | 
    Book title. Can be used for being displayed in various environments. | 
    xs:string | 
    required | 
  

  | 
    public | 
    Set publishing permissions for the documentation. If \tagem{public} is `true`, then the vendor gives permission 
        to extract the documentation from the pack and publish it on a web-page. Links to web pages are assumed to be public.
        The default value is `true`. | 
    xs:boolean | 
    optional | 
  



\delim
