from mqtt import MQTTClient   # For use of MQTT protocol
import wifiConnection 
import keys

# Try WiFi Connection
try:
    ip = wifiConnection.connect()
except KeyboardInterrupt:
    print("Keyboard interrupt")

# Use the MQTT protocol to connect to MQTT Broker
client = MQTTClient(keys.CLIENT_ID, keys.SERVER, keys.PORT)

client.connect()
print("Connected to", keys.SERVER)