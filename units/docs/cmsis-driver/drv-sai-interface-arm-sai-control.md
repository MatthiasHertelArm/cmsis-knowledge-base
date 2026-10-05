---
id: "drv-sai-interface-arm-sai-control"
type: "concept"
domain: "drivers"
title: "SAI Interface: User Defined Protocol / ARM_SAI_Control"
summary: "The function ARMSAIControl controls the SAI interface and executes various operations."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@26206e4:CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/26206e4/CMSIS/Documentation/Doxygen/Driver/src/Driver_SAI.c"
license: "Apache-2.0"
mode: "V"
---

_Part of: User Defined Protocol_

```c
int32_t ARM_SAI_Control (uint32_t control, uint32_t arg1, uint32_t arg2)
```


The function **ARM_SAI_Control** controls the SAI interface and executes various operations.

The parameter **control** specifies the operation. Values are listed in the table **Parameter _control_**.\n
The parameter **arg1** provides,  depending on the operation,  additional information or sets values. 
Refer to table **Parameter _arg1_**. \n
The parameter **arg2** provides,  depending on the operation and/or **arg1,**  additional information or sets values. 

The driver provides a receiver/transmitter pair of signals. 
In asynchronous operation mode, they operate completely independent from each other. 
In synchronous operation mode, the synchronous channel uses the Clock (SCK) and Frame Sync (WS) signal from the asynchronous one
(control category **Synchronization**).

The clock polarity can be set for every protocol, regardless whether it is already predefined for I2S, MSB/LSB Jusitified
(control category **Clock Polarity**).

A master clock provides a faster clock from which the frame can be derived (usually 256 x faster than the normal frame clock). 
You can use a master clock only in master mode. A slave will always have only one clock 
(control category **Master Clock pin (MCLK)**).

		
The table lists the operation values for **control.** Values from different categories can be ORed.


|  Parameter **control**               |                                        Bit  |              Category       | 
     Description                         | 

|  ARM_SAI_CONFIGURE_TX           |  0..7  |  Operation     | 
     Configure transmitter. **arg1** (see  **Parameter _arg1_**) and **arg2** provide additional configuration.   | 

|  ARM_SAI_CONFIGURE_RX           | 
     Configure receiver. **arg1** (see  **Parameter _arg1_**) and **arg2** provide additional configuration.   | 

|  ARM_SAI_CONTROL_TX                 | 
     Enable or disable transmitter and control mute; 
	**arg1.0** : `0=disable (default); 1=enable;` **arg1.1** : `mute` (see ARM_SAI_Send)  | 

|  ARM_SAI_CONTROL_RX             | 
     Enable or disable receiver; **arg1.0** : `0=disable (default); 1=enable` (see ARM_SAI_Receive)   | 

|  ARM_SAI_MASK_SLOTS_TX          | 
     Mask transmitter slots; **arg1** = `mask` (bit: 0=active, 1=inactive); all configured slots are active by default.   | 

|  ARM_SAI_MASK_SLOTS_RX          | 
     Mask receiver slots; **arg1** = `mask` (bit: 0=active, 1=inactive); all configured slots are active by default.   | 

|  ARM_SAI_ABORT_SEND             | 
     Abort send operation (see ARM_SAI_Send).   | 

|  ARM_SAI_ABORT_RECEIVE          | 
     Abort receive operation (see ARM_SAI_Receive).   | 

|  ARM_SAI_MODE_MASTER            |  8     |  Mode              | 
     Master mode. **arg2** specifies the audio frequency in [Hz].  You can also set the **Master Clock pin**. | 

|  ARM_SAI_MODE_SLAVE (default)   | 
     Slave mode.   | 

|  ARM_SAI_ASYNCHRONOUS (default)      |   9   |  Synchronization  | 
     Asynchronous operation using own clock and sync signal.   | 

|  ARM_SAI_SYNCHRONOUS                |  
     Synchronous operation using clock and sync signal from other transmitter/receiver.   | 

|  ARM_SAI_PROTOCOL_USER  (default)   |  10..12  |  Protocol      | 
     User defined                            | 

|  ARM_SAI_PROTOCOL_I2S               | 
     I2C                                     | 

|  ARM_SAI_PROTOCOL_MSB_JUSTIFIED     |  
     MSB (left) justified                    | 

|  ARM_SAI_PROTOCOL_LSB_JUSTIFIED     |  
     LSB (right) justified                   | 

|  ARM_SAI_PROTOCOL_PCM_SHORT         |  
     PCM with short frame                    | 

|  ARM_SAI_PROTOCOL_PCM_LONG          |  
     PCM with long frame                     | 

|  ARM_SAI_PROTOCOL_AC97              |  
     AC'97                                   | 

|  ARM_SAI_DATA_SIZE(n)               |  13..17  |  Data Size     |      
     Data size in bits; the range for **n** is `8..32`. See also: **Frame Slot Size**.     | 

|  ARM_SAI_MSB_FIRST                  |  18      |  Bit Order     |      
     Data is transferred with MSB first.     | 

|  ARM_SAI_LSB_FIRST                  | 
     Data is transferred with LSB first (User protocol only, ignored otherwise).      | 

