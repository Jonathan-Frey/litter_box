# Litter Box Monitor

Name: **Jonathan Frey**

Student Id: **jf223rf**

## Overview

In this project we will create a monitor for tracking movement in a litter box as well as the open or closed state of a nearby door(E.g. bathroom door). By doing this we can see the defecation and urination habits of the cat/cats and minimize the risk of the bathroom door being closed for too long, which may result in unneccessary stress in the cat and urination in unwanted locations.

Estimated time: **4 hours**

## Objective

In late 2023, one of my cats suffered from urinary obsruction due to bladder stones. This lead to him having to be admitted to the veterinary clinic. Luckily we caught it early and the recovery went smoothly. However, the risk of the bladder stones coming back is always there, which is why I wanted to track when the cats use the litter box. By tracking when they use the bathroom, I can look for patterns and notice when something is wrong. Knowing the state of the bathroom door lets me know if the door has been closed and forgotten for too long.

## Material

| **Item**               | **Description**                                                                            |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| 1x RB Pico W           | Microcontroller for interfacing with sensors, running logic and communication over network |
| 1x Motion Sensor       | Digital motion sensor for detecting movement in litter box                                 |
| 1x Reed Switch         | digital sensor for detecting nearby magnetic fields                                        |
| 1x Neodynium Magnet    | For triggering reed sensor                                                                 |
| 1x active piezo buzzer | For triggering an alarm when the door has been closed for too long                         |
| 1x Push Button         | For disabling sensor readings when cleaning litter box                                     |
| 1x Red/Green LED (5mm) | For displaying if sensors are disabled or not                                              |
| 2x 330ohm Resistor     | for limiting the voltage to LED channels                                                   |
| Wiring                 | For connecting sensors and actuators to the microcontroller                                |
