---
id: "alp-avh-balena-4deploy-deploy-from-balena-hub"
type: "concept"
domain: "project"
title: "Deploy IoT applications with Balena Cloud and Arm Virtual Hardware: Deploy an application to your device: Deploy from Balena Hub"
summary: "You can build and deploy your own custom applications on Balena OS, or use a pre-built application from Balena Hub."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_balena/4deploy.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_balena/4deploy/#deploy-from-balena-hub"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can build and deploy your own custom applications on Balena OS, or use a pre-built application from [Balena Hub](https://hub.balena.io/). 

As an example, you can deploy a Grafana dashboard from Balena Hub that will show the state of your Balena OS device.

Open Balena Hub in a new tab by clicking on the Balena Hub button on the top right corner of your Balena Cloud dashboard.

(figure: Balena Cloud dashboard header showing the Balena Hub button in the top right corner next to other navigation elements#center)

On the Balena Hub, click `Apps` in the top navigation bar, then search for `balena-app`. This is a pre-built dashboard backed by Grafana and served by Nginx.

(figure: Balena Hub Apps page displaying search results for balena-app, showing the application card with description and deployment options#center)

Click on the app to open the details page.

Look for the `Deploy` button in the upper-right corner of the page.

Clicking this button takes you back to your Balena Cloud dashboard with a dialog to deploy `balena-app` to a fleet.

(figure: Deployment dialog showing fleet selection options with AVH-Testing fleet highlighted and advanced configuration settings collapsed#center)

Select `Use an existing fleet instead` and choose the `AVH-Testing` fleet.

You don't need to do any advanced configuration for this app. Click the `Deploy to fleet` button to begin the deployment.

**Note:**
If you have more than one device in your fleet, this process deploys the selected application to all devices in your fleet simultaneously.


Once the deployment finishes, click on your device in Balena Cloud dashboard to open up the device page. You'll see that the Grafana and Nginx services have been deployed to and are running on your device.

(figure: Balena Cloud device page showing active services with Grafana and Nginx containers running, including service status indicators and log output#center)

You'll also be able to see the system logs from your device, and optionally get access to the device's terminal from this Balena Cloud screen.
