---
id: "tfm-adding-secure-partition-implement-the-rot-services"
type: "concept"
domain: "security"
title: "Adding Secure Partition: Process / Implement the RoT services"
summary: "To implement RoT services, the partition needs a source file which contains the implementations of the services, as well as the partition entry point. The user can create this source file under <TF-M base folder>/secure_fw/partitions/example/tfm_example_partition.c."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/integration_guide/services/tfm_secure_partition_addition.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/integration_guide/services/tfm_secure_partition_addition.html#implement-the-rot-services"
license: "BSD-3-Clause"
mode: "V"
---

_Part of: Process_

To implement RoT services, the partition needs a source file which contains the
implementations of the services, as well as the partition entry point. The user
can create this source file under
`<TF-M base folder>/secure_fw/partitions/example/tfm_example_partition.c`.

As an example, the RoT service with SID **ROT_A** will be implemented.


#### Entry point for IPC Model Partitions

This function must have a loop that repeatedly waits for input signals and
then processes them, following the Secure Partition initialization.

```c

#include "psa_manifest/tfm_example.h"
#include "psa/service.h"

void tfm_example_main(void)
{
    psa_signal_t signals = 0;

    /* Secure Partition initialization */
    example_init();

    /*
     * Continually wait for one or more of the partition's RoT Service or
     * interrupt signals to be asserted and then handle the asserted
     * signal(s).
     */
    while (1) {
        signals = psa_wait(PSA_WAIT_ANY, PSA_BLOCK);
        if (signals & ROT_A_SIGNAL) {
            rot_A();
        } else {
            /* Should not come here */
            psa_panic();
        }
    }
}
```

#### Entry init for SFN Model Partitions

In the SFN model, the Secure Partition consists of one optional initialization
function, which is declared as the `entry_init` symbol as mentioned in
section Add manifest. After initialization, the entry_init function
returns the following values:

    - Return `PSA_SUCCESS` if initialization succeeds.

    - Return `PSA_SUCCESS` if initialization is partially successful,
      and you want some SFNs to receive messages. RoT Services that are
      non-operational must respond to connection requests with
      `PSA_ERROR_CONNECTION_REFUSED`.

    - Return an error status if the initialization failed, and no SFNs
      within the Secure Partition must be called.


#### Service implementation for IPC Model

The service is implemented by the `rot_A()` function, which is called upon an
incoming signal. This implementation is up to the user, however an example
service has been included for reference. The following example sends a message
"Hello World" when called.

```c

#include "psa_manifest/tfm_example.h"
#include "psa/service.h"

/* Some other type of services. */
#define SOME_ROT_A_SERVICE_TYPE                (1)

static void rot_A(void)
{
    const int BUFFER_LEN = 32;
    psa_msg_t msg;
    int i;
    uint8_t rec_buf[BUFFER_LEN];
    uint8_t send_buf[BUFFER_LEN] = "Hello World";

    psa_get(ROT_A_SIGNAL, &msg);
    switch (msg.type) {
    case PSA_IPC_CONNECT:
    case PSA_IPC_DISCONNECT:
        /*
         * This service does not require any setup or teardown on connect
         * or disconnect, so just reply with success.
         */
        psa_reply(msg.handle, PSA_SUCCESS);
        break;
    default:
        /* Handling services requested by psa_call. */
        if (msg.type == PSA_IPC_CALL) {
            for (i = 0; i < PSA_MAX_IOVEC; i++) {
                if (msg.in_size[i] != 0) {
                    psa_read(msg.handle, i, rec_buf, BUFFER_LEN);
                }
                if (msg.out_size[i] != 0) {
                    psa_write(msg.handle, i, send_buf, BUFFER_LEN);
                }
            }
            psa_reply(msg.handle, PSA_SUCCESS);
        } else if (msg.type == SOME_ROT_A_SERVICE_TYPE) {
            /* Operations for SOME_ROT_A_SERVICE_TYPE */
        } else {
            /* Invalid type for this Secure Partition. */
            return PSA_ERROR_PROGRAMMER_ERROR;
        }
    }
}
```

