# Wissensdomänen

## Priorität 1: in Pack Docs gar nicht enthalten

| Domäne | Inhalt |
|---|---|
| RTOS-Kernel | Scheduling, Priority Inversion, Stack-Dimensionierung, ISR-Regeln, Tickless, Mapping CMSIS-RTOS2 auf RTX, FreeRTOS, Zephyr, ThreadX |
| Fehlerkatalog | Meldungen von csolution, cbuild, Linker, Compiler, pyOCD mit Ursache und Fix. Troubleshooting-Knoten mit symptoms |
| Speicher und Linker | Scatter-Files, Linker-Skripte, Map-File-Analyse, Stack/Heap, MPU, TCM, Cache |
| Fault-Analyse | HardFault-Decode, CFSR, Stack Overflow, Watchdog |

## Priorität 2: die von Matthias genannten Domänen

| Domäne | Inhalt |
|---|---|
| Optimierung | Flags je Toolchain, LTO, Codegröße, Helium, CMSIS-DSP/NN, Low Power |
| Test | Host vs. Target, Unity, FVP/AVH, HIL, Coverage, CI |
| Projektverwaltung | Layer, Reference Applications, Pack-Versionierung, reproduzierbare Builds, vcpkg |

## Priorität 3: ergänzend

| Domäne | Inhalt |
|---|---|
| Boot und Update | Startup-Code, Clock Tree, Bootloader, MCUboot |
| Security | TrustZone-M, TF-M, PSA, Secure Boot, SBOM und CRA |
| Migration | uVision nach csolution, AC5 nach AC6, GCC gegenüber armclang |
| Trace und Profiling | SWO, ETM, Event Recorder, PMU |
| Treiber-Patterns | CMSIS-Driver, DMA, Interrupt-Design, typische Bus-Fallen |
| Edge AI | Vela, Operator-Support, Arena-Größe, Quantisierung |
| Coding-Standards | MISRA, FuSa RTS, statische Analyse |
| Device-Errata | je Hersteller, im jeweiligen DFP mitgeliefert |
