from machine import Timer
import utime
from button import Button # Class for button sensor
import keys                   # Contain all keys used here
from motionSensor import MotionSensor # Class for motion sensor
from reedSwitch import ReedSwitch # Class for reed switch
from rg_led import Led # class for LED
import wifiConnection # wifi connectivity
import ujson        # Contains functions to connect/disconnect from WiFi
from boot import client # MQTT client object instantiated in boot.py

_is_on = 1

def switch_on_state():
    global _is_on
    if _is_on == 0:
        _is_on = 1  
        rg_led.green()
    else:
        _is_on = 0
        rg_led.red()

def get_is_on():
    return _is_on

rg_led = Led(13, 14)
rg_led.green()
button = Button(16, switch_on_state)
motion_sensor = MotionSensor(15, get_is_on)
reed_switch = ReedSwitch(17, get_is_on)

# Callback function to be called by the timer
def timer_callback(t):
    data = {
        "system_state" : get_is_on(),
        "movement" : motion_sensor.get_movement_detected(),
        "door_closed" : reed_switch.get_reed_switch_active()
    }

    client.publish(topic=keys.TOPIC, msg=ujson.dumps(data))

    # Reset measurements for the next interval
    motion_sensor.set_movement_detected(0)
    reed_switch.set_reed_switch_active(0)

def cleanup():
    timer.deinit()
    client.disconnect()
    wifiConnection.disconnect()
    print("Disconnected from MQTT broker.")

try:
    # Initialize a Timer object
    timer = Timer()

    # Configure the timer to call timer_callback every 10 seconds
    timer.init(period=10000, mode=Timer.PERIODIC, callback=timer_callback)
    while True:
        utime.sleep(1)
finally:
    cleanup()
