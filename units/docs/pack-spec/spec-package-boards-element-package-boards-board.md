---
id: "spec-package-boards-element-package-boards-board"
type: "concept"
domain: "pack"
title: "/package/boards element: /package/boards/board"
summary: "This element provides information to specify the board support. At least one board must be defined."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/boards_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_boards_pg.html"
license: "Apache-2.0"
mode: "V"
---

This element provides information to specify the board support. At least one board must be defined.



  | 
    Parent | 
    Chain | 
  

  | 
    boards | 
    element_boards | 
  
	
  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    vendor | 
    name of the board vendor | 
    xs:string | 
    required | 
  

  | 
    name | 
    name of the development board | 
    xs:string | 
    required | 
  

  | 
    revision | 
    Revision of the board that is suited to be used with the BSP. | 
    xs:string | 
    optional | 
  

  | 
    uuid | 
    Specifies a 128-bit UUID that is embedded it in the debugger firmware of the board tag. Format: 8-4-4-4-12 for a total of 36 characters. Example: 123e4567-e89b-12d3-a456-426614174000 | 
    128-bit UUID | 
    optional | 
  

  | 
    salesContact | 
    Either an email address or web page to contact the sales department. | 
    xs:string | 
    optional | 
  

  | 
    orderForm | 
    Link to a web page for ordering the development board. | 
    xs:anyURI | 
    optional | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    description | 
    Brief summary of the board (maximum 256 characters, recommended 128 characters). | 
    BriefDescType | 
    1 | 
  

  | 
    feature | 
	Describes the features of the development board. | 
	BoardsFeatureType | 
	1..*  | 
  

  | 
    mountedDevice | 
	Specifies the specific microcontroller device mounted on the development board. | 
	BoardsDeviceType | 
	1..*  | 
  

  | 
    compatibleDevice | 
	Specifies compatible microcontroller devices. | 
	CompatibleDeviceType | 
	1..*  | 
  

  | 
    mountedPart | 
	Specifies the parts (all devices other than the MCU) mounted on the development board. | 
	MountedPartType | 
	0..*  | 
  

  | 
    image | 
    Carries pictures of the boards to be displayed on web pages. Directory and file names are case-sensitive. | 
    ComplexType | 
    0..1 | 
  

  | 
    debugInterface | 
	Describes the debug interface of the development board. The expectation is that boards provides a hardware connector to attach external
	    debug adapters and/or on-board debug adapters, unless the board has device = "NO_MCU" or represents virtual hardware. | 
	DebugInterfaceType | 
	0..*  | 
  

  | 
    book | 
	Describes the documentation files (user manuals, schematics, etc.). Directory and file names are case-sensitive. | 
	BoardsBookType | 
	0..*  | 
  

  | 
    debugProbe | 
    Specify on-board debug probe. | 
    DebugProbeType | 
    0..1 | 
  

  | 
    memory | 
    Specify memory areas that board specific. | 
    MemoryType | 
    0..* | 
  

  | 
    algorithm | 
    Specify Flash programming algorithms for memory provided by the board. | 
    AlgorithmType | 
    0..* | 
  

  | 
    environment | 
    Specify tool specif settings. | 
    EnvironmentType | 
    0..* |
