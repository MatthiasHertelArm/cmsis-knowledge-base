---
id: "rtx-tutorial-memory-pool"
type: "concept"
domain: "rtos"
title: "tutorial: Inter-thread Communication / Memory Pool"
summary: "We can design a message queue to support the transfer of large amounts of data. However, this method has an overhead in that we are \"moving\" the data in the queue."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/tutorial.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/tutorial.md#memory-pool"
license: "Apache-2.0"
mode: "V"
---

_Part of: Inter-thread Communication_

We can design a message queue to support the transfer of large amounts of data. However, this method has an overhead in that
we are "moving" the data in the queue. In this section, we will look at designing a more efficient "zero copy" mailbox where
the data remains static. CMSIS-RTOS2 supports the dynamic allocation of memory in the form of a fixed block memory pool.
First, we can declare the memory pool attributes:

```c
osMemoryPoolAttr_t {
  const char *name;   ///< name of the memory pool
  uint32_t attr_bits; ///< attribute bits
  void *cb_mem;       ///< memory for control block
  uint32_t cb_size;   ///< size of provided memory for control block
  void *mp_mem;       ///< memory for data storage
  uint32_t mp_size;   ///< size of provided memory for data storage
} osMemoryPoolAttr_t;
```

And a handle for the memory pool:

```c
osMemoryPoolId_t mpool;
```

For the memory pool itself, we need to declare a structure which contains the memory elements we require in each memory pool
lot:

```c
typedef struct {
  uint8_t LED0;
  uint8_t LED1;
  uint8_t LED2;
  uint8_t LED3;
} memory_block_t;
```

Then we can create a memory pool in our application code:

```c
mpool = osMemoryPoolNew(16, sizeof(message_t),&memorypoolAttr_mpool);
```

Now we can allocate a memory pool slot within a thread:

```c
memory_block_t *led_data;
*led_data = (memory_block_t *) osMemoryPoolAlloc(mPool,osWaitForever);
```

and then populate it with data:

```c
    led_data->LED0 = 0;
    led_data->LED1 = 1;
    led_data->LED2 = 2;
    led_data->LED3 = 3;
```

It is then possible to place the pointer to the memory block in a message queue:

```c
osMessagePut(Q_LED,(uint32_t)led_data,osWaitForever);
```

The data can now be accessed by another task:

```c
osEvent event;
memory_block_t *received;
event = osMessageGet(Q_LED, osWatiForever);
*received = (memory_block *)event.value.p;
led_on(received->LED0);
```

Once the data in the memory block has been used, the block must be released back to the memory pool for reuse.

```c
osPoolFree(led_pool,received);
```

To create a zero copy mail box system, we can combine a memory pool to store the data with a message queue which is used to
transfer a pointer o the allocated memory pool slot. This way the message data stays static and we pass a pointer between
threads.

#### Exercise 18 - Zero Copy Mailbox

Open [Pack Installer](https://developer.arm.com/documentation/101407/latest/Creating-Applications/Software-Components/Pack-Installer):

- Use the **Search** box on the **Boards** tab to look for the **CMSIS_RTOS2_Tutorial (V2.1)** "board".
- On the **Examples** tab, copy **Ex 18 Zero Copy Mailbox** to your PC and start Keil MDK.
- In the project folder, you will find a file called "Instructions.pdf" that explains the setup and the steps you need to take to successfully finish the exercise.
