---
id: "spec-package-parts-element-package-parts-part-image"
type: "concept"
domain: "pack"
title: "/package/parts element: /package/parts/part/image"
summary: "This element specifies the part pictures. Maximum one image element can be specified. Three different picture types (top, bottom and perspective) can be specified for the same \\tagem{image} element at the same time."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/parts_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_parts_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element specifies the part pictures. Maximum one image element can be specified.
Three different picture types (`top`, `bottom` and `perspective`) can be specified for the same \tagem{image} element at the same time.
Attribute `top` displays the 'top' side of the part (or the main part picture).

**Example:**
```
<image top="Images/part_image_1.png"
       bottom="https://images.vendor.com/Images/part_image_2.png"
       perspective="https://images.vendor.com/Images/part_image_3.png"
/>
```

 		



  | 
    Parent | 
    Chain | 
  

  | 
    part | 
    element_part | 
  
	
  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    top | 
    Specifies the path to the top (or the main) part image. The path is relative to the pack base directory or a link to an image on an external web site. | 
    xs:string | 
    required | 
  

  | 
    bottom | 
    Specifies the path to the bottom part image. The path is relative to the pack base directory or a link to an image on an external web site. | 
    xs:string | 
    optional | 
  

  | 
    perspective | 
    Specifies the path to a perspective part image. The path is relative to the pack base directory or a link to an image on an external web site. | 
    xs:string | 
    optional | 
  

  | 
    public | 
    Set publishing permissions for the image. If \tagem{public} is `true`, then the vendor gives permission
        to extract the image file from the Pack and publish it on a web-page. Links to web pages are assumed to be public.
        If no \tagem{public} tag is available, it is assumed that publishing is allowed (default value is `true`). | 
    xs:boolean | 
    optional |
