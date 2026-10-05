---
id: "intr-a-simple-scheduler-via-an-interrup-the-concept"
type: "concept"
domain: "debug"
title: "A Simple Scheduler via an Interrupt-driven Actor Model: The Concept"
summary: "The classic actor model describes an actor as a message handler, similar to an interrupt handler. When handling messages, the actor may:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2023-09-13-hardware-actor-scheduler.md"
doc_source: "https://interrupt.memfault.com/blog/hardware-actor-scheduler#the-concept"
license: "CC-BY-SA-4.0"
mode: "V"
---

The classic actor model describes an actor as a message handler, similar to an interrupt handler. When handling messages, the actor may:

- create new actors
- send messages to other actors
- read/write its local state

Actors use messages and queues to communicate. Since the interrupt controller has no such functionality, it should be implemented in software. So, there are only three types of software objects: queues, actors, and messages.

Despite the actor and its mailbox being tightly coupled in classic models, it is less practical than relying on separate queues. The latter case is more flexible. Depending on the message being processed, an actor may choose which queue to poll. Here, it is assumed that the actor may only have one message, and it has to poll some queue every time it finishes handling the current message.

All available interrupt vectors are divided into two classes: those producing and consuming messages. Interrupts designated to peripheral devices are expected to post messages to queues that, in turn, have subscribed actors.

Let's implement the simplest 'blinky' application with one actor who handles messages from systick interrupt and controls onboard LED. The whole source of the example for the STM32 Bluepill board may be found [here](https://github.com/memfault/interrupt/blob/master/example/hw-actors). The messages must be sent from systick interrupt to the actor controlling the LED. Therefore, the message payload is the next LED state:

```c
struct example_msg_t {
    struct message_t header;    /* Any message must have the header */
    unsigned int led_state;     /* Payload */
};
```

The systick interrupt handler may be written as follows:

```c
void SysTick_Handler(void) {
    static unsigned int led_state = 0;
    led_state ^= 1;
    struct example_msg_t* const msg = message_alloc(&g_pool);   /* Allocate new message */

    if (msg) {
        msg->led_state = led_state;                             /* Set message payload */
        queue_push(&g_queue, &msg->header);                     /* Send to the queue */
    }
}
```

Interrupt handlers that are dedicated to actors contain only a call to the function, examining a list of active actors with priority corresponding to that vector:

```c
void USB_LP_CAN1_RX0_IRQHandler(void) {     /* Unused vector that is reused for actor execution */
    context_schedule(EXAMPLE_VECTOR);
}
```

At startup, each actor subscribes to a queue. Once the message arrives in that queue, the actor is activated. Actor activation means it gets a pointer to the message, and its state is changed to 'ready' so the scheduler can choose it on the next scheduling call. As each actor is permitted to subscribe to only one queue, the subscription may be implemented as a return value, wherein the actor must provide a valid pointer to the queue to which it wishes to subscribe. The values an actor returns may change over time but must always be a valid queue.

```c
static struct queue_t* actor(struct actor_t* self, struct message_t* m) {
    const struct example_msg_t* const msg = (struct example_msg_t*) m;

    if (msg->led_state == 0)            /* Set LED according to message payload */
        GPIOC->BSRR = GPIO_BSRR_BR13;   /* LED off */
    else
        GPIOC->BSRR = GPIO_BSRR_BS13;   /* LED on */

    message_free(m);                    /* Return the message to the pool */
    return &g_queue;
}
```

Queues can have both messages and actors. If someone writes a message in an empty queue, it will stay there until someone asks for it. If an actor tries to get a message from an empty queue it will be saved as a subscriber, and later, when a message comes in, it goes into the actor's mailbox. It is, therefore, possible for a queue to contain either messages or actors but never both. Notably, the queue is merely a head of a linked list, lacking internal buffers, thereby preventing any possibility of queue overflow.

For simplicity, messages are fixed-sized. A message allocator is just a pool of fixed-sized memory chunks. When a message pointer gets to an actor, it is assumed that the message type is known to the actor because it knows what queue it polls.
The system is also inherently asynchronous and even applicable to multiprocessor systems since (in the case of GIC) you may also trigger interrupts on other CPUs.
