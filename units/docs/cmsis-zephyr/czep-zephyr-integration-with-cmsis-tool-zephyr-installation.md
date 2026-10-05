---
id: "czep-zephyr-integration-with-cmsis-tool-zephyr-installation"
type: "concept"
domain: "project"
title: "Zephyr Integration with CMSIS-Toolbox: Zephyr installation"
summary: "The following instructions apply to Linux, macOS, and Windows. Install a supported version of Python 3 and Git before continuing."
status: "draft"
collection: "cmsis-zephyr"
source: "Arm-Examples/CMSIS-Zephyr@ef8713c:README.md"
doc_source: "https://github.com/Arm-Examples/CMSIS-Zephyr/blob/ef8713c/README.md#zephyr-installation"
license: "Apache-2.0"
mode: "V"
---

The following instructions apply to Linux, macOS, and Windows. Install a supported version of Python 3 and Git before
continuing.

> [!WARNING]
> On Windows, use Python 3.13 or earlier because the `windows-curses` package is not yet available for Python 3.14.

### Create the workspace

- Open a terminal as a regular user. On Windows, use `cmd.exe` for the commands below.

- In any suitable working directory, create a `zephyrproject` directory and change into it:

  ```console
  mkdir zephyrproject
  cd zephyrproject
  ```

- Create a virtual environment. Use the command for your operating system:

  Linux and macOS:

  ```sh
  python3 -m venv .venv
  ```

  Windows:

  ```bat
  python -m venv .venv
  ```

- Activate the virtual environment.

  Linux and macOS:

  ```sh
  source .venv/bin/activate
  ```

  Windows (`cmd.exe`):

  ```bat
  .venv\Scripts\activate.bat
  ```

  Once activated, the shell prompt is prefixed with `(.venv)`. Activate the environment again whenever you open a
  new terminal. Run `deactivate` to leave it.

- Install `west`. After activation, `python` refers to the virtual environment on every supported operating system:

  ```console
  python -m pip install west
  ```

- Get the upstream Zephyr source code and its modules:

  ```console
  west init -m https://github.com/zephyrproject-rtos/zephyr.git
  west update
  ```

- Install the Python dependencies required by Zephyr:

  ```console
  python -m pip install -r zephyr/scripts/requirements.txt
  ```

### Configure VS Code

The CMSIS Solution extension needs the Zephyr workspace and virtual environment paths when it runs `west`.

1. In VS Code, open **Settings** and search for **Cmsis-Csolution: Environment Variables**.
2. Select the **User** or **Workspace** setting and choose **Add Item** for each variable below. Replace `<work-dir>`
   with the directory in which you created your `zephyrproject` workspace.

   | Variable | Linux and macOS | Windows |
   |---|---|---|
   | `ZEPHYR_BASE` | `/<work-dir>/zephyrproject/zephyr` | `C:\<work-dir>\zephyrproject\zephyr` |
   | `PATH` | `/<work-dir>/zephyrproject/.venv/bin` | `C:\<work-dir>\zephyrproject\.venv\Scripts` |
   | `VIRTUAL_ENV` | `/<work-dir>/zephyrproject/.venv` | `C:\<work-dir>\zephyrproject\.venv` |

3. Fully restart VS Code so that the extension uses the new environment.

For more information, see [Work with Zephyr applications](https://mdk-packs.github.io/vscode-cmsis-solution-docs/zephyr.html#set-environment-variables).
