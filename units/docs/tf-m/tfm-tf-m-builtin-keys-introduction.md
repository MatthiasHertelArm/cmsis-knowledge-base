---
id: "tfm-tf-m-builtin-keys-introduction"
type: "concept"
domain: "security"
title: "TF-M builtin keys: Introduction"
summary: "When TF-M is integrated on a platform, the platform itself can provide several keys for usage which are bound to the device instead of being owned by a specific secure partition."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/tfm_builtin_keys.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/tfm_builtin_keys.html#introduction"
license: "BSD-3-Clause"
mode: "V"
---

When TF-M is integrated on a platform, the platform itself can provide several
keys for usage which are bound to the device instead of being owned by a
specific secure partition. When those keys are readable by the secure
processing environment, the platform must provide a function to load these keys
in the HAL layer, either loading them from OTP or another platform specific
location or subsystem. These keys are henceforth referred to as "builtin keys",
and might include (but are not limited to) the following:

  1. The Hardware Unique Key (HUK)
  2. The Initial Attestation Key (IAK)

The `tfm_builtin_key_loader` component implements a mechanism to discover
those keys and make them available to the PSA Crypto APIs for usage. Note that
if a key is stored in a subsystem which can't be read by the secure
processing environment, a full opaque driver [1]_ must be used to be able to use
those keys through the PSA Crypto APIs. This document focuses only on the case
where the keys can be read by the SPE (i.e. running TF-M), so the driver applies
only on those cases, which can be considered as "_transparent_ builin keys".

In TF-M's legacy solution, the IAK is loaded by the attestation service as a
volatile key, which requires some key-loading logic to be implemented by that
partition. The HUK is not loaded in the crypto service, and is instead used by
an implementation of a TF-M specific KDF algorithm which then loads the key and
invokes TF-PSA-Crypto directly. Both solutions are far from ideal as they
require an effort to load (and duplicate) the keys per each user, or require a
dedicated code in TF-M that directly interacts with the HAL layer and invokes
functions from the crypto library bypassing the PSA Crypto interface. The aim of
the `tfm_builtin_key_loader` driver is to provide a uniform interface to use
the builtin keys available in a platform.

Implementing a driver to deal with builtin keys allows to expand the legacy
solution for dealing with this type of keys in several ways. For example, it
avoids the need for partitions to implement dedicated mechanisms for probing the
HAL layer for builtin keys and load them as volatile. It removes the need to
have implementation specific call flows for deriving keys from the HUK (as that
requirement now is fulfilled by the driver itself transparently). It allows
uniform access to the keys also from the NS world (in any case, subject to the
policy dictated by the platform). Correctly abstracts away details of the key
handling mechanism from TF-M partitions into the PSA Crypto core key management
subsystem.
