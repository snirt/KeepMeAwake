__author__ = 'SnirT'

import win32api, win32con
import time


def main():

    last_x, last_y, x, y = 0, 0, 1, 1

    while True:
        x, y = get_cursor_position()
        if last_x == x or last_y == y:
            wake_up()
        last_x = x
        last_y = y
        print("checking mouse activity...")
        time.sleep(60*3)


def get_cursor_position():

    ret_x, ret_y = 0, 0
    try:
        ret_x, ret_y = win32api.GetCursorPos()
    except:
        print ("Exception! can't get cursor position")
    return ret_x, ret_y


def wake_up():
    print ("Key press faked at " + time.asctime())
    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)

main()
