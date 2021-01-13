# 주기적으로 실제 시간을 측정한 후 정해진 시간이 됐을 때 루프를 종료한다. 

import datetime 
import time 

# t1 시간 기록 (특정 날짜)
t1 = datetime.datetime(
    year=2021, month=8, day=1, hour=0, minute=0, second=00)

# 현재 시간을 기준으로 1분 뒤에 루프를 나오게 하고 싶다면, 아래처럼 써볼 수 도 있다. 
# t1 = datetime.datetime.now() + datetime.timedelta(minutes=1)

while True:
    now = datetime.datetime.now()
    print("현재 시간 : {0}".format(now))
    print("루프 만료 시간 : {0}".format(t1))
    if t1 <= now:
        break

    time.sleep(1)