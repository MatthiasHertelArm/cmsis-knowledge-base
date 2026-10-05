---
id: "alp-deploy-ml-model-to-npu-with-topo-deploy-reserve-memory-in-the-device-t"
type: "concept"
domain: "edge-ai"
title: "Deploy a machine learning application to the Arm Ethos-U65 NPU on NXP FRDM i.MX 93 with Topo: Clone and deploy the application with Topo: Reserve memory in the "
summary: "The web application and Cortex-M33 firmware exchange data through reserved physical memory. The target device tree must reserve memory for the model/input buffer and for the Ethos-U65."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/deploy.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-ml-model-to-npu-with-topo/deploy/#reserve-memory-in-the-device-tree"
license: "CC-BY-SA-4.0"
mode: "V"
---

The web application and Cortex-M33 firmware exchange data through reserved physical memory. The target device tree must reserve memory for the model/input buffer and for the Ethos-U65. This prevents Linux from allocating memory that the firmware and Ethos-U65 need to access by physical address. 

You'll now modify the device tree and reboot the target so that these modifications take effect. 

**Warning:**
Back up the board's original device tree before modifying it. The exact boot partition can differ between Linux images, so check the paths on your board before copying files.


On your host, create a working directory and dump the live device tree from the target:

```bash
mkdir -p devicetree
ssh <user>@<target-ip> 'cat /sys/firmware/fdt' > devicetree/live.dtb
dtc -I dtb -O dts -o devicetree/live.dts devicetree/live.dtb
```

Open `devicetree/live.dts` in a text editor of your choice. Then, under `remoteproc-cm33`, add the CM33 power domain if it's not already present:

```dts
power-domains = <0x61>;
```

Under `reserved-memory`, add the model memory range:

```dts
model@c0000000 {
    reg = <0x00 0xc0000000 0x00 0x400000>;
    no-map;
};
```

Update the Ethos-U reserved-memory node so it's reserved and not reusable:

```dts
ethosu_region@A8000000 {
    compatible = "shared-dma-pool";
    reg = <0x00 0xa8000000 0x00 0x8000000>;
    no-map;
    phandle = <0x60>;
};
```

Add `iomem=relaxed` to `chosen.bootargs`. For example:

```dts
bootargs = "clk-imx93.mcore_booted console=ttyLP0,115200 earlycon root=/dev/mmcblk1p2 rootwait rw iomem=relaxed";
```

Return to your host machine terminal and build the patched device tree:

```bash
dtc -I dts -O dtb -o devicetree/patched.dtb devicetree/live.dts
```

Copy it to the board:

```bash
scp devicetree/patched.dtb <user>@<target-ip>:/tmp/patched.dtb
```

Install it on the board. Adjust the boot partition path if your image uses a different location:

```bash
ssh <user>@<target-ip>
cp /run/media/boot-mmcblk1p1/imx93-11x11-frdm.dtb \
   /run/media/boot-mmcblk1p1/imx93-11x11-frdm.dtb.bak
cp /tmp/patched.dtb \
   /run/media/boot-mmcblk1p1/imx93-11x11-frdm.dtb
sync
reboot
```

After the board reboots, run the Topo health check again from the host and verify everything is still correct:

```bash
topo health --target <user>@<target-ip>
```
