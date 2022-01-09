import time
import serial
from serial_interface.serial_interface import find_serial_interface_ports

def pingArduino(connection: serial.Serial, sleep_sec: float, timeout_sec: float):
    timeout = time.time() + timeout_sec
    while timeout > time.time():
        
        print(f"Send Ping to '{connection.port}'...")
        connection.write("SELFMADE_EDRUM_PING".encode())

        print(f"Wait for response...")
        responses = connection.readlines()
        for response in responses:
            if "SELFMADE_EDRUM_PONG" in response.decode():
                print(f"Response received :)")
                return True
        print(responses)
        print(f"No response but try again afer {sleep_sec}sec")
        time.sleep(sleep_sec)
    print("Timeout: Ping failed")
    return False

def getArduinoConnection():
    
    print("Check serial ports...")
    ports = find_serial_interface_ports()
    print(f"Found: {ports}")

    for port in ports:
        try:
            print(f"Open serial connection to '{port}'")
            connection = serial.Serial(port=port, baudrate=115200, timeout=.005)
            if pingArduino(connection=connection, sleep_sec=2, timeout_sec=8):
                return connection
        except:
            print(f"Device discovery error: {connection.port}")
    return None

def waitForArduinoConnection():
    while True:
        connection = getArduinoConnection()
        if connection is not None:
            return connection
        time.sleep(2)