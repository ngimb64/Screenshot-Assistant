""" Built-in modules """
import logging
import os
import pathlib
import sys
import time
from multiprocessing import Process
# Third-party modules #
from PIL import ImageGrab
from pynput.keyboard import Key, Listener


# Global variables #
global SCREENSHOT
LAST_PIC = 0


def on_press(key) -> bool:
    """
    Checks to see if the user hit the exit key (escape).

    :param key:  The key press that was detected by the pynput listener.
    :return:  False boolean flag if escape key is detected, which communicates to
              the listener thread to terminate.
    """
    global SCREENSHOT

    # If the user hit the escape key #
    if key == Key.esc:
        # Terminate the screenshot capture process #
        SCREENSHOT.terminate()
        return False

    return True


def screenshots(path: str, seconds: int):
    """
    Loop that actively takes screenshots.

    :param path:  The base path of program execution with appended bracket.
    :param seconds:  The time interval between screenshots.
    :return: Nothing
    """
    global LAST_PIC

    while True:
        # Take a screenshot #
        pic = ImageGrab.grab()

        while True:
            # Format screenshot to number of last capture #
            pic_path = f'{path}Screenshot{LAST_PIC}.png'

            # If file name is unique #
            if not os.path.isfile(pic_path):
                # Save the picture as png #
                pic.save(pic_path)
                # Increment static count #
                LAST_PIC += 1
                break

            # Increment static count #
            LAST_PIC += 1

        time.sleep(seconds)


def main(wait_interval: int):
    """
    Facilitates listener thread and screenshot process.

    :param wait_interval:  The selected time interval per screenshot execution.
    :return:  Nothing
    """
    global SCREENSHOT

    input('Please hit enter to begin or ctrl+c to stop ')
    print('\nNow taking screenshots, hit escape to stop')

    # Create the key listener thread and screenshot process #
    key_listener = Listener(on_press=on_press)
    SCREENSHOT = Process(target=screenshots, args=(file_path, wait_interval))

    # Start the processes #
    key_listener.start()
    SCREENSHOT.start()

    # Join the processes #
    key_listener.join(600.0)
    SCREENSHOT.join(timeout=600)

    print()
    main(wait_interval)


def print_err(msg: str, secs: int):
    """
    Displays the passed in error message via stderr the durations on seconds passed in.

    :param msg:  The error message to be displayed.
    :param secs:  The time interval in which the message should be displayed.
    :return:  Nothing
    """
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
        CMD = cmds[0]
        file_path = f'{cwd}\\ScreenshotDock\\'

    # If OS is Linux #
    else:
        # Shell-escape system command input #
        CMD = cmds[1]
        file_path = f'{cwd}/ScreenshotDock/'

    # Ensure screenshot dir exists #
    pathlib.Path(file_path).mkdir(parents=True, exist_ok=True)

    try:
        TIME_INTERVAL = None

        while True:
            # Clear the display #
            os.system(CMD)
            try:
                TIME_INTERVAL = int(input('Enter screenshot time interval (1-120) seconds: '))
                # If interval is out of range #
                if TIME_INTERVAL < 1 or TIME_INTERVAL > 120:
                    print_err('Improper input: enter a number between 1-120', 2)
                    continue

                break
            # If non integer value is entered #
            except ValueError:
                print_err('Improper input: enter a number integer not other data types', 2)
                continue

        # clear the display #
        os.system(CMD)

        if TIME_INTERVAL:
            main(TIME_INTERVAL)

    # If control + c is pressed #
    except KeyboardInterrupt:
        print('* Ctrl-C detected ... program exiting *')

    # If unknown error occurs during multiprocessing #
    except OSError as ex:
        logging.exception('* Error Occurred: %s *', ex)
