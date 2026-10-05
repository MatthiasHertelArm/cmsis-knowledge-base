---
id: "spec-publish-a-cmsis-pack-using-a-pack-index-service"
type: "concept"
domain: "pack"
title: "Publish a CMSIS-Pack: Using a pack index service"
summary: "Tool, software, or silicon vendors may provide a web infra-structure that lists packs that are available from multiple vendors. Companies like Arm or IAR provide such a service for making CMSIS-Packs available to a wider audience of developers."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_publish.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html"
license: "Apache-2.0"
mode: "V"
---

Tool, software, or silicon vendors may provide a web infra-structure that lists packs that are available from multiple
vendors. Companies like Arm or IAR provide such a service for making CMSIS-Packs available to a
wider audience of developers. The packs are then found by pack management tools and their contents are listed on web sites,
such as Arm's list of CMSIS-Packs.

Once you are ready to publish your packs, please send the URL of the \elem{vendor}.\elem{name}.pdsc or \elem{vendor}.pidx
file to the following email addresses:

- for Arm tools, email to CMSIS@arm.com.
- for IAR tools, email to CMSIS@iar.com.

Arm uses the pack information to generate a list of available software packs. The following content will be processed in
order to generate the web site (https://www.keil.arm.com/packs/):
- Version
- Release notes
- Devices
- Boards
- Examples
- Software components
- Description
- An Overview.md file if present

Furthermore, the data is used to create lists of boards
and devices.

Please allow up to seven working days for the process. If the files contain any errors, you will be notified. Otherwise, the
information is added to the index server. We strongly recommend using a pidxFile for better maintainability.


### The vidx2pidx conversion tool


If you want to check the content of you pidxFile, you can use the vidx2pidx utility to create your own `index.pidx`
file. Once created, you can use it with `cpackget` to install the packs listed in the PIDX file.

Follow these steps to run the conversion and installatin:
- Download vidx2pidx.
- Create you \elem{vendor}.vidx file just listing the \elem{vendor.pidx} file.
  **Code example**
  
```xml
  <index schemaVersion="1.0" xmlns:xs=http://www.w3.org/2001/XMLSchema-instance xs:noNamespaceSchemaLocation="PackIndex.xsd">
    <vendor>vendor</vendor>
    <url></url>
    <timestamp>2024-08-08T06:30:00</timestamp>
    <vindex>
      <pidx vendor="vendor" url="https://github.com/vendor/packrepo/raw/main/"/>
    </vindex>
  </index>
```
- Run
```
  vidx2pidx vendor.vidx
```
  to create the `index.pidx.`
- Run
```
  cpackget init -R packroot index.pidx
```
  to create a new pack root directory with only the packs from the `index.pidx.`
- Run
```
  cpackget list -p -R packroot
```
  to show all packs and check if the process was successful.
- Install all listed packs using
```
  cpackget add <packID> -R packroot
```
  to check if all packs can be downloaded and installed.


### Rehosting a pack


Sometimes, it is necessary to rehost a pack (moving a pack from one URL to another). Rehosting implies changing the \elem{url}
element in the PDSC file. To ensure that the pack is found by a Pack Index Service, follow this procedure:
- Create a new version of the pack: update the \elem{vendor}.\elem{name}.pdsc file with the new \elem{url} ("url_B") and a new
  `<release>` tag with an incremented version.
- Place a copy of this latest \elem{vendor}.\elem{name}.pdsc file at url_B and url_A (the original URL).
- Add this new PDSC file to an updated \elem{vendor}.\elem{name}.\elem{version}.pack (needs to match the version number in
  the PDSC file).
- Copy the new \elem{vendor}.\elem{name}.\elem{version}.pack **only** to url_B.
- Copy all previous packs from url_A to url_B (so that they are available at the new location).
- Inform Arm about the new URL by either:
  - updating the \elem{vendor}.pidx with url_B for this pack **or**
  - emailing a link to the new PDSC file if your company does not maintain a \elem{vendor}.pidx

**Note:**
- The PDSC file and all pack versions need to be accessible from the same new URL ("url_B").
- Arm recommends to keep the url_A alive for at least six months so that users have time to pick up the change. Be aware
  that users who have not noticed the change might be unable to find pack updates once url_A have become unavailable.


### Renaming a pack


Sometimes, it is necessary to rename a pack (because the pack vendor and/or its name have changed for example). To ensure
that the pack is found by a Pack Index Service and the tools, follow this procedure:
- Create a new:
  - PDSC file with the updated \elem{name} and/or \elem{vendor}, for example NewVendor.NewName.pdsc. The
    \elem{version} should start at 1.0.0.
  - pack containing the new PDSC file with the corresponding \elem{name} and/or \elem{vendor}, for example
    NewVendor.NewName.1.0.0.pack.
- Create a new:
  - version of the old PDSC file (Vendor.Name.pdsc) with a new \elem{release} tag (with an updated version),
    containing the \elem{deprecated} and \elem{replacement} element. The latter pointing to the "NewVendor.NewName".
  - version of the old \elem{vendor}.\elem{name}.\elem{version}.pack file with the PDSC you have created above.
- Copy:
  - all four files (new PDSC and pack, updated old PDSC and pack) to the \elem{url} location.

**Note:**
- Using this approach, you can only do a one-to-one pack replacement.
- If you want to create more than one replacement pack for a given source pack, you need to work with
  requirements.
