---
id: "tfm-ff-m-isolation-default-access-rules"
type: "concept"
domain: "security"
title: "FF-M Isolation: Reference Implementation / Default access rules"
summary: "Hardware protection components MAY have the capability to collect regions not explicitly configured in static or runtime settings, and then apply default access rules to these regions."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/ff_isolation.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/ff_isolation.html#default-access-rules"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Reference Implementation_

Hardware protection components MAY have the capability to collect regions
not explicitly configured in static or runtime settings, and then apply
default access rules to these regions. Furthermore, one default rule can be
applied to multiple non-contiguous regions which makes them share a common
boundary. This operation sets up a standalone 'region' the same as other
explicitly configured regions. And it doesn't affect the analysis summary
above - just be aware that some regions listed in the table MAY not be
explicitly configured.

Take the MPU as an example, MPU can assign a default privileged access
attribute to the regions (e.g. SPM and PRoT regions) not explicitly configured.
This feature can reduce required MPU regions and ease the programming because
regions can be put non-address-contiguous and skip the explicit configuration.


**Important:** When this default access rules mechanism is applied, the implicitly configured regions must be reviewed to ensure the isolation boundaries are set correctly.
