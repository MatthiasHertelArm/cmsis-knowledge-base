---
id: "tfm-platform-documentation-rules"
type: "concept"
domain: "security"
title: "Platform Documentation: Rules"
summary: "Platform Documentation: Rules"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/platform/documenting_platform.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/platform/documenting_platform.html#rules"
license: "BSD-3-Clause"
mode: "V"
---

- Platforms documentation is gathered in `/docs/platform` folder.
  This folder is similar to the platforms implementation folder
  `/platform/ext/target` but does not need to mirror its structure.

- A vendor is represented by a subfolder with `index.rst` as an entry
  point. This file may contain general materials about a vendor
  not specific to a particular platform.

- A vendor's `index.rst` shall carry a TOCtree structure with a list of all
  supported platforms at the top level.

- An explicit platform name is preferred in a vendor's TOCtree instead of use of
  platform's title by default.


**Note:** Do not forget to update the summary file after adding a new platform `/docs/platform/platform_introduction.rst` included into TF-M introduction.
