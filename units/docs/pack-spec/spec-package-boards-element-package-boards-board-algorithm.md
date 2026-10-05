---
id: "spec-package-boards-element-package-boards-board-algorithm"
type: "concept"
domain: "pack"
title: "/package/boards element: /package/boards/board/algorithm"
summary: "Specify Flash programming algorithms with the address range and its size for board-specific memory. An algorithm with \\<default> set to true gets configured automatically to the download options of the project."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

Specify Flash programming algorithms with the address range and its size for board-specific memory.  An algorithm with 
\`<default>` set to `true` gets configured automatically to the download options of the project.



  | 
    Parents | 
    Element Chain | 
  

  | 
    board | 
    element_board | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    Pname | 
    Processor identifier. This attribute **is for boards that use devices with multiple processors**. 
        Only alphabetical characters, decimal digits, '-' and '_' are allowed.  | 
    RestrictedString | 
    optional | 
  

  | 
    name | 
    Flash Programming Algorithm file including the path, which is relative to the root folder of the software pack. | 
    xs:string | 
    required | 
  

  | 
    start | 
    Base address for the Flash programming algorithm. | 
    NonNegativeInteger | 
    required | 
  

  | 
    size | 
    Size covered by the Flash programming algorithm. End address = start + size - 1 | 
    NonNegativeInteger | 
    required | 
  

   | 
    RAMstart | 
    Base address for the RAM where the Flash programming algorithm will be executed from. If
    specified, the memory element does not require a `default` attribute. | 
    NonNegativeInteger | 
    optional | 
  

  | 
    RAMsize | 
    Maximum size of RAM available for the execution of the Flash programming algorithm. 
    End address = start + size - 1 is used for the Stack. If specified, the element_memory 
    "memory" element does not require a `default` attribute. | 
    NonNegativeInteger | 
    optional | 
  

  | 
    default | 
    If `true`, then this is the default Flash programming algorithm that gets configured
    in a project. If not specified or set to `false`, then the Flash programming algorithm can
    be configured on a lower level. However, the Flash programming algorithm of a project can be
    changed manually at any time during development.
     | 
    xs:boolean | 
    optional | 
  

    | 
    style | 
    [Version 1.4.0] Today, different toolchains support different styles of incompatible flash
    programming algorithms. The attribute specifies the style of the specified flash programming 
    algorithm. For backward compatibility the default value is `Keil`. The aim is to converge to
    the _CMSIS_ style.
     | 
    AlgorithmStyleEnum | 
    optional |
