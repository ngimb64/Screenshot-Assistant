# Built-in modules #
from multiprocessing import Process
import os, logging, pathlib, random, time

# Third-party modules #
from PIL import ImageGrab
from pynput.keyboard import Key, Listener

def on_press(key):
    global screenshot

    if key == Key.esc:
        screenshot.terminate()
        return False

def screenshots(file_path):
    for x in range(0, 120):
        pic = ImageGrab.grab()

        while True:
            pic_path = file_path + f'Screenshot {str(random.randrange(1,1000))}' + '.png'
            if not os.path.isfile(pic_path):
                pic.save(pic_path)
                break
            else:
                continue

        time.sleep(5)

def main():
    global screenshot

    input('Please hit enter to begin\n')

    key_listener = Listener(on_press=on_press)
    screenshot = Process(target=screenshots, args=(file_path,))
    key_listener.start()
    screenshot.start()
    
    key_listener.join(600.0)
    screenshot.join(timeout=600)

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
