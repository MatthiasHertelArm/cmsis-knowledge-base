---
id: "spec-revision-history"
type: "concept"
domain: "pack"
title: "Revision history"
summary: "Revision history"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/General.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pack_revisionHistory.html"
license: "Apache-2.0"
mode: "V"
---

| 
    Version | 
    Description | 
  

  | 
    Next Version | 
    
      - added use of `__connection` Bit 18 as halt-after-reset indicator
      - use `mode` Bit 9 in `BufferRead`/`BufferWrite` debug access functions
        to select APv2 (ADIv6) top-level access port address space (32-bit access only)
      - added rules for AP/DP register caching
     | 
  

  | 
    1.7.62 | 
    
      - removed optional 'Pname' attribute from 'trace' element
     | 
  

  | 
    1.7.61 | 
    
      - added optional 'name' attribute to 'tracebuffer' element
      - added Trace Buffer format to 'BufferStreamOut'
      - added 'TraceBufferSelected' debug access function
     | 
  

  | 
    1.7.60 | 
    
      - added 'FlashEraseSetup' and 'FlashProgramSetup' debug access sequences
      - added 'FlashLoadAlgorithm' debug access function
      - added 'RunPythonScript' debug access function
     | 
  

  | 
    1.7.59 | 
    
      - clarified sequence abortion in case of errors
      - added missing ResetCatchClear to debug connect flow diagram
      - added pre-defined 'TraceCapture' and 'TraceFlush' debug access sequences
      - added pre-defined '__traceclockin' and '__traceclockout' debug access variables
      - added 'traceSetup' attribute to 'sequences' element
     | 
  

  | 
    1.7.58 | 
    
      - adds rules to reserve `__` prefix for debug access variable names provided by spec
      - added '__' prefix to variable names in default debug sequence implementations
      - corrected '__FlashOp' value mapping in debug access variables documentation
      - clarified usage of 'timeout' in 'BufferStreamIn', 'BufferStreamOut', and 'FilePathExists' debug access functions
      - changed return values of 'BufferWrite' and 'FlashBufferWrite' from always '0' to number of actually written bytes
      - added Dvendor ID "ESMT:190" for Elite Semiconductor Microelectronics Technology Inc..
     | 
  

  | 
    1.7.57 | 
    
      - corrected name from 'FlashBufferWrite' to 'FlashWriteBuffer' in debug access function documentation
     | 
  

  | 
    1.7.56 | 
    
      - added "Qorvo:189" Dvendor ID
     | 
  

  | 
    1.7.55 | 
    
      - add 'description' child to part element
     | 
  

  | 
    1.7.54 | 
    
      - align documentation with XSD schema by adding 'Hrevision' description to the part element
      - add 'Hrevision' as an optional attribute of the mountedPart element
     | 
  

  | 
    1.7.53 | 
    
      - added Arm China 'Star-MC3' processor to DcoreEnum
     | 
  

  | 
    1.7.52 | 
    
      - updated 'ExampleProjectType' to allow the 'environment' element to have custom children and custom attributes
     | 
  

  | 
    1.7.51 | 
    
      - add 'HrdWyr' device vendor
     | 
  

  | 
    1.7.50 | 
    
      - add 'J-Link' and 'JLink Server' to enumeration 'DebugProbeNameEnumType'
     | 
  

  | 
    1.7.49 | 
    
      - deprecate values 'DP' and 'ACCESS_AP' from 'type' attribute in element 'datapatch' 
     | 
  

  | 
    1.7.48 | 
    
      - add 'HPROT' and 'SPROT' attributes to 'accessportV1' and 'accessportV2' element
     | 
  

  | 
    1.7.47 | 
    
      - removed optional 'Pname' attribute from 'debugvars' element
     | 
  

  | 
    1.7.46 | 
    
      - added XYD vendor
     | 
  

  | 
    1.7.45 | 
    
      - added 'CLANG_TI' to 'CompilerEnumType'
      - documentation: removed "Pack Tutorials" section and added link to CMSIS-Toolbox documentation
     | 
  

  | 
    1.7.44 | 
    
      - added optional 'environments' section below package element to hold environment-specific information pertaining to the package as a whole
     | 
  

  | 
    1.7.43 | 
    
      - added optional 'ECCN' section for EU and US export control classification numbers
     | 
  

  | 
    1.7.42 | 
    
      - added 'mode' attribute ExeGeneratorArgumentType
     | 
  

  | 
    1.7.41 | 
    
      - changed remaining 'public' attributes to all have default value 'true' if not specified.
     | 
  

  | 
    1.7.40 | 
    
      - added 'Secure-only' to DsecureEnum to specify a secure software model without provisions for a non-secure partition
     | 
  

  | 
    1.7.39 | 
    
      - modified default 'DebugPortStart' debug sequence to clear DP sticky error bits
     | 
  

  | 
    1.7.38 | 
    
      - The pack publishing process has been rewritten completely
      - removed the old tutorials that have been superseded by the online versions on GitHub
     | 
  

  | 
    1.7.37 | 
    
      - added 'Nationstech:184' to DeviceVendorEnum
      - added 'NSING:185' to DeviceVendorEnum
      - added Cortex A35 and Cortex A55 support in PACK.xsd
     | 
  

  | 
    1.7.36 | 
    
      - added pdsc_csolution_pg for clayer.yml files and project templates.
      - added element_targets to specify that a pack applies to specific devices only.
      - added to configWizard the item `<y>` to support symbol or value entries.
     | 
  

  | 
    1.7.35 | 
    
     - made board element optional in example element
     - added attribute overview to package description element
     - fixed 'BOYAMICRO' vendor value in DeviceVendorEnum
     | 
  

  | 
    1.7.34 | 
    
     - added 'Watech:183' to DeviceVendorEnum
     | 
  

  | 
    1.7.33 | 
    
     - added 'BOYAMICRO:182' to DeviceVendorEnum
     | 
  

  | 
    1.7.32 | 
    
     - FileScopeAttributeType 'private' and 'public' also used for header files.
     - attribute select also permitted for component files type header.
     - description text size limit documented with BriefDescType.
     | 
  

  | 
    1.7.31 | 
    
     - added new processor Cortex-M52
     | 
  
  
  | 
    1.7.30 | 
    
     - renamed componentExts as extensions in the schema.
     | 
  
  
  | 
    1.7.29 | 
    
     - added image child element to element_part element
     | 
  

  | 
    1.7.28 | 
    
     - changed capitalization from 'changeLogs' to 'changelogs' to align with documentation
     | 
  

  | 
    1.7.27 | 
    
     - changed capitalization from 'Clang' to 'CLANG' in 'CompilerEnumType' to align with CMSIS-Toolbox
     - added 'MinebeaMitsumi:181' to DeviceVendorEnum
     | 
  

  | 
    1.7.26 | 
    
     - added 'YTMicro:180' to DeviceVendorEnum
     | 
  

  | 
    1.7.25 | 
    
     - added 'Sinemicro:179' to DeviceVendorEnum
     | 
  

  | 
    1.7.24 | 
    
     - added environment element as child element of /package/boards/board and /package/components/.../component/environments
     | 
  

  | 
    1.7.23 | 
    
     - specified that url to a website in book element is allowed
     - aligned \`<book>` element occurrence in board table to XSD schema
     | 
  

  | 
    1.7.22 | 
    
     - added 'Hvendor' and 'Hname' as attributes of the accept, require and deny elements
     - redefined 'Hvendor' as xs:string
     | 
  

  | 
    1.7.21 | 
    
     - added 'Himax:178' to DeviceVendorEnum
     - added 'Renesas' to CompilerEnumType
     | 
  

  | 
    1.7.20 | 
    
     - added \`<clayers>` section for distributing layers in software packs. This is renamed to \`<csolution>` in 1.7.36 as it was not used before.
     | 
  

  | 
    1.7.19 | 
    
     - added generator specific component file types: 'genSource', 'genHeader', 'genParams', 'genAsset' to 'FileCategoryType' of the files element
     | 
  

  | 
    1.7.18 | 
    
     - added 'NO_VENDOR:0' to DeviceVendorEnum
     | 
  

  | 
    1.7.17 | 
    
     - added Hclass and Hgroup predefined values for \
 element classification
     - added element_part-taxonomy "\
" element to list description elements defining part classes and part group names
     | 
  

  | 
    1.7.16 | 
    
     - added 'bottom' and 'perspective' attributes to \`<image>` element
     - revert extension from v1.7.10 and replace using attributes for 'language' and 'scope' in 'FileType'
     - added 'Clang' to 'CompilerEnumType'.
     - added '3PEAK' Dvendor ID.
     | 
  

  | 
    1.7.15 | 
    
     - added 'projectpath' attribute which can be used by IDE to construct file location folder in IDE project explorer view of workspace.
     | 
  

  | 
    1.7.14 | 
    
     - added 'changelog' element providing references to change log files by component, api and bundle elements
     - added 'Puya' Dvendor ID.
     - added 'view' attribute to component element with predefined values define by 'ViewType'
     | 
  

  | 
    1.7.13 | 
    
     - added VirtualHW as a new board type in support of the Arm Virtual Hardware initiative
     - added \
 element and its child elements for describing and packaging the parts (devices other than the MCU).
     - added \`<mountedPart>` element, as child element of the \`<board>` element, for describing the parts (devices other than the MCU)
       mounted on the development board.
     | 
  

  | 
    1.7.12 | 
    
     - added 'Linkedsemi' Dvendor ID.
     | 
  

  | 
    1.7.11 | 
    
     - added 'uuid' to boards element to indicate a 128-bit universal ID in the debug firmware of the board
     - added 'memory' and 'algorithm' child elements to the boards element to describe board-specific memory
     - added 'Bvendor', 'Bname', 'Brevision' attribute to conditions element to allow board specific filtering.
     | 
  

  | 
    1.7.10 | 
    
     - added 'includeAsm', 'includeC', 'includeCpp', 'includeLd' to FileCategoryType of the components element
     - added 'headerAsm', 'includeC', 'headerCpp', 'headerLd' to FileCategoryType of the components element
     | 
  

  | 
    1.7.9 | 
    
     - added new section \`<licenseSets>` supporting association of multiple license
       files with one or more component
     | 
  

  | 
    1.7.8 | 
    
     - added extension points description for components
     | 
  

  | 
    1.7.7 | 
    
     - added 'Cortex-M85' to DcoreEnum
     - added 'Dpacbti' attribute to Processor
     - added 'Dpacbti' attribute to Condition
     - added 'DpacbtiEnum'
     | 
  

  | 
    1.7.6 | 
    
     - type of n and m attributes of BoardFeatureType and Pname becomes xs:string
     | 
  

  | 
    1.7.5 | 
    
     - Rename DcoreEnum 'Star' to 'Star-MC1'
     | 
  

  | 
    1.7.4 | 
    
     - clarified the usage of the "public" attribute and set public="true" as default.
     | 
  

  | 
    1.7.3 | 
    
     - added 'Star' to DcoreEnum
     | 
  

  | 
    1.7.2 | 
    
     - added 'XC' to CompilerEnumType to enable use of Microchip XC32 compiler
     | 
  

  | 
    1.7.1 | 
    
      - undo removing deprecated attributes as they are still used in latest pdsc file versions:
        DeviceVendorEnum: Lapis Semiconductor, DeviceVendorEnum: Pname, BoardReferenceType: Dvendor, Dname
      - added condition attribute to TaxonomyDescriptionType supporting context specific taxonomies (e.g. vendor or device specific)
     | 
  

  | 
    1.7.0 | 
    
      - added processor attribute Dcdecp for implemented Custom Datapath Extension Coprocessors (Cortex-M33)
      - extended BoardType added DebugProbeType and FlashAlgorithm.
      - removed types and references used by deprecated cprj format.
     | 
  

  | 
    1.6.3 | 
    