#### Service implementation for SFN Model

SFN model consists of a set of Secure Functions (SFN), one for each RoT
Service. The connection, disconnection and request messages do not cause a
Secure Partition signal to be asserted for SFN Secure Partitions. Instead,
the Secure Function (SFN) for the RoT Service is invoked by the framework,
with the message details provided as a parameter to the SFN. To add a secure
function (SFN) to process messages for each RoT Service, each SFN will have
following prototype.

```c

psa_status_t <<name>>_sfn(const psa_msg_t *msg);
```
A connection-based example service has been included for reference which
sends a message "Hello World" when called.

```c

#include "psa_manifest/tfm_example.h"
#include "psa/service.h"

/* Some other type of services. */
#define SOME_ROT_A_SERVICE_TYPE                (1)

psa_status_t rot_a_sfn(const psa_msg_t *msg)
{
    const int BUFFER_LEN = 32;
    int i;
    uint8_t rec_buf[BUFFER_LEN];
    uint8_t send_buf[BUFFER_LEN] = "Hello World";

    switch (msg->type) {
    case PSA_IPC_CONNECT:
    case PSA_IPC_DISCONNECT:
        /*
         * This service does not require any setup or teardown on connect
         * or disconnect, so just reply with success.
         */
        return PSA_SUCCESS;
    default:
        /* Handling services requested by psa_call. */
        if (msg->type == PSA_IPC_CALL) {
            for (i = 0; i < PSA_MAX_IOVEC; i++) {
                if (msg->in_size[i] != 0) {
                    psa_read(msg->handle, i, rec_buf, BUFFER_LEN);
                }
                if (msg.->out_size[i] != 0) {
                    psa_write(msg->handle, i, send_buf, BUFFER_LEN);
                }
            }
            return PSA_SUCCESS;
        } else if (msg->type == SOME_ROT_A_SERVICE_TYPE) {
            /* Operations for SOME_ROT_A_SERVICE_TYPE */
        } else {
            /* Invalid type for this Secure Partition. */
            return PSA_ERROR_PROGRAMMER_ERROR;
        }
    }
}
```

#### Test suites and test partitions


