# Quellenliste

Stand 04.10.2026. Das lebende Original ist das Claude Doc "CDA Wissensbasis: Quellenliste". Bei Abweichungen gilt das Doc.

Modus: V = Volltext indizieren (offene Lizenz). S = eigene Summary plus Link. R = nur Referenz.
Mit * markierte Links ließen sich nicht automatisch prüfen (Bot-Sperre). Arm-eigene Dokumente stehen vorsichtig auf S, intern vermutlich auf V hebbar.

## 1. CMSIS und Open-CMSIS-Pack

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [Open-CMSIS-Pack Spezifikation](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/index.html) | PDSC-Format, Komponenten, Bedingungen | Apache-2.0 | V |
| [Debug Description](https://open-cmsis-pack.github.io/Open-CMSIS-Pack-Spec/main/html/debug_description.html) | Debug-Sequenzen, debugvars, Trace-Setup | Apache-2.0 | V |
| [SVD Spezifikation](https://open-cmsis-pack.github.io/svd-spec/main/index.html) | Peripherie-Register-Beschreibung | Apache-2.0 | V |
| [CMSIS-Toolbox Doku](https://open-cmsis-pack.github.io/cmsis-toolbox/) | csolution, cbuild, cpackget | Apache-2.0 | V |
| [YML Input Format](https://open-cmsis-pack.github.io/cmsis-toolbox/YML-Input-Format/) | Alle Knoten von csolution, cproject, clayer | Apache-2.0 | V |
| [Build Overview](https://open-cmsis-pack.github.io/cmsis-toolbox/build-overview/), [Build Operation](https://open-cmsis-pack.github.io/cmsis-toolbox/build-operation/) | Ablauf, Kontexte, Linker-Skript-Management | Apache-2.0 | V |
| [Reference Applications](https://open-cmsis-pack.github.io/cmsis-toolbox/ReferenceApplications/) | Layer, Connections, Board-Layer | Apache-2.0 | V |
| [Create Applications](https://open-cmsis-pack.github.io/cmsis-toolbox/CreateApplications/) | Projektaufbau | Apache-2.0 | V |
| [Pack Tools](https://open-cmsis-pack.github.io/cmsis-toolbox/pack-tools/) | packchk, svdconv | Apache-2.0 | V |
| [devtools](https://github.com/Open-CMSIS-Pack/devtools) | Quelltext der Tools, Fehlermeldungen im Original | Apache-2.0 | V |
| [csolution-examples](https://github.com/Open-CMSIS-Pack/csolution-examples) | Musterprojekte | Apache-2.0, BSD-3 | V |
| [gen-pack](https://github.com/Open-CMSIS-Pack/gen-pack) | Pack-Erstellung | Apache-2.0 | V |
| [cmsis-skills](https://github.com/Open-CMSIS-Pack/cmsis-skills) | Die 24 bestehenden Skills | Apache-2.0 | V |
| [vscode-get-started](https://github.com/Open-CMSIS-Pack/vscode-get-started) | VS Code Setup, vcpkg | Apache-2.0 | V |
| [CMSIS Solution Extension](https://github.com/Open-CMSIS-Pack/vscode-cmsis-solution), [Doku](https://mdk-packs.github.io/vscode-cmsis-solution-docs/) | Bedienung, Tasks, Einstellungen | Apache-2.0 | V |
| [CMSIS Debugger Extension](https://github.com/Open-CMSIS-Pack/vscode-cmsis-debugger) | launch.json, Adapter | Apache-2.0, GPL-3.0 Anteile | V |
| [vcpkg-ce-registry](https://github.com/Open-CMSIS-Pack/vcpkg-ce-registry), [vcpkg Doku](https://learn.microsoft.com/en-us/vcpkg/) | Tool-Versionen, reproduzierbare Umgebung | Apache-2.0 (Registry) | V / S |
| [CMSIS 6 Doku](https://arm-software.github.io/CMSIS_6/latest/General/index.html) | Core, Driver, RTOS2 APIs | Apache-2.0 | V |
| [CMSIS-Compiler](https://github.com/ARM-software/CMSIS-Compiler) | Retargeting von stdio und File I/O | Apache-2.0 | V |
| [CMSIS-Driver](https://github.com/ARM-software/CMSIS-Driver) | Treiber-Implementierungen | Apache-2.0 | V |
| [CMSIS-Stream](https://github.com/ARM-software/CMSIS-Stream) | Datenfluss-Graphen | Apache-2.0 | V |
| [keil.arm.com Packs](https://www.keil.arm.com/packs/), [Boards](https://www.keil.arm.com/boards/), [Devices](https://www.keil.arm.com/devices/) | Katalog für Device- und Board-Auflösung | | S |

## 2. RTOS-Kernel

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [CMSIS-RTOS2 API](https://arm-software.github.io/CMSIS_6/latest/RTOS2/index.html) | Gemeinsame API, Thread- und ISR-Regeln | Apache-2.0 | V |
| [CMSIS-RTX Doku](https://arm-software.github.io/CMSIS-RTX/latest/index.html), [Repo](https://github.com/ARM-software/CMSIS-RTX) | Scheduler, Konfiguration, Stack-Überwachung | Apache-2.0 | V |
| [CMSIS-RTOS2 Validation](https://github.com/ARM-software/CMSIS-RTOS2_Validation) | Testfälle als Verhaltensreferenz | Apache-2.0 | V |
| [FreeRTOS Kernel Doku](https://www.freertos.org/Documentation/00-Overview) | Tasks, Queues, Tickless, Konfiguration | | S |
| [FreeRTOS-Kernel](https://github.com/FreeRTOS/FreeRTOS-Kernel) | Quelltext, Ports für Cortex-M | MIT | V |
| [FreeRTOS Kernel Book](https://github.com/FreeRTOS/FreeRTOS-Kernel-Book) | Lehrbuch zum Kernel | MIT-0 und weitere | V nach Prüfung |
| [CMSIS-FreeRTOS](https://github.com/ARM-software/CMSIS-FreeRTOS), [Doku](https://arm-software.github.io/CMSIS-FreeRTOS/latest/index.html) | RTOS2-Wrapper, Pack-Integration | | V nach Prüfung |
| [Zephyr Kernel Services](https://docs.zephyrproject.org/latest/kernel/index.html) | Threads, Scheduling, Speicher, Timing | Apache-2.0 (Repo) | V |
| [Zephyr Gesamtdoku](https://docs.zephyrproject.org/latest/) | Devicetree, Kconfig, west | Apache-2.0 (Repo) | V |
| [CMSIS-Zephyr](https://github.com/Arm-Examples/CMSIS-Zephyr) | Zephyr in csolution-Projekten | Apache-2.0 | V |
| [ThreadX](https://github.com/eclipse-threadx/threadx), [rtos-docs](https://github.com/eclipse-threadx/rtos-docs) | Kernel, User Guide | MIT | V |
| [NuttX](https://github.com/apache/nuttx) | POSIX-naher Kernel, als Vergleich | | S |

## 3. Fehlerkatalog und Troubleshooting

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [devtools Quelltext](https://github.com/Open-CMSIS-Pack/devtools) | Meldungstexte von csolution und packchk | Apache-2.0 | V |
| [cmsis-toolbox Issues](https://github.com/Open-CMSIS-Pack/cmsis-toolbox/issues) | Reale Fehlerbilder mit Auflösung | Nutzerbeiträge | S |
| [devtools Issues](https://github.com/Open-CMSIS-Pack/devtools/issues) | Wie oben, toolnäher | Nutzerbeiträge | S |
| [pyOCD Issues](https://github.com/pyocd/pyOCD/issues), [Doku](https://pyocd.io/docs/) | Verbindungs- und Flash-Fehler | Apache-2.0 (Repo) | V / S |
| [Arm Compiler Errors and Warnings Reference Guide (100074)](https://developer.arm.com/documentation/100074/latest/) * | armlink, armasm, fromelf Meldungen | Arm | S |
| [Keil Knowledgebase](https://www.keil.com/support/knowledgebase.asp) * | KBAs zu MDK, Debug, Flash. Interner Export nötig | Arm | S |
| [Keil Forum](https://community.arm.com/support-forums/f/keil-forum) | Nutzerfragen als Symptom-Quelle | Nutzerbeiträge | R |
| [SEGGER Knowledge Base](https://kb.segger.com/Main_Page) | J-Link, RTT, Verbindungsprobleme | SEGGER | S |
| [OpenOCD User Guide](https://openocd.org/doc/html/index.html) | Adapter- und Target-Fehler | GFDL | S |
| [CMSIS-Developer-Assistant](https://github.com/Open-CMSIS-Pack/CMSIS-Developer-Assistant) | Eigene Guides und Troubleshooting | MIT, Apache-2.0 | V |

## 4. Architektur, Speicher, Linker, Fault-Analyse

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [Armv7-M ARM (DDI0403)](https://developer.arm.com/documentation/ddi0403/latest/) * | Exception-Modell, SCB, Fault-Register | Arm | S |
| [Armv8-M ARM (DDI0553)](https://developer.arm.com/documentation/ddi0553/latest/) * | Dazu TrustZone, MPU v8, Helium | Arm | S |
| [AN209 Using Cortex-M Fault Exceptions (KAN209)](https://developer.arm.com/documentation/kan209/latest/) * | HardFault-Analyse | Arm | S |
| [CMSIS-Core Doku](https://arm-software.github.io/CMSIS_6/latest/Core/index.html) | Startup, Systemregister, MPU, Cache | Apache-2.0 | V |
| [AAPCS und ABI (abi-aa)](https://github.com/ARM-software/abi-aa) | Aufrufkonvention, Stack-Layout | siehe Repo | S |
| [armlink User Guide (100070)](https://developer.arm.com/documentation/100070/latest/) * | Scatter-Files, Map-File | Arm | S |
| [GNU ld Manual](https://sourceware.org/binutils/docs/ld/) * | Linker-Skripte für GCC | GFDL | S |
| [Arm C/C++ Libraries User Guide (100073)](https://developer.arm.com/documentation/100073/latest/) * | Heap, Stack, Retargeting, Microlib | Arm | S |
| [Interrupt: HardFault Debug](https://interrupt.memfault.com/blog/cortex-m-hardfault-debug) | Praxisrezept Fault-Dekodierung | siehe Repo | S |
| [Interrupt Blog](https://interrupt.memfault.com/), [Repo](https://github.com/memfault/interrupt) | Linker-Skripte, Boot, Watchdog, Codegröße | siehe Repo | S |

## 5. Toolchains und Optimierung

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [Arm Compiler for Embedded User Guide (100748)](https://developer.arm.com/documentation/100748/latest/) * | Optimierungsstufen, LTO, Codegröße | Arm | S |
| [armclang Reference Guide (100067)](https://developer.arm.com/documentation/100067/latest/) * | Optionen, Pragmas, Attribute | Arm | S |
| [Migration and Compatibility Guide (100068)](https://developer.arm.com/documentation/100068/latest/) * | AC5 nach AC6 | Arm | S |
| [Arm Toolchain for Embedded](https://github.com/arm/arm-toolchain) | LLVM-basierte Toolchain | siehe Repo | S |
| [LLVM Embedded Toolchain for Arm](https://github.com/ARM-software/LLVM-embedded-toolchain-for-Arm) | Vorgänger, Multilib, picolibc | siehe Repo | S |
| [GCC ARM Options](https://gcc.gnu.org/onlinedocs/gcc/ARM-Options.html) | mcpu, mfpu, mfloat-abi | GFDL | S |
| [GCC Optimize Options](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html) * | O-Stufen, LTO, Sections | GFDL | S |
| [Arm GNU Toolchain](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads) * | Release Notes | Arm | R |
| [CMSIS-DSP Doku](https://arm-software.github.io/CMSIS-DSP/latest/index.html), [Repo](https://github.com/ARM-software/CMSIS-DSP) | Helium- und Neon-Varianten | Apache-2.0 | V |
| [CMSIS-NN Doku](https://arm-software.github.io/CMSIS-NN/latest/index.html), [Repo](https://github.com/ARM-software/CMSIS-NN) | Optimierte Kernel je Core | Apache-2.0 | V |
| [llvm-size](https://llvm.org/docs/CommandGuide/llvm-size.html) | Größenanalyse | Apache-2.0 mit LLVM-Ausnahme | S |
| [clangd](https://clangd.llvm.org/) | Code-Navigation | Apache-2.0 mit LLVM-Ausnahme | S |
| [Arm Learning Paths: Embedded](https://learn.arm.com/learning-paths/embedded-and-microcontrollers/), [Repo](https://github.com/ArmDeveloperEcosystem/arm-learning-paths) | 70 Pfade, u. a. uvprojx-Konvertierung, CMSIS v6 Migration, RTX, TF-M, Zephyr, Ethos-U. Frontmatter mit learning_objectives, prerequisites, generierten FAQs (ai_review_required) | Text CC BY-SA 4.0, Code MIT-0 | V, getrennt halten |

## 6. Test, Simulation, CI

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [Unity](https://github.com/ThrowTheSwitch/Unity) | Unit-Tests für C | MIT | V |
| [CMock](https://github.com/ThrowTheSwitch/CMock) | Mocks | MIT | V |
| [CppUTest](https://github.com/cpputest/cpputest) | Unit-Tests für C und C++ | BSD-3 | V |
| [GoogleTest](https://google.github.io/googletest/) | Host-seitige Tests | BSD-3 | V |
| [Arm Virtual Hardware](https://github.com/ARM-software/AVH), [Doku](https://arm-software.github.io/AVH/main/overview/html/index.html) | FVP-Modelle, VIO, VSI | Apache-2.0 | V |
| [Hello_AVH](https://github.com/Arm-Examples/Hello_AVH) | FVP in CI | Apache-2.0 | V |
| [cmsis-actions](https://github.com/ARM-software/cmsis-actions) | GitHub Actions für vcpkg und Lizenz | Apache-2.0 | V |
| [CMSIS-Driver Validation](https://github.com/ARM-software/CMSIS-Driver_Validation) | Treibertests auf Hardware | Apache-2.0 | V |
| [SDS-Framework](https://github.com/ARM-software/SDS-Framework), [Doku](https://arm-software.github.io/SDS-Framework/main/index.html) | Sensordaten aufzeichnen und wiedergeben | Apache-2.0 | V |
| [Zephyr Twister](https://docs.zephyrproject.org/latest/develop/test/twister.html) | Testlauf über Boards und Emulation | Apache-2.0 (Repo) | V |
| [GitHub Actions Doku](https://docs.github.com/en/actions) | Workflows, Matrix, Caching | CC-BY-4.0 | S |
| [gcov](https://gcc.gnu.org/onlinedocs/gcc/Gcov.html) * | Coverage mit GCC | GFDL | S |

## 7. Boot, Update, Security

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [MCUboot Doku](https://docs.mcuboot.com/), [Repo](https://github.com/mcu-tools/mcuboot) | Bootloader, Image-Format, Swap | Apache-2.0 | V |
| [Trusted Firmware-M Doku](https://trustedfirmware-m.readthedocs.io/en/latest/), [Repo](https://github.com/TrustedFirmware-M/trusted-firmware-m) | Secure Partitions, Isolation | BSD-3 | V |
| [PSA Certified APIs](https://arm-software.github.io/psa-api/), [Repo](https://github.com/ARM-software/psa-api) | Crypto, Storage, Attestation, Firmware Update | siehe Repo | S |
| [Mbed TLS Doku](https://mbed-tls.readthedocs.io/en/latest/), [Repo](https://github.com/Mbed-TLS/mbedtls) | TLS und Crypto | siehe Repo | S |
| [TrustZone für Armv8-M (100690)](https://developer.arm.com/documentation/100690/latest/) * | Secure und Non-secure, SAU | Arm | S |
| [PSA Certified](https://www.psacertified.org/) | Zertifizierungsstufen | | R |
| [Cyber Resilience Act (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) | Pflichten für Produkte mit digitalen Elementen | EU | V |
| [CycloneDX](https://cyclonedx.org/specification/overview/) | SBOM-Format | Apache-2.0 | V |
| [SPDX](https://spdx.dev/use/specifications/) | SBOM-Format, Lizenz-IDs | siehe Seite | S |
| [OpenSSF Scorecard](https://github.com/ossf/scorecard) | Prüfregeln für Repo-Sicherheit | Apache-2.0 | S |

## 8. Debug, Trace, Profiling

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [Arm Debug Interface v5 (IHI0031)](https://developer.arm.com/documentation/ihi0031/latest/) * | DP, AP, SWD, Dormant State | Arm | S |
| [CoreSight Architecture Specification (IHI0029)](https://developer.arm.com/documentation/ihi0029/latest/) * | ROM-Tabellen, Topologie | Arm | S |
| [ETMv4 Architecture Specification (IHI0064)](https://developer.arm.com/documentation/ihi0064/latest/) * | Instruction Trace | Arm | S |
| [pyOCD Doku](https://pyocd.io/docs/), [Repo](https://github.com/pyocd/pyOCD) | Probe-Handling, Target-Support | Apache-2.0 | V |
| [GDB Manual](https://sourceware.org/gdb/current/onlinedocs/gdb.html/) | Kommandos, GDB/MI | GFDL | S |
| [Debug Adapter Protocol](https://microsoft.github.io/debug-adapter-protocol/) | Protokoll hinter VS Code Debugging | siehe Seite | S |
| [CMSIS-View](https://arm-software.github.io/CMSIS-View/latest/index.html), [Repo](https://github.com/ARM-software/CMSIS-View) | Event Recorder, Component Viewer, Fault | Apache-2.0 | V |
| [Cortex-Debug](https://github.com/Marus/cortex-debug) | Alternative, Konfig-Muster | MIT | V |
| [SEGGER RTT](https://wiki.segger.com/RTT) | Target-Ausgabe ohne SWO | SEGGER | S |
| [SEGGER SystemView](https://www.segger.com/products/development-tools/systemview/) | RTOS-Trace | SEGGER | R |
| [Orbuculum](https://github.com/orbcode/orbuculum) | SWO und ETM dekodieren | siehe Repo | S |

## 9. Edge AI

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [ExecuTorch Doku](https://docs.pytorch.org/executorch/stable/index.html), [Repo](https://github.com/pytorch/executorch) | Export, Runtime, Memory Planning | BSD | V |
| [ExecuTorch Arm Backend](https://github.com/pytorch/executorch/tree/main/backends/arm), [Beispiele](https://github.com/pytorch/executorch/tree/main/examples/arm) | TOSA-Lowering, Ethos-U Delegate | BSD | V |
| [LiteRT for Microcontrollers](https://ai.google.dev/edge/litert/microcontrollers/overview), [tflite-micro](https://github.com/tensorflow/tflite-micro) | Interpreter, Arena, Operator-Resolver | Apache-2.0 (Repo) | V |
| Vela: [PyPI](https://pypi.org/project/ethos-u-vela/), [Repo](https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela) | Compiler-Optionen, Operator-Support | Apache-2.0 | V |
| [ML Embedded Evaluation Kit](https://gitlab.arm.com/artificial-intelligence/ethos-u/ml-embedded-evaluation-kit) | Referenz-Anwendungen für Ethos-U | Apache-2.0 | V |
| [TOSA](https://www.mlplatform.org/tosa/) | Operator-Spezifikation | siehe Seite | S |
| [ML-zoo](https://github.com/ARM-software/ML-zoo) | Quantisierte Referenzmodelle | Apache-2.0, Modelle einzeln prüfen | S |
| [ML-examples](https://github.com/ARM-software/ML-examples) | Beispielprojekte | Apache-2.0 | V |
| [Alif Semiconductor GitHub](https://github.com/alifsemi) | DFP, Beispiele | je Repo | S |

## 10. Coding-Standards und Safety

Normtexte nie übernehmen, nur Regelnummern und eigene Erklärungen.

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [MISRA C und C++](https://misra.org.uk/) | Regelwerk | kostenpflichtig | R |
| [SEI CERT C](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard) | Security-Regeln mit Beispielen | siehe Seite | S |
| [Barr Embedded C Coding Standard](https://barrgroup.com/embedded-systems/books/embedded-c-coding-standard) | Stilregeln | Barr Group | S |
| [Zephyr Coding Guidelines](https://docs.zephyrproject.org/latest/contribute/coding_guidelines/index.html) | MISRA-basierte Regeln | Apache-2.0 (Repo) | V |
| [Keil MDK FuSa Run-Time System](https://developer.arm.com/Tools%20and%20Software/Keil%20MDK/FuSa%20Run-Time%20System) * | Zertifizierte RTX-, Core- und Lib-Varianten | Arm | S |
| [Safety-Example-STM32](https://github.com/Arm-Examples/Safety-Example-STM32) | Referenzprojekt mit FuSa RTS | Apache-2.0 | V |
| [clang-tidy](https://clang.llvm.org/extra/clang-tidy/) | Checks | Apache-2.0 mit LLVM-Ausnahme | S |
| [Cppcheck](https://cppcheck.sourceforge.io/) * | Statische Analyse | GPL-3.0 | S |
| [Linux Kernel MAINTAINERS Prozess](https://www.kernel.org/doc/html/latest/process/maintainers.html) | Vorbild für Owner je Domäne | GPL-2.0 | R |
| IEC 61508, ISO 26262, IEC 62304 | Safety-Normen | kostenpflichtig | R |

## 11. Hersteller

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [STMicroelectronics](https://github.com/STMicroelectronics) | STM32Cube HAL, CMSIS-Device | gemischt, teils restriktiv | S |
| [NXP MCUXpresso SDK](https://github.com/nxp-mcuxpresso) | Treiber, Middleware | BSD-3 (mcuxsdk-core) | V nach Prüfung |
| [Alif Semiconductor](https://github.com/alifsemi) | Ensemble DFP, Treiber | je Repo | S |
| [Infineon](https://github.com/Infineon) | ModusToolbox, PDL, HAL | je Repo | S |
| [Nordic nRF Connect SDK](https://github.com/nrfconnect/sdk-nrf), [Doku](https://docs.nordicsemi.com/) * | Zephyr-basiertes SDK | siehe Repo | S |
| [Renesas FSP](https://github.com/renesas/fsp) | Software Package für RA | siehe Repo | S |
| [Microchip MPLAB Harmony](https://github.com/Microchip-MPLAB-Harmony) | Treiber, Middleware | je Repo | S |
| [Raspberry Pi Pico SDK](https://github.com/raspberrypi/pico-sdk) | RP2040, RP2350 | BSD-3 | V |
| [Analog Devices MSDK](https://github.com/analogdevicesinc/msdk) | MAX32, MAX78 | Apache-2.0 | V |
| Datenblätter, Reference Manuals, Errata | Über book-Einträge im PDSC, bereits im Pack-Docs-System | Hersteller | S |

## 12. Community, Blogs, Bücher

| Quelle | Liefert | Lizenz | Modus |
|---|---|---|---|
| [Interrupt (Memfault)](https://interrupt.memfault.com/) | Fault-Analyse, Linker, Boot, Update | siehe Repo | S |
| [Embedded Artistry](https://embeddedartistry.com/) | Architektur, Build-Systeme | Autor | S |
| [Beningo Embedded Group](https://www.beningo.com/) | RTOS-Design, Prozesse | Autor | S |
| [MCU on Eclipse](https://mcuoneclipse.com/) | Debug-Probes, SWO, FreeRTOS | Autor | S |
| [Arm-Examples](https://github.com/Arm-Examples) | Referenzprojekte im csolution-Format | je Repo | V |
| Joseph Yiu: Definitive Guide to Arm Cortex-M | Architektur | Buch | R |
| Trevor Martin: Designer's Guide to the Cortex-M Processor Family | CMSIS, RTX, Debug | Buch | R |
| James Grenning: Test-Driven Development for Embedded C | TDD | Buch | R |
| Elecia White: Making Embedded Systems | Design-Patterns | Buch | R |
| Jacob Beningo: Embedded Software Design | Architektur, Prozess | Buch | R |
| Pete Warden, Daniel Situnayake: TinyML | ML auf Mikrocontrollern | Buch | R |

## Reihenfolge der Ingestion

1. Abschnitt 1 komplett. Daraus entsteht der Entity-Graph.
2. Meldungstexte aus devtools extrahieren, mit Issue-Trackern zum Fehlerkatalog verbinden.
3. cmsis-skills über skill2ku.py als Procedures übernehmen.
4. RTOS: erst CMSIS-RTOS2 und RTX, dann FreeRTOS, Zephyr, ThreadX.
5. Arm Learning Paths (offen, strukturiert). Parallel Rechte für Keil Knowledge Base, AN209, Compiler-Guides klären.
6. Test und CI, dann Edge AI.
7. Hersteller-Wissen über die Packs der Vendoren einsammeln.
8. Blogs und Bücher nur als references anhängen.
