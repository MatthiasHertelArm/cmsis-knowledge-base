---
id: "spec-package-requirements-package-requirements-compilers"
type: "concept"
domain: "pack"
title: "/package/requirements: /package/requirements/compilers"
summary: "/package/requirements: /package/requirements/compilers"
status: "draft"
collection: "pack-spec"
source: "Open-CMSIS-Pack/Open-CMSIS-Pack-Spec@b3f8fcf:doxygen/src/pdsc_format.txt"
doc_source: "https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/element_requirements_pg.html"
license: "Apache-2.0"
mode: "V"
---

**Example** compilers section:
```
<package xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="PACK.xsd"/>
  ...
  <requirements>
    <compilers>
      <compiler name="ARMCC" version="5.0.0:6.0.0-0"/>
    </compilers>
  </requirements>
  ...
</package>
```

**/compiler**


| Parents | Element Chain |  |  |
|---|---|---|---|
| requirements | element_requirements |  |  |
| Attributes | Description | Type | Use |
| name | Name of the required compiler (i.e. "ARMCC", "IAR") | CompilerEnumType | required |
| version | Version of the required compiler which can be: - Minimum version (higher versions are accepted). - Version range specified with min_version **:** max_version . min_version must be lower or equal than max_version . For a version range that retains the major version, the max_version is set to the next major version with minor, patch and release qualifier set to "0". - Fixed version is specified if min_version and max_version are equal. | VersionType | required |
