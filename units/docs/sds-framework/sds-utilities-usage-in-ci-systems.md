---
id: "sds-utilities-usage-in-ci-systems"
type: "concept"
domain: "test"
title: "Utilities: SDSIO-Server / Usage in CI Systems"
summary: "The SDSIO-Server can be used in CI systems. When combined with the pyOCD Debugger fully automated HIL tests can be configured."
status: "draft"
collection: "sds-framework"
source: "ARM-software/SDS-Framework@4459441:documentation/utilities.md"
doc_source: "https://github.com/ARM-software/SDS-Framework/blob/4459441/documentation/utilities.md#usage-in-ci-systems"
license: "Apache-2.0"
mode: "V"
---

_Part of: SDSIO-Server_

The SDSIO-Server can be used in CI systems. When combined with the [pyOCD Debugger](https://open-cmsis-pack.github.io/cmsis-toolbox/pyOCD-Debugger/) fully automated HIL tests can be configured.

When `sdsio-server` runs with `--playback --exit-after-playback`, playback completion requests CI termination by setting `SDS_FLAG_TERMINATE` in the flags sent to the target. If the target application writes EOT (`0x04`) to standard output retargeted through a pyOCD-managed channel, such as semihosting or RTT stdio, pyOCD can detect it when started with `--eot` and exit. If standard output is retargeted directly to UART, pyOCD does not see that character, so `--eot` will not terminate pyOCD. Keep `--timelimit` as a fallback in case the target application does not reach the termination state or EOT is not routed through pyOCD.

This example contains the relevant steps in a GitHub workflow:

```
      - name: Flash using pyOCD
        working-directory: ./RockPaperScissors/AppKit-E8_USB/out
        run: |
          pyocd load --uid L96807771A --cbuild-run SDS+AppKit-E8-U85.cbuild-run.yml

      - name: Run using pyOCD
        working-directory: ./RockPaperScissors/AppKit-E8_USB/out
        run: |
          nohup pyocd run --uid L96807771A --cbuild-run SDS+AppKit-E8-U85.cbuild-run.yml --timelimit 30 --eot > pyocd.out 2>&1 &

      - name: Start the SDSIO server on the Raspberry Pi
        working-directory: ./RockPaperScissors/AppKit-E8_USB
        run: |
          sleep 2 # Delay to ensure that pyOCD is started
          sdsio-server --control SDS.sdsio.yml --playback --exit-after-playback --no-progress-info | tee sdsio-server.log

      - name: Wait for pyocd to complete
        run: |
          while pgrep pyocd > /dev/null; do
            sleep 1
          done
```

See also: 

- [Setup Self-Hosted GitHub Runner on Raspberry Pi 5](https://github.com/Arm-Examples/.github/blob/main/profile/RPI_GH_Runner.md) explains the configuration of a Linux host system for HIL testing.
- [github.com/Arm-Examples/ModelNova/.github/workflows/Run_RPS_AppKit-E8.yml](https://github.com/Arm-Examples/ModelNova/blob/main/.github/workflows/Run_RPS_AppKit-E8.yml) for a complete CI test workflow.
