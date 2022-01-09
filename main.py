import serial
import time
import pygame
import sys
import csv

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

# Setup USB connection
inputUSB = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
inputUSB.flush()

while True:

    # Read USB input
    lines = inputUSB.readlines()
    for line in lines:
        try:
            data = line.decode().strip().split(":")
            print(data)

            sensor = data[0]
            value = data[1]

            soundsConfiguration[sensor].set_volume(0.1)
            soundsConfiguration[sensor].play()

        except:
            print("Input Error:")
            print(data)

    # Read pygame events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            sys.exit()

    time.sleep(0.05)
