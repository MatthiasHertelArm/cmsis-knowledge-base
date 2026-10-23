---
id: "drv-ethernet-mac-events"
type: "concept"
domain: "drivers"
title: "Ethernet MAC Events"
summary: "The Ethernet MAC driver generates call back events that are notified via the function ARM_ETH_MAC_SignalEvent."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_ETH_MAC.c"
license: "Apache-2.0"
mode: "V"
---

The Ethernet MAC driver generates call back events that are notified via the function ARM_ETH_MAC_SignalEvent.
 
This section provides the event values for the ARM_ETH_MAC_SignalEvent callback function.

The following call back notification events are generated:

### ARM_ETH_MAC_EVENT_RX_FRAME

```c
ARM_ETH_MAC_EVENT_RX_FRAME
```


### ARM_ETH_MAC_EVENT_TX_FRAME

```c
ARM_ETH_MAC_EVENT_TX_FRAME
```


### ARM_ETH_MAC_EVENT_WAKEUP

```c
ARM_ETH_MAC_EVENT_WAKEUP
```


### ARM_ETH_MAC_EVENT_TIMER_ALARM

```c
ARM_ETH_MAC_EVENT_TIMER_ALARM
```
