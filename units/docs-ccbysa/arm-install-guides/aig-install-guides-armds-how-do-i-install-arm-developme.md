---
id: "aig-install-guides-armds-how-do-i-install-arm-developme"
type: "concept"
domain: "project"
title: "Arm Development Studio: How do I install Arm Development Studio?"
summary: "To use the installation wizard, run armds-2026.0-1-win-x86_64.msi to open the Arm Development Studio setup wizard, then follow the on-screen instructions."
status: "draft"
collection: "arm-install-guides"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/install-guides/armds.md"
doc_source: "https://learn.arm.com/install-guides/armds/#how-do-i-install-arm-development-studio"
license: "CC-BY-SA-4.0"
mode: "V"
---

### How do I install on Windows?

Unzip the downloaded `.zip` file.

To use the installation wizard, run `armds-2026.0-1-win-x86_64.msi` to open the Arm Development Studio setup wizard, then follow the on-screen instructions.

To install silently from the command line, open a command prompt with administrative privileges and run `msiexec` on the `.msi` file:
```command
msiexec /i armds-2026.0-1-win-x86_64.msi EULA=1 SKIP_DRIVERS=1 /qn
```
**Drivers:**
This command does not install the debug probe USB drivers. If these are needed, remove `SKIP_DRIVERS=1` from the command. This requires manual interaction. You can also install them later by running `<install_dir>\sw\driver_files\driver_install.bat`.


Full installation instructions are provided in the [Arm Development Studio Getting Started Guide](https://developer.arm.com/documentation/101469/).
* [Install Arm Development Studio on Windows using the command line](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Install-Arm-Development-Studio-on-Windows-using-the-command-line)
* [Install Arm Development Studio on Windows using the installation wizard](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Install-Arm-Development-Studio-on-Windows-using-the-installation-wizard)

### How do I install on Linux?

The Linux installer is a single self-extracting `.sh` script. Make it executable and run it, following the on-screen instructions:

```command
chmod +x armds-2026.0-1-lin-x86_64.sh
./armds-2026.0-1-lin-x86_64.sh
```

To install silently from the command line, use a command similar to the following:

```command
./armds-2026.0-1-lin-x86_64.sh --i-agree-to-the-contained-eula --no-interactive -f -q
```

By default, the installer requires a post-install step that needs root privileges to install USB drivers for DSTREAM debug hardware. If you don't have root access, or don't need the drivers, add `--skip-post-install`. You can run the post-install step later as root:

```command
sudo <install_directory>/run_post_install_for_Arm_Development_Studio_2026.0-1.sh
```

**Libraries:**
The installer runs a dependency check and lists any missing Linux libraries. Install these before using Arm Development Studio. The `dependency_check_linux-x86_64.sh` script in `<install_directory>/sw/dependency_check` identifies the required libraries. For more information, see [Additional Linux libraries](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Additional-Linux-libraries).


Full installation instructions are provided in the Linux section of the [Arm Development Studio Getting Started Guide](https://developer.arm.com/documentation/101469/latest/Installing-and-configuring-Arm-Development-Studio/Installing-on-Linux).
