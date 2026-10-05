---
id: "sds-utilities-setup"
type: "concept"
domain: "test"
title: "Utilities: Setup"
summary: "Perform the following steps to setup the Python environment for using the SDS utilities."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/utilities.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#setup"
license: "Apache-2.0"
mode: "V"
---

Perform the following steps to setup the Python environment for using the SDS utilities.

- [Install Python](https://www.python.org/downloads/) or verify the version with:

```bash
>python --version
```

- Navigate to the folder `SDS/<version>/utilities` and install the required Python packages with `pip`:

```bash
>cd %CMSIS_PACK_ROOT%/ARM/SDS/3.1.0/utilities
>pip install -r requirements.txt
```

- Add to the system **Path** environment variable the path to the `%CMSIS_PACK_ROOT%/ARM/SDS/3.1.0/utilities` folder.

!!! Note
    - `%CMSIS_PACK_ROOT%` is just a placeholder for the Pack location on your local PC. The **Path** variable must be extended by the absolute path to the `utilities` folder.

### Windows

- On Windows, ensure that the environment variable **PATHEXT** contains the extension `.PY`.

!!! Tip
    - When the **Path** environment variable is configured, you may simply start the utilities by using its name. For example, entering `>sdsio-server` starts the utility.
