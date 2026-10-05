---
id: "drv-can-interface"
type: "concept"
domain: "drivers"
title: "CAN Interface"
summary: "Driver API for CAN Bus Peripheral (%DriverCAN.h)"
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_CAN.c"
license: "Apache-2.0"
mode: "V"
---

Driver API for CAN Bus Peripheral (%Driver_CAN.h)


The **Controller Area Network** Interface Bus (CAN) implements a multi-master serial bus for connecting
microcontrollers and devices, also known as nodes, to communicate with each other in applications without a host computer.
CAN is a message-based protocol, designed originally for automotive applications, but meanwhile used also in many other surroundings.
The complexity of the node can range from a simple I/O device up to an embedded computer with a CAN interface and sophisticated software.
The node may also be a gateway allowing a standard computer to communicate over a USB or Ethernet port to the devices on a CAN network.
Devices are connected to the bus through a host processor, a CAN controller, and a CAN transceiver.


The CAN Driver API allows to implement CAN Interfaces that conform to the  

CAN specifications available from BOSCH:
  - CAN 2.0B: CAN Specification 2.0B (released Sep. 1991) which is now superseded by ISO 11898-1.
  - CAN FD: CAN with Flexible Data Rate introduced in 2012 (released April 17th, 2012).

Wikipedia offers more information about the **CAN Bus**.

**CAN 2.0B**
Every CAN CMSIS-Driver supports the CAN 2.0B standard

CAN 2.0B supports:
  - message can contain up to 8 data bytes
  - bitrates of up to 1Mbits/s
  - Remote_Frame requests
  

**CAN FD**

Support for CAN FD depends on the hardware.  
A CMSIS-Driver that supports CAN FD has the capability ARM_CAN_CAPABILITIES data field **fd_mode** = `1`, which can be
retrieved with the function ARM_CAN_GetCapabilities. 

CAN FD supports:
   - message can contain up to 64 data bytes
   - faster data transfers with faster bitrate used during the data phase 

CAN FD does not support Remote_Frame requests.

**Block Diagram**

The CAN Driver API defines a **CAN** interface for middleware components. The CAN Driver supports multiple
nodes, which are able to send and receive messages, but not simultaneously.

  "CAN Node Schematic"

CAN API
-------

The following header files define the Application Programming Interface (API) for the CAN interface:
  - **%Driver_CAN.h** : Driver API for CAN Bus Peripheral

The driver implementation is a typical part of the Device Family Pack (DFP) that supports the
peripherals of the microcontroller family.


**Driver Functions**

The driver functions are published in the access struct as explained in DriverFunctions
  - ARM_DRIVER_CAN : access struct for CAN driver functions

**Example Code**

The following example code shows the usage of the CAN interface.

