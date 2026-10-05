---
id: "alp-visualizing-ethos-u-performance-7-configure-fvp-gui-configure-the-fvp-for-gui-outp"
type: "concept"
domain: "edge-ai"
title: "Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs: Enable GUI and deploy a model on Corstone-320 FVP: Configure the FVP for GUI output"
summary: "Edit the following parameters in your locally checked out executorch/backends/arm/scripts/run_fvp.sh file, to enable the Mobilenet V2 output on the FVP's GUI:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/7-configure-fvp-gui.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/visualizing-ethos-u-performance/7-configure-fvp-gui/#configure-the-fvp-for-gui-output"
license: "CC-BY-SA-4.0"
mode: "V"
---

Edit the following parameters in your locally checked out [executorch/backends/arm/scripts/run_fvp.sh](https://github.com/pytorch/executorch/blob/d5fe5faadb8a46375d925b18827493cd65ec84ce/backends/arm/scripts/run_fvp.sh#L97-L102) file, to enable the Mobilenet V2 output on the FVP's GUI:

```bash
-C mps4_board.subsystem.ethosu.num_macs=${num_macs} \
-C mps4_board.visualisation.disable-visualisation=1 \
-C vis_hdlcd.disable_visualisation=1                \
-C mps4_board.telnetterminal0.start_telnet=0        \
-C mps4_board.uart0.out_file='-'                    \
-C mps4_board.uart0.shutdown_on_eot=1               \
```

- Change `mps4_board.visualisation.disable-visualisation` to equal `0`
- Change `vis_hdlcd.disable_visualisation` to equal `0`
- Enter a `--display-ip` parameter and set it to your computer's IP address

```bash
-C mps4_board.subsystem.ethosu.num_macs=${num_macs} \
-C mps4_board.visualisation.disable-visualisation=0 \
-C vis_hdlcd.disable_visualisation=0                \
-C mps4_board.telnetterminal0.start_telnet=0        \
-C mps4_board.uart0.out_file='-'                    \
-C mps4_board.uart0.shutdown_on_eot=1               \
--display-ip <YOUR_IP_ADDRESS>                   \
```
