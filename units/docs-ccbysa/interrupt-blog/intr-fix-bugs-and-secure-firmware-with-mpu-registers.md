---
id: "intr-fix-bugs-and-secure-firmware-with-mpu-registers"
type: "concept"
domain: "debug"
title: "Fix Bugs and Secure Firmware with the MPU: MPU registers"
summary: "The MPU is configured using just five registers! A great way to build an understanding for how the unit works is to read the descriptions for these registers."
status: "draft"
collection: "interrupt-blog"
source: "memfault/interrupt@89a49b4:_posts/2019-07-16-fix-bugs-and-secure-firmware-with-the-mpu.md"
doc_source: "https://interrupt.memfault.com/blog/fix-bugs-and-secure-firmware-with-the-mpu#mpu-registers"
license: "CC-BY-SA-4.0"
mode: "V"
---

The MPU is configured using just five registers! A great way to build an understanding for how the unit works is to read the descriptions for these registers. They are well-documented in the _Register support for PMSAv7 in the SCS_ section of the [ARMv7-M reference manual](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf). Let's walk through the highlights here, go over typical configurations and discuss common mistakes made.

### MPU Type Register

`MPU_TYPE` - Address 0xE000ED90 register bit assignments:


This register is present regardless of whether or not the MPU was implemented on the _Cortex-M_ device being used. This is pretty nice because it allows us to dynamically determine at runtime or via a [GDB Python script](https://interrupt.memfault.com/blog/automate-debugging-with-gdb-python-api) whether or not an MPU is present and use it. The **only** field of interest here is `DREGION` which reveals the number of MPU regions which were implemented. A value of 0 for `DREGION` indicates the MPU was not implemented.

### MPU Control Register

`MPU_CTRL` - Address 0xE000ED94 register bit assignments:


This register is how we actually enable the MPU. Until the `ENABLE` bit is set, the MPU configuration in other registers have no effect.

`PRIVDEFENA` controls whether or not code running in _Privileged_ thread mode can access the default memory map. If the bit is set to 0, _any_ access not explicitly enabled via the MPU will result in a fault when the `ENABLE` bit is set. In a typical configuration using the MPU, this bit will be set to `1`.

`HFNMIENA` controls whether or not the MPU is active when running from fault handlers. Since most fault handler implementations end in a reboot, I usually leave this bit set to `0` so that it's easier to collect a full coredump of the memory state at the time of crash. This can greatly facilitate offline debug of why the issue which triggered the Memory Management Fault happened in the first place!

### MPU Region Number Register

`MPU_RNR` - Address 0xE000ED98 register bit assignments:


As we saw in the `MPU_TYPE` register above, the MPU is broken into a certain number of configurable-regions. The _M0+_, _M3_ & _M4_ can support up to 8 regions when the MPU is implemented and the M7 can support up to 16! The `REGION` field is used to select the active region we want to read or update. Once the region is selected, we can read or write `MPU_RBAR` & `MPU_RASR` to see the configuration and make changes.

**Caution** It's worth mentioning that there is a priority scheme to these regions. If the same memory range is covered in multiple MPU regions, the configuration in the **highest** `REGION` number will be applied. So for example, if `REGION 0` turns off access to the first _32kB_ of RAM for _Unprivileged_ mode but `REGION 1` makes the same RAM region read-only, `REGION 1` settings will take precedence. This means code running in _Unprivileged_ mode **will** be able to read the memory.

**Note** The default memory map enabled with the `PRIVDEFENA` mentioned above has a priority of `-1` and so it will be overridden by any configurations made in these regions.

### MPU Region Base Address Register

`MPU_RBAR` Address 0xE000ED9C register bit assignments:


This register is used to control the starting address (aka the _base address_) that we want to cover with the region selected in `MPU_RNR`. For example, if we wanted to protect the address range starting at the beginning of a SRAM range (i.e `0x20000000`) using `REGION 0`, we would first set `MPU_RNR` to 0 and then set `MPU_RBAR` to `0x20000000`)

To reduce the number of writes needed to change the configuration, the `VALID` bit can be set to `1` and the `REGION` field can be set to change the value of `MPU_RNR` and apply the write to a different region. For example, if we wanted to set `REGION 7` to have a base address of `0x20000000`, we could write `0x20000000 | 0x1 << 4 | 0x7 == 0x20000017` to `MPU_RBAR`. If we then read `MPU_RNR`, we would see its value is now `0x7`.

