import pathlib
from PIL import ImageGrab
from pynput.keyboard import Key, Listener
from multiprocessing import Process
import random
import logging
import time

def on_press(key):
    global screenshot

    if key == Key.esc:
        screenshot.terminate()
        return False

def screenshots(file_path):
    for x in range(0, 120):
        pic = ImageGrab.grab()
        pic.save(file_path + str(random.randrange(1,500)) + '.png')
        time.sleep(5)

def main():
    global screenshot

    input('Please hit enter to begin\n')

    key_listener = Listener(on_press=on_press) ; key_listener.start()
    screenshot = Process(target=screenshots, args=(file_path,)) ; screenshot.start()
    key_listener.join(600)
    screenshot.join(timeout=600)

    if screenshot is not None:
        screenshot.terminate()

    main()


if __name__ == '__main__':

    try:
        pathlib.Path('C:/Users/Public/Screenshots')\
                .mkdir(parents=True, exist_ok=True)
        file_path = 'C:\\Users\\Public\\Screenshots\\'

        main()

    except KeyboardInterrupt:
        print('* Ctrl-C detected ... program exiting *')

    except Exception as ex:
        logging.exception('* Error Ocurred: {} *'.format(ex))