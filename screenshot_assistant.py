# pylint: disable=E0401
""" Built-in modules """
import logging
import os
import sys
import time
from pathlib import Path
from multiprocessing import Process
from shlex import quote
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


def screenshots(path: Path, seconds: int):
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
            pic_path = path / f'Screenshot{LAST_PIC}.png'
            # If file name is unique #
            if not pic_path.exists():
                # Save the picture as png #
                pic.save(pic_path)
                # Increment static count #
                LAST_PIC += 1
                break

            # Increment static count #
            LAST_PIC += 1

        time.sleep(seconds)


def get_time_interval() -> int:
    """
    Gets the time interval integer from user and returns to main.

    :return:  The input time interval integer.
    """
    while True:
        try:
            # Get the screenshot time interval #
            interval_input = int(input('[+] Enter screenshot time interval (1-120) seconds: '))
            # If interval is out of range #
            if interval_input < 1 or interval_input > 120:
                print_err('Improper input: enter a number between 1-120', 2)
                continue

            return interval_input

        # If non integer value is entered #
        except ValueError:
            print_err('Improper input: enter a number integer not other data types', 2)
            continue


def main():
    """
    Facilitates listener thread and screenshot process.

    :param wait_interval:  The selected time interval per screenshot execution.
    :return:  Nothing
    """
    global SCREENSHOT

    input('[+] Please hit enter to begin or ctrl+c to stop ')
    # Get the time interval #
    wait_interval = get_time_interval()
    print('\n[!] Now taking screenshots, hit escape to stop')

    # Create the key listener thread and screenshot process #
    key_listener = Listener(on_press=on_press)
    SCREENSHOT = Process(target=screenshots, args=(file_path, wait_interval))
    # Start the processes #
    key_listener.start()
    SCREENSHOT.start()
    # Join the processes #
    key_listener.join(600.0)
    SCREENSHOT.join(timeout=600)

    # clear the display #
    os.system(CMD)
    # Loop back to beginning of main #
    main()


def print_err(msg: str, secs: int):
    """
    Displays the passed in error message via stderr the durations on seconds passed in.

    :param msg:  The error message to be displayed.
    :param secs:  The time interval in which the message should be displayed.
    :return:  Nothing
    """
    print(f'\n* [ERROR] {msg} *\n', file=sys.stderr)
    time.sleep(secs)
    # Clear the display #
    os.system(CMD)


if __name__ == '__main__':
    # Get the current working directory #
    cwd = Path.cwd()
    # Set the screenshot directory #
    file_path = cwd / 'ScreenshotDock'
    # Ensure screenshot dir exists #
    file_path.mkdir(parents=True, exist_ok=True)

    # If OS is Windows #
    if os.name == 'nt':
        # Shell-escape system command input #
        CMD = quote('cls')
    # If OS is Linux #
    else:
        # Shell-escape system command input #
        CMD = quote('clear')

    try:
        main()

    # If control + c is pressed #
    except KeyboardInterrupt:
        print('\n[!] Ctrl-C detected ... program exiting \n\n')

    # If unknown error occurs during multiprocessing #
    except OSError as ex:
        logging.exception('Unexpected Error Occurred: %s\n', ex)