**Caution** You may have noticed the address only occupies 27 bits and the bottom 5 bits were repurposed. What if we want to protect an address that starts with a base of `0x20000002`? You can't! The minimum region size is implementation defined but is usually 32 bytes. The actual size supported can usually be looked up in the reference manual for the specific MCU being used. Alternatively, it can also be dynamically determined by writing `0xFFFFFFE0` to `MPU_RBAR` and reading the value back. The number of trailing zeros will reveal the minimum supported alignment and consequently the minimum region size. For example, reading a value of `0xFFFFFF80` would reveal bits 5 and 6 can't be set so the minimum size supported is `2^7` (128) bytes.

{:.no_toc}

### MPU Region Attribute and Size Register

`MPU_RASR` - Address 0xE000EDA0 register bit assignments:


This is the register where nearly all of the MPU configuration magic actually happens. The `ENABLE` bit controls whether or not the region is active (when the MPU itself has been enabled by setting the `ENABLE` bit in `MPU_CTRL`).

The configuration can be broken down into four main parts:

{:.no_toc}

#### 1. Memory Type, Cacheability & Shareability

This config is comprised of the `TEX` (_Type Extension Mask_), `C` (_Cacheable_), `B` (_Bufferable_), & `S` (_Shareable_) fields. More details about each memory attribute can be found in the _Summary of ARMv7 memory attributes_ of the [ARMv7-M reference manual](https://static.docs.arm.com/ddi0403/eb/DDI0403E_B_armv7m_arm.pdf). Typically, these settings do not matter much for a single core _Cortex-M_ implementation. I usually follow the recommendations in the table below from [here](http://infocenter.arm.com/help/index.jsp?topic=/com.arm.doc.dui0552a/BABDJJGF.html):



If you are using a more complex _Cortex-M_ setup (like a _Cortex-M7_ with a cache), the vendor data sheet may have a section with better recommendations.

{:.no_toc}

#### 2. Access permissions & Execute Never encoding

This part is comprised of the `AP` (_Access Permissions_) fields used to control the rules around how the region can be accessed:


There is also the `XN` (_Execute Never_) field, used to control whether or not the processor can fetch instructions from this region. If the `XN` bit is set, an instruction fetch from the region will cause a fault.

**Caution** Even if the `XN` bit is not set, a fault could still occur on instruction fetch if read access is disabled in the `AP` config for the region we are trying to fetch an instruction from.

{:.no_toc}

#### 3. Region Size

Indicates the size the region spans over, where the size is `2 ^ (SIZE field + 1)`. The start is the address provided as the base address in `MPU_RBAR`. So for example if the base address is `0x20000000` and the `SIZE` field is `0b10000 == 16`, the MPU region will cover `0x20000000` to `0x20000000 + 2^(16+1) = 0x20020000`.

**Caution**: The `SIZE` selected here **must** be aligned with the base address provided in `MPU_RBAR`. Otherwise, you will wind up covering a region that is different than expected since the base `ADDR` is always _naturally aligned_ with the `SIZE`. For example, if we had set `ADDR` above to `0x20001000`, the same region will still wind up being covered because `0x1000` would be masked out under the hood!

{:.no_toc}

#### 4. Sub-Region Disable

The `SRD` (_Sub-Region Disable_) field is a bitmask that lets you turn off the MPU region for _1/8 units_ of the region selected. The `SIZE` of the region must be greater than _256 bytes_ for this to have any effect.

For a complex embedded device, it's easy to start to run low or out of available MPU Regions. This field provides a clever way to cover more things. For example, imagine you want to protect the first and last _32kB_ blocks of a _256kB RAM_ the same way. You could enable a MPU region that covers all _256kB_ but set the `SRD` field to `0x7e` so only the first and last _1/8_ blocks (each _32kB_) in the MPU region are active.

### MPU Alias Register Support

Up to this point, the registers we have described are the same for the _ARMv6-M_ & _ARMv7-M_ MPU implementations. The _ARMv7-M_ re-aliases the `MPU_RBAR` & `MPU_RASR` registers 3 times in a sequential address range. While not necessary to use, this can be useful for initialization because you can create a configuration array that is 32 bytes and then program four regions at once with just a stream of word writes.
