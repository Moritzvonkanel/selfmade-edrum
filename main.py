import time
import pygame
import sys
import csv
from numpy import ndarray
import scipy.signal

from arduino_connection import waitForArduinoConnection

# Setup pygame
pygame.init()
pygame.display.set_mode((300, 100))
pygame.display.set_caption("Moritz's E-Drum")
pygame.mixer.set_num_channels(80)

# Setup sound configuration
soundsConfiguration : dict = {}
for row in csv.reader(open("./sounds.csv")):
    sound = pygame.mixer.Sound("sounds/" + row[1])
    sound.set_volume(float(row[2]))
    soundsConfiguration[row[0]] = sound
print(soundsConfiguration)

# Setup Arduino connection
print("Waiting for Arduino connection...")
arduinoConnection = waitForArduinoConnection()
arduinoConnection.flush()

# Setup sensor configuration
sonsorThresholds = { 
    "A0": 35, 
    "A1": 10,
    "A2": 3, 
    "A3": 1,
    "A4": 1,
    "A5": 10,
    "A6": 5,
    "A7": 3,
    "A8": 10,
    "A9": 1,
}
sensorMutes = { "A0": time.time(), "A1": time.time(), "A2": time.time(), "A3": time.time(), "A4": time.time(), "A5": time.time(), "A6": time.time(), "A7": time.time(), "A8": time.time(), "A9": time.time() }

while True:

    # Read USB input
    inputs = arduinoConnection.readlines()
    for input in inputs:
        try:
            data = input.decode().strip().split(":")
            sensor = data[0]
            value = int(data[1])
            now = time.time()

            if value > sonsorThresholds[sensor]:
                if now > sensorMutes[sensor]:
                    soundsConfiguration[sensor].play()
                    print(str(now) +" "+sensor +":"+ str(value) + " sound")
                    sensorMutes[sensor] = now + 0.1
                else:
                    print(str(now) +" "+sensor +":"+ str(value))

        except:
            print(f"Input Error: {data}")

    # Read pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    time.sleep(0.05)
