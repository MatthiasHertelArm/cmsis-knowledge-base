---
id: "alp-avh-matter-2setup-optional-connect-via-ssh"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Prepare AVH instances of Raspberry Pi 4: (Optional) Connect via SSH"
summary: "The Console view within the browser is sufficient to complete this Learning Path."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/2setup.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/2setup/#optional-connect-via-ssh"
license: "CC-BY-SA-4.0"
mode: "V"
---

The `Console` view within the browser is sufficient to complete this Learning Path.

If you wish to connect via `SSH` (rather than `Console`), it's easiest to follow the SSH tunnel connection instructions specified in the `Connect` tab. 

As an alternative, you can also download and install the appropriate [OpenVPN Community](https://openvpn.net/community/) version for your host. Click on `DOWNLOAD OVPN FILE` within the `Connect via VPN` section.

In the `OpenVPN` GUI, select `Import` > `Import file...` and browse to the downloaded `OVPN file`. Click `Connect`.

On your host, open terminal(s), and connect to the virtual hardware instance(s) with the command shown in the `Connect` tab, or use your preferred terminal application.
