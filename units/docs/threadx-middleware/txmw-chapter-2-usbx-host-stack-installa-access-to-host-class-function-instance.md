---
id: "txmw-chapter-2-usbx-host-stack-installa-access-to-host-class-function-instance"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Host Stack Installation: Access to Host Class Function Instance"
summary: "After class registration and host controller driver (HCD) registration, the USB devices connected to USB port can be detected and enumerated."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-host-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-2.md#access-to-host-class-function-instance"
license: "MIT"
mode: "V"
---

After class registration and host controller driver (HCD) registration, the USB devices connected to USB port can be detected and enumerated. During enumeration, registered class checks connected device information, if the right information is found memory is allocated for class function instance and the instance is then activated. The instance is used by application to do class function specific operations.

When USB device is removed from USB port, the activated class function instance is then deactivated.

There are two ways to access the host instances: from registered class and/or through host change callback notification.

### Get instance through registered class

When class function instance is activated, it's linked to the class who owns the instance. So through class the instance can be accessed. E.g., to check if `storage` instance is available:

```c
    /* Find the main storage container (class)  */
    status =  ux_host_stack_class_get(_ux_system_host_class_storage_name, &ux_class);
    if (status != UX_SUCCESS)
        return(status);

    /* Find the storage instance under container (class)  */
    status =  ux_host_stack_class_instance_get(ux_class, 0, (void **) &storage);
    if (status == UX_SUCCESS)
    {
        /* Check if storage state, storage specific resources are ready.  */
        if (storage -> ux_host_class_storage_state == UX_HOST_CLASS_INSTANCE_LIVE &&
            ux_class -> ux_host_class_ext != UX_NULL &&
            ux_class -> ux_host_class_media != UX_NULL)
            return(UX_SUCCESS);
    }
```
[`ux_host_stack_class_get`](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-4.md#ux_host_stack_class_get) is used to get a registered class, given class name used on registration.

[`ux_host_stack_class_instance_get`](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-4.md#ux_host_stack_class_instance_get) is used to get function instance from specific registered class.

In example, the state of the instance and some other function related resources is checked, to confirm the instance is ready to use.

### Get instance through host change callback notification

There is an optional host change callback function which is assigned on host stack initialization. If the function is available, it's invoked when function instance is activated and in good state with all required resources available. Inside the callback the instance is passed and inside application callback user can save it for further operations.

For more details, see [**ux_host_stack_initialize**](https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-host-stack-4.md#ux_host_stack_initialize).
