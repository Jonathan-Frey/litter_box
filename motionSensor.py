from machine import Pin
import utime

class MotionSensor:
    def __init__(self, motion_sensor_pin, is_on_getter):
        self._start_time = utime.ticks_ms()
        self._motion_sensor = Pin(motion_sensor_pin, Pin.IN, Pin.PULL_UP)
        self._motion_sensor.irq(trigger=Pin.IRQ_RISING, handler=self._motion_sensor_handler)
        self.set_movement_detected(0)
        self._is_on_getter = is_on_getter
    
    # Define callback functions for each interrupt
    def _motion_sensor_handler(self, pin):
        if self.get_movement_detected() == 1:
            return

        now = utime.ticks_ms()

        if self._is_on_getter() and utime.ticks_diff(now, self._start_time) > 60000:
            self.set_movement_detected(1)
    
    def get_movement_detected(self):
        return self._movement_detected
    
    def set_movement_detected(self, value):
        if value == 0:
            self._movement_detected = 0
        elif value == 1:
            self._movement_detected = 1