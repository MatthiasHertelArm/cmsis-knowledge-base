---
id: "txmw-chapter-3-functional-components-of-execution-overview-3"
type: "concept"
domain: "rtos"
title: "Chapter 3 - Functional Components of USBX Host Stack: Execution Overview"
summary: "The following diagram illustrates the USBX host stack."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-3.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-3.md#execution-overview"
license: "MIT"
mode: "V"
---

USBX is composed of several components:

- Initialization
- Application interface calls
- Host Classes
- Hub Class
- USB Host Stack
- Host controller (with Root Hub)

The following diagram illustrates the USBX host stack.

(figure: USBX Host Stack)

### Initialization

In order to activate USBX, the function ***ux_system_initialize*** must be called. This function initializes the memory resources of USBX.

In order to activate USBX host facilities, the function ***ux_host_stack_initialize*** must be called. This function will in turn initialize all the resources used by the USBX host stack such as ThreadX threads, mutexes, and semaphores.

It is up to the application initialization to register one or more USB classes by function **ux_host_stack_class_register**. If Hub Class is registered, its ready to detect devices connected through hub port, otherwise, only devices connected to root hub ports are enumerated.

It is up to the application initialization to activate at least one USB host controller. When the host controller(s) initialization function has been called the bus is active and device discovery can start. If the root hub of the host controller detects an attached device, the USB enumeration thread, in charge of the USB topology, will be wake up and proceed to enumerate the device(s).

It is possible, due to the nature of the root hub and downstream hubs, that all attached USB devices may not have been configured completely when the host controller initialization function returns. It can take several seconds to enumerate all USB devices, especially if there are one or more hubs between the root hub and USB devices.

### Application Interface Calls

There are two levels of APIs in USBX.

- USB Host Stack APIs
- USB Host Class APIs

Normally, a USBX application should not have to call any of the USB host stack API functions. Most applications will only access the USB Class API functions.

### USB Host Stack

The host stack API functions are responsible for the registration of USBX components (host classes and host controllers), configuration of devices, and the transfer requests for available device endpoints.

### USB Host Classes

The Class APIs are very specific to each USB class. Most of the common API functions for USB classes provide services such as opening/closing a device and reading from and writing to a device.

#### CDC Class

The CDC class is in charge of enumerating and driving connected CDC devices. Currently two functionalities are supported:
* CDC-ACM, the serial converter, refer to CDC-ACM part in Chapter 5 for more details.
* CDC-ECM, the ethernet controller, refer to Chapter 6 for more details.

#### Storage Class

The Storage class is in charge of enumerating and driving connected mass storage devices. It is integrated with FileX, the Eclipse ThreadX file system support module, to offer services to operate the connected media through **FX_MEDIA** interface.

#### HID Class

The HID class is in charge of enumerating and driving connect HID devices. The following functionalities are supported by its client services:
* HID Keyboard
* HID Mouse
* HID Remote control
Refer to HID part in Chapter 5 for more details.

### Hub Class

The hub class is in charge of driving USB hubs. A USB hub can either be a stand-alone hub or as part of a compound device such as a keyboard or a monitor. A hub can be self-powered or bus-powered. Bus-powered hubs have a maximum of four downstream ports and can only allow for the connection of devices that are either self-powered or bus-powered devices that use less than 100mA of power. Hubs can be cascaded. Up to five hubs can be connected to one another.

#### Host controller
The USB host controller driver interoperates USB Host Stack operations to hardware actions. Normally, a USBX application should not have to call host controller APIs, except initialization function. When the host controller initialization function is called, the hardware is ready and the stack will reply to detect bus events and start communication with connected devices.

##### Root Hub
Each host controller instance has one or more USB root hubs. The number of root hubs is either determined by the nature of the controller or can be retrieved by reading specific registers from the controller.

### USB Host Stack

The USB host stack is the centerpiece of USBX. It has three main functions.

- Manage the topology of the USB.
- Bind a USB device to one or more classes.
- Provide an API to classes to perform device descriptor interrogation and USB transfers.

### Topology Manager

The USB stack topology thread is awakened when a new device is connected or when a device has been disconnected. Either the root hub or a regular hub can accept device connections. Once a device has been connected to the USB, the topology manager will retrieve the device descriptor. This descriptor will contain the number of possible configurations available for this device. Most devices have one configuration only. Some devices can operate differently according to the available power available on the port where it is connected. If this is the case, the device will have multiple configurations that can be selected depending on the available power. When the device is configured by the topology manager, it is then allowed to draw the amount of power specified in its configuration descriptor.