|  ARM_SAI_MONO_MODE                  |  19      |  Mono Mode |       
     Only for I2S, MSB/LSB justified. 
	     When using Driver_SAI_I2S in mono mode, only data for a single channel is sent to and received from the driver.
         Hardware will duplicate the data for the second channel on transmit and ignore the second channel on receive.     | 

|  ARM_SAI_COMPANDING_NONE (default)  |  20..22  |  Companding     | 
     No companding   | 

|  ARM_SAI_COMPANDING_A_LAW           |    
     A-Law companding (8-bit data)           | 

|  ARM_SAI_COMPANDING_U_LAW           |    
     u-Law companding (8-bit data)           | 

|  ARM_SAI_CLOCK_POLARITY_0  (default)   >  |     23    |  Clock Polarity  | 
     Drive on falling edge, capture on rising  edge.  | 

|  ARM_SAI_CLOCK_POLARITY_1       | 
     Drive on rising  edge, capture on falling edge.  | 

|  ARM_SAI_MCLK_PIN_INACTIVE  (default)   |  24..26  |  Master Clock pin (MCLK)  | 
     MCLK not used.                          | 

|  ARM_SAI_MCLK_PIN_OUTPUT            |    
     MCLK is output (Master mode only).      | 

|  ARM_SAI_MCLK_PIN_INPUT             |    
     MCLK is input (Master mode only).       | 




The parameter **arg1** provides frame-specific values depending on the **control** operation. Values from different categories can be ORed.


|  Parameter **arg1**        | 
       Bit   | 
	 Category                         | 
     Description                      | 

|  ARM_SAI_FRAME_LENGTH(n)     | 
      0..9   | 
	 Frame Length                     | 
     Frame length in bits; the possible range for **n** is `8..1024`; default depends on protocol and data.     | 

|  ARM_SAI_FRAME_SYNC_WIDTH(n) | 
     10..17  | 
	 Frame Sync Width                 | 
     Frame Sync width in bits; the possible range for **n** is `1..256`; `default=1`; User protocol only, ignored otherwise.   | 

|  ARM_SAI_FRAME_SYNC_POLARITY_HIGH    | 
     18  | 
	 Frame Sync Polarity   | 
     Frame Sync is active high (default).     | 

|  ARM_SAI_FRAME_SYNC_POLARITY_LOW     | 
     Frame Sync is active low (User protocol only, ignored otherwise).    | 

|  ARM_SAI_FRAME_SYNC_EARLY            | 
      19   | 
	 Frame Sync Early               | 
     Frame Sync one bit before the first bit of the frame (User protocol only, ignored otherwise).                    | 

|  ARM_SAI_SLOT_COUNT(n)               | 
     20..24          | 
	 Frame Sync Count                         | 
     Number of slots in frame; the possible range for **n** is `1..32`; default=`1`;  User protocol only, ignored otherwise.   | 

|  ARM_SAI_SLOT_SIZE_DEFAULT      | 
     25..26                 | 
	  Frame Slot Size                                | 
     Slot size is equal to data size (default).                  | 

|  ARM_SAI_SLOT_SIZE_16                                   | 
     Slot size is `16 bits` (User protocol only, ignored otherwise).      | 

|  ARM_SAI_SLOT_SIZE_32                                   | 
     Slot size is `32 bits` (User protocol only, ignored otherwise).      | 

|  ARM_SAI_SLOT_OFFSET(n)      | 
     27..31  | 
	 Frame Slot Offset                | 
     Offset of first data bit in slot; The range for **n** is `0..31`; default=`0`;  User protocol only, ignored otherwise.    | 





Depending on the **control** operation, the parameter **arg2** specifies the Master Clock (MCLK) prescaler and calculates the audio frequency automatically.

Parameter **arg2**                       | MCLK Prescaler
:----------------------------------------|:--------------------------------------------
ARM_SAI_MCLK_PRESCALER(n)           | MCLK prescaler; Audio frequency = MCLK/n; the range for **n** is `1..4096`; default=`1`.


**Example**

```
extern ARM_DRIVER_SAI Driver_SAI0;
 
// configure Transmitter to Asynchronous Master: I2S Protocol, 16-bit data, 16kHz Audio frequency
status = Driver_SAI0.Control(ARM_SAI_CONFIGURE_TX | 
                             ARM_SAI_MODE_MASTER  | 
                             ARM_SAI_ASYNCHRONOUS | 
                             ARM_SAI_PROTOCOL_I2S | 
                             ARM_SAI_DATA_SIZE(16), 0, 16000);
 
// configure Receiver to Asynchronous Master: I2S Protocol, 16-bit data, 16kHz Audio frequency
status = Driver_SAI0.Control(ARM_SAI_CONFIGURE_RX | 
                             ARM_SAI_MODE_MASTER  | 
                             ARM_SAI_ASYNCHRONOUS | 
                             ARM_SAI_PROTOCOL_I2S | 
                             ARM_SAI_DATA_SIZE(16), 0, 16000);
 
// enable Transmitter
status = Driver_SAI0.Control(ARM_SAI_CONTROL_TX, 1, 0);
 
// enable Receiver
status = Driver_SAI0.Control(ARM_SAI_CONTROL_RX, 1, 0);
```

****************************************************************************************************************
