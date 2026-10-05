---
id: "mlek-troubleshooting-error-with-python-environment"
type: "concept"
domain: "edge-ai"
title: "Troubleshooting: Error with Python environment"
summary: "If trying to build and you encounter an error similar to the following:"
status: "draft"
collection: "mlek"
source: "artificial-intelligence/ethos-u/ml-embedded-evaluation-kit@3cd3772:docs/sections/troubleshooting.md"
doc_source: "https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/troubleshooting.md#error-with-python-environment"
license: "Apache-2.0"
mode: "V"
---

If trying to build and you encounter an error similar to the following:

```log
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: ['/home/test/ml-embedded-evaluation-kit/resources_downloaded/env/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']


Traceback (most recent call last):
  File "./build_default.py", line 184, in <module>
    run(
  File "./build_default.py", line 89, in run
    (download_dir, env_path) = set_up_resources(
  File "/home/test/ml-embedded-evaluation-kit/set_up_default_resources.py", line 439, in set_up_resources
    call_command(command)
  File "/home/test/ml-embedded-evaluation-kit/set_up_default_resources.py", line 276, in call_command
    proc.check_returncode()
  File "/usr/lib/python3.8/subprocess.py", line 448, in check_returncode
    raise CalledProcessError(self.returncode, self.args, self.stdout,
subprocess.CalledProcessError: Command 'python3 -m venv env' returned non-zero exit status 1.
```

You can fix this error by installing Python virtual environment and removing the corrupted resources_downloaded folder.

```commandline
rm -r resources_downloaded
```

Follow the instructions to [update Python3 package to a supported version](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit/-/blob/3cd3772/docs/sections/./troubleshooting.md#how-to-update-python3-package-to-a-supported-version)
before attempting a rebuild with:

```commandline
python3 ./build_default.py
```
and the error should be fixed.
