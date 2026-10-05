---
id: "txmw-chapter-2-usbx-host-stack-installa-configuration-options"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Host Stack Installation: Configuration Options"
summary: "There are several configuration options for building the USBX library. All options are located in the ux_user.h."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-2.md#configuration-options"
license: "MIT"
mode: "V"
---

There are several configuration options for building the USBX library. All options are located in the ***ux_user.h***.

The list below details each configuration option.


- **UX_PERIODIC_RATE**: This value represents how many ticks per seconds for a specific hardware platform. The default is 1000 indicating one tick per millisecond.
- **UX_MAX_CLASS_DRIVER**: This value is the maximum number of classes that can be loaded by USBX. This value represents the class container and not the number of instances of a class. For instance, if a particular implementation of USBX needs the hub class, the printer class, and the storage class, then the UX_MAX_CLASS_DRIVER value can be set to 3 regardless of the number of devices that belong to these classes.
- **UX_MAX_HCD**: This value represents the number of different host controllers that are available in the system. For USB 1.1 support, this value will mostly be 1. For USB 2.0 support this value can be more than 1. This value represents the number of concurrent host controllers running at the same time. If for instance, there are two instances of OHCI running or one EHCI and one OHCI controllers running, the UX_MAX_HCD should be set to 2. 
- **UX_MAX_DEVICES**: This value represents the maximum number of devices that can be attached to the USB. Normally, the theoretical maximum number on a single USB is 127 devices. This value can be scaled down to conserve memory. It should be noted that this value represents the total number of devices regardless of the number of USB buses in the system.
- **UX_MAX_ED**: This value represents the maximum number of EDs in the controller pool. This number is assigned to one controller only. If multiple instances of controllers are present, this value is used by each individual controller.
- **UX_MAX_TD and UX_MAX_ISO_TD**: This value represents the maximum number of regular and isochronous TDs in the controller pool. This number is assigned to one controller only. If multiple instances of controllers are present, this value is used by each individual controller.
- **UX_THREAD_STACK_SIZE**: This value is the size of the stack in bytes for the USBX threads. It can be typically 1024 bytes or 2048 bytes depending on the processor used and the host controller.
- **UX_HOST_ENUM_THREAD_STACK_SIZE**: This value is the stack size of the USB host enumeration thread. If this symbol I not set, the USBX host enumeration thread stack size is set to **UX_THREAD_STACK_SIZE**. 
- **UX_HOST_HCD_THREAD_STACK_SIZE**: This value is the stack size of the USB host HCD thread. If this symbol I not set, the USBX host HCD thread stack size is set to **UX_THREAD_STACK_SIZE**.
- **UX_THREAD_PRIORITY_ENUM**: This is the ThreadX priority value for the USBX enumeration threads that monitors the bus topology.
- **UX_THREAD_PRIORITY_CLASS**: This is the ThreadX priority value for the standard USBX threads.
- **UX_THREAD_PRIORITY_KEYBOARD**: This is the ThreadX priority value for the USBX HID keyboard class.
- **UX_THREAD_PRIORITY_HCD**: This is the ThreadX priority value for the host controller thread.
- **UX_NO_TIME_SLICE**: This value actually defines the time slice that will be used for threads. For example, if defined to 0, the ThreadX target port does not use time slices.
- **UX_MAX_HOST_LUN**: This value represents the maximum number of SCSI logical units represented in the host storage class driver.
- **UX_HOST_CLASS_STORAGE_INCLUDE_LEGACY_PROTOCOL_SUPPORT**: If defined, this value includes code to handle storage devices that use the CB or CBI protocol (such as floppy disks). It is off by default because these protocols are obsolete, being superseded by the Bulk Only Transport (BOT protocol, which virtually all modern storage devices use.
- **UX_HOST_CLASS_HID_KEYBOARD_EVENTS_KEY_CHANGES_MODE**: If defined, this value causes ux_host_class_hid_keyboard_key_get to only report key changes that is, key presses and key releases. By default, it only reports when a key is down.
- **UX_HOST_CLASS_HID_KEYBOARD_EVENTS_KEY_CHANGES_MODE_REPORT_KEY_DOWN_ONLY**: Only used if **UX_HOST_CLASS_HID_KEYBOARD_EVENTS_KEY_CHANGES_MODE** is defined. If defined, causes ux_host_class_hid_keyboard_key_get to only report key pressed/down changes; key released/up changes are not reported.
- **UX_HOST_CLASS_HID_KEYBOARD_EVENTS_KEY_CHANGES_MODE_REPORT_LOCK_KEYS**: Only used if **UX_HOST_CLASS_HID_KEYBOARD_EVENTS_KEY_CHANGES_MODE** is defined. If defined, causes ux_host_class_hid_keyboard_key_get to report lock key (CapsLock/NumLock/ScrollLock) changes.
- **UX_HOST_CLASS_HID_KEYBOARD_EVENTS_KEY_CHANGES_MODE_REPORT_MODIFIER_KEYS**: Only used if **UX_HOST_CLASS_HID_KEYBOARD_EVENTS_KEY_CHANGES_MODE** is defined. If defined, causes ux_host_class_hid_keyboard_key_get to report modifier key (Ctrl/Alt/Shift/GUI) changes.
- **UX_HOST_CLASS_CDC_ECM_NX_PKPOOL_ENTRIES**: If defined, this value represents the number of packets in the CDC-ECM host class. The default is 16.
