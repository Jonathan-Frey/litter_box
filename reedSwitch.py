from machine import Pin

class ReedSwitch:
    def __init__(self, reed_switch_pin, is_on_getter):
        self.reed_switch = Pin(reed_switch_pin, Pin.IN, Pin.PULL_UP)
        self.reed_switch.irq(trigger=Pin.IRQ_FALLING, handler=self._reed_switch_handler)
        self.set_reed_switch_active(0)
        self._is_on_getter = is_on_getter
    
    # Define callback functions for each interrupt
    def _reed_switch_handler(self, pin):
        if self._is_on_getter() and self.get_reed_switch_active() != 1:
            self.set_reed_switch_active(1)
    
    def get_reed_switch_active(self):
        return self._reed_switch_active
    
    def set_reed_switch_active(self, value):
        if value == 0:
            self._reed_switch_active = 0
        elif value == 1:
            self._reed_switch_active = 1