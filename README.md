<div align="center" style="font-family: monospace">
<h1>Screenshot Assistant</h1>
&#9745;&#65039; Bandit verified &nbsp;|&nbsp; &#9745;&#65039; Synk verified &nbsp;|&nbsp;&#9745;&#65039; Pylint verified 9.44/10
</div>

![alt text](https://github.com/ngimb64/Screenshot-Assistant/blob/master/ScreenshotAssistant.gif?raw=true)
![alt text](https://github.com/ngimb64/Screenshot-Assistant/blob/master/ScreenshotAssistant.png?raw=true)

### Purpose
This is a simple, functional program designed automate gathering screenshots based on time interval.<br>
It automates screenshots using a keyboard listener to control whether the program starts, stops, or exits.

### Prereqs
This program runs on Windows 10 and Debian-based Linux, written in Python 3.8 and updated to version 3.10.6

### Installation
- Run the setup.py script to build a virtual environment and install all external packages in the created venv.

> Examples:<br> 
>       &emsp;&emsp;- Windows:  `python setup.py venv`<br>
>       &emsp;&emsp;- Linux:  `python3 setup.py venv`

- Once virtual env is built traverse to the (Scripts-Windows or bin-Linux) directory in the environment folder just created.
- For Windows, in the venv\Scripts directory, execute `activate` or `activate.bat` script to activate the virtual environment.
- For Linux, in the venv/bin directory, execute `source activate` to activate the virtual environment.
- If for some reason issues are experienced with the setup script, the alternative is to manually create an environment, activate it, then run pip install -r packages.txt in project root.
- To exit from the virtual environment when finished, execute `deactivate`.

### How to use
- Open up shell such as Command Prompt or Terminal
- Enter directory with program and run it
- Open the graphical file manager and go to path specified in program
- Click on the open CMD and hit enter
- Checkout the file manager and to visualize screenshots created every 5 seconds
- If you want the program to pause hit Esc
- If you want to start again hit enter again.
- OR if you would like to exit hit Ctrl + C

### Function Layout
-- screenshot_assistant.py --
> on_press &nbsp;-&nbsp; Checks to see if the user hit the exit key (escape).

> screenshots &nbsp;-&nbsp; Loop that actively takes screenshots.

> get_time_interval &nbsp;-&nbsp; Gets the time interval integer from user and returns to main.

> main &nbsp;-&nbsp; Facilitates listener thread and screenshot process.

> print_err &nbsp;-&nbsp; Prints timed error message.