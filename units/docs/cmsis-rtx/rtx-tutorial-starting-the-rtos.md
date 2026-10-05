---
id: "rtx-tutorial-starting-the-rtos"
type: "concept"
domain: "rtos"
title: "tutorial: Starting the RTOS"
summary: "To build a simple RTOS, program we declare each thread as a standard 'C' function and also declare a thread ID variable for each function."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#starting-the-rtos"
license: "Apache-2.0"
mode: "V"
---

To build a simple RTOS, program we declare each thread as a standard 'C' function and also declare a thread ID variable for each function.

```c
void thread1 (void);
void thread2 (void);
 
osThreadId thrdID1, thrdID2;
```

Once the processor leaves the reset vector, we will enter the `main()` function as normal. Once in `main()`, we must call osKernelInitialize to setup the RTOS. It is not possible to call any RTOS function before the osKernelInitialize function has successfully completed. Once osKernelInitialize has completed, we can create further threads and other RTOS objects. This can be done by creating a launcher thread, in the example below this is called `app_main()`. Inside the `app_main()` thread, we create all the RTOS threads and objects we need to start our application running. As we will see later, it is also possible to dynamically create and destroy RTOS objects as the application is running. Next, we can call osKernelStart to start the RTOS and the scheduler task switching. You can run any initializing code you want before starting the RTOS to setup peripherals and initialize the hardware.

```c
void app_main(void *argument) {
  T_led_ID1 = osThreadNew(led_Thread1, NULL, &ThreadAttr_LED1);
  T_led_ID2 = osThreadNew(led_Thread2, NULL, &ThreadAttr_LED2);
  osDelay(osWaitForever);
  while (1)
    ;
}
 
void main(void) {
  IODIR1 = 0x00FF0000;               // Do any C code you want
  osKernelInitialize();              // Initialize the kernel
  osThreadNew(app_main, NULL, NULL); // Create the app_main() launcher thread
  osKernelStart();                   // Start the RTOS
}
```

When threads are created they are also assigned a priority. If there are a number of threads ready to run and they all have the same priority, they will be allotted run time in a round-robin fashion. However, if a thread with a higher priority becomes ready to run, the RTOS scheduler will de-schedule the currently running thread and start the high priority thread running. This is called pre-emptive priority-based scheduling. When assigning priorities, you have to be careful because the high priority thread will continue to run until it enters a waiting state or until a thread of equal or higher priority is ready to run.

### Exercise 1 - A First CMSIS-RTOS2 Project

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 01 First Project** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.
