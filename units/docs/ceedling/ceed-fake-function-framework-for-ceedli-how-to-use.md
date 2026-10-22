---
id: "ceed-fake-function-framework-for-ceedli-how-to-use"
type: "concept"
domain: "test"
title: "Fake Function Framework for Ceedling: How to use"
summary: "You use fff with Ceedling the same way you used to use CMock."
status: "draft"
collection: "ceedling"
source: "ThrowTheSwitch/Ceedling@2c60022:docs/mkdocs/plugins/fff.md"
doc_source: "https://throwtheswitch.github.io/Ceedling/plugins/fff/#how-to-use"
license: "MIT"
mode: "V"
---

You use fff with Ceedling the same way you used to use CMock.

If you want to "mock" `some_module.h` in your tests, just `#include "mock_some_module.h"`.
This creates a fake function for each of the functions defined in `some_module.h`.

The name of each fake is the original function name with an appended `_fake`.
For example, if we're generating fakes for a stack module with `push` and `pop` functions, we would have the fakes `push_fake` and `pop_fake`.
These fakes are linked into our test executable so that any time our unit under test calls `push` or `pop` our fakes are called instead.

Each of these fakes is actually a structure containing information about how the function was called, and what it might return.
We can use Unity to inspect these fakes in our tests, and verify the interactions of our units.
There is also a global structure named `fff` which we can use to check the sequence of calls.

The fakes can also be configured to return particular values, so you can exercise the unit under test however you want.

The examples below explain how to use fff to test a variety of module interactions.
Each example uses fakes for a "display" module, created from a display.h file with `#include "mock_display.h"`. The `display.h` file must exist and must contain the prototypes for the functions to be faked.

### Test that a function was called once

```c
void
test_whenTheDeviceIsReset_thenTheStatusLedIsTurnedOff()
{
    // When
    event_deviceReset();

    // Then
    TEST_ASSERT_EQUAL(1, display_turnOffStatusLed_fake.call_count);
}
```

### Test that a function was NOT called

```c
void
test_whenThePowerReadingIsLessThan5_thenTheStatusLedIsNotTurnedOn(void)
{
    // When
    event_powerReadingUpdate(4);

    // Then
    TEST_ASSERT_EQUAL(0, display_turnOnStatusLed_fake.call_count);
}
```

### Test that a single function was called with the correct argument

```c
void
test_whenTheVolumeKnobIsMaxed_thenVolumeDisplayIsSetTo11(void)
{
    // When
    event_volumeKnobMaxed();

    // Then
    TEST_ASSERT_EQUAL(1, display_setVolume_fake.call_count);
    TEST_ASSERT_EQUAL(11, display_setVolume_fake.arg0_val);
}
```

### Test that calls are made in a particular sequence

```c
void
test_whenTheModeSelectButtonIsPressed_thenTheDisplayModeIsCycled(void)
{
    // When
    event_modeSelectButtonPressed();
    event_modeSelectButtonPressed();
    event_modeSelectButtonPressed();

    // Then
    TEST_ASSERT_EQUAL_PTR((void*)display_setModeToMinimum, fff.call_history[0]);
    TEST_ASSERT_EQUAL_PTR((void*)display_setModeToMaximum, fff.call_history[1]);
    TEST_ASSERT_EQUAL_PTR((void*)display_setModeToAverage, fff.call_history[2]);
}
```

### Fake a return value from a function

```c
void
test_givenTheDisplayHasAnError_whenTheDeviceIsPoweredOn_thenTheDisplayIsPoweredDown(void)
{
    // Given
    display_isError_fake.return_val = true;

    // When
    event_devicePoweredOn();

    // Then
    TEST_ASSERT_EQUAL(1, display_powerDown_fake.call_count);
}
```

### Fake a function with a value returned by reference

```c
void
test_givenTheUserHasTypedSleep_whenItIsTimeToCheckTheKeyboard_theDisplayIsPoweredDown(void)
{
    // Given
    char mockedEntry[] = "sleep";
    void return_mock_value(char * entry, int length)
    {
        if (length > strlen(mockedEntry))
        {
            strncpy(entry, mockedEntry, length);
        }
    }
    display_getKeyboardEntry_fake.custom_fake = return_mock_value;

    // When
    event_keyboardCheckTimerExpired();

    // Then
    TEST_ASSERT_EQUAL(1, display_powerDown_fake.call_count);
}
```

### Fake a function with a function pointer parameter

```c
void
test_givenNewDataIsAvailable_whenTheDisplayHasUpdated_thenTheEventIsComplete(void)
{
    // A mock function for capturing the callback handler function pointer.
    void(*registeredCallback)(void) = 0;
    void mock_display_updateData(int data, void(*callback)(void))
    {
        //Save the callback function.
        registeredCallback = callback;
    }
    display_updateData_fake.custom_fake = mock_display_updateData;

    // Given
    event_newDataAvailable(10);

    // When
    if (registeredCallback != 0)
    {
        registeredCallback();
    }

    // Then
    TEST_ASSERT_EQUAL(true, eventProcessor_isLastEventComplete());
}
```
