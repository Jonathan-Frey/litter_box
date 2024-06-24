from machine import Pin

class Led:

    def __init__(self, greenPin, redPin):
        self._rg_green = Pin(greenPin, Pin.OUT)
        self._rg_red = Pin(redPin, Pin.OUT)
        self.off()
    
    def off(self):
        self._rg_green.value(0)
        self._rg_red.value(0)
    
    def green(self):
        self._rg_green.value(1)
        self._rg_red.value(0)

    def red(self):
        self._rg_green.value(0)
        self._rg_red.value(1)
    
    def yellow(self):
        self._rg_green.value(1)
        self._rg_red.value(1)