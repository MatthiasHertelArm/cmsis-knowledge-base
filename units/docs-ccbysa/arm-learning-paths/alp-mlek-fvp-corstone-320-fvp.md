---
id: "alp-mlek-fvp-corstone-320-fvp"
type: "concept"
domain: "edge-ai"
title: "Build and run the Arm Machine Learning Evaluation Kit examples: Install Arm Ecosystem FVP: Corstone-320 FVP"
summary: "This section describes installation of the Corstone-320 FVP to run on your local machine. Similar instructions would apply for other platforms."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/mlek/fvp.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/mlek/fvp/#corstone-320-fvp"
license: "CC-BY-SA-4.0"
mode: "V"
---

This section describes installation of the [Corstone-320 FVP](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms/IoT%20FVPs) to run on your local machine. Similar instructions would apply for other platforms.

Arm provides a selection of free to use Ecosystem Fixed Virtual Platforms (FVPs) that can be downloaded from the [Arm Developer](https://developer.arm.com/Tools%20and%20Software/Fixed%20Virtual%20Platforms#Downloads) website.

You can review Arm's full FVP offering and general installation steps in the [Fast Model and Fixed Virtual Platform](https://learn.arm.com/install-guides/fm_fvp/) install guide.

**Note:**
It is recommended to perform these steps in a new terminal window.


Download the Corstone-320 Ecosystem FVP archive:

```bash
cd $HOME
wget https://developer.arm.com/-/cdn-downloads/permalink/FVPs-Corstone-IoT/Corstone-320/FVP_Corstone_SSE-320_11.27_25_Linux64.tgz
```

Unpack it with `tar`, run the installation script, and add the path to the FVP executable to the `PATH` environment variable.

```bash
tar -xf FVP_Corstone_SSE-320_11.27_25_Linux64.tgz

./FVP_Corstone_SSE-320.sh --i-agree-to-the-contained-eula --no-interactive -q

export PATH=$HOME/FVP_Corstone_SSE-320/models/Linux64_GCC-9.3:$PATH
```

The FVP requires an additional dependency, `libpython3.9.so.1.0`, which can be installed using a supplied script.

```bash
source $HOME/FVP_Corstone_SSE-320/scripts/runtime.sh
```

Run the executable:

```bash
FVP_Corstone_SSE-320
```

You will observe output similar to the following:

```output
telnetterminal0: Listening for serial connection on port 5000
telnetterminal1: Listening for serial connection on port 5001
telnetterminal2: Listening for serial connection on port 5002
telnetterminal5: Listening for serial connection on port 5003
```

If you encounter graphics driver errors, you can disable the development board and LCD visualization with additional command options:

```bash
FVP_Corstone_SSE-320	\
	-C mps4_board.visualisation.disable-visualisation=1 \
	-C vis_hdlcd.disable_visualisation=1
```

Stop the executable with `Ctrl+C`.

Now you are ready to run the MLEK applications on the FVP.