- removed CMSIS Project Description format (cpdsc) from CMSIS-Pack. Format has been superseeded by new format specification located in the CMSIS
  **Build** tab.
- added debug setup tutorial to the documentation.
- updated documentation of PackChk "errors and warnings".
- updated documentation to reflect switch from 'http' to 'https'.
- added 'folder' attribute to example's \`<environment>` element.
- added 'ACCESS_AP' to DataPatchAccessTypeEnum.
- added 'Cortex-M55' to DcoreEnum.
- added 'uninit' attribute to \`<memory>` element to replace deprecated 'init' attribute.
- updated DmveEnum 'DmveEnum' specification.
- updated minimum length of \`<Cclass>`, \`<Cgroup>` and \`<Cvariant>` attributes in \`<component>` from 3 to 2.
- removed all types specific to cpdsc format. Cpdsc is replaced by Cprj with dedicated schema.
     | 
  

  | 
    1.6.2 | 
    Modifications compared to Version 1.6.1
  - added \`<accessportV1>` and \`<accessportV2>` to describe CoreSight access port parameters.
  - added attribute '__apid' to \`<debug>` and \`<datapatch>` to reference \`<accessportV1>` and \`<accessportV2>` elements.
  - added attribute 'dormant' to \`<debugconfig>` element.
     | 
  

  | 
    1.6.1 | 
    Modifications compared to Version 1.6.0
