---
id: "tfm-adding-secure-partition-add-manifest"
type: "concept"
domain: "security"
title: "Adding Secure Partition: Process / Add manifest"
summary: "Each Secure Partition must have resource requirements declared in a manifest file. The Secure Partition Manager (SPM) uses the manifest file to assemble and allocate resources within the SPE. The manifest includes the following:"
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@b7db526:docs/integration_guide/services/tfm_secure_partition_addition.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_secure_partition_addition.html#add-manifest"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Process_

Each Secure Partition must have resource requirements declared in a manifest
file. The Secure Partition Manager (SPM) uses the manifest file to assemble and
allocate resources within the SPE. The manifest includes the following:

- A Secure Partition name.
- A list of implemented RoT Services.
- Access to other RoT Services.
- Memory requirements.
- Scheduling hints.
- Peripheral memory-mapped I/O regions and interrupts.

The current manifest format in TF-M is "yaml" which is different from the
requirement of PSA FF.
The users can set LOW, NORMAL or HIGH in `priority` attribute in a Secure
Partition manifest.

The manifest tool `tools/tfm_parse_manifest_list.py` calculates the load
priority of Secure Partitions based on their `priority` values and their
dependencies.
SPM determines the loading and initialization order of Secure Partitions
based on their load priority values during TF-M initialization.

- A Secure Partition with a higher `priority` is loaded and initialized
  before Secure Partitions with lower `priority`.
- A Secure Partition is loaded and initialized after its dependencies are.
Here is a manifest reference example for the IPC model:

To use SFN model, the user needs to replace `"model": "IPC"` to
`"model": "SFN"`. The user also needs to remove the attribute
`"entry_point"`, and optionally replace it with `"entry_init"`.
```yaml

{
  "psa_framework_version": 1.1,
  "name": "TFM_SP_EXAMPLE",
  "type": "APPLICATION-ROT",
  "priority": "NORMAL",
  "model": "IPC",
  "entry_point": "tfm_example_main",
  "stack_size": "0x0200",
  "services" : [
    {
      "name": "ROT_A",
      "sid": "0x000000E0",
      "non_secure_clients": true,
      "connection_based": true,
      "version": 1,
      "version_policy": "STRICT"
      "mm_iovec": "disable"
    }
  ],
  "mmio_regions": [
    {
      "name": "TFM_PERIPHERAL_A",
      "permission": "READ-WRITE"
    }
  ],
  "irqs": [
    {
      "source": "TFM_A_IRQ",
      "name": "A_IRQ",
      "handling": "SLIH"
    }
  ]
  "dependencies": [
    "TFM_CRYPTO",
    "TFM_INTERNAL_TRUSTED_STORAGE_SERVICE"
  ]
}
```

#### Update manifest list

The `<TF-M base folder>/tools/tfm_manifest_list.yaml` is used to collect
necessary information of secure partition.
The manifest tool `tools/tfm_parse_manifest_list.py` processes it and
generates necessary files while building.

Please refer to the tfm_manifest_list for the format of manifest lists.

Reference configuration example:

```yaml

{
  "description": "TFM Example Partition",
  "manifest": "secure_fw/partitions/example/tfm_example_partition.yaml",
  "conditional": "@TFM_PARTITION_EXAMPLE@",
  "output_path": "partitions/example",
  "version_major": 0,
  "version_minor": 1,
  "pid": 290,
  "linker_pattern": {
    "library_list": [
      "*tfm_*partition_example*"
     ]
  }
}
```
TF-M also supports out-of-tree Secure Partition build where you can have your
own manifest lists.
Please refer to Out-of-tree Secure Partition build for details.


#### Secure Partition ID Distribution

Every Secure Partition has an identifier (ID). TF-M will generate a header file
that includes definitions of the Secure Partition IDs. The header file is
`<TF-M build folder>generated/interface/include/psa_manifest/pid.h`. Each
definition uses the `name` attribute in the manifest as its name and the
value is allocated by SPM.

The Partition ID can be set to a fixed value or omitted to be auto allocated.

```c

#define name id-value
```

==================================== ======================
**Secure Partitions**                **PID Range**
==================================== ======================
TF-M Internal Partitions             0 - 255
PSA and user Partitions              256 - 2999
TF-M test Partitions                 3000 - 4999
Firmware Framework test Partitions   5000 - 5999
Reserved                             6000 -
==================================== ======================
Please refer to `<TF-M base folder>/tools/tfm_manifest_list.yaml`,
''<TF-M extras repo>/partitions/\*/\*_manifest_list.yaml'',
`<TF-M test repo>/tests_reg/test/secure_fw/tfm_test_manifest_list.yaml` and
`<TF-M test repo>/tests_psa_arch/spe/tfm_psa_ff_test_manifest_list.yaml` for the detailed
PID allocations.

