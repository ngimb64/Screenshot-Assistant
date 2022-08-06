# Screenshot Assistant
![alt text](https://github.com/ngimb64/Screenshot-Assistant/blob/master/ScreenshotAssistant.gif?raw=true)
![alt text](https://github.com/ngimb64/Screenshot-Assistant/blob/master/ScreenshotAssistant.png?raw=true)

&#9745;&#65039; Bandit verified<br>
&#9745;&#65039; Synk verified<br>
&#9745;&#65039; Pylint verified 9.45/10

## Prereqs
 This program runs on Windows and Linux, written in Python 3.8

## Purpose
This is a simple, functional program designed automate gathering screenshots.<br>
It automates screenshots using a keyboard listener to control whether the program starts, stops, or exits.

## Installation
- Run the setup.py script to build a virtual environment and install all external packages in the created venv.

> Example: `python3 setup.py venv`

- Once virtual env is built traverse to the (Scripts-Windows or bin-Linux) directory in the environment folder just created.
- For Windows in the Scripts directory, for execute the `./activate` script to activate the virtual environment.
- For Linux in the bin directory, run the command `source activate` to activate the virtual environment.

## How to use
- Open up shell such as Command Prompt or Terminal
- Enter directory with program and run it
- Open the graphical file manager and go to path specified in program
- Click on the open CMD and hit enter
- Checkout the file manager and to visualize screenshots created every 5 seconds
- If you want the program to pause hit Esc
- If you want to start again hit enter again.
- OR if you would like to exit hit Ctrl + C

## Function Layout
-- screenshot_assistant.py --
> on_press &nbsp;-&nbsp; Checks to see if the user hit the exit key (escape).

> screenshots &nbsp;-&nbsp; Loop that actively takes screenshots.

> main &nbsp;-&nbsp; Facilitates listener thread and screenshot process.

> print_err &nbsp;-&nbsp; Prints timed error message.