---
id: "drv-mci-uhs-i-signal-voltage-switch"
type: "concept"
domain: "drivers"
title: "MCI UHS-I Signal Voltage Switch"
summary: "Host-controller phases of the SD UHS-I signal-voltage switch."
status: "draft"
collection: "cmsis-driver"
source: "ARM-software/CMSIS_6@acf7392:CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
doc_source: "https://github.com/ARM-software/CMSIS_6/blob/acf7392/CMSIS/Documentation/Doxygen/Driver/src/Driver_MCI.c"
license: "Apache-2.0"
mode: "V"
---

Host-controller phases of the SD UHS-I signal-voltage switch.


Call ARM_MCI_Control with **control** = ARM_MCI_UHS_VOLTAGE_SWITCH.
Set **arg** to one of the phase codes below.

To perform a voltage switch, MCI controlling software must use this order:
1. PREPARE.
2. Send voltage switch command using ARM_MCI_SendCommand and wait for its completion.
3. APPLY.
4. Wait at least 5 ms.
5. CLOCK_ON.
6. Wait at least 1 ms.
7. VERIFY.

**Example:**
```
volatile uint32_t MCI_Events;

void MCI_SignalEvent_Callback (uint32_t event) {
  // Save current event
  MCI_Events |= event;
}

// Switch Signaling Voltage
void mci_switch_signaling_voltage(void) {
  int32_t status;
  uint32_t r1 = 0U;

  // Prepare host controller for signaling voltage switch
  if (MCIdrv->Control(ARM_MCI_UHS_VOLTAGE_SWITCH, ARM_MCI_VOLTAGE_SWITCH_PREPARE) != ARM_DRIVER_OK) {
    return;
  }

  // Clear previous events
  MCI_Events = 0;

  // Send voltage switch command
  status = MCIdrv->SendCommand(11, 0U, ARM_MCI_RESPONSE_SHORT|ARM_MCI_RESPONSE_CRC, &r1);

  if (status == ARM_DRIVER_OK) {
    // Wait for event
    while ((MCI_Events & ARM_MCI_EVENT_COMMAND_COMPLETE) == 0U);

    // Change the signaling voltage selection from 3.3V to 1.8V
    status = MCIdrv->Control(ARM_MCI_UHS_VOLTAGE_SWITCH, ARM_MCI_VOLTAGE_SWITCH_APPLY);

    if (status == ARM_DRIVER_OK) {
      // Wait for the signaling voltage to stabilize
      delay_ms(5);

      // Turn on the SD clock after the voltage switch
      status = MCIdrv->Control(ARM_MCI_UHS_VOLTAGE_SWITCH, ARM_MCI_VOLTAGE_SWITCH_CLOCK_ON);

      if (status == ARM_DRIVER_OK) {
        // Wait for the card to release the data lines
        delay_ms(1);

        // Verify the voltage switch after memory card releases data lines
        status = MCIdrv->Control(ARM_MCI_UHS_VOLTAGE_SWITCH, ARM_MCI_VOLTAGE_SWITCH_VERIFY);

        if (status == ARM_DRIVER_OK) {
          // Voltage switch successful
          return;
        }
      }
    }
  }
  // Failed to switch signaling voltage, abort procedure
  MCIdrv->Control(ARM_MCI_UHS_VOLTAGE_SWITCH, ARM_MCI_VOLTAGE_SWITCH_ABORT);
}
```
