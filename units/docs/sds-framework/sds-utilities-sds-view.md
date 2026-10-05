---
id: "sds-utilities-sds-view"
type: "concept"
domain: "test"
title: "Utilities: SDS-View"
summary: "The Python utility SDS-View generates a time-based plot from data recorded in SDS files (<stream-name>.<label>.sds) using the metadata provided in <stream-name>.sds.yml."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/utilities.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#sds-view"
license: "Apache-2.0"
mode: "V"
---

The Python utility [**SDS-View**](https://github.com/ARM-software/SDS-Framework/tree/main/utilities) generates a time-based plot
from data recorded in SDS files (`<stream-name>.<label>.sds`) using the metadata provided in `<stream-name>.sds.yml`.

The horizontal time scale is derived from the number of data points in a recording and `sample-frequency:` provided in the metadata description.
All plots from a single recording are displayed on the same figure (shared vertical scale).

If there are 3 values described in the metadata file, an optional 3D view may be displayed.

!!! Note
    - SDS-View requires that all values in the [`<stream-name>.sds.yml` metadata file](https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/theory.md#sds-metadata-format) have the same data type (float, uint32_t, uint16_t, ...)

### Usage

- [Setup](#setup) the Python environment.
- Invoke the tool as explained below.

```txt
usage: sds-view.py [-h]
                   -i <sds_file> [<sds_file> ...]
                   -y <yaml_file>
                   [--3D]

View SDS data

options:
  -h, --help                      Show this help message and exit

required:
  -i <sds_file> [<sds_file> ...]  SDS files
  -y <yaml_file>                  YAML metadata file

optional:
  --3D                            Plot 3D view in addition to normal 2D
```

**Example:**

```bash
python sds-view.py -i test/Gyroscope.0.sds -y test/Gyroscope.sds.yml
```

**Example display:**

(figure: Example output)
