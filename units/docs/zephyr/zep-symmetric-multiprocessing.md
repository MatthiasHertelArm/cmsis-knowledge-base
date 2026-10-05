---
id: "zep-symmetric-multiprocessing"
type: "concept"
domain: "rtos"
title: "Symmetric Multiprocessing"
summary: "On multiprocessor architectures, Zephyr supports the use of multiple physical CPUs running Zephyr application code. This support is \"symmetric\" in the sense that no specific CPU is treated specially by default."
status: "draft"
collection: "zephyr"
source: "zephyrproject-rtos/zephyr@8f62a4a:doc/kernel/services/smp/smp.rst"
doc_source: "https://github.com/zephyrproject-rtos/zephyr/blob/8f62a4a/doc/kernel/services/smp/smp.rst"
license: "Apache-2.0"
mode: "V"
---

On multiprocessor architectures, Zephyr supports the use of multiple
physical CPUs running Zephyr application code.  This support is
"symmetric" in the sense that no specific CPU is treated specially by
default.  Any processor is capable of running any Zephyr thread, with
access to all standard Zephyr APIs supported.

No special application code needs to be written to take advantage of
this feature.  If there are two Zephyr application threads runnable on
a supported dual processor device, they will both run simultaneously.

SMP configuration is controlled under the `CONFIG_SMP` kconfig
variable.  This must be set to "y" to enable SMP features, otherwise
a uniprocessor kernel will be built.  In general the platform default
will have enabled this anywhere it's supported. When enabled, the
number of physical CPUs available is visible at build time as
`CONFIG_MP_MAX_NUM_CPUS`.  Likewise, the default for this will be the
number of available CPUs on the platform and it is not expected that
typical apps will change it.  But it is legal and supported to set
this to a smaller (but obviously not larger) number for special
purposes (e.g. for testing, or to reserve a physical CPU for running
non-Zephyr code).
