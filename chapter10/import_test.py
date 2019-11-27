# import_test.py
from datetime import date, time, datetime
import chapter10.my_module1
import random
import datetime
import calendar

if __name__ == "__main__":
    print("== import_test.py ==")

    # 랜덤
    dice1 = random.randint(1, 6) #임의의 정수가 생성됨
    dice2 = random.randint(1, 6)
    print("주사위 두 개의 숫자: {0}, {1}".format(dice1, dice2))

    num1 = random.randrange(1, 10, 2) # 1~9(10-1) 중 임의의 홀수 선택
    num2 = random.randrange(0, 100, 10) # 0~99(100-1) 중 임의의 10의 단위 숫자 선택
    print("num1 : {0}, num2 : {1}".format(num1, num2))

    menu = ['비빔밥', '된장찌게', '볶음밥', '불고기', '스파게티', '피자', '탕수육']
    print(random.choice(menu))

    print(random.sample([1,2,3,4,5],2)) # 모집단에서 두 개의 인자 선택

    # 날짜, 시간
    set_day = datetime.date(2019, 11, 27)
    print(type(set_day), set_day)
    print('{0}/{1}/{2}'.format(set_day.year,set_day.month,set_day.day))

    day1 = datetime.date(2019, 4, 1)
    day2 = datetime.date(2019, 7, 10)
    diff_day = day2 - day1
    print(type(diff_day), diff_day)
    print("** 지정된 두 날짜의 차이는 {}일 입니다. **".format(diff_day.days))
    print(datetime.date.today())

    today = datetime.date.today()
    special_day = datetime.date(2019, 12, 31)
    print(special_day - today)

    set_time = datetime.time(15, 30, 45)
    print(set_time)
    print('{0}:{1}:{2}'.format(set_time.hour, set_time.minute, set_time.second))

    set_dt = datetime.datetime(2018, 10, 9, 10, 20, 0)
    print(set_dt)
    print('날짜 {0}/{1}/{2}'.format(set_dt.year, set_dt.month, set_dt.day))
    print('시각 {0}:{1}:{2}'.format(set_dt.hour, set_dt.minute, set_dt.second))

    now = datetime.datetime.now()
    print(now)

    print("Date & Time : {:%Y-%m-%d, %H:%M:%S}".format(now))
    print("Date: {:%Y-%m-%d}".format(now))
    print("Time: {:%H:%M:%S}".format(now))

    set_dt = datetime.datetime(2017, 12, 1, 12, 30, 45)

    print("현재 날짜 및 시간 : ", now)
    print("차이 : ", set_dt - now)

    print(date(2019, 7, 1))
    print(date.today())
    print(time(15, 30, 45))
    print(datetime.datetime(2020, 2, 14, 18, 10, 50))
    print(datetime.datetime.now())

    # 달력
    print(calendar.calendar(2019))
    print(calendar.calendar(2019, m=4))
    print(calendar.month(2020,9))
    print(calendar.monthrange(2020,2))
    print(calendar.firstweekday())

    # 일주일의 시작을 월 -> 일 바꿈
    calendar.setfirstweekday(calendar.SUNDAY)
    print(calendar.month(2020,9))

    # 해당 날짜의 요일을 반환
    print(calendar.weekday(2018, 10, 14))

    # 윤년
    print(calendar.isleap(2018))
    print(calendar.isleap(2020))

else:
    print("import")

