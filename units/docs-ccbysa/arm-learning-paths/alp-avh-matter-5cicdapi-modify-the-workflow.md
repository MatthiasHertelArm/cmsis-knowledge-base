---
id: "alp-avh-matter-5cicdapi-modify-the-workflow"
type: "concept"
domain: "project"
title: "Develop for Matter with Arm Virtual Hardware: Control Arm Virtual Hardware with API: Modify the workflow"
summary: "In the lighting-app instance console, edit the previously created workflow."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/avh_matter/5cicdapi.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/avh_matter/5cicdapi/#modify-the-workflow"
license: "CC-BY-SA-4.0"
mode: "V"
---

In the `lighting-app` instance console, edit the previously created workflow.
```console
cd ~/connectedhomeip
nano .github/workflows/cicd_demo.yml
```
**Append** this `job` to the file:
```yml
  chip_tool:
    needs: rebuild_lighting_app
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install Node
        uses: actions/setup-node@aa759c6c94d3800c55b8601f21ba4b2371704cb7

      - name: Install AVH API and Websocket
        run: npm install @arm-avh/avh-api websocket --save

      - name: Run script
        env:
          API_TOKEN: ${{ secrets.API_TOKEN }}
        run: node .github/workflows/chip_tool.js
```
Save and exit.

This job invokes the following `JavaScript` which will transmit the `on/off` commands to the `chip-tool` instance via the `Websocket` interface.

Create a script:
```console
nano .github/workflows/chip_tool.js
```
containing the below:
```js
const readline = require('readline')
const { ArmApi, ApiClient } = require('@arm-avh/avh-api');
const W3CWebSocket = require('websocket').w3cwebsocket;

const BearerAuth = ApiClient.instance.authentications['BearerAuth']
const api = new ArmApi()

function delay(time) {
	return new Promise(resolve => setTimeout(resolve, time));
}

async function main() {
	console.log('Logging in...');
	const apiToken = process.env.API_TOKEN
	const authInfo = await api.v1AuthLogin({ apiToken });
	BearerAuth.accessToken = authInfo.token
	
	console.log("Locate instance named chip-tool...");
	console.log("[User must edit JavaScript if instance has different name (or >10000 instances)]");
	let instances = await api.v1GetInstances()
	for(let i=0; i<10000; i++){
		var instance = instances[i];
		if (instance.name == "chip-tool") break;
	}
	
	console.log("Open Websocket...");
	let url = await api.v1GetInstanceConsole(instance.id);
	var mySocket = await new W3CWebSocket(url.url);
	
	mySocket.onopen = function() {
		console.log(`WebSocket open.`);};
	mySocket.onerror = function() {
		console.log('WebSocket Connection Error.')};

	// Log in - comment the lines below if user has already logged in using the UI console
	mySocket.send("pi\n");
	await delay(1000);
    mySocket.send("raspberry\n");
    await delay(1000);
	
	console.log("Wait 60s to ensure lighting-app is initialized...");
	await delay(60000);
	
	console.log("Turn light on...");
	mySocket.send("/home/pi/connectedhomeip/examples/chip-tool/out/debug/chip-tool onoff on 0x11 1\n");
	
	console.log("Wait 5 seconds...");
	await delay(5000);
	
	console.log("Turn light off...");
	mySocket.send("/home/pi/connectedhomeip/examples/chip-tool/out/debug/chip-tool onoff off 0x11 1\n");
	
	console.log("Wait 5 seconds...");
	await delay(5000);
	
	console.log("Turn light on again...");
	mySocket.send("/home/pi/connectedhomeip/examples/chip-tool/out/debug/chip-tool onoff on 0x11 1\n");
	
	console.log("Wait 5 seconds...");
	await delay(5000);
	
	console.log("Turn light off again...");
	mySocket.send("/home/pi/connectedhomeip/examples/chip-tool/out/debug/chip-tool onoff off 0x11 1\n");
	
	console.log("Wait 5 seconds...");
	await delay(5000);
	
	console.log('Closing WebSocket...');
	mySocket.close();
		mySocket.onclose = function() {
		console.log(`WebSocket closed.`);};
	mySocket.onerror = function() {
		console.log('WebSocket Error.')};
	
	return;
}

main().catch((err) => {
    console.error(err);
});
```
Note that the JavaScript refers to instance name `chip-tool`, and `API_TOKEN` secret. The `job` refers to the script `chip_tool.js`, as well as the `API_TOKEN` secret. If these were named differently, you'll need to update the script(s) appropriately.

When all edits are complete, push the changes back to GitHub:
```console
cd ~/connectedhomeip
git add .
git commit -m "added chip-tool automation"
git push
```
You'll again be prompted for your GitHub username and Personal Access Token (password)..

A new run of the Action will be triggered.
