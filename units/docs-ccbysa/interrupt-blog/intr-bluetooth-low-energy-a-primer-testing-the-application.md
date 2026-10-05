---
id: "intr-bluetooth-low-energy-a-primer-testing-the-application"
type: "concept"
domain: "debug"
title: "Bluetooth Low Energy: A Primer: Implementation of a BLE Peripheral (nRF52 example) / Testing the Application"
summary: "Part of: Implementation of a BLE Peripheral (nRF52 example)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-30-bluetooth-low-energy-a-primer.md"
doc_source: "https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer#testing-the-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Implementation of a BLE Peripheral (nRF52 example)_

Even though we verified that our application is running correctly and no errors show up in the terminal window, we still need to verify its BLE functionality. The easiest way to do so is by running a BLE Central mobile app such as nRF Connect ([iOS](https://apps.apple.com/us/app/nrf-connect/id1054362403) or [Android](https://play.google.com/store/apps/details?id=no.nordicsemi.android.mcp&hl=en_US)) or LightBlue ([iOS](https://apps.apple.com/us/app/lightblue-explorer/id557428110) or [Android](https://play.google.com/store/apps/details?id=com.punchthrough.lightblueexplorer&hl=en_US)).

The different aspect we want to test include:

1. Making sure the BLE Peripheral advertises and can be discovered by the BLE Central.
2. Making sure we can connect to the Peripheral.
3. Verifying that we can discover the Simple Service and its Button 1 Characteristic.
4. Verifying that we can read the state of Button 1 (pressed: 0x01 or released: 0x00).
5. Verifying that we can subscribe to Notifications and get notified when Button 1's state changes.

Let's go through each of these tests. We'll be using LightBlue for our tests here.

#### 1. Advertisements
Once you launch LightBlue, you'll be presented with a screen showing all the BLE devices advertising in the vicinity. *Make sure you have Bluetooth enabled on your phone first*.

 

#### 2. Connection
Now that we verified that we can discover our device ("Memfault_Example"), we can attempt to connect to it. Simply click on the device and it should initiate a connection. You should momentarily see a message similar to the following before it establishes the connection:



After the connection is established, you will be presented with a screen similar to this:



#### 3. GATT Service & Characteristic Discovery
The previous screen also verifies that the Simple Service was discovered correctly and it contains our Button 1 Characteristic.

If we click on the Simple Service, we should see the Button 1 Characteristic:



#### 4. Characteristic Value Read
To verify that we can read the value of the Button 1 Characteristic, we can tap on "Read again". To verify further, we can hold down Button 1 on the development board and then click "Read again". This time it should display a value of 0x01.


 
#### 5. Notifications
Finally, let's verify that we can get notified when the Button 1 state changes. We can do so by clicking on the "Listen for notifications" button.

Once you click on it, you can test it by pressing Button 1 and releasing it a few times. You should see the updated values come in as you press and release the button:

Notifications disabled:



Notifications enabled:


