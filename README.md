# Selfmade E-Drum
Selfmade edrums made for school project

If you're not familiar with Git, download the source code [[Zip Download]](https://github.com/Moritzvonkanel/selfmade-edrum/archive/refs/heads/main.zip) and extract it to a folder of your choice.

# Software Requirements
- **Python 3.9+**
  - *Download (https://www.python.org/downloads/)*
  - *Ensure to Add Python to Path:* <br>
    ![image](https://user-images.githubusercontent.com/97349263/148652062-6ab9f78a-c8fa-4137-a475-0e49513e7c97.png)
- **Arduino IDE 1.8+**
  - *Download (https://www.arduino.cc/en/software)*
- **Optional: Code editor for Python**
  - *We use Visual Studio Code with Python plugin (https://code.visualstudio.com/Download)*

# Arduino Setup
- Ensure you have installed **Python 3.9+** and **Arduino IDE 1.8+** (See requirements)
- Connect the Arduino Board using USB with your computer
- Open file `<edrum-folder>/arduino/arduino.ino` with Arduino IDE
- Select Board Arduino Mega or Mega 2560: <br>
  ![image](https://user-images.githubusercontent.com/97349263/148652670-96ec2d0d-a293-4132-b14e-4c322c0964cd.png)
- Make sure the python program doesn't run yet! (The next step would fail)
- Upload code to Arduino: <br>
  ![image](https://user-images.githubusercontent.com/97349263/148654549-21ba1bc6-f001-457a-864c-b2b74b67a51b.png)

# User Guide
- Ensure you have installed **Python 3.9+** (See requirements)
- Ensure you have dowloaded the code.
- Connect the Arduino Board using USB with your computer
- Open a Terminal / CMD and navigate to the e-drum project
  - Type `cd <path-to-your-dowload-folder>` (Example `cd C://projects/selfmade-edrum`) and press enter
  - Install all python dependency
  - Type `pip install -r requirements.txt` and press enter
- Start the E-Drum application
  - Type `python main.py` and press enter
