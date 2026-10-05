---
id: "txmw-chapter-2-usbx-device-stack-instal-definition-of-usb-device-controller"
type: "concept"
domain: "rtos"
title: "Chapter 2 - USBX Device Stack Installation: Definition of USB Device Controller"
summary: "Only one USB device controller can be defined at any time to operate in device mode. The application initialization file should contain this definition. The following line performs the definition of a generic usb controller:"
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/usbx/usbx-device-stack-2.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/usbx/usbx-device-stack-2.md#definition-of-usb-device-controller"
license: "MIT"
mode: "V"
---

Only one USB device controller can be defined at any time to operate in device mode. The application initialization file should contain this definition. The following line performs the definition of a generic usb controller:

```c
ux_dcd_controller_initialize(0x7BB00000, 0, 0xB7A00000);
```

The USB device initialization has the following prototype:

```c
UINT ux_dcd_controller_initialize(ULONG dcd_io, ULONG dcd_irq, ULONG dcd_vbus_address);
```

Where:

- *dcd_io*: Address of the controller IO.
- *dcd_irq*: Interrupt used by the controller.
- *dcd_vbus_address*: Address of the VBUS GPIO .

The following example is the initialization of USBX in device mode with the storage device class and a generic controller:

```c
/* Initialize USBX Memory */

ux_system_initialize(memory_pointer,(128*1024), 0, 0);

/* The code below is required for installing the device portion of USBX */
status = ux_device_stack_initialize(&device_framework_high_speed, DEVICE_FRAMEWORK_LENGTH_HIGH_SPEED,
                                    &device_framework_full_speed, DEVICE_FRAMEWORK_LENGTH_FULL_SPEED,
                                    &string_framework, STRING_FRAMEWORK_LENGTH,
                                    &language_id_framework, LANGUAGE_ID_FRAMEWORK_LENGTH,
                                    UX_NULL);

/* If status equals UX_SUCCESS, installation was successful. */

/* Store the number of LUN in this device storage instance: single LUN. */
storage_parameter.ux_slave_class_storage_parameter_number_lun = 1;

/* Initialize the storage class parameters for reading/writing to the Flash Disk. */
storage_parameter.ux_slave_class_storage_parameter_lun[0].ux_slave_class_storage_media_last_lba = 0x1e6bfe;
storage_parameter.ux_slave_class_storage_parameter_lun[0].ux_slave_class_storage_media_block_length = 512;
storage_parameter.ux_slave_class_storage_parameter_lun[0].ux_slave_class_storage_media_type = 0;
storage_parameter.ux_slave_class_storage_parameter_lun[0].ux_slave_class_storage_media_removable_flag = 0x80;
storage_parameter.ux_slave_class_storage_parameter_lun[0].ux_slave_class_storage_media_read = demo_thread_flash_media_read;
storage_parameter.ux_slave_class_storage_parameter_lun[0].ux_slave_class_storage_media_write = demo_thread_flash_media_write;
storage_parameter.ux_slave_class_storage_parameter_lun[0].ux_slave_class_storage_media_status = demo_thread_flash_media_status;

/* Initialize the device storage class. The class is connected with interface 0 */
status = ux_device_stack_class_register(ux_system_slave_class_storage_name ux_device_class_storage_entry, ux_device_class_storage_thread, 0, (VOID *)&storage_parameter);

/* Register the device controllers available in this system */
status = ux_dcd_controller_initialize(0x7BB00000, 0, 0xB7A00000);

/* If status equals UX_SUCCESS, registration was successful. */
```
