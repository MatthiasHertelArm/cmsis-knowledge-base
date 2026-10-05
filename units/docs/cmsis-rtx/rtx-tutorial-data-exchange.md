---
id: "rtx-tutorial-data-exchange"
type: "concept"
domain: "rtos"
title: "tutorial: Inter-thread Communication / Data Exchange"
summary: "So far, all of the inter-thread communication methods have only been used to trigger execution of threads; they do not upport the exchange of program data between threads."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#data-exchange"
license: "Apache-2.0"
mode: "V"
---

_Part of: Inter-thread Communication_

So far, all of the inter-thread communication methods have only been used to trigger execution of threads; they do not
upport the exchange of program data between threads. Clearly, in a real program we will need to move data between threads.
This could be done by reading and writing to globally declared variables. In anything but a very simple program, trying to
guarantee data integrity would be extremely difficult and prone to unforeseen errors. The exchange of data between threads
needs a more formal asynchronous method of communication.

CMSIS-RTOS provides two methods of data transfer between threads. The first method is a message queue which creates a
buffered data 'pipe' between two threads. The message queue is designed to transfer integer values.

The second form of data transfer is a mail queue. This is very similar to a message queue except that it transfers blocks of
data rather than a single integer.

Message and mail queues both provide a method for transferring data between threads. This allows you to view your design as
a collection of objects (threads) interconnected by data flows. The data flow is implemented by message and mail queues.
This provides both a buffered transfer of data and a well defined communication interface between threads. Starting with a
system level design based on threads connected by mail and message queues allows you to code different subsystems of your
project, especially useful if you are working in a team. Also as each thread has well defined inputs and outputs it is easy
to isolate for testing and code reuse.

#### Message Queue

To setup a message queue we first need to allocate the memory resources:

```c
osMessageQId_t Q_LED;
 
osMessageQueueAttr_t {
  const char *name;   ///< name of the message queue
  uint32_t attr_bits; ///< attribute bits
  void *cb_mem;       ///< memory for control block
  uint32_t cb_size;   ///< size of provided memory for control block
  void *mq_mem;       ///< memory for data storage
  uint32_t mq_size;   ///< size of provided memory for data storage
};
```

Once the message queue handle and attributes have been declared we can create the message queue in a thread:

```c
Q_LED = osMessageNew(DepthOfMesageQueue,WidthOfMessageQueue,&osMessageQueueAttr);
```

Once the message queue has been created we can put data into the queue from one thread:

```c
osMessageQueuePut(Q_LED,&dataIn,messagePrioriy,osWaitForever);
```

and then read if from the queue in another:

```c
result = osMessageQueueGet(Q_LED,&dataOut,messagePriority,osWaitForever);
```

#### Exercise 16 - Message Queue

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 16 Message Queue** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.

#### Extended Message Queue

In the last example we defined a word wide message queue. If you need to send a larger amount of data it is also possible to
define a message queue where each slot can hold more complex data. First, we can define a structure to hold our message
data:

```c
typedef struct {
  uint32_t duration;
  uint32_t ledNumber;
  uint8_t priority;
} message_t;
```

Then we can define a message queue which is formatted to receive this type of message:

```c
Q_LED = osMessageQueueNew(16,sizeof(message_t),&queueAttr_Q_LED );
```

#### Exercise 17 - Message Queue {# rtos2_tutorial_ex17}

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 17 Extended Message Queue** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.
