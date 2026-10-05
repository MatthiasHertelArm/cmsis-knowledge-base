---
id: "ocp-ocp-tools-readmes-readme-gpio-configuration-and-usage"
type: "concept"
domain: "project"
title: "ocp-tools-readmes README: GPIO Configuration and usage"
summary: "ocp-tools-readmes README: GPIO Configuration and usage"
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/RefApp-Framework@54fba8b:layer/Board/IMXRT1050-EVKB/IoT/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/layer/Board/IMXRT1050-EVKB/IoT/README.md#gpio-configuration-and-usage"
license: "Apache-2.0"
mode: "V"
---

| Functional Group       | Pin | Peripheral | Signal      | Identifier  | Pin Settings                                        | Usage
|:-----------------------|:----|:-----------|:------------|:------------|:----------------------------------------------------|:-----
| BOARD_InitDEBUG_UART   | K14 | LPUART1    | TX          | UART1_TXD   | default                                             | UART1 TX for debug console (GPIO_AD_B0_12)
| BOARD_InitDEBUG_UART   | L14 | LPUART1    | RX          | UART1_RXD   | default                                             | UART1 RX for debug console (GPIO_AD_B0_13)
| BOARD_InitENET         | A7  | ENET       | MDC         | ENET_MDC    | default                                             | Ethernet KSZ8081RNB pin MDC (GPIO_EMC_40)
| BOARD_InitENET         | C7  | ENET       | MDIO        | ENET_MDIO   | default                                             | Ethernet KSZ8081RNB pin MDIO (GPIO_EMC_41)
| BOARD_InitENET         | B13 | ENET       | REF_CLK     | ENET_TX_CLK | Direction Output, Software Input On Enabled         | Ethernet KSZ8081RNB pin XI (GPIO_B1_10)
| BOARD_InitENET         | E12 | ENET       | RX_DATA, 0  | ENET_RXD0   | default                                             | Ethernet KSZ8081RNB pin RXD0 (GPIO_B1_04)
| BOARD_InitENET         | D12 | ENET       | RX_DATA, 1  | ENET_RXD1   | default                                             | Ethernet KSZ8081RNB pin RXD1 (GPIO_B1_05)
| BOARD_InitENET         | C12 | ENET       | RX_EN       | ENET_CRS_DV | default                                             | Ethernet KSZ8081RNB pin CRS_DV (GPIO_B1_06)
| BOARD_InitENET         | C13 | ENET       | RX_ER       | ENET_RXER   | default                                             | Ethernet KSZ8081RNB pin RXER (GPIO_B1_11)
| BOARD_InitENET         | B12 | ENET       | TX_DATA, 0  | ENET_TXD0   | default                                             | Ethernet KSZ8081RNB pin TXD0 (GPIO_B1_07)
| BOARD_InitENET         | A12 | ENET       | TX_DATA, 1  | ENET_TXD1   | default                                             | Ethernet KSZ8081RNB pin TXD1 (GPIO_B1_08)
| BOARD_InitENET         | A13 | ENET       | TX_EN       | ENET_TXEN   | default                                             | Ethernet KSZ8081RNB pin TXEN (GPIO_B1_09)
| BOARD_InitENET         | G13 | GPIO1      | gpio_io, 10 | ENET_INT    | Direction Output, GPIO initial state 1              | Ethernet KSZ8081RNB pin INTRP (GPIO_AD_B0_10)
| BOARD_InitUSDHC        | J2  | USDHC1     | DATA, 3     | SD1_D3      | default                                             | SD Card pin D3 (GPIO_SD_B0_05)
| BOARD_InitUSDHC        | H2  | USDHC1     | DATA, 2     | SD1_D2      | default                                             | SD Card pin D2 (GPIO_SD_B0_04)
| BOARD_InitUSDHC        | K1  | USDHC1     | DATA, 1     | SD1_D1      | default                                             | SD Card pin D1 (GPIO_SD_B0_03)
| BOARD_InitUSDHC        | J1  | USDHC1     | DATA, 0     | SD1_D0      | default                                             | SD Card pin D0 (GPIO_SD_B0_02)
| BOARD_InitUSDHC        | J4  | USDHC1     | CMD         | SD1_CMD     | default                                             | SD Card pin CMD (GPIO_SD_B0_00)
| BOARD_InitUSDHC        | J3  | USDHC1     | CLK         | SD1_CLK     | default                                             | SD Card pin CLK (GPIO_SD_B0_01)
| BOARD_InitARDUINO_UART | J12 | LPUART3    | TX          | LPUART3_TX  | default                                             | Arduino UNO R3 pin D1 (GPIO_AD_B1_06)
| BOARD_InitARDUINO_UART | K10 | LPUART3    | RX          | LPUART3_RX  | default                                             | Arduino UNO R3 pin D0 (GPIO_AD_B1_07)
| BOARD_InitUSER_LED     | F14 | GPIO1      | gpio_io, 09 | USER_LED    | Direction Output, GPIO initial state 1, mode PullUp | User LED (GPIO_AD_B0_09)
| BOARD_InitUSER_BUTTON  | L6  | GPIO5      | gpio_io, 00 | USER_BUTTON | Direction Input, mode PullUp                        | User Button SW8 (WAKEUP)
| BOARD_InitI2C          | J11 | LPI2C1     | SCL         | I2C1_SCL    | Software Input On, Open drain                       | I2C1 for FXOS8700CQ and WM8960 (GPIO_AD_B1_00)
| BOARD_InitI2C          | K11 | LPI2C1     | SDA         | I2C1_SDA    | Software Input On, Open drain                       | I2C1 for FXOS8700CQ and WM8960 (GPIO_AD_B1_01)
| BOARD_InitAudio        | H13 | GPIO1      | gpio_io, 24 | CSI_D9      | Direction Input, Rising Edge, mode PullUp           | Audio Codec WM8960 pin GPIO1 (GPIO_AD_B1_08)
| BOARD_InitAudio        | M13 | SAI1       | MCLK        | CSI_D8      | Direction Output, Software Input On                 | Audio Codec WM8960 pin MCLK (GPIO_AD_B1_09)
| BOARD_InitAudio        | H12 | SAI1       | RX_DATA, 0  | CSI_D5      | default                                             | Audio Codec WM8960 pin ADCDAT (GPIO_AD_B1_12)
| BOARD_InitAudio        | H11 | SAI1       | TX_DATA, 0  | CSI_D4      | default                                             | Audio Codec WM8960 pin DACDAT (GPIO_AD_B1_13)
| BOARD_InitAudio        | G12 | SAI1       | TX_BCLK     | CSI_D3      | default                                             | Audio Codec WM8960 pin BCLK (GPIO_AD_B1_14)
| BOARD_InitAudio        | J14 | SAI1       | TX_SYNC     | CSI_D2      | default                                             | Audio Codec WM8960 pin DACLRC (GPIO_AD_B1_15)
