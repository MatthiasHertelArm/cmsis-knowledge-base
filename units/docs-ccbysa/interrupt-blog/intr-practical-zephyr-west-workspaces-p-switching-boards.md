---
id: "intr-practical-zephyr-west-workspaces-p-switching-boards"
type: "concept"
domain: "debug"
title: "Practical Zephyr - West workspaces (Part 6): Switching boards"
summary: "With our workspace set up and our knowledge about Zephyr's imports, we're ready to add support for the STM32 Nucleo-64 development board. The first thing we need is an overlay file to specify the /chosen LED node:"
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2024-05-16-practical_zephyr_west.md"
doc_source: "https://interrupt.memfault.com/blog/practical_zephyr_west#switching-boards"
license: "CC-BY-SA-4.0"
mode: "V"
---

With our workspace set up and our knowledge about Zephyr's imports, we're ready to add support for the [STM32 Nucleo-64 development board](https://www.st.com/en/evaluation-tools/nucleo-f411re.html). The first thing we need is an overlay file to specify the `/chosen` LED node:

`app/boards/nucleo_f411re.overlay`

```dts
/ {
    chosen {
        app-led = &green_led_2;
    };
};
```

Knowing that we're still missing the STM32 HAL, we can look it up in Zephyr's `west.yml` file:

```bash
$ grep stm32 deps/zephyr/west.yml -A 2 --ignore-case
    - name: hal_stm32
      revision: 286dd285b5bb4fddafdfff27b5405264e5a61bfe
      path: modules/hal/stm32
      groups:
        - hal
```

The STM32 HAL is part of the project `hal_stm32`, which we can now add to our allow-list in the manifest file:

`app/west.yml`

```yaml
manifest:
  version: 1.2

  self:
    path: app

  projects:
    - name: zephyr
      revision: v4.3.0
      url: https://github.com/zephyrproject-rtos/zephyr
      import:
        path-prefix: deps
        name-allowlist:
          - cmsis
          - cmsis_6
          - hal_nordic
          - hal_stm32 # <-- added STM32 HAL
```

Running `west update`, _West_ populates the `stm32` HAL in the expected folder `deps/modules/hal/stm32`:

```bash
$ west update
$ tree --dirsfirst -a -L 5
.
├── .west
│   └── config
├── app
└── deps
    ├── modules
    │   └── hal
    │       ├── cmsis
    │       ├── nordic
    │       └── stm32
    └── zephyr  [43 entries exceeds filelimit, not opening dir]
```

Building the application for the STM32 development kit now succeeds as expected:

```bash
$ west build --no-sysbuild --board nucleo_f411re app --pristine
...

[159/159] Linking C executable zephyr/zephyr.elf
Memory region         Used Size  Region Size  %age Used
           FLASH:       18726 B       512 KB      3.57%
             RAM:        4352 B       128 KB      3.32%
        IDT_LIST:          0 GB         2 KB      0.00%
```

Connecting the development kit to my computer, I should now be able to program the application, right? Let's try:

```bash
$ west flash
-- west flash: rebuilding
ninja: no work to do.
-- west flash: using runner openocd
FATAL ERROR: required program openocd not found; install it or add its location to PATH
```

Oh, the STM32 development kit uses a different _runner_ than the nRF52840 development kit: Nordic's development kits use `jlink`, whereas this development kit uses `openocd`.

Thus, you don't only need the host tools and Zephyr SDK for your target, but also all other supporting tools, such as Nordic's command line tools or in this case `openocd`. On my computer, a simple `brew install open-ocd` fixes this problem, and I'm able to flash the application to the device.

In a more serious setup, your entire toolchain should be maintained in a much better way, but - as promised - I won't try to tell how you should do that - it's entirely up to you.
