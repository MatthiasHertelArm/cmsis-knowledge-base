---
id: "tfm-trusted-firmware-m-profile-medium-design-details-2"
type: "concept"
domain: "security"
title: "Trusted Firmware-M Profile Medium-ARoT-less: Design details"
summary: "Most of design in Profile Medium-ARoT-less is identical to that in Profile Medium. Refer to Profile Medium document [2] for details. Only the differences between Profile Medium-ARoT-less and Profile Medium are specified below."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/configuration/profiles/tfm_profile_medium_arot-less.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/configuration/profiles/tfm_profile_medium_arot-less.html#design-details"
license: "BSD-3-Clause"
mode: "V"
---

Most of design in Profile Medium-ARoT-less is identical to that in Profile Medium. Refer to
Profile Medium document [2]_ for details.
Only the differences between Profile Medium-ARoT-less and Profile Medium are specified below.


### Firmware framework


PSA Certified ARoT-less [1]_ is only applicable to devices that don’t support Application RoT (ARoT)
services.
The platform only consists of PSA RoT domain(s) in SPE making it unnecessary to implement the
isolation between ARoT and PSA RoT.
Therefore, this profile selects isolation level 1 to simplify implementation and optimize memory
footprint and performance.

Since only isolation level 1 is required, this profile enables SFN model rather than IPC mode for
further simplification.


### Protected Storage


Protected Storage (PS) is implemented as an Application RoT service in TF-M by default.
Therefore, PS is disabled by default in this profile.


### FWU RoT Service


As PSA Certified ARoT-less requests, FWU RoT Service is enabled by default to support secure
update of platform if the platform supports FWU.

.. note ::

    **Implementation note**

    The entire secure update sequence involves multiple agents and components, including bootloader,
    TF-M FWU RoT Service, image update application(s), remote server(s), etc.

    The secure update sequence is implementation-defined. Here is a reference of TF-M integration
    with FreeRTOS OTA [8]_.
