---
id: "tfm-rollback-protection-in-tf-m-secure-nv-counters-and-anti-rollback-protection"
type: "concept"
domain: "security"
title: "Rollback protection in TF-M secure boot: NV counters and anti-rollback protection"
summary: "Trusted non-volatile counters might not be supported by a hardware platform. In this case anti-rollback protection might still be feasible."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/booting/secure_boot_rollback_protection.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/booting/secure_boot_rollback_protection.html#nv-counters-and-anti-rollback-protection"
license: "BSD-3-Clause"
mode: "V"
---

Trusted non-volatile counters might not be supported by a hardware platform.
In this case anti-rollback protection might still be feasible.

The device threat model needs to consider the following aspects:

 - What is the trust level of the boot loader towards the active software

  - If the boot loader cannot protect the anti-rollback mechanism from the
    secure image then the following threat is unmitigated: The content of the
    memory area which holds the active image could be replaced with a valid but
    an older version of the software with software only attack, i.e.: remote
    code execution.
  - If the boot loader does not trust the loaded image at all then security
    counter must have a copy in NV counter area.

 - Another aspect to consider is where the active image is stored

  - Trusted memory: i.e. on-chip flash (eFlash). The threat that a malicious
    actor can modify the content of trusted memory with HW attack is out of
    scope for the current implementation. It is assumed that if an active image
    and related manifest data is stored in trusted memory then the included
    security counter cannot be compromised.
  - Untrusted memory: i.e. external (off-chip) storage, where malicious actor
    can physically access it so it is possible to modify its content, therefore
    the value of included security counter is unreliable.

If the active image is stored in untrusted storage and it is feasible to modify
its content (i.e. replace the whole image to an older version including
corresponding manifest) then the value of security counter must be copied to
the NV counter area. During software validation the boot loader must compare
the new image's security counters against the security counter stored in
non-volatile counters.

If the active image is stored in trusted memory and boot loader trusts in the
active software then it is not mandatory to store the security counter to
non-volatile counter area. During software validation the boot loader is
allowed to compare the new image's security counters against active image's
security counter.

The evaluation of trusted and untrusted memory must be done per target platform
during threat modelling.

For the most robust implementation the following principles should be applied:

 - Always use NV counters for storing security counter value if supported by
   the hardware.
 - Each software stage must not be able to decrease their corresponding NV
   counter.