- added a Bash script to support pack generation on Linux or Windows.
- added **custom** attribute to component element.
- added **TrustZone-disabled** value to software model selection.
- added dbg_setup_tutorial in CMSIS-Pack documentation.
     | 
  

  | 
    1.6.0 | 
    Modifications compared to Version 1.5.0
- added Armv8.1-M MVE processor feature attribute 'Dmve'.
- added local and global pre-include section Pre_Include_Local_Component_h, Pre_Include_Global_h.
- added file categories 'preIncludeLocal' and 'preIncludeGlobal' to the FileCategoryEnum.
- added file attribute 'path' for file category 'header' to add support for relative include paths.
- added to package element the possibility to restrict the usage of the with attributes Dcore, Dname, Dvendor, and Tcompiler.
- added dominate element to overwrites identical devices, APIs, or components.
- added attribute 'condition' to the api element so that an API can be excluded based on a condition.
- added new pack_Cclass : "Audio", "Board Part", "Data Exchange", "Extension Board", "IoT Client", "IoT Utility", "Security", "Utility".
     | 
  

  | 
    1.5.0 | 
    Modifications compared to Version 1.4.9
- added sdf_pg
- updates to Device Vendor
- removed usage of DP CTRL/STAT CDBGRSTREQ from debugPortStart default sequence
- added flashinfo with children `<block>` and `<gap>` to describe flash devices for sequence-based flash download
- new debug access functions and global debug variables for sequence-based flash download
- added repository element for specifying origin of public repositories
- added attributes to release element specifying repository tag and url for downloading repository content
- added new processor Cortex-M35P
     | 
  

  | 
    1.4.9 | 
    Modifications compared to Version 1.4.8
