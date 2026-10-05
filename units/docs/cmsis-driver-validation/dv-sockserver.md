---
id: "dv-sockserver"
type: "concept"
domain: "drivers"
title: "SockServer"
summary: "The SockServer is an application providing a set of services used by the WiFi CMSIS-Driver Validation suite to test the Socket interface of the WiFi driver. It is located in the <pack installation root>/Tools/SockServer subdirectory of the pack root directory."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_WiFi.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/wifi_sock_setup.html"
license: "Apache-2.0"
mode: "V"
---

The **SockServer** is an application providing a set of services used by the WiFi CMSIS-Driver Validation suite to test the
Socket interface of the WiFi driver. It is located in the **`<pack installation root>/Tools/SockServer`** subdirectory of the pack root directory.
The SockServer is available for different target systems. It runs several standard network services.

The **SockServer** is available for **Personal Computer** running Microsoft Windows (executable located in **`<pack installation root>/Tools/SockServer/PC/Win`**).

The following services are available by SockServer:
- **Echo** service on port `7`, TCP and UDP
  \n (two instances of TCP service, one instance of UDP service)
- **Discard** service on port `9`, TCP and UDP
  \n (one instance of TCP service, one instance of UDP service)
- **Chargen** service on port `19`, TCP and UDP
  \n (two instances of TCP service, one instance of UDP service)
- **Assistant** service on port `5000`
  \n (helper service used to test WiFi sockets in server mode (socket accept functionality))
- **Telnet** service on port `23`
  \n (SockServer status monitoring service)
