---
id: "view-component-viewer-component-viewer-usage-example"
type: "concept"
domain: "trace"
title: "Component Viewer: Component Viewer Usage Example"
summary: "The following steps enable views for static information of software components in the µVision debugger. Other tools might use different ways to accomplish this."
status: "draft"
collection: "cmsis-view"
source: "ARM-software/CMSIS-View@285e935:Documentation/Doxygen/src/cmp_viewer.md"
doc_source: "https://github.com/ARM-software/CMSIS-View/blob/285e935/Documentation/Doxygen/src/cmp_viewer.md#component-viewer-usage-example"
license: "Apache-2.0"
mode: "V"
---

The following steps enable views for static information of software components in the µVision debugger. Other tools might use different ways to accomplish this.

**For User Code:**

 1. Create an SCVD file to display cv_static_information.
 2. Add the SCVD file to µVision as described in \manscvd.
 3. Use the µVision debugger windows as described in \cviewer.

**For Pre-annotated software components:**

The software packs for MDK-Middleware, CMSIS, and CMSIS-FreeRTOS already contain the relevant *.SCVD files.

 - Add the SCVD file of the desired software component to µVision as described in \manscvd.
 - Use the µVision debugger windows as described in \cviewer.

For examples on how to write SCVD files, refer to the ExampleProjects section.

### Static Component Information

The *.SCVD file can be used to format static information of the application using the elem_objects.

Example code that is stored in the file **MyTest.c** (the file name is important for static variables).

```c
static int some_error = 1;
char string[10] = "MyTest";
```

The following **MyTest.scvd** file reads static program information from the variables in the above code snippet:

```xml
<?xml version="1.0" encoding="utf-8"?>

<component_viewer schemaVersion="0.1" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="Component_Viewer.xsd">
  <component name="MyExample" version="1.0.0"/>    <!-- name and version of the component  -->
  
  <objects>
    <object name="MyProgram">
      <read name="error_val"   type="int32_t" symbol="MyTest.c/some_error"   />
      <read name="string_val"  type="int8_t"  symbol="string"  size="10"     />
      <out name="MyProgram">
        <item property="some_error" value="%d[error_val]" /> 
        <item property="string"     value="%t[string_val]" /> 
      </out>
    </object>
  </objects>

</component_viewer>
```

**Adding the file in the µVision debugger**

In the µVision debugger, this *.SCVD file is specified in the dialog **Options for Target -> Debug -> Manage Component Viewer Description Files**. Click on **Add Component Viewer Description File** and add the related *.SCVD file.

(figure: Manage *.SCVD files)

Using the SCVD file, µVision debugger shows static information about the program. The related view opens with **View - Watch Windows - MyProgram**.

(figure: "Event Recorder output formatted with *.SCVD file")
