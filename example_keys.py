import ubinascii              # Conversions between binary data and various encodings
import machine                # To Generate a unique id from processor

# Wireless network
WIFI_SSID =  "YOUR-WIFI-SSID"
WIFI_PASS = "YOUR-WIFI-PASSWORD"

# MQTT  broker  setup
SERVER = "YOUR-BROKER-URL"
PORT = 1883
CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
TOPIC = "YOUR-TOPIC"