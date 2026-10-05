---
id: "zep-soc-porting-guide-write-your-soc-yaml"
type: "concept"
domain: "bring-up"
title: "SoC Porting Guide: Write your SoC YAML"
summary: "The SoC YAML file describes the SoC family, SoC series, and SoC at a high level."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/hardware/porting/soc_porting.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/hardware/porting/soc_porting.rst"
license: "Apache-2.0"
mode: "V"
---

The SoC YAML file describes the SoC family, SoC series, and SoC at a high level.

Detailed configurations, such as hardware description and configuration are done
in devicetree and Kconfig.

The skeleton of a simple SoC YAML file containing just one SoC is:

```yaml

socs:
  - name: <soc1>
```
It is possible to have multiple SoC located in the SoC folder.
For example if they belong to a common family or series it is recommended to
locate such SoC in a common tree.
Multiple SoCs and SoC series in a common folder can be described in the
`soc.yml` file as:

```yaml

family:
  - name: <family-name>
    series:
      - name: <series-1-name>
        socs:
          - name: <soc1>
            cpuclusters:
              - name: <coreA>
              - name: <coreB>
                ...
          - name: <soc2>
      - name: <series-2-name>
        ...
```
