---
id: "zep-getting-started-guide-get-zephyr-and-install-python-dependenci"
type: "concept"
domain: "project"
title: "Getting Started Guide: Get Zephyr and install Python dependencies"
summary: "Next, use west to create a workspace and fetch Zephyr together with its modules."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/develop/getting_started/index.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/develop/getting_started/index.rst"
license: "Apache-2.0"
mode: "V"
---

Next, use west to create a workspace and fetch Zephyr together
with its modules.

These commands use `zephyrproject` as the workspace name; you can choose
another name and location. You will also install Zephyr's Python dependencies in
a Python virtual environment so they stay separate from your system Python
installation.

#. Create a new virtual environment:

#. Activate the virtual environment:

   Once activated your shell will be prefixed with `(.venv)`. The
   virtual environment can be deactivated at any time by running
   `deactivate`.


**Note:** Remember to activate the virtual environment every time you start a new terminal session before working with Zephyr. If you don't, commands such as `west` will not be found, or may run against a different Python environment, leading to confusing errors.

#. Install west:

   West is Zephyr's workspace manager; the next commands use it to create and
   update the workspace.

```shell

pip install west
```
#. Get the Zephyr source code:

   `west init` creates a `west workspace` and clones
   `https://github.com/zephyrproject-rtos/zephyr` as its :term:`manifest
   repository <west manifest repository>`.

   `west update` then fetches the various
   `west projects <west project>` (modules) listed in Zephyr's
   `west manifest` (hardware abstraction layers (HALs), libraries, etc.).


**Tip:** To reduce disk space usage and avoid downloading unnecessary modules or vendor HALs during setup, you may configure west-manifest-groups before running `west update`.

#. Install Zephyr's Python dependencies:

   `west packages` reads the Python requirements from the checked-out Zephyr
   workspace (including its modules), so the installed packages match the Zephyr
   version you fetched.


**Note:** Installing these dependencies can downgrade or upgrade west itself.

#. Export a Zephyr CMake package. This registers your current
   Zephyr checkout in CMake's user package registry so `find_package(Zephyr)`
   can locate it automatically when building applications.

```shell

west zephyr-export
```
