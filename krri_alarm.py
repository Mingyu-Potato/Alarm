# -*- coding: utf-8 -*-
from playsound import playsound
import schedule
import os, sys, time

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def volume_change():
    # Get default audio device using PyCAW
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
        
    # 음소거 토글 해제
    volume.SetMute(0, None)

    # Get current volume 
    VolumeRangeDb = volume.GetVolumeRange()
    max_db, min_db = VolumeRangeDb[-1], VolumeRangeDb[0]

    vol = (max_db - min_db) * percent + min_db 
    if vol > 0: vol = 0
    volume.SetMasterVolumeLevel(vol, None)

def lunch():
    print('-----Music Start-----')
    print('-----11:25분은 점심시간-----')
    
    volume_change()
    playsound('C:\\Users\\실습생\\Mingyu\\krri_alarm\\music\\lunch.mp3')
    
    print('-----Music End-----')
    print()
    print('Schedule 실행 중...')

def getoffwork():
    print('-----Music Start-----')
    print('-----17:55분은 퇴근시간-----')
    
    volume_change()
    playsound('C:\\Users\\실습생\\Mingyu\\krri_alarm\\music\\getoffwork.mp3')
    
    print('-----Music End-----')
    print()
    print('Schedule 실행 중...')

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
    global percent
    percent = 0.7   # 0.0(min) ~ 1.0(max)
    run()