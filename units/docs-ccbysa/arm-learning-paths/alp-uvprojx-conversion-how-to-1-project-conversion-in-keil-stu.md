---
id: "alp-uvprojx-conversion-how-to-1-project-conversion-in-keil-stu"
type: "concept"
domain: "project"
title: "Convert uvprojx-based projects to csolution: Using Keil Studio: Project conversion in Keil Studio"
summary: "2. Click on the CMSIS icon in the Activity Bar to open the CMSIS View. At the top, click on the hammer icon to build the project:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/uvprojx-conversion/how-to-1.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/uvprojx-conversion/how-to-1/#project-conversion-in-keil-studio"
license: "CC-BY-SA-4.0"
mode: "V"
---

1. In VS Code, go to **File - Open Folder** and select the folder containing the uvprojx file (here `Blinky.uvprojx`).

1. Once the folder is open in VS Code, right-click the uvprojx file and select **Convert µVision project to csolution**:

   (figure: Convert project)

1. The following files (and more) are generated:
   - `Blinky.csolution.yaml`
   - `Blinky.cproject.yaml`
   - `vcpkg-configuration.json`

1. The **Output** window shows a successful conversion:

   (figure: Successful conversion)

1. The vcpkg configuration file is automatically activated. You notice a couple of "Arm Tools" available in the
   **Status Bar** at the bottom:

   (figure: vcpkg activated)

2. Click on the **CMSIS** icon in the **Activity Bar** to open the **CMSIS View**. At the top, click on the hammer icon to
   build the project:

   (figure: CMSIS build)

3. The `cbuild` task starts. A successful project build will end with:

   ```output
   Program size: Code=... RO-data=... RW-data=... ZI-data=...
   info cbuild: build finished successfully!
   Build complete
   ```

**Note:**
For more information, refer to the [Arm Keil Studio user's guide](https://mdk-packs.github.io/vscode-cmsis-solution-docs/importuv.html).
