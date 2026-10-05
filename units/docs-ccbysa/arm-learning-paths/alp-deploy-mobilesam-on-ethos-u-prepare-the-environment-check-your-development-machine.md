---
id: "alp-deploy-mobilesam-on-ethos-u-prepare-the-environment-check-your-development-machine"
type: "concept"
domain: "edge-ai"
title: "Run MobileSAM prompt segmentation on Arm Ethos-U85 with ExecuTorch: Prepare the ExecuTorch and Arm environment: Check your development machine"
summary: "Run the following preflight check before downloading the source:"
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/deploy-mobilesam-on-ethos-u/prepare-the-environment/#check-your-development-machine"
license: "CC-BY-SA-4.0"
mode: "V"
---

Run the following preflight check before downloading the source:

```bash
case "$(uname -s)/$(uname -m)" in
  Linux/x86_64|Linux/aarch64|Linux/arm64|Darwin/arm64)
    echo "Supported host: $(uname -s)/$(uname -m)"
    ;;
  *)
    echo "Unsupported host: $(uname -s)/$(uname -m)" >&2
    exit 1
    ;;
esac

for tool in python3.12 git cmake c++; do
  command -v "$tool" >/dev/null || {
    echo "Missing required tool: $tool" >&2
    exit 1
  }
done

python3.12 - <<'PY' || exit 1
import platform
import sys

if sys.platform == "darwin":
    version = platform.mac_ver()[0]
    if not version or int(version.split(".")[0]) < 15:
        raise SystemExit(f"macOS 15 or later is required; found {version or 'unknown'}.")
elif sys.platform.startswith("linux"):
    libc, version = platform.libc_ver()
    if libc != "glibc" or tuple(map(int, version.split(".")[:2])) < (2, 28):
        raise SystemExit(
            f"Linux with glibc 2.28 or later is required; found {libc} {version}."
        )
PY

if ! command -v ninja >/dev/null && ! command -v make >/dev/null; then
  echo "Install Ninja or Make before continuing." >&2
  exit 1
fi

python3.12 --version
git --version
cmake --version | head -n 1
c++ --version | head -n 1
```

The check confirms that you are using a supported Linux host or Apple silicon Mac. It also checks for the availability of the following:

- Python 3.12
- Git
- CMake
- A host C++ compiler
- Ninja or Make

The Python export dependencies require macOS 15 or later on Apple silicon, or glibc 2.28 or later on Linux. The pinned [TOSA tools](https://pypi.org/project/tosa-tools/2026.5.0/#files) set the macOS minimum, and the [PyTorch wheels](https://pypi.org/project/torch/2.14.0/#files) require the Linux glibc version. The preflight check verifies these requirements before you install the dependencies.
