---
id: "spec-package-releases-element-package-releases-release"
type: "concept"
domain: "pack"
title: "/package/releases element: /package/releases/release"
summary: "Contains brief information of the main changes in each release version of a Pack. The content is a string written between the opening and closing release tags."
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_releases.html"
license: "Apache-2.0"
mode: "V"
---

Contains brief information of the main changes in each release version of a Pack. The content is a string written between the opening and closing **release** tags.
This list must be strictly ordered by `version`, with the highest release `version` at the top.

**Example:**
```
<releases>
  <release version="1.1.1" date="2020-05-12">Fixed a problem with the feature xyz.
  </release>
  <release version="1.1.0" date="2020-03-13">Introduces a new feature xyz.
  </release>
  <release version="1.0.0" date="2020-02-23">First published version.
  </release>
</releases>
```

**Example** for a public repository:
```
<package>
  ...
  <repository type="git">https://github.com/ARM-software/CMSIS-Driver.git</repository>
  <releases>
    <release version="2.1.0" tag="2.1.0" url="https://github.com/ARM-software/CMSIS-Driver/archive/2.1.0.zip">
      Added LAN9220 Ethernet MAC+PHY driver.
    </release>
    <release version="2.0.0" tag="2.0.0" url="https://github.com/ARM-software/CMSIS-Driver/archive/2.0.0.zip">
      First published version.
    </release>
  </releases>
  ...
</package>
```

**Example** for a deprecated pack with a replacement:
```
<releases>
  <release version="1.0.1" date="2020-04-18" deprecated="2020-04-18" replacement="Vendor.pack_name">
  </release>
  <release version="1.0.0" date="2020-03-24">Initial version.
  </release>
</releases>
```


 



| Parent Element | Element Chain |  |  |
|---|---|---|---|
| releases | element_releases |  |  |
| Attributes | Description | Type | Use |
| version | Version number of the release. The version format is described in Version Type. | VersionType | required |
| date | Release date (specified as YYYY-MM-DD, for example 2014-12-14 (14th December 2014). Note: release date is only user information. The version number identifies the latest pack. | xs:date | optional |
| tag | In case the repository element is specified, the tag attribute is used to specify the repository tag that corresponds to this release of the pack. | xs:string | optional |
| url | HTTPS URL specifying the location of the pack of the specified version. This can be used to override the default location being `\`<url>`/\`<vendor>`.\`<name>`.\`<version>`.pack | xs:anyURI | optional |
| deprecated | Pack is no longer officially supported after the set date. It will be excluded from checks for update. Deprecated packs may remain available for download from the server. Tools will continue to work but may provide indicators highlighting end of support for the pack and its content. Not recommended for use with new projects. Note this attribute is only relevant when set for the latest release located on top of the releases section. | xs:date | optional |
| replacement | Specifies the vendor and name of the Pack that shall be used instead. Use in conjunction with the deprecated attribute. E.g. the maintainer of the Pack A.X_DFP changes from vendor **A** to vendor **B.** In this case the attribute deprecated gets set in the A.X_DFP.pdsc and the replacement attribute set to B.X_DFP. Tools use this information to redirect users to a supported pack. | xs:string | optional |
