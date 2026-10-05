---
id: "tfm-booting-a-multi-cpu-system-api-additions"
type: "concept"
domain: "security"
title: "Booting a Multi CPU System: API Additions"
summary: "For all three, an empty implementation will be provided with a weak symbol so that platforms only have to provide the new functions if they are required."
status: "draft"
collection: "tf-m"
source: "TrustedFirmware-M/trusted-firmware-m@9671378:docs/design_docs/multi-cpu/booting_a_multi_cpu_system.rst"
doc_source: "https://trustedfirmware-m.readthedocs.io/en/latest/design_docs/multi-cpu/booting_a_multi_cpu_system.html#api-additions"
license: "BSD-3-Clause"
mode: "V"
---

Three new HAL functions are required:

```c

void tfm_hal_boot_ns_cpu(uintptr_t start_addr);
```
- Called on the secure core from `ns_agent_mailbox` partition when it first
  runs (after protections have been configured).

- Performs the necessary actions to start the non-secure core running the code
  at the specified address.

```c

void tfm_hal_wait_for_ns_cpu_ready(void);
```
- Called on the secure core from `ns_agent_mailbox` partition after making the
  above call.

- Flags that the secure core has completed its initialization, including setting
  up the IPC mechanism.

- Waits, if necessary, for the non-secure core to flag that it has completed its
  initialisation

```c

void tfm_ns_wait_for_s_cpu_ready(void);
```
- Called on the non-secure core from `main()` after the multi-cpu-specific
  initialization (on a single core system, this would be the start of the
  non-secure code), before the first use of the IPC mechanism.

- Flags that the non-secure side has completed its initialization.

- Waits, if necessary, for the secure core to flag that it has completed its
  initialization.

For all three, an empty implementation will be provided with a weak symbol so
that platforms only have to provide the new functions if they are required.

---------------

Copyright (c) 2019-2022 Cypress Semiconductor Corporation. All rights reserved.
SPDX-FileCopyrightText: Copyright The TrustedFirmware-M Contributors
SPDX-License-Identifier: BSD-3-Clause
