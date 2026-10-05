---
id: "intr-mcuboot-walkthrough-and-porting-gu-mcuboot-configuration-options"
type: "concept"
domain: "debug"
title: "MCUboot Walkthrough and Porting Guide: MCUboot Configuration Options"
summary: "MCUboot has many configuration options which are controlled byMCUBOOT defines added to a configuration header. The best documentation for the options available that I could find was the Kconfig wrapper in the port for the Zephyr RTOS."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2020-11-04-mcuboot-overview.md"
doc_source: "https://interrupt.memfault.com/blog/mcuboot-overview#mcuboot-configuration-options"
license: "CC-BY-SA-4.0"
mode: "V"
---

MCUboot has many configuration options which are controlled by`MCUBOOT_` defines added to a configuration header. The best documentation for the options available that I could find was the [Kconfig](https://github.com/mcu-tools/MCUboot/blob/master/boot/zephyr/Kconfig) wrapper in the port for the Zephyr RTOS.
While a full discussion of configuration options is outside the scope of this article, there are a
few that are particularly interesting and deserve a brief overview.

### Upgrade Strategies

For upgrades, MCUboot uses the following nomenclature:
* `images` - The individual firmware binaries that run on a system. For a typical setup, there will
  be one application image but MCUboot also has some initial support for managing multiple images
  as well. (For example, when using a Cortex-M33 with ARM Trustzone enabled, you may want to have a "Secure" Image and "Non-Secure" Image.)
* `slots` - Every image can be saved in a "primary" slot or "secondary" slot. The "primary" slot is where the binary executes from. The "secondary" slot is where an image is staged prior to being installed.

MCUboot has a number of ways "upgrades" from the "secondary" to "primary" slot can take place:

#### Overwrite Mode

* `MCUBOOT_OVERWRITE_ONLY`: When an update is requested in this mode, the contents of the primary slot are erased and the contents of the secondary slot are copied into the primary slot.

#### Swap Mode

Several of the upgrade strategies MCUboot offers swap the primary and secondary images. If the new
image installed is not working well, one can then revert to the image that was installed before the
upgrade.

* `MCUBOOT_SWAP_USING_MOVE`: This strategy relies on an extra sector of space being in the primary "slot". For this strategy, the bootloader will shift the entire firmware binary in the primary slot up by one sector and then "swap" the sectors between the secondary and primary slots.

* `MCUBOOT_SWAP_USING_SCRATCH`: This relies on allocating a "scratch" flash region. Sectors are temporarily stashed in the scratch region while the primary & secondary slots are being swapped. If the scratch area is small, there can be a lot of wear on the internal flash because every single sector gets copied in here during the swap.

The benefit of the swap approach is the ability to roll back a buggy firmware to a previous
version. The disadvantage of the strategy is it adds a lot of complexity to the bootloader system
and can wear down the flash faster due to the heavier writing. It also means any firmware installed
needs to support downgrades.

> Idea: An alternative and simpler recovery mechanism could be to use `MCUBOOT_OVERWRITE_ONLY` and store a
> "recovery" image elsewhere on flash. If an upgrade is buggy and needs to be reverted, the
> recovery image  could then be copied into the secondary slot and installed from there.

### Crypto Backends

MCUboot does not implement its own cryptographic libraries (thank goodness). Instead, it expects you
to link an existing implementation. There are default ports available for [Tinycrypt](https://github.com/intel/tinycrypt) and [Mbed TLS](https://github.com/ARMmbed/mbedtls) which can be enabled using the `MCUBOOT_USE_TINYCRYPT` and `MCUBOOT_USE_MBED_TLS` flags, respectively.

If a hardware accelerator is available, a port can be implemented to take advantage of that as well. There is already an implementation present for the NRF platform crypto engine which can be enabled with `MCUBOOT_USE_CC310`.

The `MCUBOOT_VALIDATE_PRIMARY_SLOT` flag controls whether or not images are validated on each
boot. The default (and recommended) setting is to validate on every boot. If your image is large or your MCUs clock is slow, a hardware crypto accelerator will likely have a noticeable difference on your boot time.

> For an initial port, I'd recommend starting with one of the software crypto libraries, measuring
> what the boot and upgrade times look like, and making a decision about whether or not the
> hardware accelerator is needed from those results.
