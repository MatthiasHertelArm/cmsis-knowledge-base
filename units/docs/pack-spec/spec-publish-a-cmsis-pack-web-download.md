---
id: "spec-publish-a-cmsis-pack-web-download"
type: "concept"
domain: "pack"
title: "Publish a CMSIS-Pack: Web download"
summary: "If you want to make your packs publicly available, you need to host them on the web. For publishing packs, these options are available: - cp_HowWebDownloadWorks - cp_GitHubHosting"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pack_publish.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/createPackPublish.html"
license: "Apache-2.0"
mode: "V"
---

If you want to make your packs publicly available, you need to host them on the web. For publishing packs, these
options are available:
- cp_HowWebDownloadWorks
- cp_GitHubHosting

The following diagram shows how you can publish your packs when using a pack indexing service:

 "Pack hosting and indexing service"

When you run the command `cpackget` `update-index,` the tool queries the package index file (index.pidx)
from the pack index server. This file is generated using the vidx2pidx tool from the
vendor index file (index.vidx) which points to all known \elem{vendor}.pidx and stand-alone PDSC files.

The PIDX file allows you to change pack versions and add packs to your distribution list. All packs that are referenced in the
PIDX file will be processed and validated. Only error-free packs will become available via web pages and development tools.

**Note:** Refer to the cp_KeilComPack section for more information how to get listed on such an indexing server.


### Self-hosted packs


Any web server can be used to host a software pack (specified by the `\elem{url}` element in the PDSC file). At this location,
the following files should be present:
-# \elem{vendor}.\elem{name}.pdsc [required]: pack description file.
-# \elem{vendor}.\elem{name}.\elem{version}.pack [required]: pack file where \elem{version} refers to the latest version
   specified in the PDSC file.
-# \elem{vendor}.pidx [optional]: list with all packs hosted and maintained by the vendor (refer to pidxFile)

All previous versions listed in the \elem{releases} section of the PDSC file should be present at the `\elem{url}` as well. This
allows users to revert updates or to download a previous version of a software pack (for maintenance purposes).

The \elem{vendor}.pidx allows you to publish multiple packs to a Pack Index Service at once.

**Note:**
- The \elem{url} element in \elem{vendor}.\elem{name}.pdsc is the location where these services check for new packs. At this
  \elem{url} location, an (unversioned) \elem{vendor}.\elem{name}.pdsc file and a (versioned)
  \elem{vendor}.\elem{name}.\elem{version}.pack must be available.
- The \elem{url} is the page where the pack is downloaded. This means, if the URL or the PDSC/pack files become unavailable, users are unable to download the pack.
- When a new PDSC/pack file is available, it is important to update the version number, otherwise the Pack Index Service will not recognize that the pack has changed.
- Previous versions of a (versioned) \elem{vendor}.\elem{name}.\elem{version}.pack should remain available.


### GitHub-hosted packs


If you develop your packs publicly on GitHub, you can use the infrastructure to host your packs. The recommended way to do
this is as follows (note that in this example, \elem{orgname} is equal to \elem{vendor} in the other examples. We use
\elem{orgname} here as this is the nomenclature on GitHub):
- Create a repository for the PIDX file, for example `github.com/orgname/indexrepo.` The PIDX file should be named \elem{orgname}.pidx.
- Create seperate repositories for each pack, for example:
  - `github.com/orgname/name1`
  - `github.com/orgname/name2`
- At the top-level of each repository's `main` branch, you need have a \elem{orgname}.\elem{nameX}.pdsc file.
- Once you publish a pack, attach the \elem{orgname}.\elem{nameX}.\elem{version}.pack file to the release assets - this will be
  used as the download location of the pack.

This diagram shows an exemplary set up on GitHub with pack versions 1.0.0 and 1.3.0:

 "Hosting packs on GitHub"


#### PIDX file on GitHub


The vendor (orgname) PIDX file would look like the following:

```xml
<?xml version="1.0" encoding="UTF-8" ?>

<index schemaVersion="1.0.0" xs:noNamespaceSchemaLocation="PackIndex.xsd" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance">
  <vendor>orgname</vendor>
  <url>https://github.com/orgname/indexrepo/raw/main/</url>
  <timestamp>2024-08-22T15:00:10.7300074+00:00</timestamp>
  <pindex>
    <pdsc url="https://github.com/orgname/name1/raw/main/" vendor=”orgname" name=”name1" version="1.0.0"/>
    <pdsc url="https://github.com/orgname/name2/raw/main/" vendor=”orgname" name=”name2" version="1.0.0"/>
  </pindex>
</index>
```

**Note:** When updating one of the packs, you only need to change the version number and update the timestamp. All other entries
remain the same. Please make sure that only release quality packs are made available using this mechanism. You can build local
releases of a pack anytime for testing purposes.


#### PDSC file on GitHub


A PDSC file for one of the repositories would look like this:

```xml
<?xml version="1.0" encoding="utf-8"?>

<package schemaVersion="1.7.7" xmlns:xs="http://www.w3.org/2001/XMLSchema-instance" xs:noNamespaceSchemaLocation="PACK.xsd">
  <vendor>orgname</vendor>
  <name>name1</name>
  <license>LICENSE</license>
  <description>Whatever Pack</description>
  <url>https://github.com/orgname/name1/raw/main/</url>
  <supportContact>info@orgname.com</supportContact>
  <repository type="git">https://github.com/orgname/name1.git</repository>
  <releases>
    <release version="1.0.0" tag="v1.0.0" date="2024-08-22" url="https://github.com/orgname/name1/releases/download/v1.0.0/orgname.name1.1.0.0.pack">Initial release</release>
  </releases>
…	
```

When updating a pack, you need to:
- Change the \elem{url} to the location of the latest pack file in the PDSC.
- Add a new \elem{release} version with the correct entries in the PDSC.
- Attach the pack file to the release assets.
- Update the PIDX file with the latest version information.

**Note:**
While the repository's `main` branch can be used to host the PDSC file, additional confidence against unwanted changes can
be made if you use a dedicated branch for hosting the PDSC file. This avoids breaking unintentionally the pack location when
accepting a pull request (PR).
