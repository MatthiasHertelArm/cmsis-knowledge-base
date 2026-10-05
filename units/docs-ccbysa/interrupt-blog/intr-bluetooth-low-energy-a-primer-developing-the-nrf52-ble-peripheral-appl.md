---
id: "intr-bluetooth-low-energy-a-primer-developing-the-nrf52-ble-peripheral-appl"
type: "concept"
domain: "debug"
title: "Bluetooth Low Energy: A Primer: Implementation of a BLE Peripheral (nRF52 example) / Developing the nRF52 BLE Peripheral Application"
summary: "Part of: Implementation of a BLE Peripheral (nRF52 example)"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-30-bluetooth-low-energy-a-primer.md"
doc_source: "https://interrupt.memfault.com/blog/bluetooth-low-energy-a-primer#developing-the-nrf52-ble-peripheral-application"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Implementation of a BLE Peripheral (nRF52 example)_

We will be using one of the BLE examples provided as part of the nRF5 SDK as a starting point. The example is called "**ble_app_template**" and is located at:

```
<nRF5_SDK_Folder>/examples/ble_peripheral/ble_app_template/
```

The example is provided as a boilerplate template that you could use whenever you're developing an nRF52 BLE application from scratch. Here's a screenshot of the contents of this example's folder:



The example consists of a single source file named `main.c`, which we'll be modifying to do the following:

