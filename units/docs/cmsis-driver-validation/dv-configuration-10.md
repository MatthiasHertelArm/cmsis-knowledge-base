---
id: "dv-configuration-10"
type: "concept"
domain: "drivers"
title: "Configuration"
summary: "The WiFi driver validation settings are available in the DV_WiFi_Config.h configuration file."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_WiFi.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/wifi_config.html"
license: "Apache-2.0"
mode: "V"
---

The WiFi driver validation settings are available in the **DV_WiFi_Config.h** configuration file.

Some settings depend on the test environment and need to be changed for proper operation of the WiFi driver validation.

These settings can be found under **Configuration** settings in the **DV_WiFi_Config.h** configuration file and need to 
be set as follows:

 "DV_WiFi_Config.h configuration file in Configuration Wizard view mode"

**Station** related settings needed for WiFi module to connect to the WiFi Access Point in the local network:
- SSID
- Password
- Security Type
- Channel: use 0 for auto-detect channel
- WPS PIN: PIN used for WPS tests (the Access Point has to have the same PIN enabled and WPS service running)

**Access Point** related settings needed for testing Access Point functionality (network creation) of the WiFi module:
- SSID
- Password
- Security Type
- Channel: use 0 for auto-detect channel
- WPS PIN: PIN used for WPS tests (auxiliary station has to have the same PIN enabled)

**Socket** related setting needed for Socket API and Socket Operation tests:
- SockServer IP: IP address assigned to the SockServer on your local network
- Number of sockets: Number of sockets that the driver supports and that will be tested

**Note:** IP address is displayed by the SockServer application (on the embedded board's LCD when using embedded SockServer).

Under **Tests** select testing functionality as required.
For details on tests performed by each test function please refer to WiFi Tests.

**Control**, **Management** and **Socket API (requires SockServer)** group of tests enable or disable 
WiFi Driver API function tests respectively.

**Management (requires user interaction)** and **Socket Operation (requires SockServer)** group of tests 
are used for more complex operational test of the WiFi driver.

A brief description of each test functionality can be viewed by using 
Configuration Wizard
view of the **DV_WiFi_Config.h** file and clicking on the test or hovering a mouse pointer over it.
