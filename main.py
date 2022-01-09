import time
import pygame
import sys
import csv

from arduino_connection import waitForArduinoConnection

# Setup pygame
pygame.init()
pygame.display.set_mode((300, 100))
pygame.display.set_caption("Moritz's E-Drum")
pygame.mixer.set_num_channels(80)

# Setup sound configuration
soundsConfiguration = {}
for row in csv.reader(open("./sounds.csv")):
    soundsConfiguration[row[0]] = pygame.mixer.Sound("sounds/" + row[1])
print(soundsConfiguration)

# Setup Arduino connection
print("Waiting for Arduino connection...")
arduinoConnection = waitForArduinoConnection()
arduinoConnection.flush()

while True:

    # Read USB input
    lines = arduinoConnection.readlines()
    for line in lines:
        try:
            data = line.decode().strip().split(":")
            print(data)

            sensor = data[0]
            value = int(data[1])

            if value > 0:
                soundsConfiguration[sensor].set_volume(0.1)
                soundsConfiguration[sensor].play()

        except:
            print(f"Input Error: {data}")

    # Read pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    time.sleep(0.05)
