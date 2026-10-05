---
id: "svd-svd-description-svd-format"
type: "concept"
domain: "pack"
title: "SVD Description (*.svd) Format"
summary: "The CMSIS-SVD format is based on XML and was influenced by IP-XACT."
status: "draft"
collection: "svd-spec"
source: "Open-CMSIS-Pack/svd-spec@b449298:doxygen/src/svd.txt"
doc_source: "https://open-cmsis-pack.github.io/svd-spec/main/svd_Format_pg.html"
license: "Apache-2.0"
mode: "V"
---

The CMSIS-SVD format is based on XML and was influenced by IP-XACT.
Due to the much wider scope and complexity of IP-XACT, it was decided to specify a separate
format focused and tailored towards the description of the programmer's view of a device.

**CMSIS-SVD XML Hierarchy**

    "CMSIS-SVD Hierarchy Levels"

One CMSIS-SVD file contains the description of a single device. A device consists of a processor and at least
one peripheral. Each peripheral contains at least one register. A register may consist of one or more fields.
The range of values for a field may be further described with enumerated values.

- File Conventions:
Outlines the main conventions for writing an SVD description file.
\n\n
- svd_Example_pg
Provides an example outlining the SVD XML structure.
\n\n
- Device Level:
The top level of a System View Description is the device. On this level, information is captured that
is specific to the device as a whole. For example, the device name, description, or version. The minimal
addressable unit as well as the bit-width of the data bus are required by the debugger to perform the
correct target accesses. \n
Default values for register attributes like register size, reset value, and access permissions can be set for the
whole device on this level and are implicitly inherited by the lower levels of the description. If however specified
on a lower level, the default setting from a higher level will get overruled.
\n\n
- CPU Level:
The CPU section describes the processor included in the microcontroller device.
This section is mandatory if the SVD file is used to generate the device header file.
\n\n
- Peripherals Level:
A peripheral is a named collection of registers. A peripheral is mapped to a defined _base address_ within the
device's address space. A peripheral allocates one or more exclusive address blocks relative to its base address,
such that all described registers fit into the allocated address blocks. Allocated addresses without an associated
register description are automatically considered reserved. The peripheral can be assigned to a group of
peripherals and may be associated with one or more interrupts.
\n\n
- Registers Level:
A register is a named, programmable resource that belongs to a peripheral. Registers are mapped to a defined address in
the address space of the device. An address is specified relative to the peripheral base address.
The description of a register documents the purpose and function of the resource. A debugger requires information
about the permitted access to a resource as well as side effects triggered by read and write accesses respectively.
\n\n
- Fields Level:
Registers may be partitioned into chunks of bits of distinct functionality. A chunk
is referred to as _field_. The field names within a single register must be unique.
Only architecturally defined fields shall be described. Any bits not being explicitly described are treated as reserved.
They are not displayed in the System Viewer and are padded in the bit fields of the device header file.
The case-insensitive field named **"reserved"** is treated as a keyword and each field with this name
is ignored.
\n\n
- Enumerated Values Level:
An enumeration maps an unsigned integer constant to a descriptive identifier and, optionally, to a description string.
Enumerations are used in C to enhance the readability of source code. Similarly, it can be used by debuggers to
provide more instructive information to the programmer, avoiding a lookup in the device documentation.
\n\n
- Special Elements:
Specific elements that occur in various other elements are described in this section.
\n\n
- **Vendor Extensions:**
The CMSIS-SVD format includes a section named \tagem{vendorExtensions} positioned after the closing tag \tagem{/peripherals}.
This allows silicon vendors and tool partners to extend the description beyond the current specification.


**Multiple Instantiation**

CMSIS-SVD supports the reuse of whole sections of the description. The attribute **derivedFrom** for
`<peripheral>`, `<register>`, and `<field>` specifies the source of the section to be copied from.
Note that a section must be specified before it can be referenced. There is no support for forward references.
Individual tags can be used to redefine specific elements within a copied section.

**Array of Elements**

A powerful construct in data structures of the C programming language is the array. An
array is a series of data elements of the same type selected via an index. CMSIS-SVD supports arrays
for `<peripheral>`, `<cluster>`, and `<register>`.

**Peripheral Grouping**

Peripherals that provide similar functionality (Simple Timer, Complex Timer) can be grouped with the element \tagem{groupName}.
Peripheral groups help structuring the list of peripherals in the debugger.
All peripherals associated with the same group name are collectively listed under this group
in the order they were specified in the SVD file.

**Descriptions**

On each level, the tag \tagem{description} provides verbose information about the respective element.
The description field plays an important part in improving software development productivity as it gives
instant access to information that otherwise would need to be looked up in the device documentation.

All multiple whitespace characters (space, tab, linefeed, carriage return) may be removed from the description
by any tool for further processing (i.e. SVDConv does). In order to preserve explicit linebreaks one has to
use the linefeed escape sequence (i.e. \\n).
