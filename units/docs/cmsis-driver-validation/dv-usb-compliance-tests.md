---
id: "dv-usb-compliance-tests"
type: "concept"
domain: "drivers"
title: "USB Compliance Tests"
summary: "USB drivers need to be tested against the requirements of the USB standard."
status: "draft"
collection: "cmsis-driver-validation"
source: "ARM-software/CMSIS-Driver_Validation@81a7e18:Documentation/Doxygen/src/DV_USBD.txt"
doc_source: "https://arm-software.github.io/CMSIS-Driver_Validation/latest/usbd_comp_test.html"
license: "Apache-2.0"
mode: "V"
---

USB drivers need to be tested against the requirements of the USB standard. The following tools are provided by the
USB Implementers Forum: 
 - USB Command Verifier (USB20CV Tools) for
   USB 2.0 controllers
 - USB Command Verifier (USB3CV Tools) for USB 3
   controllers

Before using the command verifier tools, make sure that you have an application running with the USB device class that you
are going to test. For example, if you want to test the behavior of the USB MSC device class, create a µVision project
containing this class. For more information, refer to the
MDK Middleware
documentation.

Then, follow these steps to run the verification tools on a Windows PC:

- Install the appropriate USB Command Verifier tool and reboot your PC.
- Connect your device to the PC.
- Open the Windows Device Manager and select **View - Devices by connection** to view the USB host controllers available
  on the PC:

   "Select USB Device"

- Expand the entry and verify the controller properties to which your device is connected. Remember the location of the
  controller that will be tested:
  
   "Device Location"

- Run the USB Command Verifier tool and select the controller according to the location found in the previous step:

   "Select Controller"

**Note:** 
Do not test the controller that is connected to the keyboard or mouse. All devices connected to the tested controller will
stop working.

- When selecting the **Compliance Test** mode all test cases will run. In the **Debug** mode, you can choose individual
  test cases by selecting the related check boxes. Test reports are saved automatically in the **Reports** directory.

 "Compliance Tests"
The following tests should be executed for:
 - USB Mass Storage Class: Chapter 9 Tests + MSC Tests
 - USB HID class: Chapter 9 Tests + HID Tests
 - Any other class (CDC, ADC, etc.): only Chapter 9 Tests

**Chapter 9 Tests** refers to the USB Device Framework chapter of the USB specification. Every USB peripheral is required
conform to this test which must be passed. Passed tests offer a good level of confidence that there are no major flows in the
USB device drivers.

The USB Command Verifier does not test how well a device behaves under stress. To get a better confidence, conduct stress
tests of all available examples:
  - USB MSC: Send a long file to the mass storage device and read it back and compare the output.
  - USB HID: Use the HID Client (available in the MDK installation directory below \\ARM\\Utilities\\HID_Client\\Release) to
    see how the device works under stress.
  - USB CDC (Virtual COM): Send a large file on the Virtual COM Port and capture it on the UART and vice versa. Compare sent
    and received files for both directions.
  - USB ADC: Play a sound file form the board for some time and listen for any sound distortion. Record sounds coming from
    a microphone and verify the recorded file on the USB Host.

After the completion of the tests, click **Exit** to switch back the USB stack. Otherwise, the USB stack will stay in test
mode.
