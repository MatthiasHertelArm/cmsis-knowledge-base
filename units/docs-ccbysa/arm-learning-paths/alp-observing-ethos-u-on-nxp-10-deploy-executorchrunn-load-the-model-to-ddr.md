---
id: "alp-observing-ethos-u-on-nxp-10-deploy-executorchrunn-load-the-model-to-ddr"
type: "concept"
domain: "edge-ai"
title: "Deploy ExecuTorch firmware on NXP FRDM i.MX 93 for Ethos-U65 acceleration: Deploy and test on FRDM-IMX93: Load the model to DDR"
summary: "The executor_runner firmware reads the .pte model from DDR at address 0xC0000000. Write the model into DDR using /dev/mem:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/observing-ethos-u-on-nxp/10-deploy-executorchrunner-nxp-board/#load-the-model-to-ddr"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `executor_runner` firmware reads the `.pte` model from DDR at address `0xC0000000`. Write the model into DDR using `/dev/mem`:

```bash { command_line="root@frdm-imx93" output_lines="8" }
python3 -c "
import mmap, os
pte = open('/tmp/mobilenetv2_u65.pte', 'rb').read()
fd = os.open('/dev/mem', os.O_RDWR | os.O_SYNC)
m = mmap.mmap(fd, len(pte), mmap.MAP_SHARED, mmap.PROT_WRITE, offset=0xC0000000)
m.write(pte)
m.close()
os.close(fd)
print(f'Wrote {len(pte)} bytes to 0xC0000000')
"
Wrote 3507872 bytes to 0xC0000000
```

**Note:**
You can also load the model via U-Boot if the `.pte` file is on the SD card's first partition. At the U-Boot prompt, run `fatload mmc 0:1 0xc0000000 mobilenetv2_u65.pte` followed by `boot`. The model remains in DDR across Linux boot because the region is marked `no-map`.
