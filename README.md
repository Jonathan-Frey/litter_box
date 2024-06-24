# Litter Box Monitor

Name: **Jonathan Frey**

Student Id: **jf223rf**

## Overview

In this project we will create a monitor for tracking movement in a litter box as well as the open or closed state of a nearby door(E.g. bathroom door). By doing this we can see the defecation and urination habits of the cat/cats and minimize the risk of the bathroom door being closed for too long, which may result in unneccessary stress in the cat and urination in unwanted locations.

Estimated time: **4 hours**

## Objective

In late 2023, one of my cats suffered from urinary obstruction due to bladder stones. This lead to him having to be admitted to the veterinary clinic. Luckily we caught it early and the recovery went great. However, the risk of the bladder stones coming back is always there, which is why I wanted to track when the cats use the litter box. By tracking when they use the bathroom, I can look for patterns and notice when something is wrong. Knowing the state of the bathroom door lets me know if the door accidentally has been left closed.

## Material

| **Item**                                                                                     | **Description**                                                                            |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| 1x Raspberry Pi Pico WH ![Raspberry Pi Pico WH](/assets/images/pico.jpg)                     | Microcontroller for interfacing with sensors, running logic and communication over network |
| 1x HC-SR501 PIR Motion Sensor ![HC-SR501 PIR Motion Sensor](/assets/images/hc-sr501.jpg)     | Digital motion sensor for detecting movement in litter box                                 |
| 1x KY-021 Reed Switch Module Mini ![KY-021 Reed Switch Module Mini](/assets/images/reed.jpg) | digital sensor for detecting nearby magnetic fields                                        |
| 1x Neodynium Magnet                                                                          | For triggering reed sensor                                                                 |
| 1x KY-004 Push Button ![KY-004 Push Button](/assets/images/button.png)                       | For disabling sensor readings when cleaning litter box                                     |
| 1x KY-011 R/G LED module (5mm) ![KY-011 R/G LED module (5mm)](/assets/images/led.jpg)        | For displaying if sensor readings are disabled or not                                      |
| 2x 330ohm Resistor                                                                           | for limiting the voltage to LED channels                                                   |
| Male-to-female and Male-to-male Wires                                                        | For connecting sensors and actuators to the microcontroller                                |
| micro-USB cable                                                                              | For providing power to the microcontroller                                                 |

In this tutorial these componentswill be used with the microcontroller mounted to a breadboard, but to move on from the prototyping stage, soldering wires directly to the components and putting them in casings is recommended.

The Pico WH comes with pins pre-soldered onto the board. A Pico W can be used instead, but will require you to solder the pins yourself.

## Computer Setup

**Step 1: Flashing the Firmware**

1. **Download the MicroPython firmware:**

   - Go to the official Raspberry Pi Pico MicroPython download page.

   - Download the latest UF2 file for the Raspberry Pi Pico W.

2. **Connect the Pico W to your computer**:

   - Hold down the BOOTSEL button on the Pico W and connect it to your computer via a USB cable. Release the BOOTSEL button after connecting.

3. **Flash the MicroPython firmware**:

   - The Pico W should appear as a mass storage device on your computer.

   - Drag and drop the downloaded UF2 file onto the Pico W's mass storage device. The device will reboot automatically and appear as a USB serial device.

**Step 2: Installing VSCode and Pymakr Plugin**

