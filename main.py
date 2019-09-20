import search
import input
import mouse
import directkeys
import time
def denter():
    directkeys.enter()
    time.sleep(0.01)
    directkeys.enter()
def chushi():
    directkeys.f10()
    time.sleep(1)
    mouse.moren()
    time.sleep(1)
    mouse.dianji()
    time.sleep(1)
if __name__ == "__main__":
    time.sleep(5)
    var = 1
    while var == 1:
        chushi()
        str = 'moshas'
        time.sleep(0.1)
        input.key_autinput(str)
        time.sleep(1)
        directkeys.space()
        # time.sleep(1)
        # str = 'henji'
        # time.sleep(0.1)
        # input.key_autinput(str)
        # time.sleep(1)
        # directkeys.space()
        time.sleep(2)
        directkeys.enter()
        time_start =time.time()
        time.sleep(0.01)
        mouse.first()
        time.sleep(0.01)
        a=search.number()
        print(a)
        mouse.second()
        time.sleep(0.01)
        if 40 < a <=170000:
            denter()
            time_end = time.time()
            print(time_end-time_start)
            time.sleep(3)
            directkeys.esc()
            time.sleep(3)
        else:
            time_end = time.time()
            print(time_end - time_start)
            time.sleep(3)
            directkeys.esc()
            time.sleep(3)
