---
id: "tfm-internal-trusted-storage-its-servi-detailed-design-considerations"
type: "concept"
domain: "security"
title: "Internal Trusted Storage (ITS) Service: Detailed design considerations"
summary: "The ITS APIs identify assets with 64-bit UIDs, to which the ITS service must append the 32-bit client ID of the calling partition for access control."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/design_docs/services/tfm_its_service.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/services/tfm_its_service.html#detailed-design-considerations"
license: "BSD-3-Clause"
mode: "V"
---

### Mapping UID onto file ID

The ITS APIs identify assets with 64-bit UIDs, to which the ITS service must
append the 32-bit client ID of the calling partition for access control. The
existing filesystem uses 32-bit file IDs to identify files, so some mapping
would be required to convert between the identifiers.

SST uses the object table to do the mapping from client ID, UID pairs to file
IDs, which means making an extra filesystem read/write for each get/set
operation. This mapping has minimal overhead for SST though, because object
table lookups are already required for rollback protection.

For ITS, no rollback protection feature is required, so there are two options:

- Keep a simplified version of the SST object table that just maps from
  (client ID, UID) to file ID

- Modify the filesystem to take (at least) 96-bit file IDs, in the form of a
  fixed-length char buffer.

The advantage of the former is that it would require no extra modification to
the existing filesystem code, and the existing SST object table could be cut
down for ITS. However, it would mean that every ITS request would invoke twice
the number of filesystem operations, increasing latency and flash wear. The code
size of the ITS partition would be increased, as would RAM usage as the table
would need to be read into RAM.

The latter option would make the filesystem slightly more complex: the size of a
metadata entry would be increased by 64-bits and the 96-bit fids would need to
be copied and compared with `memcpy` and `memcmp` calls. On the other hand,
mapping onto file IDs would incur only the cost of copying the UID and client ID
values into the file ID buffer.

A third, even more general, solution would be to use arbitrary-length
null-terminated strings as the file IDs. This is the standard solution in
full-featured filesystems, but we do not currently require this level of
complexity in secure storage.

With this in mind, the proposed option is the second.


### Storing create flags

The ITS APIs provide a 32-bit `create_flags` parameter, which contains bit
flags that determine the properties of the stored data. Only one flag is
currently defined for ITS: `PSA_STORAGE_FLAG_WRITE_ONCE`, which prevents a UID
from being modified or deleted after it is set for the first time.

There are two places that these flags could be stored: in the file data or as
part of the file metadata.

For the first option, the ITS implementation would need to copy to the flags
into the buffer containing the data, and adjust the size accordingly, for each
set operation, and the reverse for each get. Every get_info operation would need
to read some of the file data, rather than just the metadata, implying a second
flash read. A potential downside is that many of the cryptographic assets stored
in ITS will be aligned to power-of-two sizes; adding an extra 32-bits would
misalign the size, which may reduce flash performance or necessitate adding
padding to align to the flash page size.

To implement the second option, a 32-bit `flag` field would be added to the
filesystem's metadata structure, whose interpretation is defined by the user.
This field would clearly be catered towards the PSA Storage APIs, even if
nominally generic, and alternative filesystems may not have any such field.
However, it is a more intuitive solution and would simplify both flash alignment
and get_info operations.

Overall, it seems more beneficial to store the flags in the metadata, so this is
the proposed solution.


### Code sharing between Protected Storage and ITS

To de-duplicate the filesystem code used by both Protected Storage and ITS, it
is proposed that Protected Storage calls ITS APIs as its backend filesystem.

Protected Storage essentially becomes an encryption, authentication and rollback
protection layer on top of ITS. It makes IPC requests or secure function calls
to the ITS service to do filesystem operations on its behalf.

This has a couple of advantages:

- It shrinks Protected Storage's stack size, because the filesystem and flash
  layer stack is only in ITS.

- It automatically solves the problem of ensuring mutual exclusion in the
  filesystem and flash layers when Protected Storage and ITS are called
  concurrently. The second request to ITS will just be made to wait by the SPM.

The disadvantage of this approach is that it will increase the latency of
Protected Storage requests, due to the extra overhead associated with making a
second IPC request or secure function call. It also limits Protected Storage to
using only the ITS APIs, unless extra veneers are added solely for Protected
Storage to use. This, for example, prevents Protected Storage from doing partial
writes to file without reading and re-writing the whole file.

ITS will need to be modified to direct calls from Protected Storage to a
different flash device. It can use the client ID to detect when the caller is
Protected Storage, and pass down the identity of the flash device to use to the
flash layer, which then calls the appropriate driver.

An open question is what to do if Protected Storage itself wants to store
something in internal storage in the future (e.g. rollback counters, hash
tree/table or top hash). A couple of possible solutions would be:

- Divide up the UIDs, so certain UIDs from Protected Storage refer to assets in
  internal storage, and others to ones in external storage.

- Use the `type` field of `psa_call` in IPC model to distinguish between
  internal and external storage requests.

The other option for code sharing would be for Protected Storage and ITS to
directly share filesystem code, which would be placed in a shared code region.
With this approach, mutual exclusion to the flash device would need to be
implemented separately, as would some way of isolating static memory belonging
to each partition but not the code. Because of these complications, this option
has not been considered further at this time.
