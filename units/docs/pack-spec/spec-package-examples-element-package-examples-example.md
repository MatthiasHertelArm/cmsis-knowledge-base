---
id: "spec-package-examples-element-package-examples-example"
type: "concept"
domain: "pack"
title: "/package/examples element: /package/examples/example"
summary: "An example section is used to provide the required information for accessing an example project contained in a Pack. All examples contained in the installed packs can be listed including a brief description."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/examples_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_examples_pg.html"
license: "Apache-2.0"
mode: "V"
---

An example section is used to provide the required information for accessing an example project contained in a Pack. All examples contained in the installed packs can be 
listed including a brief description. A selected example will get copied into a user selected destination folder. Based on the user selected environment the respective project 
file will be loaded. The ID of an example is the combination of the Pack vendor, the board information and the example name and version. Examples with the same ID are
treated as a single example.



  | 
    Parent | 
    Chain | 
  

  | 
    examples | 
    element_examples | 
  
	
  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    Name of the example | 
    xs:string | 
    required | 
  

  | 
    folder | 
    Relative path to the example base folder within the package. If selected, then the directory including all sub-folders and files will be copied,
 	unless the archive attribute gets set. | 
    xs:string | 
    required | 
  

  | 
    archive | 
    Filename and extension of the archive file containing all files and sub-folders of the example. The archive is located in the path specified by the 
	attribute **_folder_.** If selected, then the whole archive will be extracted. | 
    xs:string | 
    optional | 
  

  | 
    doc | 
	Document that describes the example. | 
	xs:string | 
	required | 
  

  | 
    version | 
    Example version number.  The version format is described in Version Type. | 
	 | 
    VersionType | 
    optional | 
  

  | 
    public | 
    Set publishing permissions for the documentation. If \tagem{public} is `true`, then the vendor gives permission 
        to extract the documentation from the pack and publish it on a web-page. Links to web pages are assumed to be public.
        The default value is `true`. | 
    xs:boolean | 
    optional | 
  

  | 
    Child Elements | 
    Description | 
    Type | 
    Occurrence | 
  

  | 
    description | 
    Briefly documents the purpose and scope of the example (maximum 256 characters, recommended 128 characters). The test can be displayed in an example selector. | 
    BriefDescType | 
    1 | 
  

  | 
    board | 
    Complex type providing a reference to a board description using board name and vendor. | 
    BoardReferenceType | 
    0..* | 
  

  | 
    project | 
	Complex type describing the project files for different environments | 
	ExampleProjectType | 
	1 | 
  

  | 
    attributes | 
	Group element for project attributes, which list required components, define example categories, and set keywords to filter and search for examples. | 
	ExampleAttributesType | 
	0..1 |
