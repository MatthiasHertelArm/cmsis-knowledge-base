---
id: "sds-sds-with-sdsio-via-vsi-simulator-fvp-configuration"
type: "concept"
domain: "test"
title: "SDS with SDSIO via VSI (Simulator): FVP Configuration"
summary: "The Arm Virtual Hardware is configured for Corstone-300 with the fvpconfig.txt and for Corstone-320 with the fvpconfig.txt. You can leave the configuration settings at their default values, a change is not necessary."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:template/sdsio/fvp/README.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/template/sdsio/fvp/README.md#fvp-configuration"
license: "Apache-2.0"
mode: "V"
---

The Arm Virtual Hardware is configured for **Corstone-300** with the [fvp_config.txt](https://github.com/ARM-software/SDS-Framework/blob/main/template/Board/Corstone-300/fvp_config.txt)
and for **Corstone-320** with the [fvp_config.txt](https://github.com/ARM-software/SDS-Framework/blob/main/template/Board/Corstone-320/fvp_config.txt).
You can leave the configuration settings at their default values, a change is not necessary.

An important configuration setting is the path to the Python simulation scripts. The path refers to the solution folder:

- For **Corstone-300 with Ethos-U55**:

  ```txt
  mps3_board.v_path=./Board/Corstone-300/vsi/python/
  ```

- For **Corstone-320 with Ethos-U85**:

  ```txt
  mps4_board.v_path=./Board/Corstone-320/vsi/python/
  ```
