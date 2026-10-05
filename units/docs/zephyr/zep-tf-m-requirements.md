---
id: "zep-tf-m-requirements"
type: "concept"
domain: "security"
title: "TF-M Requirements"
summary: "The following are some of the boards that can be used with TF-M:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/services/tfm/requirements.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/services/tfm/requirements.rst"
license: "Apache-2.0"
mode: "V"
---

The following are some of the boards that can be used with TF-M:


* - Board
  - NSPE board name
* - mps2_an521_board
  - `mps2/an521/cpu0/ns` (qemu supported)
* - mps3
  -
    - `mps3/corstone300/fvp/ns` (armfvp supported)
    - `mps3/corstone310/fvp/ns` (armfvp supported)
* - mps4
  -
    - `mps4/corstone315/fvp/ns` (armfvp supported)
    - `mps4/corstone320/fvp/ns` (armfvp supported)
* - bl5340_dvk
  - `bl5340_dvk/nrf5340/cpuapp/ns`
* - lpcxpresso55s69
  - `lpcxpresso55s69_ns`
* - nrf9160dk_nrf9160
  - `nrf9160dk/nrf9160/ns`
* - nrf5340dk
  - `nrf5340dk/nrf5340/cpuapp/ns`
* - b_u585i_iot02a
  - `b_u585i_iot02a/stm32u585xx/ns`
* - nucleo_l552ze_q
  - `nucleo_l552ze_q/stm32l552xx/ns`
* - stm32l562e_dk
  - `stm32l562e_dk/stm32l562xx/ns`
* - v2m_musca_b1
  - `v2m_musca_b1/musca_b1/ns`
To make sure TF-M is supported for a board
in its output, check that `CONFIG_TRUSTED_EXECUTION_NONSECURE`
is set to `y` in that board's default configuration.
