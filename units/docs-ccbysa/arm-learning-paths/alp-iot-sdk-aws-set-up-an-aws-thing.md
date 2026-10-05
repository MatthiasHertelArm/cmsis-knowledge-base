---
id: "alp-iot-sdk-aws-set-up-an-aws-thing"
type: "concept"
domain: "project"
title: "Build and run Arm Total Solutions for IoT: Enable AWS connectivity: Set up an AWS thing"
summary: "You can send the output data to an AWS thing using MQTT."
status: "draft"
collection: "arm-learning-paths"
source: "ArmDeveloperEcosystem/arm-learning-paths@6b164c9:content/learning-paths/embedded-and-microcontrollers/iot-sdk/aws.md"
doc_source: "https://learn.arm.com/learning-paths/embedded-and-microcontrollers/iot-sdk/aws/#set-up-an-aws-thing"
license: "CC-BY-SA-4.0"
mode: "V"
---

You can send the output data to an `AWS thing` using [MQTT](https://mqtt.org/).

Open the AWS console in your browser.

In the same AWS region where you launched your Arm Virtual Hardware instance, navigate to `IoT Core`.

### Create IoT policy
An AWS IoT policy defines how your `thing` can be accessed.

1. Select `Manage` > `Security` > `Policies`.

2. Click `Create policy` and give it a meaningful name.

3. In the `Policy document` section, create 4 statements (use `Add new statement` button to add more) where:

* `Policy effect` = `Allow`

`Policy action` = one each of:
* `iot:Connect`
* `iot:Publish`
* `iot:Receive`
* `iot:Subscribe`

`Policy resource` will be unique to you, of the form:
* `arn:aws:iot:<region>:<account-id>:*`

For example, if you are in region `us-east-1`, and your account number is `1111-2222-3333`, use:

* `arn:aws:iot:us-east-1:111122223333:*`

4. Click `Create` to define the policy.

### Create an AWS thing
1. Select `Manage` > `All devices` > `Things`, and click on `Create things`.

2. Select `Create a single thing` and give it a meaningful name. Click `Next` leaving all other options as default.

3. Select `Auto-generate a new certificate` and click `Next`.

4. Select the `Policy` created [above](#policy) and click `Create thing`.

5. When prompted, download the `device certificate` (`.crt`) and public and private `keys` (`.pem.key`) for your `thing`. Click `Done`.

### Observe MQTT data
In your AWS console, click on your `thing`.

1. Select the `Activity` tab and open `MQTT test client`.

2. Subscribe to `thingname/ml/inference` where `thingname` is the name from the previous section. You can subscribe to `#` as a catch-all wildcard if you prefer.

3. Click `Edit` and enable `MQTT payload display` > `Display payloads as strings (more accurate)`. Click `Confirm`.
