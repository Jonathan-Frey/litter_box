from machine import Pin
import utime

class Button:
    def __init__(self, buttonPin, callback):
        self._start_time = utime.ticks_ms()
        self._lastButtonPress = self._start_time
        self._button= Pin(buttonPin, Pin.IN, Pin.PULL_UP)
        self._button.irq(trigger=Pin.IRQ_FALLING, handler=self._button_press_handler)
        self._callback = callback
    
    def _button_press_handler(self, pin):
        now = utime.ticks_ms()
        # Check if at least 1000 ms have passed since the last button press
        if utime.ticks_diff(now, self._lastButtonPress) > 1000:
            self._lastButtonPress = now
            self._callback()