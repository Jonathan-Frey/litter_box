from machine import Pin, Timer
import utime
from mqtt import MQTTClient   # For use of MQTT protocol
import keys                   # Contain all keys used here
import wifiConnection 
import ujson        # Contains functions to connect/disconnect from WiFi 

startTime = utime.ticks_ms()
isOn = 1
lastButtonPress = startTime
lastReedSwitchActivation = startTime
movement_detected = 0
reed_switch_active = 0


# Pin setup
rg_led_pin1 = 13
rg_led_pin2 = 14
motion_sensor_pin = 15
button_pin = 16
reed_switch_pin = 17

rg_green = Pin(rg_led_pin1, Pin.OUT)
rg_red = Pin(rg_led_pin2, Pin.OUT)
rg_green.value(1)
rg_red.value(0)

# Define callback functions for each interrupt
def motion_sensor_handler(pin):
    now = utime.ticks_ms()
    global movement_detected
    if isOn and utime.ticks_diff(now, startTime) > 60000:
        movement_detected = 1

def button_press_handler(pin):
    now = utime.ticks_ms()
    global lastButtonPress, isOn
    # Check if at least 1000 ms have passed since the last button press
    if utime.ticks_diff(now, lastButtonPress) > 1000:
        lastButtonPress = now
        if isOn == 0:
            isOn = 1
            rg_green.value(1)
            rg_red.value(0)
        else:
            isOn = 0
            rg_green.value(0)
            rg_red.value(1)


def reed_switch_handler(pin):
    if isOn:
        now = utime.ticks_ms()
        global lastReedSwitchActivation, reed_switch_active
        # Check if at least 200 ms have passed since the last reed switch activation
        if utime.ticks_diff(now, lastReedSwitchActivation) > 200:
            lastReedSwitchActivation = now
            reed_switch_active = 1

# Setup pins with interrupts
motion_sensor = Pin(motion_sensor_pin, Pin.IN, Pin.PULL_UP)
motion_sensor.irq(trigger=Pin.IRQ_RISING, handler=motion_sensor_handler)

button = Pin(button_pin, Pin.IN, Pin.PULL_UP)
button.irq(trigger=Pin.IRQ_FALLING, handler=button_press_handler)

reed_switch = Pin(reed_switch_pin, Pin.IN, Pin.PULL_UP)
reed_switch.irq(trigger=Pin.IRQ_FALLING, handler=reed_switch_handler)

# Callback function to be called by the timer
def timer_callback(t):
    global movement_detected, reed_switch_active
    data = {
        "system_state" : isOn,
        "movement" : movement_detected,
        "door_closed" : reed_switch_active
    }

    print(ujson.dumps(data))

    client.publish(topic=keys.TOPIC, msg=ujson.dumps(data))

    # Reset movement_detected for the next iteration
    movement_detected = 0
    reed_switch_active = 0

def cleanup():
    timer.deinit()
    client.disconnect()
    wifiConnection.disconnect()
    print("Disconnected from MQTT broker.")

# Try WiFi Connection
try:
    ip = wifiConnection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Use the MQTT protocol to connect to Adafruit IO
client = MQTTClient(keys.CLIENT_ID, keys.SERVER, keys.PORT)

client.connect()
print("Connected to", keys.SERVER)

try:
    # Initialize a Timer object
    timer = Timer()

    # Configure the timer to call timer_callback every 10 seconds
    timer.init(period=10000, mode=Timer.PERIODIC, callback=timer_callback)
    while True:
        utime.sleep(1)
finally:
    cleanup()
