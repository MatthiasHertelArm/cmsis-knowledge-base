---
id: "zep-install-linux-host-dependencies"
type: "concept"
domain: "project"
title: "Install Linux Host Dependencies"
summary: "Documentation is available for these Linux distributions:"
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@76280bc:doc/develop/getting_started/installation_linux.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/76280bc/doc/develop/getting_started/installation_linux.rst"
license: "Apache-2.0"
mode: "V"
---

Documentation is available for these Linux distributions:

* Ubuntu
* Fedora
* Clear Linux
* Arch Linux

For distributions that are not based on rolling releases, some of the
requirements and dependencies may not be met by your package manager. In that
case please follow the additional instructions that are provided to find
software from sources other than the package manager.


**Note:** If you're working behind a corporate firewall, you'll likely need to configure a proxy for accessing the internet, if you haven't done so already.  While some tools use the environment variables `http_proxy` and `https_proxy` to get their proxy settings, some use their own configuration files, most notably `apt` and `git`.
