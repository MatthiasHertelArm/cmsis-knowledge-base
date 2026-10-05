---
id: "drv-wifi-interface-arm-wifi-bypasscontrol"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_BypassControl"
summary: "The function ARMWIFIBypassControl enables or disables the WiFi bypass mode."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_BypassControl (uint32_t interface, uint32_t mode)
```


The function **ARM_WIFI_BypassControl** enables or disables the WiFi bypass mode.

The WiFi Bypass mode can only be enabled, if there is a bypass mode supported in the WiFi driver.
You can check this by checking the driver's capabilities.

**Note:**
Bypass mode is enabled by default if the module does not support the Socket interface.

The argument **mode** specifies the desired state of the WiFi Bypass mode, which is
enabled or disabled.
 
**Example:**
```
extern ARM_DRIVER_WIFI Driver_WiFi0;
static ARM_DRIVER_WIFI *wifi;
static ARM_ETH_MAC_ADDR own_mac_address;
 
static void wifi_notify (uint32_t event, ,void *arg) {
  switch (event)  {
     :
  }  
}
 
void initialize_wifi_bypass (void) {
  ARM_WIFI_CAPABILITIES capabilities;
 
  wifi = &Driver_WiFi0;
  capabilities = wifi->GetCapabilities ();
  if (capabilities.bypass_mode == 0) {
    // error handling 
  } 
 
  // Initialize and Power-on WiFi Interface
  wifi->Initialize ((capabilities.eth_rx_frame_event) ? wifi_notify : NULL);
  wifi->PowerControl (ARM_POWER_FULL);
 
  // populate own_mac_address with the address to use for station
  wifi->SetOption(0U, ARM_WIFI_MAC, &own_mac_address, 6U);
 
  wifi->BypassControl (0U, 1U); // Enable bypass mode for station
}
```