A regression test suite can be added to verify whether the new secure partition
works as expected. Refer to
[Adding TF-M Regression Test Suite](https://trustedfirmware-m.readthedocs.io/projects/tf-m-tests/en/latest/tfm_test_suites_addition.html#adding-a-new-test-suite)
for the details of adding a regression test suite.

Some regression tests require a dedicated RoT service. The implementations of
the RoT service for test are similar to secure partition addition. Refer to
[Adding partitions for regression tests](https://trustedfirmware-m.readthedocs.io/projects/tf-m-tests/en/latest/tfm_test_partitions_addition.html)
to get more information.


#### Out-of-tree Secure Partition build


TF-M supports out-of-tree Secure Partition build, whose source code folders
are maintained outside TF-M repo. Developers can configure
`TFM_EXTRA_MANIFEST_LIST_FILES` and `TFM_EXTRA_PARTITION_PATHS` in build
command line to include out-of-tree Secure Partitions.

- `TFM_EXTRA_MANIFEST_LIST_FILES`

  A list of the absolute path(s) of the manifest list(s) provided by out-of-tree
  Secure Partition(s).
  Use semicolons `;` to separate multiple manifest lists. Wrap the multiple
  manifest lists with double quotes.

- `TFM_EXTRA_PARTITION_PATHS`

  A list of the absolute directories of the out-of-tree Secure Partition source
  code folder(s). TF-M build system searches `CMakeLists.txt` of partitions in
  the source code folder(s).
  Use semicolons `;` to separate multiple out-of-tree Secure Partition
  directories. Wrap the multiple directories with double quotes.

A single out-of-tree Secure Partition folder can be organized as the figure
below.

:
```
secure partition folder
      ├── CMakeLists.txt
      ├── manifest_list.yaml
      ├── out_of_tree_partition_manifest.yaml
      └── source code
```
In the example above, `TFM_EXTRA_MANIFEST_LIST_FILES` and
`TFM_EXTRA_PARTITION_PATHS` in the build command can be configured as listed
below.

```bash

-DTFM_EXTRA_MANIFEST_LIST_FILES=<Absolute-path-sp-folder/manifest_list.yaml>
-DTFM_EXTRA_PARTITION_PATHS=<Absolute-path-sp-folder>
```
Multiple out-of-tree Secure Partitions can be organized in diverse structures.
For example, multiple Secure Partitions can be maintained under the same
directory as shown below.

:
```
top-level folder
      ├── Partition 1
      │       ├── CMakeLists.txt
      │       ├── partition_1_manifest.yaml
      │       └── source code
      ├── Partition 2
      │       └── ...
      ├── Partition 3
      │       └── ...
      ├── manifest_list.yaml
      └── Root CMakeLists.txt
```
In the example above, a root CMakeLists.txt includes all the partitions'
CMakLists.txt, for example via `add_subdirectory()`. The manifest_list.yaml
lists all partitions' manifest files.
`TFM_EXTRA_MANIFEST_LIST_FILES` and `TFM_EXTRA_PARTITION_PATHS` in build
command line can be configured as listed below.

```bash

-DTFM_EXTRA_MANIFEST_LIST_FILES=<Absolute-path-top-level-folder/manifest_list.yaml>
-DTFM_EXTRA_PARTITION_PATHS=<Absolute-path-top-level-folder>
```
Alternatively, out-of-tree Secure Partitions can be separated in different
folders.

:
```
partition 1 folder                    partition 2 folder
    ├── CMakeLists.txt                    ├── CMakeLists.txt
    ├── manifest_list.yaml                ├── manifest_list.yaml
    ├── partition_1_manifest.yaml         ├── partition_2_manifest.yaml
    └── source code                       └── source code
```
In the example above, each Secure Partition manages its own manifest files and
CMakeLists.txt. `TFM_EXTRA_MANIFEST_LIST_FILES` and
`TFM_EXTRA_PARTITION_PATHS` in build command line can be configured as listed
below. Please note those input shall be wrapped with double quotes.

```bash

-DTFM_EXTRA_MANIFEST_LIST_FILES="<Absolute-path-part-1-folder/manifest_list.yaml>;<Absolute-path-part-2-folder/manifest_list.yaml>"
-DTFM_EXTRA_PARTITION_PATHS="<Absolute-path-part-1-folder>;<Absolute-path-part-2-folder>"
```

Manifest list paths in `TFM_EXTRA_MANIFEST_LIST_FILES` do NOT have to be
one-to-one mapping to Secure Partition directories in
`TFM_EXTRA_PARTITION_PATHS`. The orders don't matter either.

`TFM_EXTRA_MANIFEST_LIST_FILES` and `TFM_EXTRA_PARTITION_PATHS` can be
configured in multiple extra sources. It is recommended to use CMake list
`APPEND` method to avoid unexpected override.

#### Further Notes


- In the IPC model, Use PSA FF proposed memory accessing mechanism. SPM
  provides APIs and checking between isolation boundaries, a free accessing
  of memory can cause program panic.
- In the IPC model, the memory checking inside partition runtime is
  unnecessary. SPM handles the checking while memory accessing APIs are
  called.
- In the IPC model, the client ID had been included in the message structure
  and secure partition can get it when calling psa_get() function. The secure
  partition does not need to call `tfm_core_get_caller_client_id()` to get
  the caller client ID anymore.
- In the IPC model, SPM will check the security policy and partition
  dependence between client and service. So the service does not need to
  validate the secure caller anymore.
