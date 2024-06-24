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

Step 1: Flashing the Firmware

1. Download the MicroPython firmware:

   - Go to the official Raspberry Pi Pico MicroPython download page.

   - Download the latest UF2 file for the Raspberry Pi Pico W.

2. Connect the Pico W to your computer:

   - Hold down the BOOTSEL button on the Pico W and connect it to your computer via a USB cable. Release the BOOTSEL button after connecting.

3. Flash the MicroPython firmware:

   - The Pico W should appear as a mass storage device on your computer.

   - Drag and drop the downloaded UF2 file onto the Pico W's mass storage device. The device will reboot automatically and appear as a USB serial device.

Step 2: Installing VSCode and Pymakr Plugin

1. Install Visual Studio Code (VSCode):

   - Download and install VSCode from [here](https://code.visualstudio.com/).

2. Install Pymakr Plugin:

   - Open VSCode and go to the Extensions view by clicking the Extensions icon in the Activity Bar on the side of the window.

   - Search for "Pymakr" and click "Install" on the Pymakr plugin by Pycom.

3. Configure Pymakr Plugin:

   - After installing the Pymakr plugin, you need to configure it to communicate with your Pico W.

   - Click on the Pymakr icon on the VSCode status bar. At the bottom a list of identified devices can be seen.

   - Connect your Pico W to your computer while watching the list of devices. A new device will apear in the list. That is the Pico W.

   - Hover over the device and press "connect device".

   - To find it easierr in the future you can right-click the device and press "configure device"

   - Here you can both change the name of the device and configure Pymakr to automatically connect to the device when connected to the computer.

Step 3: Install Required Software

1. Install Node.js:

   - Download and install Node.js from [here](https://nodejs.org/en).

   - Node.js is required for some of the Pymakr functionalities.

Step 4: Uploading Code to the Pico W

1. Create a new MicroPython project in VSCode:

   - Open VSCode and create a new folder for your project.

   - Inside this folder, create a new Python file (e.g., main.py) and write your MicroPython code.

2. Connect to the Pico W:

   - Ensure your Pico W is connected to your computer via USB.

   - Click the Pymakr icon on the status bar and select "Connect".

3. Upload the code:

   - Once connected, you can upload your code to the Pico W by clicking the Pymakr icon and selecting "sync project to device".

   - The code will be transferred to the Pico W and run automatically.

   - You may also start development mode, automatically uploading changed files to the device and restarting it.
