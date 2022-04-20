import argparse
import random
from datetime import datetime
from time import sleep

import pyautogui

pyautogui.FAILSAFE = False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("interval", type=float, required=False, default=3,
                        help="Mouse movement interval in minutes")
    args = parser.parse_args()
    assert args.interval > 0, "Interval must be positive"
    while(True):
        sleep(args.interval * 60)
        pyautogui.moveTo(random.randint(0, 100),
                         random.randint(0, 100))
        print("Mouse activity at {}".format(datetime.now().time()))

if __name__ == "__main__":
    main()
