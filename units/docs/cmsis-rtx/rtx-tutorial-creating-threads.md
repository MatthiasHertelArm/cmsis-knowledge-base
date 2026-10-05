---
id: "rtx-tutorial-creating-threads"
type: "concept"
domain: "rtos"
title: "tutorial: Creating Threads"
summary: "Once the RTOS is running, there are a number of system calls that are used to manage and control the active threads. The documentation lists all thread management functions."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#creating-threads"
license: "Apache-2.0"
mode: "V"
---

Once the RTOS is running, there are a number of system calls that are used to manage and control the active threads. The documentation lists all thread management functions.

As we saw in the first example, the `app_main()` thread is used as a launcher thread to create the application threads. This is done in two stages. First a thread structure is defined; this allows us to define the thread operating parameters.

```c
osThreadId thread1_id; // thread handle
 
static const osThreadAttr_t threadAttr_thread1 = {
    “Name_String ",      //Human readable Name for debugger
    Attribute_bits Control_Block_Memory,
    Control_Block_Size,
    Stack_Memory,
    Stack_Size,
    Priority,
    TrustZone_ID,
    reserved};
```

The thread structure requires us to define the name of the thread function, its thread priority, any special attribute bits, its TrustZone_ID and its memory allocation. This is quite a lot of detail to go through but we will cover everything by the end of this application note. Once the thread structure has been defined, the thread can be created using the osThreadNew API call. Then the thread is created from within the application code, this is often the within the `app_main()` thread but a thread can be created at any point within any thread.

```c
thread1_id = osThreadNew(name_Of_C_Function, argument,&threadAttr_thread1);
```

This creates the thread and starts it running. It is also possible to pass a parameter to the thread when it starts.

```c
uint32_t startupParameter = 0x23;
thread1_id = osThreadNew(name_Of_C_Function, (uint32_t)startupParameter,&threadAttr_thread1);
```

### Exercise 2 - Creating and Managing Threads

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 02 Threads** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.