```

#include <stdio.h>
#include <string.h>
#include "cmsis_os.h"
 
#include "Driver_CAN.h"
 
// CAN Driver Controller selector
#define  CAN_CONTROLLER         1       // CAN Controller number
 
#define _CAN_Driver_(n)         Driver_CAN##n
#define  CAN_Driver_(n)        _CAN_Driver_(n)
extern   ARM_DRIVER_CAN         CAN_Driver_(CAN_CONTROLLER);
#define  ptrCAN               (&CAN_Driver_(CAN_CONTROLLER))
 
uint32_t                        rx_obj_idx  = 0xFFFFFFFFU;
uint8_t                         rx_data[8];
ARM_CAN_MSG_INFO                rx_msg_info;
uint32_t                        tx_obj_idx  = 0xFFFFFFFFU;
uint8_t                         tx_data[8];
ARM_CAN_MSG_INFO                tx_msg_info;
 
static void Error_Handler (void) { while (1); }
 
void CAN_SignalUnitEvent (uint32_t event) {}
 
void CAN_SignalObjectEvent (uint32_t obj_idx, uint32_t event) {
 
  if (obj_idx == rx_obj_idx) {                  // If receive object event
    if (event == ARM_CAN_EVENT_RECEIVE) {       // If message was received successfully
      if (ptrCAN->MessageRead(rx_obj_idx, &rx_msg_info, rx_data, 8U) > 0U) {
                                                // Read received message
        // process received message ...
      }
    }
  }
  if (obj_idx == tx_obj_idx) {                  // If transmit object event
    if (event == ARM_CAN_EVENT_SEND_COMPLETE) { // If message was sent successfully
      // acknowledge sent message ...
    }
  }
}
 
int main (void) {
  ARM_CAN_CAPABILITIES     can_cap;
  ARM_CAN_OBJ_CAPABILITIES can_obj_cap;
  int32_t                  status;
  uint32_t                 i, num_objects;
 
  can_cap = ptrCAN->GetCapabilities (); // Get CAN driver capabilities
  num_objects = can_cap.num_objects;    // Number of receive/transmit objects
 
  status = ptrCAN->Initialize    (CAN_SignalUnitEvent, CAN_SignalObjectEvent);  // Initialize CAN driver
  if (status != ARM_DRIVER_OK ) { Error_Handler(); }
 
  status = ptrCAN->PowerControl  (ARM_POWER_FULL);                              // Power-up CAN controller
  if (status != ARM_DRIVER_OK ) { Error_Handler(); }
 
  status = ptrCAN->SetMode       (ARM_CAN_MODE_INITIALIZATION);                 // Activate initialization mode
  if (status != ARM_DRIVER_OK ) { Error_Handler(); }
 
  status = ptrCAN->SetBitrate    (ARM_CAN_BITRATE_NOMINAL,              // Set nominal bitrate
                                  100000U,                              // Set bitrate to 100 kbit/s
                                  ARM_CAN_BIT_PROP_SEG(5U)   |          // Set propagation segment to 5 time quanta
                                  ARM_CAN_BIT_PHASE_SEG1(1U) |          // Set phase segment 1 to 1 time quantum (sample point at 87.5% of bit time)
                                  ARM_CAN_BIT_PHASE_SEG2(1U) |          // Set phase segment 2 to 1 time quantum (total bit is 8 time quanta long)
                                  ARM_CAN_BIT_SJW(1U));                 // Resynchronization jump width is same as phase segment 2
  if (status != ARM_DRIVER_OK ) { Error_Handler(); }
 
  for (i = 0U; i < num_objects; i++) {                                          // Find first available object for receive and transmit
    can_obj_cap = ptrCAN->ObjectGetCapabilities (i);                            // Get object capabilities
    if      ((rx_obj_idx == 0xFFFFFFFFU) && (can_obj_cap.rx == 1U)) { rx_obj_idx = i; }
    else if ((tx_obj_idx == 0xFFFFFFFFU) && (can_obj_cap.tx == 1U)) { tx_obj_idx = i; break; }
  }
  if ((rx_obj_idx == 0xFFFFFFFFU) || (tx_obj_idx == 0xFFFFFFFFU)) { Error_Handler(); }
 
  // Set filter to receive messages with extended ID 0x12345678 to receive object
  status = ptrCAN->ObjectSetFilter(rx_obj_idx, ARM_CAN_FILTER_ID_EXACT_ADD, ARM_CAN_EXTENDED_ID(0x12345678U), 0U);
  if (status != ARM_DRIVER_OK ) { Error_Handler(); }
 
  status = ptrCAN->ObjectConfigure(tx_obj_idx, ARM_CAN_OBJ_TX);                 // Configure transmit object
  if (status != ARM_DRIVER_OK ) { Error_Handler(); }
 
  status = ptrCAN->ObjectConfigure(rx_obj_idx, ARM_CAN_OBJ_RX);                 // Configure receive object
  if (status != ARM_DRIVER_OK ) { Error_Handler(); }
  
  status = ptrCAN->SetMode (ARM_CAN_MODE_NORMAL);                               // Activate normal operation mode
  if (status != ARM_DRIVER_OK ) { Error_Handler(); }
  
  memset(&tx_msg_info, 0U, sizeof(ARM_CAN_MSG_INFO));                           // Clear message info structure
  tx_msg_info.id = ARM_CAN_EXTENDED_ID(0x12345678U);                            // Set extended ID for transmit message
  tx_data[0]     = 0xFFU;                                                       // Initialize transmit data
  while (1) {
    tx_data[0]++;                                                               // Increment transmit data
    status = ptrCAN->MessageSend(tx_obj_idx, &tx_msg_info, tx_data, 1U);        // Send data message with 1 data byte
    if (status != 1U) { Error_Handler(); }
    for (i = 0U; i < 1000000U; i++) { __nop(); }                                // Wait a little while
  }
}
```
