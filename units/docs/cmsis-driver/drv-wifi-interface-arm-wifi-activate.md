---
id: "drv-wifi-interface-arm-wifi-activate"
type: "concept"
domain: "drivers"
title: "WiFi Interface: ARM_WIFI_Activate"
summary: "The function ARM_WIFI_Activate activates the specified interface."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_WiFi.c"
license: "Apache-2.0"
mode: "V"
---

```c
int32_t ARM_WIFI_Activate (uint32_t interface, const ARM_WIFI_CONFIG_t *config)
```


The function **ARM_WIFI_Activate** activates the specified interface.

The argument **interface** specifies the interface (0 = Station, 1 = Access Point).

When station interface is specified, the WiFi module connects to a wireless network.

The wireless network trying to connect to must be available,
otherwise the operation will fail after a timeout.

Available wireless networks can be scanned by using the function ARM_WIFI_Scan.

When access point interface is specified, the WiFi module creates a wireless network
by activating the access point.

The argument **config** is a pointer to the configuration ARM_WIFI_CONFIG_t
which provides information needed to connect to a WiFi network for station interface
or information used to configure the access point (AP) for access point interface.

**ssid** specifies the name of the network to connect to or the network to create.

**pass** specifies the password for accessing the wireless network.

**security** specifies the security type which will be used for the connection.

**ch** specifies the WiFi channel which will be used for the connection.
Valid channels for 2.4 GHz frequency are from `1` to `13`. If the value for **ch** = `0`,
the system automatically selects the channel.
For station interface the channel of the AP being connected to is used.
For access point interface the module automatically selects the best channel for the WiFi connection.

**Note:**
Optionally BSSID parameter can be also set using ARM_WIFI_SetOption.
It allows connection to specific BSSID when connecting to an access point or specifies
the BSSID of the access point.

**wps_method** specifies if WiFi Protected Setup (WPS) is used and which method.

**wps_pin** specifies the PIN used with WPS (ARM_WIFI_WPS_METHOD_PIN).

With the **push-button** method, you typically press the button, either real or virtual,
both at the access point and the station. No credentials are needed.

With **PIN** method, you must provide the PIN code that you read from the label or screen
on the wireless device.

WPS configuration for station is used when station connects to an access point.
It enables to connect without specifying SSID, Password, Security Type or WiFi Channel.
The actual network information can be retrieved once connected with ARM_WIFI_GetNetInfo.

WPS configuration for access point is used when access point is activated.
Subsequent activate calls re-trigger the WPS procedure.

**Note:**
WPS is typically activated by pressing the WPS button at the access point.
During the discovery mode (usually 2 minutes or less) any wireless device may connect
to the access point (PIN needs to match when PIN method is selected).

**Example:**
```
ARM_WIFI_CONFIG_t wifi_config;
 
wifi_config.ssid = "GuestAccess";
wifi_config.pass = "guest";
wifi_config.security = ARM_WIFI_SECURITY_WPA2;
wifi_config.ch = 0U;
wifi_config.wps_method = ARM_WIFI_WPS_METHOD_NONE;
 
// Connect to wireless network
status = wifi->Activate (0U, &wifi_config);
if (status != ARM_DRIVER_OK) {
  // error handling
}
```