About where to add the definition, please refer to the chapter Update manifest list.


#### RoT Service ID (SID) Distribution

An RoT Service is identified by its RoT Service ID (SID). A SID is a 32-bit
number that is associated with a symbolic name in the Secure Partition
manifest. The bits [31:12] uniquely identify the vendor of the RoT Service.
The remaining bits [11:0] can be used at the discretion of the vendor.

Here is the RoT Service ID table used in TF-M.


=========================== ====================== ========================
**Partitions**              **Vendor ID(20 bits)** **Function ID(12 bits)**
=========================== ====================== ========================
initial_attestation         0x00000                0x020-0x03F
platform                    0x00000                0x040-0x05F
protected_storage           0x00000                0x060-0x06F
internal_trusted_storage    0x00000                0x070-0x07F
crypto                      0x00000                0x080-0x09F
firmware_update             0x00000                0x0A0-0x0BF
tfm_secure_client           0x0000F                0x000-0x01F
tfm_ipc_client              0x0000F                0x060-0x07F
tfm_ipc_service             0x0000F                0x080-0x09F
tfm_slih_test_service       0x0000F                0x0A0-0x0AF
tfm_flih_test_service       0x0000F                0x0B0-0x0BF
tfm_ps_test_service         0x0000F                0x0C0-0x0DF
tfm_secure_client_2         0x0000F                0x0E0-0x0FF
tfm_sfn_test_service_1      0x0000F                0x100-0x11F
tfm_sfn_test_service_2      0x0000F                0x120-0x13F
tfm_attest_test_service     0x0000F                0x140-0x15F
=========================== ====================== ========================

#### RoT Service Stateless Handle Distribution

A Secure partition may include stateless services. They are distinguished and
referenced by stateless handles. In manifest, a `stateless_handle` attribute
is set for indexing stateless services. It must be either `"auto"` or a
number in the range [1, 32] in current implementation and may extend. Also the
`connection-based` attribute must be set to `false` for stateless services.

The indexes of stateless handles are divided into two ranges for different
usages.
Indexes [1, 16] are assigned to TF-M Secure Partitions.
The rest indexes [17, 32] are reserved for any other Secure Partitions, for
example Secure Partitions in `tf-m-tests` and `tf-m-extras`.

The following table summaries the stateless handle allocation for the TF-M
Secure Partitions.


=============================== =======================
 **Partition name**              **Stateless Handle**
=============================== =======================
TFM_SP_CRYPTO                   1
TFM_SP_PS                       2
TFM_SP_ITS                      3
TFM_SP_INITIAL_ATTESTATION      4
TFM_SP_FWU                      5
TFM_SP_PLATFORM                 6
TFM_SP_POWER_MGMT               7
=============================== =======================
For the indexes of other Secure Partitions, please refer to their manifests or
documentations.


#### stack_size

The `stack_size` is required to indicate the stack memory usage of the Secure
Partition.
The value of this attribute must be a decimal or hexadecimal value in bytes.
It can also be a build configurable with default value defined in
`config_base.cmake`.
The value of the configuration can be overridden to fit different use cases.


#### heap_size

This attribute is optional. The default value is 0.
It indicates the heap memory usage of the Secure Partition.
The allowed values are the same as the `stack_size`.


#### mmio_regions

This attribute is a list of MMIO region objects which the Secure Partition
needs access to. TF-M only supports the `named_region` current. Please refer
to PSA FF for more details about it. The user needs to provide a name macro to
indicate the variable of the memory region.

TF-M uses the below structure to indicate a peripheral memory.

```c

struct platform_data_t {
  uint32_t periph_start;
  uint32_t periph_limit;
  int16_t periph_ppc_bank;
  int16_t periph_ppc_loc;
};
```
This structure is not expected by TF-M, it's only that the current
implementations are using. Other peripherals that need different information
to create isolation need to define a different structure with the same name.
Here is an example for it:

```c

struct platform_data_t tfm_peripheral_A;
#define TFM_PERIPHERAL_A                 (&tfm_peripheral_A)
```

#### mm_iovec

Memory-mapped iovecs (MM-IOVEC) provides direct mapping of client input and output vectors into the
Secure Partition.
When this attribute is set to `enable`, it enables Secure Partitions to use the MM-IOVEC APIs if
the framework supports MM-IOVEC.

Using MM-IOVEC provides a memory and runtime optimization for larger buffers, but reduces mitigation
for common security vulnerabilities.
Please refer to Firmware Framework for M 1.1 Extensions for more details.
Whether to use MM-IOVEC depends on the requirements of memory and runtime optimization and security.
