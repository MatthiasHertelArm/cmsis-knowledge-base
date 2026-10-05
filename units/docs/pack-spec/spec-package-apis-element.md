---
id: "spec-package-apis-element"
type: "concept"
domain: "pack"
title: "/package/apis element"
summary: "Application Programming Interfaces (apis) are C/C++ interface specifications that allow software to be divided into largely independent modules. Such modules can then be developed, tested, and maintained independently, and reused by different projects."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/apis_schema.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/pdsc_apis_pg.html"
license: "Apache-2.0"
mode: "V"
---

Application Programming Interfaces (apis) are C/C++ interface specifications that allow software to be divided into largely independent modules.
Such modules can then be developed, tested, and maintained independently, and reused by different projects. One example is the use of device drivers.
If device drivers are developed for different devices implementing the same API, the application software itself can be written independent from the
device it is build for.

The **apis** allow to distribute the Application Programming Interface Specifications decoupled from actual implementation. One example is the CMSIS-RTOS API,
which is specified as part of CMSIS, however, the actual RTOS implementation is provided by different vendors.

An API consists of a name, a brief description as well as one or more header files, and a document containing a detailed specification of the API.

The API typically defines one or more header files and optionally an include directory. It should have also related documentation that describes the API.

**Example:**

```
<api Cclass="ACloud IF" Cgroup="TRNG" Capiversion="1.2.0">
  <files>
    <file category="header" name="include/trng.h"/>
    <file category="include" name="include/somestuff"/>
    <file category="doc" name="html/trng.html"/>
  </files>
</api>
```

The API can be used either in the same software pack or other software packs. Having the API definition in one central software pack provides the
benefit that implementations are consistent.

The include file and directory are **included in the application project** when a **component** is selected that specifics the same **Cclass** and **Cgroup.**
The selection of a software component adds therefore both to a project: the files specified by the component element and the files specified by the api element.
Therefore, the component that is based on the API should not contain the header file that defines the API.

**Example:** this component adds also the api header file above

```
<component Cclass="ACloud IF" Cgroup="TRNG" Csub="Emulation" Capiversion="1.1.0">
  <description>Software simulation of random number generator</description>
  <files>
    <file category="sourceC" name="source/trng_emulation.c"/>
  </files>
</component>
```
Optionally, it is possible to request a minimum API version using the **Capiversion** attribute.

It is also possible to expose a combination of API definitions.  An example for that is the CMSIS-Driver for Ethernet that is defined as:
  - **Ethernet MAC** interface
  - **Ethernet PHY** interface
  - **Ethernet** interface that defines both MAC and PHY (this defines two API header files)
