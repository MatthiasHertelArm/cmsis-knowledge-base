---
id: "dv-sockserver-sockserver-for-pc-running-microsoft-wind"
type: "concept"
domain: "drivers"
title: "SockServer: SockServer for PC running Microsoft Windows"
summary: "SockServer is already built and can be executed by running the SockServer.exe file in <pack installation root>/Tools/SockServer/PC/Win."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_WiFi.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/wifi_sock_setup.html"
license: "Apache-2.0"
mode: "V"
---

**Requirements:**
 - Personal Computer running Microsoft Windows
 - PC connection to local network

SockServer is already built and can be executed by running the **SockServer.exe** file in **`<pack installation root>/Tools/SockServer/PC/Win`**.

If you need to change the functionality of SockServer, source files and a batch script for building the executable are
available in **`<pack installation root>/Tools/SockServer/PC/Win`**.

**Note:**
- SockServer build process requires Minimalist GNU for Windows (MinGW).
- To build the SockServer executable for Windows, follow these steps:
  - Download and install MinGW from https://winlibs.com/
  - Set environment path in Microsoft Windows as explained under Usage heading on https://winlibs.com/#usage
  - Run **Build.bat** located in **`<pack installation root>/Tools/SockServer/PC/Win`** which will result in an executable that is located
    in **`<pack installation root>/Tools/SockServer/PC/Win`**


### Troubleshooting


Problems and solutions:
 1. SockServer not responding to requests
    - Open Windows firewall -> Advanced settings
      - select inbound rules
    - create a new custom rule (New Rule...)
      - Rule type:     Program
      - Program:       This program path (select path to SockServer.exe)
      - Action:        Allow the connection
      - Profile:       Domain, Private (Public not advised)
      - Name:          SockServer  
 2. Test computer not responding to ping
    - Open Windows firewall -> Advanced settings
      - select inbound rules, enable rule
        File and Printer sharing (Echo request - ICMPv4-In)
      
    - If rule does not exist, create a new custom rule (New Rule...)
      - Rule type:     Custom
      - Program:       All programs
      - Protocol type: ICMPv4
      - ICMP Settings: Customize - Specific ICMP types: Echo Request
      - Scope:         Any IP address
      - Action:        Allow the connection
      - Profile:       Domain, Private (Public not advised)
      - Name:          Ping Echo