- added Toptions attribute for use in conditions
- updated documentation for generator section to reflect new exe, web, and eclipse sections
     | 
  

  | 
    1.4.8 | 
    Modifications compared to Version 1.4.7
- added support for semantic versioning quality information in ConditionVersionType
- updated Pack schema file making some elements optional
- added Pack Index File Specification and schema file
     | 
  

  | 
    1.4.7 | 
    Modifications compared to Version 1.4.6
- added multiple version types to tighten the schema checking depending on context
- added new generator sections for exe, web and eclipse based generators in <generator>
- added new processor attributes Dtz = Trustzone and Ddsp = DSP instructions for Armv8-M
- added new attributes Dtz, Ddsp, Dsecure to conditions <require>, <deny>, <accept>
- added new processors Cortex-M23 and Cortex-M33 and other in DcoreEnum
- added new attribute public to books and images to indicate public use of documents and board images
     | 
  

  | 
    1.4.6 | 
    Modifications compared to Version 1.4.5
- refined Dname string pattern restriction (RestrictedStringDname)
     | 
  

  | 
    1.4.5 | 
    Modifications compared to Version 1.4.4
- added: Punits to ProcessorType
- added: Punit to DebugType
     | 
  

  | 
    1.4.4 | 
    Modifications compared to Version 1.4.3
