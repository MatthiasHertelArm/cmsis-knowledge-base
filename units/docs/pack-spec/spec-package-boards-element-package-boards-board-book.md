---
id: "spec-package-boards-element-package-boards-board-book"
type: "concept"
domain: "pack"
title: "/package/boards element: /package/boards/board/book"
summary: "The element provides information about documentation parts related to a development board."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

The element provides information about documentation parts related to a development board.

**Example**
```
<book category="overview" name="http://www.st.com/web/catalog/tools/FM116/SC959/SS1532/LN1199/PF259090" title="32F429IDISCOVERY Web Page"/>
<book category="setup" name="Documents/UM1662.pdf" title="Getting Started"/>
```

 		



  | 
    Parent | 
    Chain | 
  

  | 
    board | 
    element_board | 
  
	
  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    category | 
    Describes the type of documentation. Use predefined values as defined in the table Board Book Categories. | 
    BoardBookCategoryEnum | 
    optional | 
  

  | 
    name | 
	Is the name of the document (including the path within the Pack). The link to a document on an external web site is also allowed. | 
	xs:string | 
	optional | 
  

  | 
    title | 
	Is the title of the document to be displayed in the **Books** window of uVision. | 
	xs:string | 
	optional | 
  

  | 
    public | 
    Set publishing permissions for the documentation. If \tagem{public} is `true`, then the vendor gives permission 
        to extract the documentation from the pack and publish it on a web-page. Links to web pages are assumed to be public.
        The default value is `true`. | 
    xs:boolean | 
    optional | 
  




 

 **Table: Board Book Categories**

The table lists values to identify a specific type of documentation for development boards. 


  | 
    category= | 
    Description | 
  

  | 
    setup | 
    Documentation about how to setup the development board. | 
  

  | 
    schematic | 
    Schematics of the development board. | 
  

  | 
    overview | 
    Overview/data sheet of the development board. | 
  

  | 
    manual | 
    User manual of the development board | 
  

  | 
    layout | 
    PCB layout file of the board (e.g. in Gerber format) | 
  

  | 
    other | 
    All other documentation. | 
  



**Note:**
By convention, the following `<book>` entry:
```
<book category="other" name="README.md" title="Guide"/>
```
specifies a Markdown based documentation page for the board that can be displayed on web sites.
