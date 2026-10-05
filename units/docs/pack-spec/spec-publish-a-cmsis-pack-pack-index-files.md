---
id: "spec-publish-a-cmsis-pack-pack-index-files"
type: "concept"
domain: "pack"
title: "Publish a CMSIS-Pack: Pack index files"
summary: "CMSIS-Pack is designed as a web-based distribution network. Each provider of a CMSIS-Pack (also referred to as vendor) is responsible for hosting, maintaining and publishing unique versions of a CMSIS-Pack."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_publish.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html"
license: "Apache-2.0"
mode: "V"
---

CMSIS-Pack is designed as a web-based distribution network. Each provider of a CMSIS-Pack (also referred to as _vendor)_ is
responsible for hosting, maintaining and publishing unique versions of a CMSIS-Pack.

A CMSIS-Pack is uniquely identified by `<vendor>`.\
.`<version>`.pack. All published versions of a pack and the
PDSC file need to be available in the same web folder specified by \elem{url}. Multiple different packs may be located in the
same web folder.


### Package index file (PIDX)


The package index file lists all CMSIS-Packs hosted and maintained by a vendor. The file is hosted by the vendor and has the
name `<vendor>`.pidx. The `<vendor>` tag needs to match the file name. The file also contains the \elem{url} to it's origin, as
well as a `<timestamp>` of it's last update.

It is the vendor's obligation to update this file whenever:
- a new pack is added.
- a new version of a pack is added.
- a pack is deprecated.
- a replacement for a pack becomes available.

**MyVendor.pidx** example

```xml
<?xml version="1.0" encoding="UTF-8" ?>

<index schemaVersion="1.0.0" xs:noNamespaceSchemaLocation="PackIndex.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance">
  <vendor>MyVendor</vendor>
  <url>https://www.MyVendor.com/pack/</url>
  <timestamp>2024-01-25T15:00:10.7300074+00:00</timestamp>
  <pindex>
    <pdsc url="https://www.MyVendor.com/pack/mypack/" vendor="MyVendor" name="MyPack" version="1.1.0"/>
    ...
  </pindex>
</index>
```

Each individual pack is referenced by the attributes:
- \elem{url} = web folder where the PDSC and packs reside.
- \elem{vendor} = vendor of the pack.
- \elem{name} = the name of the pack.
- \elem{version} = the version number of the latest available release for the pack.

The package index file for the CMSIS-Pack compliant packs, hosted on www.keil.com can be found here:
https://www.keil.com/pack/Keil.pidx.

The benefit of a single package index file is, that this file only needs to be exchanged once and can be polled for updates
and additions of packs by a vendor. To add a vendor's packs to the public list maintained on www.keil.com, send an email to
CMSIS@arm.com attaching a version of the `<vendor>`.pidx file.


### Vendor index file (VIDX)


A vendor index file lists package index files from different vendors. This information can be used to compile a list of known
packs.

**MyVendor.vidx** example

```xml
<?xml version="1.0" encoding="UTF-8" ?>

<index schemaVersion="1.0" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="PackIndex.xsd">
  <vendor>MyVendor</vendor>
  <url>www.MyVendor.com/pack</url>
  <timestamp>2024-01-08T10:30:00</timestamp>
  <vindex>
    <pidx url="http://www.othervendor.com/MyPacks/" vendor="OtherVendor" />
    ...
  </vindex>
  <!-- the section below is only intended for the transition until all vendors use the <vendor>.pidx file
  <pindex>
    <pdsc url="http://www.othervendor2.com/packs/" vendor="OtherVendor2" name="MyPack" version="2.3.0"/>
    ...
    </pindex>
</index>
```

The latest index file of CMSIS-Packs belonging to vendor="ARM" and vendor="Keil" that are hosted and maintained here:
https://www.keil.com/pack/Keil.pidx

Arm also maintains a flat list of all CMSIS-Pack compliant packs reported to Arm here:
https://www.keil.com/pack/index.pidx

The vendor index file containing references to the package index files (or optionally PDSC files) used for compiling this
summary index file are listed in the Keil.vidx file and can be downloaded from here:
https://www.keil.com/pack/Keil.vidx

Based on these publicly available index files, everyone is equally positioned to create an index of available packs and their
latest versions.


### Index schema file

\verbinclude "PackIndex.xsd"
