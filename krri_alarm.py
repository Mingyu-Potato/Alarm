from playsound import playsound
import schedule
import time
import sys

def lunch():
    print('-----Music Start-----')
    print('-----11:25분은 점심시간-----')
    playsound('sample.mp3')

def getoffwork():
    print('-----Music Start-----')
    print('-----17:55분은 퇴근시간-----')
    playsound('sample.mp3')

def end_alarm():
    print('-----Music End-----')
    sys.exit(0)

schedule.every().day.at('11:25').do(lunch)
schedule.every().day.at('11:30').do(end_alarm)
schedule.every().day.at('17:55').do(getoffwork)
schedule.every().day.at('18:00').do(end_alarm)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except KeyboardInterrupt:
        print('프로그램 종료')
        sys.exit(0)