---
id: "tfm-firmware-update-service-benefits-analysis-on-this-partition"
type: "concept"
domain: "security"
title: "Firmware Update Service: Benefits Analysis on this Partition"
summary: "The APIs listed in PSA Firmware Update API spec [1] can also be implemented in the non-secure side."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/services/tfm_fwu_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_fwu_service.html#benefits-analysis-on-this-partition"
license: "BSD-3-Clause"
mode: "V"
---

### Implement the FWU functionality in the non-secure side

The APIs listed in PSA Firmware Update API spec [1]_ can also be implemented in
the non-secure side.


### Pros and Cons for implementing FWU APIs in secure side



#### Pros

- It protects the image in the passive or staging area from being tampered with
  by the NSPE. Otherwise, a malicious actor from NSPE can tamper the image
  stored in the non-secure area to break image update.

- It protects secure image information from disclosure. In some cases, the
  non-secure side shall not be permitted to get secure image information.

- It protects the active image from being manipulated by NSPE. Some bootloader
  supports testing the image. After the image is successfully installed and
  starts to run, the user should set the image as permanent image if the image
  passes the test. To achieve this, the area of the active image needs to be
  accessed. In this case, implementing FWU service in SPE can prevent NSPE
  from manipulating the active image area.

- On some devices, such as the Arm Musca-B1 board, the passive or staging area
  is restricted as secure access only. In this case, the FWU partition should
  be implemented in the secure side.


#### Cons

- It increases the image size of the secure image.
- It increases the execution latency and footprint. Compared to implementing
  FWU in NSPE directly, calling the Firmware Update APIs which are implemented
  in the secure side increases the execution latency and footprint.
- It can increase the attack surface of the secure runtime.

Users can decide whether to call the FWU service in TF-M directly or implement
the Firmware Update APIs in the non-secure side based on the pros and cons
analysis above.
