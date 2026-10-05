---
id: "threadx-chapter-5-device-drivers-for-threa-simple-driver-example"
type: "concept"
domain: "rtos"
title: "Chapter 5 - Device Drivers for ThreadX: Simple Driver Example"
summary: "An example is the best way to describe a device driver. In this example, the driver assumes a simple serial hardware device with a configuration register, an input register, and an output register."
status: "draft"
collection: "threadx"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/threadx/chapter5.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/threadx/chapter5.md#simple-driver-example"
license: "MIT"
mode: "V"
---

An example is the best way to describe a device driver. In this example, the driver assumes a simple serial hardware device with a configuration register, an input register, and an output register. This simple driver example illustrates the initialization, input, output, and interrupt functional areas.

### Simple Driver Initialization

The ***tx_sdriver_initialize*** function of the simple driver creates two counting semaphores that are used to manage the driver's input and output operation. The input semaphore is set by the input ISR when a character is received by the serial hardware device. Because of this, the input semaphore is created with an initial count of zero.

Conversely, the output semaphore indicates the availability of the serial hardware transmit register. It is created with a value of one to indicate the transmit register is initially available.

The initialization function is also responsible for installing the low-level interrupt vector handlers for input and output notifications. Like other ThreadX interrupt service routines, the low-level handler must call ***_tx_thread_context_save*** before calling the simple driver ISR. After the driver ISR returns, the low-level handler must call ***_tx_thread_context_restore***.

> **Important:** *It is important that initialization is called before any of the other driver functions. Typically, driver initialization is called from **tx_application_define**.*

```c
VOID tx_sdriver_initialize(VOID)
{
    /* Initialize the two counting semaphores used to control
    the simple driver I/O. */
    tx_semaphore_create(&tx_sdriver_input_semaphore,
                        "simple driver input semaphore", 0);
    tx_semaphore_create(&tx_sdriver_output_semaphore,
                        "simple driver output semaphore", 1);

    /* Setup interrupt vectors for input and output ISRs.
    The initial vector handling should call the ISRs
    defined in this file. */

    /* Configure serial device hardware for RX/TX interrupt
    generation, baud rate, stop bits, etc. */
}
```
**FIGURE 9. Simple Driver Initialization**

### Simple Driver Input

Input for the simple driver centers around the input semaphore. When a serial device input interrupt is received, the input semaphore is set. If one or more threads are waiting for a character from the driver, the thread waiting the longest is resumed. If no threads are waiting, the semaphore simply remains set until a thread calls the drive input function.

There are several limitations to the simple driver input handling. The most significant is the potential for dropping input characters. This is possible because there is no ability to buffer input characters that arrive before the previous character is processed. This is easily handled by adding an input character buffer.

> **Note:** *Only threads are allowed to call the* ***tx_sdriver_input*** *function.*

Figure 10 shows the source code associated with simple driver input.

```c
UCHAR tx_sdriver_input(VOID)
{
  /* Determine if there is a character waiting. If not,
  suspend. */
  tx_semaphore_get(&tx_sdriver_input_semaphore,
  TX_WAIT_FOREVER;

  /* Return character from serial RX hardware register. */
  return(*serial_hardware_input_ptr);
}
  VOID tx_sdriver_input_ISR(VOID)
{
  /* See if an input character notification is pending. */
  if (!tx_sdriver_input_semaphore.tx_semaphore_count)
  {
    /* If not, notify thread of an input character. */
    tx_semaphore_put(&tx_sdriver_input_semaphore);
  }
}
```
**FIGURE 10. Simple Driver Input**

### Simple Driver Output

Output processing utilizes the output semaphore to signal when the serial device's transmit register is free. Before an output character is actually written to the device, the output semaphore is obtained. If it is not available, the previous transmit is not yet complete.

The output ISR is responsible for handling the transmit complete interrupt. Processing of the output ISR amounts to setting the output semaphore, thereby allowing output of another character.

> **Note:** *Only threads are allowed to call the* ***tx_sdriver_output*** *function.*

Figure 11 shows the source code associated with simple driver output.

```c
VOID tx_sdriver_output(UCHAR alpha)
{
  /* Determine if the hardware is ready to transmit a
  character. If not, suspend until the previous output
  completes. */
  tx_semaphore_get(&tx_sdriver_output_semaphore,
                                          TX_WAIT_FOREVER);

  /* Send the character through the hardware. */
  *serial_hardware_output_ptr = alpha;
}
  
VOID tx_sdriver_output_ISR(VOID)
{
  /* Notify thread last character transmit is
  complete. */
  tx_semaphore_put(&tx_sdriver_output_semaphore);
}
```
**FIGURE 11. Simple Driver Output**

### Simple Driver Shortcomings

This simple device driver example illustrates the basic idea of a ThreadX device driver. However, because the simple device driver does not address data buffering or any overhead issues, it does not fully represent real-world ThreadX drivers. The following section describes some of the more advanced issues associated with device drivers.