- Enable advertising as a BLE Peripheral that accepts a connection from a BLE Central device.
- Define a GATT service which we'll call "simple service" which consists of one characteristic:
	- A "**Button 1**" Characteristic (exposes the current state of the development kit's Button 1: pressed (0x01) or released (0x00)). The Characteristic will allow both **reads** and **notifications** to allow a client to read the value and get notified only when the value changes (instead of polling for the value waiting for a change to occur). 
- Handling of the Button 1 events (presses and releases).

Let's go through the steps and code changes needed to implement our application. All the code used in this blog post is available on [GitHub](https://github.com/memfault/interrupt/tree/master/example/ble-primer/).

#### Enabling the nRF Log Module

In order to enable logging and see debug data, you need to do the following (some of these may already be enabled in your template application) in `pca10056/s140/config/sdk_config.h`:

- Enable the `NRF_LOG_ENABLED` macro:

	```c
	// <e> NRF_LOG_ENABLED - nrf_log - Logger
	//==========================================================
	#ifndef NRF_LOG_ENABLED
	#define NRF_LOG_ENABLED 1
	#endif
	```
	
- Set the log level to 3 (or 4 more debugging information):

	```c
	// <o> NRF_LOG_DEFAULT_LEVEL  - Default Severity level
	 
	// <0=> Off 
	// <1=> Error 
	// <2=> Warning 
	// <3=> Info 
	// <4=> Debug 
	
	#ifndef NRF_LOG_DEFAULT_LEVEL
	#define NRF_LOG_DEFAULT_LEVEL 3
	#endif
	```
	
- Since we'll be using a terminal program (such as CoolTerm), we need to enable logging via the UART backend. This is done by enabling the `NRF_LOG_BACKEND_UART_ENABLED` as follows:

	```c
	// <e> NRF_LOG_BACKEND_UART_ENABLED - nrf_log_backend_uart - Log UART backend
	//==========================================================
	#ifndef NRF_LOG_BACKEND_UART_ENABLED
	#define NRF_LOG_BACKEND_UART_ENABLED 1
	#endif
	```
	
That's it! Now you have logging enabled and you will be able to see log messages show up in your terminal program of choice. We'll get to configuring the terminal program in the "Testing" section.

#### Handling the Button Presses

The application already comes ready with code that sets up the LEDs and Buttons to be used. However, we'll be modifying it to utilize an nRF module called the "App Button" module. This module simplifies the code for handling button events compared to the originally included BSP library.

You can find more about the App Button library here:

[**nRF5 SDK Button Handler Library**](https://infocenter.nordicsemi.com/topic/com.nordic.infocenter.sdk5.v15.3.0/group__app__button.html?resultof=%22%61%70%70%22%20%22%62%75%74%74%6f%6e%22%20)

We will need to add three different segments of code to `main.c` to enable handling of Button 1 events:

- Configure the button we'll be using (Button 1 on the dev kit). We also add a forward declaration of the function responsible for handling the button events: 

	```c
	static void button_event_handler(uint8_t pin_no, uint8_t button_action);
	
	#define NUM_OF_BUTTONS 1
	static const app_button_cfg_t app_buttons[NUM_OF_BUTTONS] =
	{
	    {BUTTON_1, false, BUTTON_PULL, button_event_handler},
	};
	```
	
- The button event handler function. The function handles the Button 1 press and release events, and then calls a function to update our characteristic value that's associated with the button.

	```c
	static void button_event_handler(uint8_t pin_no, uint8_t button_action)
	{
	    switch (pin_no)
	    {
	        case BUTTON_1:
	            NRF_LOG_INFO("Button 1 %s\r\n", button_action == 1 ? "pressed":"released");
	            button_1_characteristic_update(&m_simple_service, &button_action);
	            break;
	        default:
	            APP_ERROR_HANDLER(pin_no);
	            break;
	    }
	}
	```

- The function to initialize and configure the LEDs and Buttons. We will change the following code:

	```c
	static void buttons_leds_init(bool * p_erase_bonds)
	{
	    ret_code_t err_code;
	    bsp_event_t startup_event;
	
	    err_code = bsp_init(BSP_INIT_LEDS | BSP_INIT_BUTTONS, bsp_event_handler);
	    APP_ERROR_CHECK(err_code);
	
	    err_code = bsp_btn_ble_init(NULL, &startup_event);
	    APP_ERROR_CHECK(err_code);
	
	    *p_erase_bonds = (startup_event == BSP_EVENT_CLEAR_BONDING_DATA);
	}
	```

	to

	```c
	static void buttons_leds_init(bool * p_erase_bonds))
	{
		ret_code_t err_code;	
		bsp_event_t startup_event;
		
		err_code = bsp_init(BSP_INIT_LEDS, bsp_event_handler);
		APP_ERROR_CHECK(err_code);
		
		err_code = bsp_btn_ble_init(NULL, &startup_event);
    APP_ERROR_CHECK(err_code);
	
		//init app_button module, 50ms detection delay (button debouncing)
		err_code = app_button_init((app_button_cfg_t *)app_buttons,
		                               NUM_OF_BUTTONS,
		                               APP_TIMER_TICKS(50));
		APP_ERROR_CHECK(err_code);
	
		err_code = app_button_enable();
		APP_ERROR_CHECK(err_code);
		
		*p_erase_bonds = (startup_event == BSP_EVENT_CLEAR_BONDING_DATA);
	}
	```

	Notice we removed the initialization of the buttons from the `bsp_init()` call and instead used the `app_button_init()` API. We also pass the buttons array to the API to configure only Button 1.

Those are all the changes needed to handle the Button 1 press and release events.

#### Initializing GATT Services and Characteristics

The boilerplate example provides example code to initialize your own Service (which in turn initializes its Characteristics) in the following function in `main.c`:

```c
/**@brief Function for initializing services that will be used by the application.
 */
static void services_init(void)
{
    ret_code_t         err_code;
    nrf_ble_qwr_init_t qwr_init = {0};

    // Initialize Queued Write Module.
    qwr_init.error_handler = nrf_qwr_error_handler;

    err_code = nrf_ble_qwr_init(&m_qwr, &qwr_init);
    APP_ERROR_CHECK(err_code);

    /* YOUR_JOB: Add code to initialize the services used by the application.
       ble_xxs_init_t                     xxs_init;
       ble_yys_init_t                     yys_init;

       // Initialize XXX Service.
       memset(&xxs_init, 0, sizeof(xxs_init));

       xxs_init.evt_handler                = NULL;
       xxs_init.is_xxx_notify_supported    = true;
       xxs_init.ble_xx_initial_value.level = 100;

       err_code = ble_bas_init(&m_xxs, &xxs_init);
       APP_ERROR_CHECK(err_code);

       // Initialize YYY Service.
       memset(&yys_init, 0, sizeof(yys_init));
       yys_init.evt_handler                  = on_yys_evt;
       yys_init.ble_yy_initial_value.counter = 0;

       err_code = ble_yy_service_init(&yys_init, &yy_init);
       APP_ERROR_CHECK(err_code);
     */
}
```

Let's modify this function to initialize our own service "simple_service" which we'll provide the code for in the next section.

```c
/**@brief Function for initializing services that will be used by the application.
 */
static void services_init(void)
{
    ret_code_t         err_code;
    nrf_ble_qwr_init_t qwr_init = {0};

    // Initialize Queued Write Module.
    qwr_init.error_handler = nrf_qwr_error_handler;

    err_code = nrf_ble_qwr_init(&m_qwr, &qwr_init);
    APP_ERROR_CHECK(err_code);
    
    // Initialize the Simple service
    err_code = ble_simple_service_init(&m_simple_service, NULL);
    APP_ERROR_CHECK(err_code);
}
```

Another change we need to make to `main.c` is to include our Service header file `simple_service.h`. We do this towards the top of `main.c`:

```c
#include "simple_service.h"
```

We also need to instantiate a variable for our Simple Service. This is done by adding the following code:

```c
BLE_SIMPLE_SERVICE_DEF(m_simple_service);
```

The final change we want to make in `main.c` is to change the advertised device name. By default, it's set to `"Nordic_Template"`. Let's change it to the following:

```c
#define DEVICE_NAME   "Memfault_Example"   /**< Name of device. Will be included in the advertising data. */
```

That's it for `main.c`! The source code for `main.c` is available on [GitHub](https://github.com/memfault/interrupt/tree/master/example/ble-primer/). 


#### Implementation of the GATT Services and Characteristics

For implementation of our Simple Service we will create two source files: `simple_service.h` and `simple_service.c` and place them in the same folder as `main.c`.



##### GATT Service and Characteristic UUIDs

Before we go through the implementation of each of these, we need to assign the GATT Service and Characteristic their own custom UUIDs (a 128-bit value), which we can simply autogenerate using an online tool called [**Online GUID Generator**](https://www.guidgenerator.com/).

"A UUID is a universally unique identifier that is guaranteed to be unique across all space and all time"
*(Bluetooth 5.1 spec, Vol 3, Part B, section 2.5.1 UUID)*.

The one restriction for use of a UUID for a custom BLE Service or Characteristic is that it does not overlap with the Bluetooth SIG Adopted UUIDs. Adopted UUIDs are represented with 16-bit value and its equivalent 128-bit value is computed as follows:

128-bit value = 16-bit-value * 2^96 + BluetoothBaseUUID

where the BluetoothBaseUUID is 00000000-0000-1000-8000-00805F9B34FB

Examples include:

0x180F -> Battery Service UUID (128-bit UUID: 0000**180F**-0000-1000-8000-00805F9B34FB)

0x2A00 -> Device Name Characteristic UUID (128-bit UUID: 0000**2A00**-0000-1000-8000-00805F9B34FB)

The digits in **bold** represent the 16-bit value.

We can simply generate one UUID for the Service and increment it for the Characteristic, and as long as it doesn't use the same "base" as the SIG Adopted UUIDs, we'll be good!



So, we'll use:

**Simple Service UUID**: E54B**0001**-67F5-479E-8711-B3B99198CE6C

**Button 1 Characteristic UUID**: E54B**0002**-67F5-479E-8711-B3B99198CE6C (simply increment the **bold** digits)

Now on to developing the code for our GATT Service and Characteristic.

##### `simple_service.h`


The `simple_service.h` file serves as the header file for our Simple Service. We'll cover the most important parts of the code (the full source code is available on [GitHub](https://github.com/memfault/interrupt/tree/master/example/ble-primer/) for your reference).

First, we'll define the macro that gets used in `main.c` to instantiate a Simple Service object:

```c
#define BLE_SIMPLE_SERVICE_DEF(_name)                                                               \
static ble_simple_service_t _name;                                                                  \
NRF_SDH_BLE_OBSERVER(_name ## _obs,                                                                 \
                     BLE_LBS_BLE_OBSERVER_PRIO,                                                     \
                     ble_simple_service_on_ble_evt, &_name)
```

This is code that you'll find used in many of the Nordic examples, and we simply customized it to our needs.

Next, we'll define the "base" UUID to use along with the 16-bit definitions for each of the Simple Service and the Button 1 Characteristic. The following method is the common method of defining custom (also referred to as *vendor-specific*) Services and Characteristics in Nordic nRF applications.

```c
// Simple service:                     E54B0001-67F5-479E-8711-B3B99198CE6C
//   |--> Button 1 press characteristic:    E54B0002-67F5-479E-8711-B3B99198CE6C

// The bytes are stored in little-endian format, meaning the
// Least Significant Byte is stored first
// (reversed from the order they're displayed as)

// Base UUID: E54B0000-67F5-479E-8711-B3B99198CE6C
#define BLE_UUID_SIMPLE_SERVICE_BASE_UUID  {0x6C, 0xCE, 0x98, 0x91, 0xB9, 0xB3, 0x11, 0x87, 0x9E, 0x47, 0xF5, 0x67, 0x00, 0x00, 0x4B, 0xE5}

// Service & characteristics UUIDs
#define BLE_UUID_SIMPLE_SERVICE_UUID        0x0001
#define BLE_UUID_BUTTON_1_PRESS_CHAR_UUID   0x0002
```

Following that we define the data structure for the Simple Service:

```c
typedef struct ble_simple_service_s ble_simple_service_t;
```

Next, we define the events for Notifications getting enabled or disabled for the Button 1 Characteristic:

```c
typedef enum
{
    BLE_BUTTON_1_PRESS_EVT_NOTIFICATION_ENABLED,
    BLE_BUTTON_1_PRESS_EVT_NOTIFICATION_DISABLED,
} ble_simple_evt_type_t;

typedef struct
{
    ble_simple_evt_type_t evt_type;
} ble_simple_evt_t;
```

In the following code we define the function prototype for the BLE event handler:

```c
typedef void (*ble_simple_evt_handler_t) (ble_simple_service_t * p_simple_service, ble_simple_evt_t * p_evt);
```

We then define the actual structure of the Simple Service which holds the crucial information needed by the Service:

```c
typedef struct ble_simple_service_s
{
    uint16_t                         conn_handle;
    uint16_t                         service_handle;
    uint8_t                          uuid_type;
    ble_simple_evt_handler_t         evt_handler;
    ble_gatts_char_handles_t         button_1_press_char_handles;

} ble_simple_service_t;
```

Finally, we declare the APIs exposed by the Simple Service. This includes functions for: initialization, the BLE event handler (which is needed by the Nordic SoftDevice), and the function for updating the Characteristic value (called when Button 1 is pressed or released:

```c
uint32_t ble_simple_service_init(ble_simple_service_t * p_simple_service, ble_simple_evt_handler_t app_evt_handler);

void ble_simple_service_on_ble_evt(ble_evt_t const * p_ble_evt, void * p_context);

void button_1_characteristic_update(ble_simple_service_t * p_simple_service, uint8_t *button_action);
```

That's the end of the header file. Next, we'll move on to the source file implementation.

##### `simple_service.c`

Let's go over the most important parts of `simple_service.c`.

- A couple of global variables needed for storing the Button 1 Characteristic name and one for tracking whether Notifications are enabled or not.

	```c
	static const uint8_t Button1CharName[]   = "Button 1 press";
	static bool button_notifications_enabled = false;
	``` 

- A function for handling the connection event. In this function, we store the connection handle and make sure the `button_notifications_enabled` boolean is disabled.

	```c
	static void on_connect(ble_simple_service_t * p_simple_service, ble_evt_t const * p_ble_evt)
	{
	    p_simple_service->conn_handle = p_ble_evt->evt.gap_evt.conn_handle;
	    button_notifications_enabled = false;
	}
	``` 
	
- A function for handling the disconnection event. In this function, we invalidate the connection handle and make sure the `button_notifications_enabled` boolean is disabled.

	```c
	static void on_disconnect(ble_simple_service_t * p_simple_service, ble_evt_t const * p_ble_evt)
	{
	    UNUSED_PARAMETER(p_ble_evt);
	    p_simple_service->conn_handle = BLE_CONN_HANDLE_INVALID;
	    button_notifications_enabled = false;
	}
	```
	
- A function for handling the Characteristic Write event. In this function, we handle writing to the CCCD (Client Characteristic Configuration Descriptor) which is used for enabling or disabling Notifications. The event is then passed up to the application layer via the application event handler that's set during the initialization of the Service.

	```c
	static void on_write(ble_simple_service_t * p_simple_service, ble_evt_t const * p_ble_evt)
	{
	    ble_gatts_evt_write_t const * p_evt_write = &p_ble_evt->evt.gatts_evt.params.write;
	
	    // Custom Value Characteristic Written to.
	    if (    (p_evt_write->handle == p_simple_service->button_1_press_char_handles.cccd_handle)
	        &&  (p_evt_write->len == 2))
	    {
	        ble_simple_evt_t evt;
	
	        if (ble_srv_is_notification_enabled(p_evt_write->data))
	        {
	            NRF_LOG_INFO("Notifications ENABLED for button 1 press");
	            evt.evt_type = BLE_BUTTON_1_PRESS_EVT_NOTIFICATION_ENABLED;
	            button_notifications_enabled = true;
	        }
	        else
	        {
	            NRF_LOG_INFO("Notifications DISABLED for button 1 press");
	            evt.evt_type = BLE_BUTTON_1_PRESS_EVT_NOTIFICATION_DISABLED;
	            button_notifications_enabled = false;
	        }
	
	        if (p_simple_service->evt_handler != NULL)
	        {
	            // CCCD written, call application event handler.
	            p_simple_service->evt_handler(p_simple_service, &evt);
	        }
	    }
	}
	```
	
 - A function for adding the Button 1 Characteristic to the BLE stack. This function handles:
	 - Setting the CCCD permissions to allow subscribing to Notifications.
	 - Setting the Characteristic value permissions to allow read only (no write permissions).
	 - Setting the Characteristic name.
	 - Setting the UUID for the Characteristic.
	 - Defining the size of the Characteristic value (1 byte: 0x00 for released state and 0x01 for pressed state).
	 - Finally, calling the `sd_ble_gatts_characteristic_add()` API to add the Characteristic.

	```c
	static uint32_t button_1_press_char_add(ble_simple_service_t * p_simple_service)
	{
	    ble_gatts_char_md_t char_md;
	    ble_gatts_attr_md_t cccd_md;
	    ble_gatts_attr_t    attr_char_value;
	    ble_uuid_t          ble_uuid;
	    ble_gatts_attr_md_t attr_md;
	    uint8_t init_value = 0;
	
	    memset(&char_md, 0, sizeof(char_md));
	    memset(&cccd_md, 0, sizeof(cccd_md));
	    memset(&attr_md, 0, sizeof(attr_md));
	    memset(&attr_char_value, 0, sizeof(attr_char_value));
	
	    // Set permissions on the CCCD and Characteristic value
	    BLE_GAP_CONN_SEC_MODE_SET_OPEN(&cccd_md.read_perm);
	
	    // Set Security to Mode 1 Level 2 (Encryption, No Authentication (no MITM protection))
	    // Refer to <nRF5_SDK>/components/softdevice/s140/headers/ble_gap.h for macros to set
	    // specific Security Modes and Levels
	    BLE_GAP_CONN_SEC_MODE_SET_ENC_NO_MITM(&cccd_md.write_perm);
	
	
	    BLE_GAP_CONN_SEC_MODE_SET_NO_ACCESS(&attr_md.write_perm);
	    BLE_GAP_CONN_SEC_MODE_SET_OPEN(&attr_md.read_perm);
	
	    // CCCD settings (needed for notifications and/or indications)
	    cccd_md.vloc = BLE_GATTS_VLOC_STACK;
	
	    // Characteristic Metadata
	    char_md.char_props.read          = 1;
	    char_md.char_props.notify        = 1;
	    char_md.p_char_user_desc         = Button1CharName;
	    char_md.char_user_desc_size      = sizeof(Button1CharName);
	    char_md.char_user_desc_max_size  = sizeof(Button1CharName);
	    char_md.p_char_pf                = NULL;
	    char_md.p_user_desc_md           = NULL;
	    char_md.p_cccd_md                = &cccd_md;
	    char_md.p_sccd_md                = NULL;
	
	    // Define the Button ON press Characteristic UUID
	    ble_uuid.type = p_simple_service->uuid_type;
	    ble_uuid.uuid = BLE_UUID_BUTTON_1_PRESS_CHAR_UUID;
	
	    // Attribute Metadata settings
	    attr_md.vloc       = BLE_GATTS_VLOC_STACK;
	    attr_md.rd_auth    = 0;
	    attr_md.wr_auth    = 0;
	    attr_md.vlen       = 0;
	
	    // Attribute Value settings
	    attr_char_value.p_uuid       = &ble_uuid;
	    attr_char_value.p_attr_md    = &attr_md;
	    attr_char_value.init_len     = sizeof(uint8_t);
	    attr_char_value.init_offs    = 0;
	    attr_char_value.max_len      = sizeof(uint8_t);
	    attr_char_value.p_value      = &init_value;
	
	    return sd_ble_gatts_characteristic_add(p_simple_service->service_handle, &char_md,
	                                           &attr_char_value,
	                                           &p_simple_service->button_1_press_char_handles);
	}
	``` 

- A function to initialize the Service. It handles the following:
	- Assigning the application level event handler (if passed in).
	- Assigning the Service UUID and adding it to the BLE stack.
	- Adding the Service to the BLE stack.
	- Finally, adding the Button 1 Characteristic to the Service.

	```c
	uint32_t ble_simple_service_init(ble_simple_service_t * p_simple_service, ble_simple_evt_handler_t app_evt_handler)
	{
	    uint32_t   err_code;
	    ble_uuid_t ble_uuid;
	
	    // Initialize service structure
	    p_simple_service->conn_handle = BLE_CONN_HANDLE_INVALID;
	    if (app_evt_handler != NULL)
	    {
	        p_simple_service->evt_handler = app_evt_handler;
	    }
	
	    // Add service UUID
	    ble_uuid128_t base_uuid = {BLE_UUID_SIMPLE_SERVICE_BASE_UUID};
	    err_code = sd_ble_uuid_vs_add(&base_uuid, &p_simple_service->uuid_type);
	    if (err_code != NRF_SUCCESS)
	    {
	        return err_code;
	    }
	
	    // Set up the UUID for the service (base + service-specific)
	    ble_uuid.type = p_simple_service->uuid_type;
	    ble_uuid.uuid = BLE_UUID_SIMPLE_SERVICE_UUID;
	
	    // Set up and add the service
	    err_code = sd_ble_gatts_service_add(BLE_GATTS_SRVC_TYPE_PRIMARY, &ble_uuid, &p_simple_service->service_handle);
	    if (err_code != NRF_SUCCESS)
	    {
	        return err_code;
	    }
	
	    // Add the different characteristics in the service:
	    //   Button 1 press characteristic:   E54B0002-67F5-479E-8711-B3B99198CE6C
	    err_code = button_1_press_char_add(p_simple_service);
	    if (err_code != NRF_SUCCESS)
	    {
	        return err_code;
	    }
	
	    return NRF_SUCCESS;
	}
	```

- A function to handle the different BLE events reported by the SoftDevice. The three events handled are: the connected event, disconnected event, and the Characteristic write event.

	```c
	void ble_simple_service_on_ble_evt(ble_evt_t const * p_ble_evt, void * p_context)
	{
	    ble_simple_service_t * p_simple_service = (ble_simple_service_t *)p_context;
	
	    switch (p_ble_evt->header.evt_id)
	    {
	        case BLE_GAP_EVT_CONNECTED:
	            on_connect(p_simple_service, p_ble_evt);
	            break;
	
	        case BLE_GAP_EVT_DISCONNECTED:
	            on_disconnect(p_simple_service, p_ble_evt);
	            break;
	
	        case BLE_GATTS_EVT_WRITE:
	            on_write(p_simple_service, p_ble_evt);
	            break;
	        default:
	            // No implementation needed.
	            break;
	    }
	}
	```
	
- Finally, a function to handle updates to the Button 1 Characteristic value. This function handles:
	- Setting the corresponding value to the Characteristic based on whether a Button 1 press or release event has occurred. This gets called by the application layer (in `main.c`).
	- Sending a Notification along with the updated value to the Client if it has enabled Notifications.

	```c
	void button_1_characteristic_update(ble_simple_service_t * p_simple_service, uint8_t *button_action)
	{
	    uint32_t err_code = NRF_SUCCESS;
	
	    ble_gatts_value_t gatts_value;
	
	    if (p_simple_service->conn_handle != BLE_CONN_HANDLE_INVALID)
	    {
	        // Initialize value struct.
	        memset(&gatts_value, 0, sizeof(gatts_value));
	
	        gatts_value.len     = sizeof(uint8_t);
	        gatts_value.offset  = 0;
	        gatts_value.p_value = button_action;
	
	        // Update database.
	        err_code = sd_ble_gatts_value_set(p_simple_service->conn_handle,
	                                          p_simple_service->button_1_press_char_handles.value_handle,
	                                          &gatts_value);
	        APP_ERROR_CHECK(err_code);
	
	        if (button_notifications_enabled)
	        {
	            NRF_LOG_INFO("Sending notification for button 1 press/release");
	            uint16_t               len = sizeof (uint8_t);
	            ble_gatts_hvx_params_t hvx_params;
	            memset(&hvx_params, 0, sizeof(hvx_params));
	
	            hvx_params.handle = p_simple_service->button_1_press_char_handles.value_handle;
	
	            hvx_params.type   = BLE_GATT_HVX_NOTIFICATION;
	            hvx_params.offset = 0;
	            hvx_params.p_len  = &len;
	            hvx_params.p_data = (uint8_t*)button_action;
	
	            err_code = sd_ble_gatts_hvx(p_simple_service->conn_handle, &hvx_params);
	            APP_ERROR_CHECK(err_code);
	        }
	    }
	}
	```
	
#### Custom (Vendor-Specific) Services and Characteristics in nRF Applications
Before we can build the application, there's one last important change that we need to make. This change will be in the `sdk_config.h` file (located at `ble_app_template/pca10056/s140/config/sdk_config.h`).

We need to modify a macro responsible for telling the SoftDevice (Nordic's BLE stack) about the number of vendor-specific UUIDs used in the application. This change is needed since it requires some (extra) dedicated memory for storing these UUIDs. We only need to increment this macro for each "base" UUID, basically for each time the `sd_ble_uuid_vs_add()` API is called. So, in our case we only need to increment it by 1 (since the Service and Characteristic share the same "base").

Look for the macro named `NRF_SDH_BLE_VS_UUID_COUNT` in `sdk_config.h` and change its value from 0 to 1:

```c
// <o> NRF_SDH_BLE_VS_UUID_COUNT - The number of vendor-specific UUIDs. 
#ifndef NRF_SDH_BLE_VS_UUID_COUNT
#define NRF_SDH_BLE_VS_UUID_COUNT 1
#endif
```

Along with this change, we will need to make a change in the RAM offset and size — we'll get to this in the **Testing** section since it requires us to actually run the application and get the appropriate values from the log output.
