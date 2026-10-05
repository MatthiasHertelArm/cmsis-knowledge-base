---
id: "ocp-gpio-driver-api-proposal"
type: "concept"
domain: "project"
title: "GPIO Driver API Proposal"
summary: "Following is an API proposal for GPIO (General-purpose Input/Output) Driver. The API features I/O operations on pin level (does not support simultaneous operations on multiple pins belonging to the same port)."
status: "draft"
collection: "ocp-tools-readmes"
source: "Open-CMSIS-Pack/RefApp-Framework@54fba8b:interface/gpio/include/README.md"
doc_source: "https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/interface/gpio/include/README.md"
license: "Apache-2.0"
mode: "V"
---

Following is an API proposal for GPIO (General-purpose Input/Output) Driver. 
The API features I/O operations on pin level (does not support simultaneous operations on multiple pins belonging to the same port). 
The API provides basic pin configuration (direction, output mode, pull-resistor, event trigger) excluding advanced settings (drive strength or speed, input filter, ...), 
setting outputs and reading inputs.

Current proposal is the [API not aligned with CMSIS-Driver specification](#api-not-aligned-with-cmsis-driver-specification).

The API is defined in the [Driver_GPIO.h](https://github.com/Open-CMSIS-Pack/RefApp-Framework/blob/54fba8b/interface/gpio/include/./Driver_GPIO.h) header file.
