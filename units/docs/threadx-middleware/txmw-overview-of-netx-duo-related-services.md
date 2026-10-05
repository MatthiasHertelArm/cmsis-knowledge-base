---
id: "txmw-overview-of-netx-duo-related-services"
type: "concept"
domain: "rtos"
title: "Overview of NetX Duo: Related services"
summary: "NetX Duo provides the following additional services."
status: "draft"
collection: "threadx-middleware"
source: "eclipse-threadx/rtos-docs@1e36a62:rtos-docs/netx-duo/overview-netx-duo.md"
doc_source: "https://github.com/eclipse-threadx/rtos-docs/blob/1e36a62/rtos-docs/netx-duo/overview-netx-duo.md#related-services"
license: "MIT"
mode: "V"
---

NetX Duo provides the following additional services.

- Azure IoT Middleware
- Microsoft Defender for IoT
- Device update for IoT Hub

### Azure IoT Middleware

NetX Duo includes [Azure IoT Middleware for Eclipse ThreadX](https://github.com/eclipse-threadx/netxduo/blob/master/addons/azure_iot/README.md), a platform-specific library that acts as a binding layer between Eclipse ThreadX and the Azure SDK for Embedded C to facilitate connectivity to Azure IoT services. The goals of Azure IoT Middleware are the following.

- Provide the smart client interfaces (IoTHub_Client, DeviceProvisioning_Client) that developers need for their applications.
- Orchestrate the interaction between the Embedded C SDK and the platform.
- Provide Eclipse ThreadX platform initialization.
- IoT Plug and Play support.
- Security capabilities.
- Resource limitation aware.
- Protocol support.

(figure: NetX Duo Related Services)

### Microsoft Defender for IoT

The Microsoft Defender for IoT security module provides a comprehensive security solution for Eclipse ThreadX devices. The Security Module for Eclipse ThreadX offers malicious network activity detection, custom alert based device behavior baselining, and helps improve device security hygiene. Learn more about the [Security Module for Eclipse ThreadX](https://learn.microsoft.com/azure/defender-for-iot/device-builders/iot-security-azure-rtos) or get started with [Configure Security Module for Eclipse ThreadX](https://learn.microsoft.com/azure/defender-for-iot/device-builders/how-to-azure-rtos-security-module) quickstart.

### Device Update for IoT Hub

[Azure Device Update for IoT Hub](https://learn.microsoft.com/azure/iot-hub-device-update/understand-device-update) is a service that enables you to deploy over-the-air updates (OTA) for your IoT devices. The Device Update for IoT Hub module is the implementation of Device Update for IoT Hub Agent in NetX Duo. It provides simple APIs for device builders to integrate the Device Update capability in their application.

See the samples of key semiconductors evaluation boards that include the get started guides to learn configure, build and deploy the over-the-air (OTA) updates to the devices.

To learn more details about use, see [Device Update for IoT Hub with Eclipse ThreadX](https://learn.microsoft.com/azure/iot-hub-device-update/device-update-azure-real-time-operating-system).
