from playsound import playsound
import schedule
import time
import sys
import multiprocessing

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import Audio

def lunch():
    print('-----Music Start-----')
    print('-----11:25분은 점심시간-----')
    playsound('lunch.mp3')

def getoffwork():
    print('-----Music Start-----')
    print('-----17:55분은 퇴근시간-----')
    playsound('lunch.mp3')

def _init():
    schedule.every().day.at('11:25').do(lunch)
    schedule.every().day.at('17:55').do(getoffwork)

def run():
    _init()
    print('Schedule 실행 중...')

    while True:
        try:
            schedule.run_pending()
            time.sleep(1)
        except KeyboardInterrupt:
            print('프로그램 종료')
            sys.exit(0)

if __name__ == '__main__':
    run()