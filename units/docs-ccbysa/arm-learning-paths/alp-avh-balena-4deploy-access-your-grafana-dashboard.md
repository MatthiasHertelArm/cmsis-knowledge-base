---
id: "alp-avh-balena-4deploy-access-your-grafana-dashboard"
type: "concept"
domain: "project"
title: "Deploy IoT applications with Balena Cloud and Arm Virtual Hardware: Deploy an application to your device: Access your Grafana dashboard"
summary: "Your application is now running, but it's not accessible from the outside world. To view your Grafana dashboard in your browser, you need to tell Balena to make your device accessible from a public URL."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_balena/4deploy.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_balena/4deploy/#access-your-grafana-dashboard"
license: "CC-BY-SA-4.0"
mode: "V"
---

Your application is now running, but it's not accessible from the outside world. To view your Grafana dashboard in your browser, you need to tell Balena to make your device accessible from a public URL. 

Toggle the `Public Device URL` switch to the `On` position.

A link appears next to the switch, click on it to open the newly created public URL.

(figure: Balena-app login screen showing username and password fields over a dark background with the Grafana logo and branding#center)

This opens the `balena-app` on your device in your browser. You're presented with a log in screen, use the default username `admin` and password `admin` to log in. You'll be prompted to set a new password for the `admin` user before continuing.

(figure: Grafana dashboard showing real-time system metrics including CPU usage, memory consumption, network traffic, and container status for the Balena OS device#center)

You now see the Grafana dashboard monitoring your Balena OS installation on this device, including the containers running Grafana and Nginx.
