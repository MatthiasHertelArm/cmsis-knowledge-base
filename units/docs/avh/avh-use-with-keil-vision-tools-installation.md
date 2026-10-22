---
id: "avh-use-with-keil-vision-tools-installation"
type: "concept"
domain: "test"
title: "Use with Keil µVision: Tools Installation"
summary: "Use with Keil µVision: Tools Installation"
status: "draft"
collection: "avh"
source: "ARM-software/AVH@60f78be:DoxyGen/infrastructure/src/avh_mdk_uv4.md"
doc_source: "https://github.com/ARM-software/AVH/blob/60f78be/DoxyGen/infrastructure/src/avh_mdk_uv4.md#tools-installation"
license: "Apache-2.0"
mode: "V"
---

- [Download and install Keil MDK µVision](https://developer.arm.com/documentation/101407/latest/About-uVision/Installation)
  on your Windows PC, if not present yet.
- Ensure that a user-based license is activated either for the [MDK-Community](https://www.keil.arm.com/mdk-community)
  (evaluation and non-commercial use) or [MDK-Professional](https://www.keil.arm.com/keil-mdk/#mdk-v6-editions)
  (commercial use) editions. This is required for running Arm FVP models.
- [*Optional*] Enable Telnet Client on Windows 10. This will allow to observe UART output from the AVH device during
  debug.
    - Open **Start > Settings**.
    - In the search box, type **Turn Windows features on or off** and click on the suggested item. The
      **Windows Features** dialog opens.
    - Select the **Telnet Client** check box and click **OK**. The installation might take several minutes to complete.

(figure: Enable Windows Telnet Client)
