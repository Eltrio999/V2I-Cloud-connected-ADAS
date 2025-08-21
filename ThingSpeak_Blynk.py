import time
import serial
import pynmea2
import requests
import BlynkLib

# Blynk authentication token
BLYNK_AUTH = '2MDhoP2b34S6yojTxnmDYIBwoeR6oFhF'
# ThingSpeak API settings
THINGSPEAK_API_KEY = '6QNB56I4C3WRIUXO'
THINGSPEAK_URL = f'https://api.thingspeak.com/update?api_key={THINGSPEAK_>

# Set up Blynk connection
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Set up GPS serial communication (adjust to your Raspberry Pi GPIO or se>
gps_serial = serial.Serial('/dev/serial0', baudrate=9600, timeout=1)

# Function to send data to ThingSpeak
def send_data_to_thingspeak(latitude, longitude):
    url = f'{THINGSPEAK_URL}&field1={latitude}&field2={longitude}'
    response = requests.get(url)
if response.status_code == 200:
        print("Data sent to ThingSpeak successfully.")
    else:
        print("Failed to send data to ThingSpeak.")

# Main loop
while True:
    # Read a line from the GPS
    line = gps_serial.readline().decode('utf-8', errors='ignore')

    # Check if it's a GPRMC sentence
    if line.startswith('$GPRMC'):
        try:
            msg = pynmea2.parse(line)

            # Ensure we have a valid GPS fix
            if msg.status == 'A':  # 'A' means valid fix
                latitude = float(msg.latitude)
                longitude = float(msg.longitude)
 # Print the GPS coordinates to the terminal
                print(f"Latitude: {latitude}, Longitude: {longitude}")

                # Send to Blynk
                blynk.virtual_write(0, latitude)  # Send Latitude to Virt>
                blynk.virtual_write(1, longitude)  # Send Longitude to Vi>

                # Send data to ThingSpeak
                send_data_to_thingspeak(latitude, longitude)

                # Wait for a bit before next reading
                time.sleep(15)
            else:
                print("Waiting for GPS fix...")
        except pynmea2.nmea.ParseError as e:
            print(f"Error parsing GPS data: {e}")

    # Handle Blynk event loop
    blynk.run()




