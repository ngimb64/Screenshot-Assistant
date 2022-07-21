# Built-in modules #
import logging
import os
import pathlib
import sys
import time
from multiprocessing import Process
from shlex import quote

# Third-party modules #
from PIL import ImageGrab
from pynput.keyboard import Key, Listener


'''
################
Function Index #
########################################################################################################################
OnPress - Checks to see if the user hit the exit key (escape).
Screenshots - Loop that actively takes screenshots.
main - Facilitates listener thread and screenshot process.
PrintErr - Prints timed error message.
########################################################################################################################
'''


# Global variables #
global screenshot
last_pic = 0


'''
########################################################################################################################
Name:       OnPress
Purpose:    Checks to see if the user hit the exit key (escape).
Parameters: The key the user pressed detected by the key listener.
Returns:    False boolean flag, which terminates the key listener thread.
########################################################################################################################
'''
def OnPress(key) -> bool:
    global screenshot

    # If the user hit the escape key #
    if key == Key.esc:
        # Terminate the screenshot capture process #
        screenshot.terminate()
        return False


'''
########################################################################################################################
Name:       Screenshots
Purpose:    Loop that actively takes screenshots.
Parameters: The path where the screenshots are being stored.
Returns:    Nothing
########################################################################################################################
'''
def Screenshots(path: str, seconds: int):
    global last_pic

    while True:
        # Take a screenshot #
        pic = ImageGrab.grab()

        while True:
            # Format screenshot to number of last capture #
            pic_path = f'{path}Screenshot{last_pic}.png'

            # If file name is unique #
            if not os.path.isfile(pic_path):
                # Save the picture as png #
                pic.save(pic_path)
                # Increment static count #
                last_pic += 1
                break

            # Increment static count #
            last_pic += 1

        time.sleep(seconds)


'''
########################################################################################################################
Name:       main
Purpose:    Facilitates listener thread and screenshot process.
Parameters: Nothing
Returns:    Nothing
########################################################################################################################
'''
def main():
    global screenshot

    input('Please hit enter to begin\n')

    # Create the key listener thread and screenshot process #
    key_listener = Listener(on_press=OnPress)
    screenshot = Process(target=Screenshots, args=(file_path, time_interval))

    # Start the processes #
    key_listener.start()
    screenshot.start()

    # Join the processes #
    key_listener.join(600.0)
    screenshot.join(timeout=600)

    main()


'''
########################################################################################################################
Name:       PrintErr
Purpose:    Displays the passed in error message via stderr the durations on seconds passed in.
Parameters: The message to be displayed the duration is should be displayed.
Returns:    Nothing
########################################################################################################################
'''
def PrintErr(msg: str, secs: int):
    print(f'\n* [ERROR] {msg} *\n', file=sys.stderr)
    time.sleep(secs)


if __name__ == '__main__':
    # Command syntax tuple #
    cmds = ('cls', 'clear')

    # Get the current working directory #
    cwd = os.getcwd()

    # If OS is Windows #
    if os.name == 'nt':
        # Shell-escape system command input #
        cmd = quote(cmds[0])
        file_path = f'{cwd}\\ScreenshotDock\\'

    # If OS is Linux #
    else:
        # Shell-escape system command input #
        cmd = quote(cmds[1])
        file_path = f'{cwd}/ScreenshotDock/'

    # Ensure screenshot dir exists #
    pathlib.Path(file_path).mkdir(parents=True, exist_ok=True)

    try:
        time_interval = None

        while True:
            # Clear the display #
            os.system(cmd)
            try:
                time_interval = int(input('Enter screenshot time interval (1-120) seconds: '))
                # If interval is out of range #
                if time_interval < 1 or time_interval > 120:
                    PrintErr('Improper input: enter a number between 1-120', 2)
                    continue

                break
            # If non integer value is entered #
            except ValueError:
                PrintErr('Improper input: enter a number integer not other data types', 2)
                continue

        # clear the display #
        os.system(cmd)

        if time_interval:
            main()

    # If control + c is pressed #
    except KeyboardInterrupt:
        print('* Ctrl-C detected ... program exiting *')

    # If unknown error occurs #
    except Exception as ex:
        logging.exception(f'* Error Occurred: {ex} *')
