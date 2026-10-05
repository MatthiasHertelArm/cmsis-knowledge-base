---
id: "intr-device-firmware-update-cookbook-boot-stability"
type: "concept"
domain: "debug"
title: "Device Firmware Update Cookbook: Design Patterns & Recipes / Boot Stability"
summary: "An especially terrible way to brick a device is to go into a boot loop. It goes like this: a new update has a deadly bug, and crashes shortly upon boot. Your device then enters a loop."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-06-23-device-firmware-update-cookbook.md"
doc_source: "https://interrupt.memfault.com/blog/device-firmware-update-cookbook#boot-stability"
license: "CC-BY-SA-4.0"
mode: "V"
---

_Part of: Design Patterns & Recipes_

An especially terrible way to brick a device is to go into a boot loop. It goes
like this: a new update has a deadly bug, and crashes shortly upon boot. Your
device then enters a loop. It starts, goes into the loader, then the
application, then crashes. Again, and again, and again.

To avoid boot-looping, I recommend using a boot counter which gets incremented
on every boot and cleared once the application is deemed "stable". Once the
counter reaches a certain threshold, the Loader stops loading the Application
and instead goes into DFU mode.

How might we implement this? With our shared memory region! Let's add a boot
counter to it, and implement some getters/setters:

```c
// shared_memory.c
typedef struct __attribute__((packed)) {
    uint32_t magic;
    uint32_t flags;
    uint8_t boot_counter;
} shared_memory_t;

void shared_memory_increment_boot_counter(void) {
    shared_memory.boot_counter++;
}

void shared_memory_clear_boot_counter(void) {
    shared_memory.boot_counter = 0;
}

uint8_t shared_memory_get_boot_counter(void) {
    return shared_memory.boot_counter;
}
```

Before it starts the app, the Loader checks the counter and skips loading the
app if the counter exceeds a threshold:

```c
const int max_boot_attempts = 3;
if (shared_memory_get_boot_counter() >= max_boot_attempts) {
    shared_memory_clear_boot_counter();
    printf("App unstable, dropping back into DFU mode\n");
    break;
}
```

Otherwise, it increments the counter and starts the application.

```c
printf("Booting slot 2\n");
shared_memory_increment_boot_counter();
image_start(hdr);
```

Last but not least, the Application must clear the counter once it believes it
is stable. When might that be? That depends on your application. One option is
to set a timer and mark the app as stable after it has been running for a few
minutes. Another option is to wait until it has managed to connect to a gateway
or the cloud. Whatever you do, the main requirement is that the Application can
receive an instruction to boot into DFU mode, so that we can bail out if it
turns out there is another bug lurking.

In my example, I simply created a firmware shell command which marks the app as
stable:

```c
int cli_command_mark_stable(int argc, char *argv[]) {
    shell_put_line("Marking app as stable");
    shared_memory_clear_boot_counter();
    return 0;
}
```