1. **Install Visual Studio Code (VSCode):**

   - Download and install VSCode from [here](https://code.visualstudio.com/).

2. **Install Pymakr Plugin:**

   - Open VSCode and go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window.

   - Search for "Pymakr" and click "Install" on the Pymakr plugin by Pycom.

3. **Configure Pymakr Plugin:**

   - After installing the Pymakr plugin, you need to configure it to communicate with your Pico W.

   - Click on the Pymakr icon on the VSCode status bar. At the bottom a list of identified devices can be seen.

   - Connect your Pico W to your computer while watching the list of devices. A new device will apear in the list. That is the Pico W.

   - Hover over the device and press "connect device".

   - To find it easierr in the future you can right-click the device and press "configure device"

   - Here you can both change the name of the device and configure Pymakr to automatically connect to the device when connected to the computer.

**Step 3: Install Required Software**

**1. Install Node.js:**

- Download and install Node.js from [here](https://nodejs.org/en).

- Node.js is required for some of the Pymakr functionalities.

**Step 4: Uploading Code to the Pico W**

**1. Create a new MicroPython project in VSCode:**

- Open VSCode and create a new folder for your project.

- Inside this folder, create a new Python file (e.g., main.py) and write your MicroPython code.

**2. Connect to the Pico W:**

- Ensure your Pico W is connected to your computer via USB.

- Click the Pymakr icon on the status bar and select "Connect".

**3. Upload the code:**

- Once connected, you can upload your code to the Pico W by clicking the Pymakr icon and selecting "sync project to device".

- The code will be transferred to the Pico W and run automatically.

- You may also start development mode, automatically uploading changed files to the device and restarting it.

## Putting Everything Together

## Platform

**Overview:**

I have chosen the TIG-stack containerized using Docker for receiving, storing and visualizing data.

**TIG Stack:** TIG stands for Telegraf, InfluxDB, and Grafana. These three tools work together to collect, store, and visualize metrics.

**Telegraf:** A plugin-driven server agent for collecting and reporting metrics.
**InfluxDB:** A time-series database designed to handle high write and query loads.
**Grafana:** A powerful visualization tool for time-series data.

**Platform Chosen:** DigitalOcean

Why DigitalOcean? DigitalOcean provides a straightforward and cost-effective cloud platform that is easy to set up and manage. It is ideal for small to medium-sized projects and offers a good balance of performance and price. As a student I also receive $200 in credits that can be used to rent droplets (virtual machines).

If you don't want to rely on external services, you may instead host the TIG-stack docker containers on your personal computer. But this means data will only be collected while the computer is powered on and not in sleep mode. It will also not be accessible from other devices without extra setup such as receiving a permanent IP-adress.

**Functionality and Features:**

**Telegraf:**

- Used to collects metrics from the Pico W through a MQTT broker.

- writes the received data to the influxDB database.

**InfluxDB:**

- Optimized for time-series data, supporting high write and query throughput.

- Stores the received data with timestamps.

**Grafana:**

- Provides a rich set of visualization tools to create interactive and customizable dashboards from the data.

## The Code

## Transmitting The Data / Connectivity

**Overview:**
The Pico W is connected to WiFi for internet access.

In this setup, data from the Pico W is transmitted every 10 seconds to the test.mosquitto.org MQTT broker using JSON format. Telegraf subscribes to specific topics from the broker and saves the data to the influxDB database.

**Wireless Protocol:**

- **WiFi:** Used for connecting the Raspberry Pi Pico W to the internet.

**Transport Protocol:**

- **MQTT:** A lightweight messaging protocol for small sensors and mobile devices, optimized to minimize network bandwidth and device resource requirements.

**Data Format:**

- **JSON:** The data is formatted as JSON since influxDB can parse the message automatically and save the data with correct topics, headers and values.

**In the Code:**

The `wifiConnection.py` file provides a connection as well as a disconnection function for wifi connectivity. It uses the `WIFI_SSID` and `WIFI_PASS` variables from the `keys.py` file to access the network. The connect-function is called on boot in `boot.py`, and the disconnect-function is called inside the cleanup-function in `main.py` when script is stopped.

After connecting to the network, the MQTTClient class provided by the `mqtt.py` file is used to connect to the MQTT broker, using the `SERVER`, `PORT`and `CLIENT_ID` variables from the `keys.py` file.

Every 10 seconds, data in the following JSON-format is sent to the MQTT broker using the publish method provided by the MQTTCLient object:

```JSON
{
  "system_state" : 0,
  "movement" : 1,
  "door_closed" : 0
}
```

## Presenting The Data

InfluxDB allows you to specify a bucket retention time to schedule old data for deletion. For default, the retention time is set as infinite. I chose to keep it that way, since I would like to see all data streching back as far as they go, and don't see the storage rounning oout in the immediate future.

Below is a snapshot of the dashboard with the three main panels. They show the state of the system (if sensor readings are disabled or not), the open/closed state of the bathroom door and the timeline for motion inside the litter box.

![Grafana Dashboard](assets/images/dashboard.png)

I chose not to extrapolate the number of times cats have visited the litter box from the movement data at this stage since I can not be sure if seperate movement readings are from seperate visits or the same visit. But by analyzing the data I will receive across multiple weeks, I will look at the patterns and figure out a ruleset for determening this.

## Finalizing The Design