---
id: "rtx-create-an-rtx5-project-component-selection"
type: "concept"
domain: "rtos"
title: "Create an RTX5 Project: Component selection"
summary: "In your IDE, open the Manage software components dialog."
status: "draft"
collection: "cmsis-rtx"
source: "ARM-software/CMSIS-RTX@161e285:Documentation/Doxygen/src/project.md"
doc_source: "https://github.com/ARM-software/CMSIS-RTX/blob/161e285/Documentation/Doxygen/src/project.md#component-selection"
license: "Apache-2.0"
mode: "V"
---

### In the Arm CMSIS Solution extension

In your IDE, open the
[Manage software components](https://mdk-packs.github.io/vscode-cmsis-solution-docs/create_app.html#software-components)
dialog.

1. If you cannot see the **CMSIS:RTOS2 (API):Keil RTX5** component, select to display **All installed packs**.
2. Select the component. Choose to use the **Library** or the **Source** variant.
3. Add the **CMSIS:OS Tick (API):SysTick** component.
4. **Save** the selection.

(figure: Component selection in Arm CMSIS Solution extension)

In the **CMSIS** view, you can add template files to the project:

1. Click on the `+` next to a group.
2. Select **Add From Component Code Template**.
3. Select one of the templates that are shown:

(figure: Add code template)

### In uVision

- In the Manage Run-Time Environment window, select **CMSIS\::CORE**, **CMSIS\::OS Tick (API)\::SysTick** and **CMSIS\::RTOS2 (API)\::Keil RTX5**. You can choose to either add RTX as a library (Variant: **Library**) or to add the full source code (Variant: **Source**) - required if using the [Event Recorder](https://arm-software.github.io/CMSIS-View/latest/evr.html):

(figure: Run-Time Environment for RTX5 in Keil uVision)

- If the **Validation Output** requires other components to be present, try to use the **Resolve** button.
- Click **OK**.
- If using the Variant: **Source** as stated above, you have to assure to use at least C99 compiler mode (Project Options -> C/C++ -> C99 Mode).
- You can add template files to the project by right-clicking on **Source Group 1** and selecting **Add New Item to 'Source Group 1'**. In the new window, click on **User Code Template**. On the right-hand side you will see all available template files for CMSIS-RTOS RTX:

(figure: Adding RTX template files to the project)

- Configure RTX5 to the application's needs using the **%RTX_Config.h** file.

\endif

\if ARMCA