- added: attribute defaultResetSequence to DebugType.
- added: <requirements> section:
    - <packages> defining dependencies between packs
    - <languages> defining required language support e.g. C99
    - <compiler> defining required toolchains
- added: <create> section used for tool independent project description
    - attributes: name, documentation, condition
    - <target> specifies the board and device targeted by the project
    - <options>
    - <files> specifies the grouped files
- updated: <algorith> element
    - added attributes: style, parameter and endian
- updated: <memory> element
    - added attributes: name, access and alias
    - deprecating attribute: id (replaced by name + access)
     | 
  

  | 
    1.4.3 | 
    Modifications compared to Version 1.4.1
- Adding attribute "sdf" to debugconfig element within section <devices>
     | 
  

  | 
    1.4.1 | 
    Modifications compared to Version 1.4.0
- pName, Dname, Dvariant type changed from xs:string to RestrictedString
     | 
  

  | 
    1.4.0 | 
    Modifications compared to Version 1.3.3:
- device section _memory_ specification redefined, deprecating _id_ attribute
- device section _algorithm_ support multiple flash programming algorithm styles
- device section _debug_ adding CJTAG debug port type
     | 
  

  | 
    1.3.3 | 
    Modifications compared to Version 1.3.1:
- Schema Version remains unchanged, since no incompatible update
- _Added_ generator section can specify a target GPDSC file that it will generate
- _Added_ A component can be linked to a generator and the generator's GPDSC file will be
  automatically included in the project as part of the component.
- _Added_ A generator command is optionally extended by a separate description of arguments
- _Updated_ Vendor list
- _Updated_ Utility packChk.exe to Version 1.3.0.0:
  - detect redefinitions of boards
  - check presence of board image files
  - check for duplicate device features
  - check for duplicate device definitions
  - check for
  - minor bug fixes
     | 
  

  | 
    1.3.1 | 
    Modifications compared to Version 1.3:
- Schema Version remains unchanged, since no incompatible update
- _Added_ Cortex-M7 to the predefined list of processors
- _Updated_ Vendor list
- _Added_ File version attribute to debugvars element of device description
- _Updated_ XML file header encoding tag set to capital "UTF8"
- _Deprecated_ init attribute of <memory> element in <devices> section deprecated
     | 
  

  | 
    1.3 | 
    Modifications compared to Version 1.2:
 - _Added_ attributes to release tag for managing deprecation and changing Pack IDs
 - _Removed_ external RAMn and ROMn memory IDs in memory tag
 - _Added_ FileCategoryTypes in <file> element for C, C++, Assembler, Linker
 - _Extended_ specification of <require>, <accept> and <deny> with Cversion and Capiversion ranges
 - _Added_ createPackUtil and packchk for Pack validation
 - _Added_ documentation for the Example Pack based on LPC1800 Device Family
 - _Refined_ <debug> element description
 - Many clarifications in the documentation along with examples
     | 
  

  | 
    1.2 | 
    Clarifications for release. | 
  

  | 
    1.1 - Preliminary | 
    Update release for review:
 - _new_ Boards description
 - _new_ Debug description
 - _revised_ Device Feature capture
 - _new_ Generator description
 - _new_ Flash Algorithm Specification
 - _new_ Configuration Wizard Annotation Specification | 
  

  | 
    1.0 - Preliminary | 
    Preliminary release for review | 
  

  | 
    0.10 | 
    Release for beta review |
