---
id: "spec-package-components-element-package-files-file"
type: "concept"
domain: "pack"
title: "/package/components element: /package/.../files/file"
summary: "The element file is the mechanism to attach files to the software. The file purpose is defined through the category attribute. The name attribute identifies the file."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/components_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_components_pg.html"
license: "Apache-2.0"
mode: "V"
---

The element **file** is the mechanism to attach files to the software.
The file purpose is defined through the **category** attribute. The **name** attribute identifies the file.


**Example:**
```
<package>
  ...
  <apis>
    <api Cclass="Device" Cgroup="Driver UART" exclusive="0">
      <files>
        <file category="doc" name="Driver/Doc/UART/html/index.html"/>
        <file category="header" name="Driver/Include/Driver_UART.h"/>
      </files>
    </api>
  </apis>
  ...
  <components>
    <component Cclass="Device" Cgroup="Startup" Cversion="3.1.1" >
      <files>
        <file category="header" name="Device/Include/system_stm32f2xx.h"/>
        <file category="source" name="Device/Source/ARM/startup_stm32f2xx.s" attr="template"/>
        <file category="source" name="Device/Source/system_stm32f2xx.c" attr="template"/>
      </files>
    </component>
  </components>
  ...
</package>
```


 



  | 
    Parents | 
    Element Chain | 
  

  | 
    files | 
    /package/apis/api/files | 
  

  | 
    files | 
    /package/components/component/files | 
  

  | 
    files | 
    /package/components/bundle/component/files | 
  

  | 
    files | 
    /package/generators/generator/project_files | 
  

  | 
    Attributes | 
    Description | 
    Type | 
    Use | 
  

  | 
    name | 
    File path, file name, and file extension in the format **path/name.extension**. The file path is relative to the root directory of the Pack.
    \n `For <b>category="doc"</b> then the name can be either a file relative to the root or a URL to an online documentation resource.` | 
    xs:string | 
    required | 
  

  | 
    path | 
    for **category="header"** the path attribute explicitly can be used to specify the include path to be added to the commandline of the build tools,
        specifying an incomplete path. This way the include file requires the specification of the subdirectory (e.g. \#include "sub_dir/includeFile.h") which can act as
        acting as namespace for header files which otherwise have the same name. | 
    xs:string | 
    optional | 
  

  | 
    category | 
    Defines the purpose of the file. Select the predefined value as listed in the table File Categories.
    \n `Only one <b>category="doc"</b> should be included per component.` | 
    FileCategoryEnum | 
    required | 
  

  | 
    language | 
    Defines the language of the file category `source`, `header`, `include`. Select one of the predefined value as listed
        in the table File Language Attribute. If not specified, a source file is identified based
        on known file extensions, header files and include paths will be applied for all tools. | 
    FileLanguageAttributeType | 
    optional | 
  

  | 
    scope | 
    Defines the visibility of `header` and `include`. Select one of the predefined value as listed in the table
        File Scope Attribute. If not specified, a header file or an
        include path is considered `public`. | 
    FileScopeAttributeType | 
    optional | 
  | 
    attr | 
    Defines the special use and handling of a file. Select a predefined value as defined in the table File Attributes.
     | 
    FileAttributeEnum | 
    optional | 
  

  | 
    condition | 
    Enter the identifier (attribute ****id**)** of a condition. The element is used if the condition resolves to `true`.
    If the condition resolves to `false`, then the element will be ignored.
    For example, a library might be specific for a certain toolchain or processor instruction set. | 
    xs:string | 
    optional | 
  

  | 
    select | 
    Brief description and purpose of the file. The **_select_** attribute is **required** when **_attr_** is set to `template`.
    When multiple template files of a component have the same **_select_** string, they are treated as a single selectable template. This way, multiple template
    or interface files can be bundled. The **_select_** attribute is **optional** for files with **_category_** `header` to indicate the usage of a header file.
     | 
    xs:string | 
    optional | 
  

  | 
    src | 
    Path information. The path is specified relative to the Pack Description File. If **\b** category is set to `library`,
    then the **\b** src string can contain a list of directory paths separated by semicolons. A debugger will search those paths
    for locating the source files of the modules archived in the library supporting the debugging of library code. | 
    xs:string | 
    optional | 
  

  | 
    version | 
    File-specific version information. This is used particularly for files copied into the project workspace.
    Before a file gets copied, a version check avoids unnecessary copy actions. If a file does not have a version, then the component version is used.
    The version format is described in Version Type. | 
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
    projectpath | 
    View location path for a file of component inside IDE project explorer view. When a component is selected into a project, IDE
        can use it to construct component file view location path inside the IDE project explorer view. It gives component files a better
        organization view instead of just flat placing them in the project explorer. IDE can also directly ignore this attribute,
        then all files of the component will be flat placed inside the project explorer view under Cclass. | 
    xs:string | 
    optional | 
  




 


 **Table: File Attributes**

The file attribute defines the special handling in the project when being used as configuration, template, or interface file.
The table lists the values available as a file attribute.


  | 
    attr= | 
    Description | 
  

  | 
    config | 
    The file is a configuration file of the component. It is expected that only configuration options are modified.
    The file is managed as part of the component, as a project-specific file typically copied into the component section of the project.s | 
  

  | 
    template | 
    The file is used as a source code template file. It is expected to be edited and extended by the software developer.
    The file can be copied into a user section of the project. | 
  

<!--
  | 
    interface | 
    The file contains the source code of an interface that connects two software components. It is a working reference implementation that may need customization.
    The file can be copied to a user section of the project. | 
  

-->


**Note:**
Header files with the attribute `config` must be located in a directory within the pack that is
not otherwise specified as an "include folder" of this or any other component's files of the category "header" or "include".
For example:
```
<file category="header"  name="src/config/user_config.h" attr="config" version="1.0.0" />
```
Config files are copied into the project folder and are adopted specifically for that project. Due to the include path search order of the compiler,
chances exist that the unmodified header file in the pack repository is found first and used by the
compiler (creating unexpected results).

**Note:**
The attribute `copy` is deprecated and should no longer be used.


 

 **Table: File Categories**

File category types define the use of component files within the application. Typically, these files are added to
the project and processed by the build tools.

File categories are used in the following elements:
- element_file
- element_gen_file

The table lists the predefined values for a file category.


  | 
    category= | 
    Description | 
  

  | 
    doc | 
    Documentation | 
  

  | 
    header | 
    Header file used in the component. Sets an include file path and adds the file name attribute to the list of files to be added
    to a module using the **\#include** statement. Note: specify only those files as header files that form part of the API of the component, required to use the component | 
  

  | 
    include | 
    Sets an include file path. Note: ensure that the name attribute specifies a directory and ends with a '/'. | 
  

  | 
    library | 
    Library file | 
  

  | 
    object | 
    Object file that can be added to the application | 
  

  | 
    source | 
    Startup-, system-, and other C/C++, assembler, etc. source files. Relying on commonly used file extensions. | 
  

  | 
    sourceC | 
    C source file | 
  

  | 
    sourceCpp | 
    C++ source file | 
  

  | 
    sourceAsm | 
    Assembly source file | 
  

  | 
    linkerScript | 
    linker script file that can be selected by tool-chains | 
  

  | 
    utility | 
    a command line tool that can be configured for pre- or post-processing during the build process | 
  

  | 
    image | 
    Files of image type are marked for special processing into a File System Image embedded into the application.
        This category requires the _attr_ being set to _template_<!-- or _interface_ -->.
     | 
  

  | 
    preIncludeGlobal | 
    The specified file is added as a pre-include file to the compiler command line for all modules of the whole **project** (globally). | 
  

  | 
    preIncludeLocal | 
    The specified file is added as a pre-include file to the compiler command line for all modules of the **component** (locally). | 
  

  | 
    genSource | 
    The specified file is a source file which is exclusively used by the generator associated with this component specified by attribute _generator_. | 
  

  | 
    genHeader | 
    The specified file is a header file which is exclusively used by the generator associated with this component specified by attribute _generator_. | 
  

  | 
    genParams | 
    The specified file is a parameter file which is exclusively used by the generator associated with this component specified by attribute
        _generator_. | 
  

  | 
    genAsset | 
    The specified file is an asset file which is exclusively used by the generator associated with this component specified by attribute _generator_.
        it is up to the generator to identify purpose and format of the file by name or file type. | 
  

  | 
    other | 
    Other file types not covered in the list above | 
  




 


 **Table: File Language Attribute**

File language attribute type defines the language for `source`, `header` and `include` file categories. Based on the language 
the information is used by language specific build tools.

File language attribute is used in the following elements:
- element_file
- element_gen_file

The table lists the predefined values for a file language.


  | 
    language= | 
    Description | 
  

  | 
    asm | 
    The file information is passed to an assembler. | 
  

  | 
    c | 
    The file information is passed to a C compiler. | 
  

  | 
    cpp | 
    The file information is passed to a C++ compiler. | 
  

  | 
    c-cpp | 
    The file information is passed to both C- as well as C++ compiler. | 
  

  | 
    link | 
    The file information is passed to a linker. | 
  




 



 **Table: File Scope Attribute**

File scope attribute type defines the visibility of `header` file and `include` path file categories.
Based on the specified scope header files or include paths are `public` or `private`.

File language attribute is used in the following elements:
- element_file
- element_gen_file

The table lists the predefined values for the scope attribute.


  | 
    scope= | 
    Description | 
  

  | 
    public | 
    Applies only to file elements of category `include` and category `header`; ignored otherwise. A `public` include path
        is added to the command line for building any modules of the specified language. A `public` header file
    is suggested for inclusion by other modules and is considered the contract of the component. | 
  

  | 
    private | 
    Applies only to file elements of category `include` and category `header`; ignored otherwise. A `private` include path
        is added to the command line for building any module of the component for the specified language.  A `private` header file
        is indicating an internal header file which must not be explicitly included by modules outside of the scope of the component. |
