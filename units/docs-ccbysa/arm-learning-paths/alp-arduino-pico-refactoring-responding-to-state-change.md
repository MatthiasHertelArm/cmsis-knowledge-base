---
id: "alp-arduino-pico-refactoring-responding-to-state-change"
type: "concept"
domain: "project"
title: "Embedded programming with Arduino on the Raspberry Pi Pico: Refactor the application: Responding to state change"
summary: "Previously the loop() code had to perform multiple checks."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/arduino-pico/refactoring.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/arduino-pico/refactoring/#responding-to-state-change"
license: "CC-BY-SA-4.0"
mode: "V"
---

Previously the `loop()` code had to perform multiple checks. 

First, it had to read the current state of the PIR sensor into `val`, then it had to compare the current state to the previous state stored in `motionState`, and finally it had to do something different depending on the four possible combinations of values for the two variables.

Now, there is just one variable to consider. The updated `loop()` function is below: 

```arduino
void loop() {
  // put your main code here, to run repeatedly:

  // Every iteration of the loop has a half-second delay, this reduces the processing load on the device
  delay(500);
  
  if (motionDetected) {
    Serial.println("Motion Detected!");
  
    // First we write to the USB console that motion was detected
    Serial.println("Motion detected");
    // Next we turn the LED off, indicating that we're not longer in the waiting state
    ledOff();
    // Then we trigger the beep
    doBeep();
    // And increment our counter
    counter++;
    Serial.print("Counter is now at ");
    Serial.println(counter);
    
    // Turn the LED back on, indicating that we're re-entering a waiting state
    ledOn();
    // Finally we save the fact that we've handled this motion event
    motionDetected = false;

  }

}
```

As you can see, the nested if/else blocks have been replaced by a single check, `if (motionDetected)`. If it's true, call the helper functions `ledOff()`, `doBeep()`, and `ledOn()`, increment the counter, and write the new value to the serial console. 

You'll notice that you don't need the "cooling off" code anymore. That's because the `RISING` interrupt won't happen again until the PIR sensor has cooled off, returning `motionPin` to a `LOW` state.

Finally, you do have to set `motionDetected = false` because the event has been handled.
